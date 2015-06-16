# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014, 2015 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from __future__ import division

from ..base import *  # noqa
from ..caracteristiques_socio_demographiques.demographie import isol


@reference_formula
class parent_isole_individu(EntityToPersonColumn):
    entity_class = Individus
    label = u"Parent isolé (individu)"
    role = CHEF
    variable = isol


@reference_formula
class parent_isole_menage(PersonToEntityColumn):
    entity_class = Menages
    label = u"Parent isolé (ménage)"
    operation = 'or'
    variable = parent_isole_individu


@reference_formula
class fsl_eligibilite(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = Menages
    label = u"Éligibilité au fonds de solidarité pour le logement (FSL) de la ville de Paris"
    url = u'http://www.paris.fr/pratique/toutes-les-aides-et-allocations/aides-sociales/le-fonds-de-solidarite-logement/rub_9737_stand_100945_port_24193'  # noqa

    def function(self, simulation, period):
        unites_consommation_paris = simulation.calculate('unites_consommation_paris', period)
        plafond_personne_seule = 1390

        fsl_plafond_indicatif = plafond_personne_seule * unites_consommation_paris
        statut_occupation = simulation.calculate('statut_occupation', period)
        eligibilite_logement = (statut_occupation == 3) + (statut_occupation == 4) + (statut_occupation == 5) + \
            (statut_occupation == 7)
        ass_base_ressources_i_holder = simulation.compute('ass_base_ressources_i')
        ass_base_ressources = self.sum_by_entity(ass_base_ressources_i_holder)
        # loyer = simulation.calculate('loyer', period)
        # eligibilite_taux_effort =
        return period, eligibilite_logement * (ass_base_ressources < fsl_plafond_indicatif)


@reference_formula
class unites_consommation_paris(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = Menages
    label = u"Unités de consommation selon la ville de Paris"

    def function(self, simulation, period):
        age_holder = simulation.compute('age', period)
        age_by_role = self.split_by_roles(age_holder)
        parent_isole_menage = simulation.calculate('parent_isole_menage', period)
        age_seuil_adulte = 20  # TODO store in legislation, check value

        uc_adulte_additionnel = 0.5
        uc_enfant = 0.3
        uc_isole = 0.2
        uc = 0.5
        for age in age_by_role.itervalues():
            adulte = (age_seuil_adulte < age) & (age <= 150)
            enfant = (0 <= age) & (age <= age_seuil_adulte)
            enfant_de_parent_isole = enfant & parent_isole_menage
            uc += adulte * uc_adulte_additionnel + enfant * (uc_enfant + enfant_de_parent_isole * uc_isole)
        return period, uc
