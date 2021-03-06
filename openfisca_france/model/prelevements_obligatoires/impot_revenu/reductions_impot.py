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

import logging

from numpy import minimum as min_, maximum as max_, logical_not as not_, around

from ...base import *  # noqa analysis:ignore


log = logging.getLogger(__name__)


@reference_formula
class reductions(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"reductions"

    @dated_function(start = date(2002, 1, 1), stop = date(2002, 12, 31))
    def function_20020101_20021231(self, simulation, period):
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2002
        '''
        period = period.start.offset('first-of', 'year').period('year')
        adhcga = simulation.calculate('adhcga', period)
        assvie = simulation.calculate('assvie', period)
        cappme = simulation.calculate('cappme', period)
        cotsyn = simulation.calculate('cotsyn', period)
        dfppce = simulation.calculate('dfppce', period)
        daepad = simulation.calculate('daepad', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        donapd = simulation.calculate('donapd', period)
        ecpess = simulation.calculate('ecpess', period)
        garext = simulation.calculate('garext', period)
        intemp = simulation.calculate('intemp', period)
        invfor = simulation.calculate('invfor', period)
        invrev = simulation.calculate('invrev', period)
        ip_net = simulation.calculate('ip_net', period)
        prcomp = simulation.calculate('prcomp', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (adhcga + assvie + cappme + cotsyn + dfppce + daepad + doment + domlog + donapd + ecpess +
                garext + intemp + invfor + invrev + prcomp + rsceha + saldom + spfcpi)
        return period, min_(ip_net, total_reductions)

    @dated_function(start = date(2003, 1, 1), stop = date(2004, 12, 31))
    def function_20030101_20041231(self, simulation, period):
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2003 et 2004
        '''
        period = period.start.offset('first-of', 'year').period('year')
        adhcga = simulation.calculate('adhcga', period)
        assvie = simulation.calculate('assvie', period)
        cappme = simulation.calculate('cappme', period)
        cotsyn = simulation.calculate('cotsyn', period)
        dfppce = simulation.calculate('dfppce', period)
        daepad = simulation.calculate('daepad', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        donapd = simulation.calculate('donapd', period)
        ecpess = simulation.calculate('ecpess', period)
        garext = simulation.calculate('garext', period)
        intemp = simulation.calculate('intemp', period)
        invfor = simulation.calculate('invfor', period)
        invrev = simulation.calculate('invrev', period)
        ip_net = simulation.calculate('ip_net', period)
        prcomp = simulation.calculate('prcomp', period)
        repsoc = simulation.calculate('repsoc', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (adhcga + assvie + cappme + cotsyn + dfppce + daepad + doment + domlog + donapd + ecpess +
                garext + intemp + invfor + invrev + prcomp + repsoc + rsceha + saldom + spfcpi)
        return period, min_(ip_net, total_reductions)

    @dated_function(start = date(2005, 1, 1), stop = date(2005, 12, 31))
    def function_20050101_20051231(self, simulation, period):
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2005
        '''
        period = period.start.offset('first-of', 'year').period('year')
        adhcga = simulation.calculate('adhcga', period)
        cappme = simulation.calculate('cappme', period)
        cotsyn = simulation.calculate('cotsyn', period)
        daepad = simulation.calculate('daepad', period)
        dfppce = simulation.calculate('dfppce', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        donapd = simulation.calculate('donapd', period)
        ecpess = simulation.calculate('ecpess', period)
        intagr = simulation.calculate('intagr', period)
        intcon = simulation.calculate('intcon', period)
        invfor = simulation.calculate('invfor', period)
        invlst = simulation.calculate('invlst', period)
        ip_net = simulation.calculate('ip_net', period)
        prcomp = simulation.calculate('prcomp', period)
        repsoc = simulation.calculate('repsoc', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (adhcga + cappme + cotsyn + daepad + dfppce + doment + domlog + donapd + ecpess + intagr +
                intcon + invfor + invlst + prcomp + repsoc + rsceha + saldom + spfcpi)
        return period, min_(ip_net, total_reductions)

    @dated_function(start = date(2006, 1, 1), stop = date(2006, 12, 31))
    def function_20060101_20061231(self, simulation, period):
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2006
        '''
        period = period.start.offset('first-of', 'year').period('year')
        adhcga = simulation.calculate('adhcga', period)
        cappme = simulation.calculate('cappme', period)
        cotsyn = simulation.calculate('cotsyn', period)
        creaen = simulation.calculate('creaen', period)
        daepad = simulation.calculate('daepad', period)
        deffor = simulation.calculate('deffor', period)
        dfppce = simulation.calculate('dfppce', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        donapd = simulation.calculate('donapd', period)
        ecpess = simulation.calculate('ecpess', period)
        intagr = simulation.calculate('intagr', period)
        invfor = simulation.calculate('invfor', period)
        invlst = simulation.calculate('invlst', period)
        ip_net = simulation.calculate('ip_net', period)
        prcomp = simulation.calculate('prcomp', period)
        repsoc = simulation.calculate('repsoc', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        sofica = simulation.calculate('sofica', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (adhcga + cappme + cotsyn + creaen + daepad + deffor + dfppce + doment + domlog + donapd +
        ecpess + intagr + invfor + invlst + prcomp + repsoc + rsceha + saldom + sofica + spfcpi)
        return period, min_(ip_net, total_reductions)

    @dated_function(start = date(2007, 1, 1), stop = date(2007, 12, 31))
    def function_20070101_20071231(self, simulation, period):
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2007
        '''
        period = period.start.offset('first-of', 'year').period('year')
        adhcga = simulation.calculate('adhcga', period)
        cappme = simulation.calculate('cappme', period)
        cotsyn = simulation.calculate('cotsyn', period)
        creaen = simulation.calculate('creaen', period)
        daepad = simulation.calculate('daepad', period)
        deffor = simulation.calculate('deffor', period)
        dfppce = simulation.calculate('dfppce', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        donapd = simulation.calculate('donapd', period)
        ecpess = simulation.calculate('ecpess', period)
        intagr = simulation.calculate('intagr', period)
        invfor = simulation.calculate('invfor', period)
        invlst = simulation.calculate('invlst', period)
        ip_net = simulation.calculate('ip_net', period)
        prcomp = simulation.calculate('prcomp', period)
        repsoc = simulation.calculate('repsoc', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        sofica = simulation.calculate('sofica', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (adhcga + cappme + cotsyn + creaen + daepad + deffor + dfppce + doment + domlog + donapd +
        ecpess + intagr + invfor + invlst + prcomp + repsoc + rsceha + saldom + sofica + spfcpi)

        return period, min_(ip_net, total_reductions)

    @dated_function(start = date(2008, 1, 1), stop = date(2008, 12, 31))
    def function_20080101_20081231(self, simulation, period):
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2008
        '''
        period = period.start.offset('first-of', 'year').period('year')
        adhcga = simulation.calculate('adhcga', period)
        cappme = simulation.calculate('cappme', period)
        cotsyn = simulation.calculate('cotsyn', period)
        creaen = simulation.calculate('creaen', period)
        daepad = simulation.calculate('daepad', period)
        deffor = simulation.calculate('deffor', period)
        dfppce = simulation.calculate('dfppce', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        donapd = simulation.calculate('donapd', period)
        ecpess = simulation.calculate('ecpess', period)
        intagr = simulation.calculate('intagr', period)
        invfor = simulation.calculate('invfor', period)
        invlst = simulation.calculate('invlst', period)
        ip_net = simulation.calculate('ip_net', period)
        mohist = simulation.calculate('mohist', period)
        prcomp = simulation.calculate('prcomp', period)
        repsoc = simulation.calculate('repsoc', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        sofica = simulation.calculate('sofica', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (adhcga + cappme + cotsyn + creaen + daepad + deffor + dfppce + doment + domlog + donapd +
        ecpess + intagr + invfor + invlst + mohist + prcomp + repsoc + rsceha + saldom + sofica + spfcpi)
        return period, min_(ip_net, total_reductions)

    @dated_function(start = date(2009, 1, 1), stop = date(2009, 12, 31))
    def function_20090101_20091231(self, simulation, period):
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2009
        '''
        period = period.start.offset('first-of', 'year').period('year')
        adhcga = simulation.calculate('adhcga', period)
        cappme = simulation.calculate('cappme', period)
        cotsyn = simulation.calculate('cotsyn', period)
        creaen = simulation.calculate('creaen', period)
        daepad = simulation.calculate('daepad', period)
        deffor = simulation.calculate('deffor', period)
        dfppce = simulation.calculate('dfppce', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        domsoc = simulation.calculate('domsoc', period)
        donapd = simulation.calculate('donapd', period)
        ecodev = simulation.calculate('ecodev', period)
        ecpess = simulation.calculate('ecpess', period)
        intagr = simulation.calculate('intagr', period)
        invfor = simulation.calculate('invfor', period)
        invlst = simulation.calculate('invlst', period)
        ip_net = simulation.calculate('ip_net', period)
        locmeu = simulation.calculate('locmeu', period)
        mohist = simulation.calculate('mohist', period)
        prcomp = simulation.calculate('prcomp', period)
        repsoc = simulation.calculate('repsoc', period)
        resimm = simulation.calculate('resimm', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        scelli = simulation.calculate('scelli', period)
        sofica = simulation.calculate('sofica', period)
        sofipe = simulation.calculate('sofipe', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (adhcga + cappme + cotsyn + creaen + daepad + deffor + dfppce + doment + domlog + domsoc +
        donapd + ecodev + ecpess + intagr + invfor + invlst + locmeu + mohist + prcomp + repsoc + resimm + rsceha +
        saldom + scelli + sofica + sofipe + spfcpi)
        return period, min_(ip_net, total_reductions)

    @dated_function(start = date(2010, 1, 1), stop = date(2010, 12, 31))
    def function_20100101_20101231(self, simulation, period):  # TODO: check (sees checked) and report in Niches.xls
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2010
        '''
        period = period.start.offset('first-of', 'year').period('year')
        adhcga = simulation.calculate('adhcga', period)
        cappme = simulation.calculate('cappme', period)
        cotsyn = simulation.calculate('cotsyn', period)
        creaen = simulation.calculate('creaen', period)
        daepad = simulation.calculate('daepad', period)
        deffor = simulation.calculate('deffor', period)
        dfppce = simulation.calculate('dfppce', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        domsoc = simulation.calculate('domsoc', period)
        donapd = simulation.calculate('donapd', period)
        ecpess = simulation.calculate('ecpess', period)
        intagr = simulation.calculate('intagr', period)
        invfor = simulation.calculate('invfor', period)
        invlst = simulation.calculate('invlst', period)
        ip_net = simulation.calculate('ip_net', period)
        locmeu = simulation.calculate('locmeu', period)
        mohist = simulation.calculate('mohist', period)
        patnat = simulation.calculate('patnat', period)
        prcomp = simulation.calculate('prcomp', period)
        repsoc = simulation.calculate('repsoc', period)
        resimm = simulation.calculate('resimm', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        scelli = simulation.calculate('scelli', period)
        sofica = simulation.calculate('sofica', period)
        sofipe = simulation.calculate('sofipe', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (adhcga + cappme + cotsyn + creaen + daepad + deffor + dfppce + doment + domlog + domsoc +
        donapd + ecpess + intagr + invfor + invlst + locmeu + mohist + patnat + prcomp + repsoc + resimm + rsceha +
        saldom + scelli + sofica + sofipe + spfcpi)  # TODO: check (sees checked) and report in Niches.xls
        return period, min_(ip_net, total_reductions)

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2011
        '''
        period = period.start.offset('first-of', 'year').period('year')
        adhcga = simulation.calculate('adhcga', period)
        cappme = simulation.calculate('cappme', period)
        cotsyn = simulation.calculate('cotsyn', period)
        creaen = simulation.calculate('creaen', period)
        daepad = simulation.calculate('daepad', period)
        deffor = simulation.calculate('deffor', period)
        dfppce = simulation.calculate('dfppce', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        domsoc = simulation.calculate('domsoc', period)
        donapd = simulation.calculate('donapd', period)
        ecpess = simulation.calculate('ecpess', period)
        intagr = simulation.calculate('intagr', period)
        invfor = simulation.calculate('invfor', period)
        invlst = simulation.calculate('invlst', period)
        ip_net = simulation.calculate('ip_net', period)
        locmeu = simulation.calculate('locmeu', period)
        mohist = simulation.calculate('mohist', period)
        patnat = simulation.calculate('patnat', period)
        prcomp = simulation.calculate('prcomp', period)
        repsoc = simulation.calculate('repsoc', period)
        resimm = simulation.calculate('resimm', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        scelli = simulation.calculate('scelli', period)
        sofica = simulation.calculate('sofica', period)
        sofipe = simulation.calculate('sofipe', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (adhcga + cappme + cotsyn + creaen + daepad + deffor + dfppce + doment + domlog + domsoc +
        donapd + ecpess + intagr + invfor + invlst + locmeu + mohist + patnat + prcomp + repsoc + resimm + rsceha +
        saldom + scelli + sofica + sofipe + spfcpi)
        return period, min_(ip_net, total_reductions)

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2012
        '''
        period = period.start.offset('first-of', 'year').period('year')
        adhcga = simulation.calculate('adhcga', period)
        cappme = simulation.calculate('cappme', period)
        creaen = simulation.calculate('creaen', period)
        daepad = simulation.calculate('daepad', period)
        deffor = simulation.calculate('deffor', period)
        dfppce = simulation.calculate('dfppce', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        domsoc = simulation.calculate('domsoc', period)
        donapd = simulation.calculate('donapd', period)
        ecpess = simulation.calculate('ecpess', period)
        intagr = simulation.calculate('intagr', period)
        invfor = simulation.calculate('invfor', period)
        invlst = simulation.calculate('invlst', period)
        ip_net = simulation.calculate('ip_net', period)
        locmeu = simulation.calculate('locmeu', period)
        mohist = simulation.calculate('mohist', period)
        patnat = simulation.calculate('patnat', period)
        prcomp = simulation.calculate('prcomp', period)
        repsoc = simulation.calculate('repsoc', period)
        resimm = simulation.calculate('resimm', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        scelli = simulation.calculate('scelli', period)
        sofica = simulation.calculate('sofica', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (adhcga + cappme + creaen + daepad + deffor + dfppce + doment + domlog + domsoc +
        donapd + ecpess + intagr + invfor + invlst + locmeu + mohist + patnat + prcomp + repsoc + resimm + rsceha +
        saldom + scelli + sofica + spfcpi)
        return period, min_(ip_net, total_reductions)

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Renvoie la somme des réductions d'impôt à intégrer pour l'année 2013
        '''
        period = period.start.offset('first-of', 'year').period('year')
        accult = simulation.calculate('accult', period)
        adhcga = simulation.calculate('adhcga', period)
        cappme = simulation.calculate('cappme', period)
        creaen = simulation.calculate('creaen', period)
        daepad = simulation.calculate('daepad', period)
        deffor = simulation.calculate('deffor', period)
        dfppce = simulation.calculate('dfppce', period)
        doment = simulation.calculate('doment', period)
        domlog = simulation.calculate('domlog', period)
        donapd = simulation.calculate('donapd', period)
        duflot = simulation.calculate('duflot', period)
        ecpess = simulation.calculate('ecpess', period)
        garext = simulation.calculate('garext', period)
        intagr = simulation.calculate('intagr', period)
        invfor = simulation.calculate('invfor', period)
        invlst = simulation.calculate('invlst', period)
        ip_net = simulation.calculate('ip_net', period)
        locmeu = simulation.calculate('locmeu', period)
        mecena = simulation.calculate('mecena', period)
        mohist = simulation.calculate('mohist', period)
        patnat = simulation.calculate('patnat', period)
        prcomp = simulation.calculate('prcomp', period)
        repsoc = simulation.calculate('repsoc', period)
        resimm = simulation.calculate('resimm', period)
        rsceha = simulation.calculate('rsceha', period)
        saldom = simulation.calculate('saldom', period)
        scelli = simulation.calculate('scelli', period)
        sofica = simulation.calculate('sofica', period)
        spfcpi = simulation.calculate('spfcpi', period)

        total_reductions = (accult + adhcga + cappme + creaen + daepad + deffor + dfppce + doment + domlog + donapd +
        duflot + ecpess + garext + intagr + invfor + invlst + locmeu + mecena + mohist +
        patnat + prcomp + repsoc + resimm + rsceha + saldom + scelli + sofica + spfcpi)
        return period, min_(ip_net, total_reductions)


#pour tous les dfppce:
    # : note de bas de page
    # TODO: plafonnement pour parti politiques depuis 2012 P.ir.reductions_impots.dfppce.max_niv


@reference_formula
class adhcga(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"adhcga"

    def function(self, simulation, period):
        '''
        Frais de comptabilité et d'adhésion à un CGA ou AA
        2002-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ff = simulation.calculate('f7ff', period)
        f7fg = simulation.calculate('f7fg', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.adhcga

        return period, min_(f7ff, P.max * f7fg)


@reference_formula
class assvie(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"assvie"
    start_date = date(2002, 1, 1)
    stop_date = date(2004, 12, 31)

    def function(self, simulation, period):
        '''
        Assurance-vie (cases GW, GX et GY de la 2042)
        2002-2004
        '''
        period = period.start.offset('first-of', 'year').period('year')
        nb_pac = simulation.calculate('nb_pac', period)
        f7gw = simulation.calculate('f7gw', period)
        f7gx = simulation.calculate('f7gx', period)
        f7gy = simulation.calculate('f7gy', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.assvie

        max1 = P.max + nb_pac * P.pac
        return period, P.taux * min_(f7gw + f7gx + f7gy, max1)


@reference_formula
class cappme(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"cappme"

    @dated_function(start = date(2002, 1, 1), stop = date(2002, 12, 31))
    def function_20020101_20021231(self, simulation, period):
        '''
        Souscriptions au capital des PME
        2002
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7cf = simulation.calculate('f7cf', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.cappme

        base = f7cf
        seuil = P.seuil * (marpac + 1)
        return period, P.taux * min_(base, seuil)

    @dated_function(start = date(2003, 1, 1), stop = date(2003, 12, 31))
    def function_20030101_20031231(self, simulation, period):
        '''
        Souscriptions au capital des PME
        2003
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7cf = simulation.calculate('f7cf', period)
        f7cl = simulation.calculate('f7cl', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.cappme

        base = f7cf + f7cl
        seuil = P.seuil * (marpac + 1)
        return period, P.taux * min_(base, seuil)

    @dated_function(start = date(2004, 1, 1), stop = date(2004, 12, 31))
    def function_20040101_20041231(self, simulation, period):
        '''
        Souscriptions au capital des PME
        2004
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7cf = simulation.calculate('f7cf', period)
        f7cl = simulation.calculate('f7cl', period)
        f7cm = simulation.calculate('f7cm', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.cappme

        base = f7cf + f7cl + f7cm
        seuil = P.seuil * (marpac + 1)
        return period, P.taux * min_(base, seuil)

    @dated_function(start = date(2005, 1, 1), stop = date(2008, 12, 31))
    def function_20050101_20081231(self, simulation, period):
        '''
        Souscriptions au capital des PME
        2005-2008
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7cf = simulation.calculate('f7cf', period)
        f7cl = simulation.calculate('f7cl', period)
        f7cm = simulation.calculate('f7cm', period)
        f7cn = simulation.calculate('f7cn', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.cappme

        base = f7cf + f7cl + f7cm + f7cn
        seuil = P.seuil * (marpac + 1)
        return period, P.taux * min_(base, seuil)

    @dated_function(start = date(2009, 1, 1), stop = date(2010, 12, 31))
    def function_20090101_20101231(self, simulation, period):
        '''
        Souscriptions au capital des PME
        2009-2010
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7cf = simulation.calculate('f7cf', period)
        f7cl = simulation.calculate('f7cl', period)
        f7cm = simulation.calculate('f7cm', period)
        f7cn = simulation.calculate('f7cn', period)
        f7cu = simulation.calculate('f7cu', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.cappme

        base = f7cf + f7cl + f7cm + f7cn + f7cu
        seuil = P.seuil * (marpac + 1)
        seuil = P.seuil_tpe * (marpac + 1) * (f7cu > 0) + P.seuil * (marpac + 1) * (f7cu <= 0)
        return period, P.taux * min_(base, seuil)

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Souscriptions au capital des PME
        2011
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7cf = simulation.calculate('f7cf', period)
        f7cl = simulation.calculate('f7cl', period)
        f7cm = simulation.calculate('f7cm', period)
        f7cn = simulation.calculate('f7cn', period)
        f7cq = simulation.calculate('f7cq', period)
        f7cu = simulation.calculate('f7cu', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.cappme

        base = f7cl + f7cm + f7cn + f7cq
        seuil = P.seuil_tpe * (marpac + 1) * (f7cu > 0) + P.seuil * (marpac + 1) * (f7cu <= 0)
        max0 = max_(seuil - base, 0)
        return period, max_(P.taux25 * min_(base, seuil), P.taux * min_(max0, f7cf + f7cu))

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Souscriptions au capital des PME
        2012 cf. 2041 GR
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7cf = simulation.calculate('f7cf', period)
        f7cl = simulation.calculate('f7cl', period)
        f7cm = simulation.calculate('f7cm', period)
        f7cn = simulation.calculate('f7cn', period)
        f7cq = simulation.calculate('f7cq', period)
        f7cu = simulation.calculate('f7cu', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.cappme

        #TODO: gérer les changements de situation familiale
        base = f7cl + f7cm + f7cn
        seuil1 = P.seuil * (marpac + 1)
        seuil2 = max_(0, P.seuil_tpe * (marpac + 1) - min_(base, seuil1) - min_(f7cq, seuil1) - min_(f7cu, seuil1))
        seuil3 = min_(P.seuil_tpe * (marpac + 1) - min_(base, seuil1) - min_(f7cq, seuil1), seuil1)
        return period, P.taux25 * min_(base, seuil1) + P.taux * min_(f7cq, seuil1) + P.taux18 * (min_(f7cf, seuil3) +
                mini(f7cu, seuil2, seuil1))

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Souscriptions au capital des PME
        2013
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7cc = simulation.calculate('f7cc', period)
        f7cf = simulation.calculate('f7cf', period)
        f7cl = simulation.calculate('f7cl', period)
        f7cm = simulation.calculate('f7cm', period)
        f7cn = simulation.calculate('f7cn', period)
        f7cq = simulation.calculate('f7cq', period)
        f7cu = simulation.calculate('f7cu', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.cappme

        base = f7cl + f7cm
        seuil1 = P.seuil * (marpac + 1)
        seuil2 = max_(0, P.seuil_tpe * (marpac + 1) - min_(base, seuil1) - min_(f7cn, seuil1) - min_(f7cu, seuil1))
        seuil3 = min_(P.seuil_tpe * (marpac + 1) - min_(base, seuil1) - min_(f7cq, seuil1), seuil1)
        return period, P.taux25 * min_(base, seuil1) + P.taux22 * min_(f7cn, seuil1) + P.taux18 * (min_(f7cf + f7cc, seuil3) +
                min_(f7cu + f7cq, seuil2))


#TODO: vérifier l'existence du "max_"


@reference_formula
class cotsyn(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"cotsyn"

    def function(self, simulation, period):
        '''
        Cotisations syndicales (2002-20131
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ac_holder = simulation.compute('f7ac', period)
        salaire_imposable_holder = simulation.compute_add('salaire_imposable', period)
        cho_holder = simulation.compute('cho', period)
        rst_holder = simulation.compute('rst', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.cotsyn

        f7ac = self.filter_role(f7ac_holder, role = VOUS)
        f7ae = self.filter_role(f7ac_holder, role = CONJ)
        f7ag = self.filter_role(f7ac_holder, role = PAC1)

        cho = self.split_by_roles(cho_holder)
        rst = self.split_by_roles(rst_holder)
        salaire_imposable = self.split_by_roles(salaire_imposable_holder)

        tx = P.seuil

        salv, salc, salp = salaire_imposable[VOUS], salaire_imposable[CONJ], salaire_imposable[PAC1]
        chov, choc, chop = cho[VOUS], cho[CONJ], cho[PAC1]
        rstv, rstc, rstp = rst[VOUS], rst[CONJ], rst[PAC1]
        maxv = (salv + chov + rstv) * tx
        maxc = (salc + choc + rstc) * tx
        maxp = (salp + chop + rstp) * tx

        return period, P.taux * (min_(f7ac, maxv) + min_(f7ae, maxc) + min_(f7ag, maxp))


@reference_formula
class creaen(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"creaen"

    @dated_function(start = date(2006, 1, 1), stop = date(2008, 12, 31))
    def function_20060101_20081231(self, simulation, period):
        '''
        Aide aux créateurs et repreneurs d'entreprises
        2006-2008
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7fy = simulation.calculate('f7fy', period)
        f7gy = simulation.calculate('f7gy', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.creaen

        return period, (P.base * f7fy + P.hand * f7gy)

    @dated_function(start = date(2009, 1, 1), stop = date(2009, 12, 31))
    def function_20090101_20091231(self, simulation, period):
        '''
        Aide aux créateurs et repreneurs d'entreprises
        2009
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7fy = simulation.calculate('f7fy', period)
        f7gy = simulation.calculate('f7gy', period)
        f7jy = simulation.calculate('f7jy', period)
        f7hy = simulation.calculate('f7hy', period)
        f7ky = simulation.calculate('f7ky', period)
        f7iy = simulation.calculate('f7iy', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.creaen

        return period, (P.base * ((f7jy + f7fy) + f7hy / 2) +
                    P.hand * ((f7ky + f7gy) + f7iy / 2))

    @dated_function(start = date(2010, 1, 1), stop = date(2011, 12, 31))
    def function_20100101_20111231(self, simulation, period):
        '''
        Aide aux créateurs et repreneurs d'entreprises
        2010-2011
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7fy = simulation.calculate('f7fy', period)
        f7gy = simulation.calculate('f7gy', period)
        f7jy = simulation.calculate('f7jy', period)
        f7hy = simulation.calculate('f7hy', period)
        f7ky = simulation.calculate('f7ky', period)
        f7iy = simulation.calculate('f7iy', period)
        f7ly = simulation.calculate('f7ly', period)
        f7my = simulation.calculate('f7my', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.creaen

        return period, (P.base * ((f7jy + f7fy) + (f7hy + f7ly) / 2) +
                    P.hand * ((f7ky + f7gy) + (f7iy + f7my) / 2))

    @dated_function(start = date(2012, 1, 1), stop = date(2014, 12, 31))
    def function_20120101_20141231(self, simulation, period):
        '''
        Aide aux créateurs et repreneurs d'entreprises
        2012-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ly = simulation.calculate('f7ly', period)
        f7my = simulation.calculate('f7my', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.creaen

        return period, (P.base * (f7ly / 2) +
                    P.hand * (f7my / 2))


@reference_formula
class deffor(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"deffor"
    start_date = date(2006, 1, 1)

    def function(self, simulation, period):
        '''
        Défense des forêts contre l'incendie
        2006-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7uc = simulation.calculate('f7uc', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.deffor

        return period, P.taux * min_(f7uc, P.max)


@reference_formula
class daepad(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"daepad"

    def function(self, simulation, period):
        '''
        Dépenses d'accueil dans un établissement pour personnes âgées dépendantes
        ?-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7cd = simulation.calculate('f7cd', period)
        f7ce = simulation.calculate('f7ce', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.daepad

        return period, P.taux * (min_(f7cd, P.max) + min_(f7ce, P.max))


@reference_formula
class dfppce(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"dfppce"

    @dated_function(start = date(2002, 1, 1), stop = date(2003, 12, 31))
    def function_20020101_20031231(self, simulation, period):
        '''
        Dons aux autres oeuvres et dons effectués pour le financement des partis
        politiques et des campagnes électorales
        '''
        period = period.start.offset('first-of', 'year').period('year')
        rbg_int = simulation.calculate('rbg_int', period)
        f7uf = simulation.calculate('f7uf', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.dfppce

        base = f7uf
        max1 = P.max * rbg_int
        return period, P.taux * min_(base, max1)

    @dated_function(start = date(2004, 1, 1), stop = date(2004, 12, 31))
    def function_20040101_20041231(self, simulation, period):
        '''
        Dons aux autres oeuvres et dons effectués pour le financement des partis
        politiques et des campagnes électorales
        '''
        period = period.start.offset('first-of', 'year').period('year')
        rbg_int = simulation.calculate('rbg_int', period)
        f7uf = simulation.calculate('f7uf', period)
        f7xs = simulation.calculate('f7xs', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.dfppce

        base = f7uf + f7xs
        max1 = P.max * rbg_int
        return period, P.taux * min_(base, max1)

    @dated_function(start = date(2005, 1, 1), stop = date(2005, 12, 31))
    def function_20050101_20051231(self, simulation, period):
        '''
        Dons aux autres oeuvres et dons effectués pour le financement des partis
        politiques et des campagnes électorales
        '''
        period = period.start.offset('first-of', 'year').period('year')
        rbg_int = simulation.calculate('rbg_int', period)
        f7uf = simulation.calculate('f7uf', period)
        f7xs = simulation.calculate('f7xs', period)
        f7xt = simulation.calculate('f7xt', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.dfppce

        base = f7uf + f7xs + f7xt
        max1 = P.max * rbg_int
        return period, P.taux * min_(base, max1)

    @dated_function(start = date(2006, 1, 1), stop = date(2006, 12, 31))
    def function_20060101_20061231(self, simulation, period):
        '''
        Dons aux autres oeuvres et dons effectués pour le financement des partis
        politiques et des campagnes électorales
        '''
        period = period.start.offset('first-of', 'year').period('year')
        rbg_int = simulation.calculate('rbg_int', period)
        f7uf = simulation.calculate('f7uf', period)
        f7xs = simulation.calculate('f7xs', period)
        f7xt = simulation.calculate('f7xt', period)
        f7xu = simulation.calculate('f7xu', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.dfppce

        base = f7uf + f7xs + f7xt + f7xu
        max1 = P.max * rbg_int
        return period, P.taux * min_(base, max1)

    @dated_function(start = date(2007, 1, 1), stop = date(2007, 12, 31))
    def function_20070101_20071231(self, simulation, period):
        '''
        Dons aux autres oeuvres et dons effectués pour le financement des partis
        politiques et des campagnes électorales
        '''
        period = period.start.offset('first-of', 'year').period('year')
        rbg_int = simulation.calculate('rbg_int', period)
        f7uf = simulation.calculate('f7uf', period)
        f7xs = simulation.calculate('f7xs', period)
        f7xt = simulation.calculate('f7xt', period)
        f7xu = simulation.calculate('f7xu', period)
        f7xw = simulation.calculate('f7xw', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.dfppce

        base = f7uf + f7xs + f7xt + f7xu + f7xw
        max1 = P.max * rbg_int
        return period, P.taux * min_(base, max1)

    @dated_function(start = date(2008, 1, 1), stop = date(2010, 12, 31))
    def function_20080101_20101231(self, simulation, period):
        '''
        Dons aux autres oeuvres et dons effectués pour le financement des partis
        politiques et des campagnes électorales
        '''
        period = period.start.offset('first-of', 'year').period('year')
        rbg_int = simulation.calculate('rbg_int', period)
        f7uf = simulation.calculate('f7uf', period)
        f7xs = simulation.calculate('f7xs', period)
        f7xt = simulation.calculate('f7xt', period)
        f7xu = simulation.calculate('f7xu', period)
        f7xw = simulation.calculate('f7xw', period)
        f7xy = simulation.calculate('f7xy', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.dfppce

        base = f7uf + f7xs + f7xt + f7xu + f7xw + f7xy
        max1 = P.max * rbg_int
        return period, P.taux * min_(base, max1)

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Dons aux autres oeuvres et dons effectués pour le financement des partis
        politiques et des campagnes électorales (2011-2013)
        '''
        period = period.start.offset('first-of', 'year').period('year')
        rbg_int = simulation.calculate('rbg_int', period)
        f7uf = simulation.calculate('f7uf', period)
        f7xs = simulation.calculate('f7xs', period)
        f7xt = simulation.calculate('f7xt', period)
        f7xu = simulation.calculate('f7xu', period)
        f7xw = simulation.calculate('f7xw', period)
        f7xy = simulation.calculate('f7xy', period)
        f7vc = simulation.calculate('f7vc', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.dfppce

        base = f7uf + f7vc + f7xs + f7xt + f7xu + f7xw + f7xy
        max1 = P.max * rbg_int
        return period, P.taux * min_(base, max1)

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Dons aux autres oeuvres et dons effectués pour le financement des partis
        politiques et des campagnes électorales (2011-2013)
        '''
        period = period.start.offset('first-of', 'year').period('year')
        rbg_int = simulation.calculate('rbg_int', period)
        f7uf = simulation.calculate('f7uf', period)
        f7xs = simulation.calculate('f7xs', period)
        f7xt = simulation.calculate('f7xt', period)
        f7xu = simulation.calculate('f7xu', period)
        f7xw = simulation.calculate('f7xw', period)
        f7xy = simulation.calculate('f7xy', period)
        f7vc = simulation.calculate('f7vc', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.dfppce

        base = min_(P.max_niv, f7uf) + f7vc + f7xs + f7xt + f7xu + f7xw + f7xy
        max1 = P.max * rbg_int
        return period, P.taux * min_(base, max1)

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Dons aux autres oeuvres et dons effectués pour le financement des partis
        politiques et des campagnes électorales (2011-2013)
        '''
        period = period.start.offset('first-of', 'year').period('year')
        rbg_int = simulation.calculate('rbg_int', period)
        f7uf = simulation.calculate('f7uf', period)
        f7uh = simulation.calculate('f7uh', period)
        f7xs = simulation.calculate('f7xs', period)
        f7xt = simulation.calculate('f7xt', period)
        f7xu = simulation.calculate('f7xu', period)
        f7xw = simulation.calculate('f7xw', period)
        f7xy = simulation.calculate('f7xy', period)
        f7vc = simulation.calculate('f7vc', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.dfppce

        base = min_(P.max_niv, f7uf + f7uh) + f7vc + f7xs + f7xt + f7xu + f7xw + f7xy
        max1 = P.max * rbg_int
        return period, P.taux * min_(base, max1)


    # TODO: note de bas de page
    #       Introduire plus de détails dans la déclaration pour séparer les dons aux partis poitiques
    #       et aux candidats des autres dons


# Outre-mer : TODO: plafonnement, cf. 2041-GE 2042-IOM
@reference_formula
class doment(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"doment"

    @dated_function(start = date(2005, 1, 1), stop = date(2005, 12, 31))
    def function_20050101_20051231(self, simulation, period):
        '''
        Investissements dans les DOM-TOM dans le cadre d'une entrepise.
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ur = simulation.calculate('f7ur', period)
        f7oz = simulation.calculate('f7oz', period)
        f7pz = simulation.calculate('f7pz', period)
        f7qz = simulation.calculate('f7qz', period)
        f7rz = simulation.calculate('f7rz', period)

        return period,  f7ur + f7oz + f7pz + f7qz + f7rz

    @dated_function(start = date(2006, 1, 1), stop = date(2008, 12, 31))
    def function_20060101_20081231(self, simulation, period):
        '''
        Investissements dans les DOM-TOM dans le cadre d'une entrepise.
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ur = simulation.calculate('f7ur', period)
        f7oz = simulation.calculate('f7oz', period)
        f7pz = simulation.calculate('f7pz', period)
        f7qz = simulation.calculate('f7qz', period)
        f7rz = simulation.calculate('f7rz', period)
        f7sz = simulation.calculate('f7sz', period)

        return period,  f7ur + f7oz + f7pz + f7qz + f7rz + f7sz

    @dated_function(start = date(2009, 1, 1), stop = date(2009, 12, 31))
    def function_20090101_20091231(self, simulation, period):
        '''
        Investissements dans les DOM-TOM dans le cadre d'une entrepise.
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7oz = simulation.calculate('f7oz', period)
        f7pz = simulation.calculate('f7pz', period)
        f7qz = simulation.calculate('f7qz', period)
        f7rz = simulation.calculate('f7rz', period)
        f7sz = simulation.calculate('f7sz', period)
        f7qe = simulation.calculate('f7qe', period)
        f7qf = simulation.calculate('f7qf', period)
        f7qg = simulation.calculate('f7qg', period)
        f7qh = simulation.calculate('f7qh', period)
        f7qi = simulation.calculate('f7qi', period)
        f7qj = simulation.calculate('f7qj', period)

        return period,  f7oz + f7pz + f7qz + f7rz + f7sz + f7qe + f7qf + f7qg + f7qh + f7qi + f7qj

    @dated_function(start = date(2010, 1, 1), stop = date(2010, 12, 31))
    def function_20100101_20101231(self, simulation, period):
        '''
        Investissements dans les DOM-TOM dans le cadre d'une entrepise.
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7oz = simulation.calculate('f7oz', period)
        f7pz = simulation.calculate('f7pz', period)
        f7qz = simulation.calculate('f7qz', period)
        f7rz = simulation.calculate('f7rz', period)
        f7qe = simulation.calculate('f7qe', period)
        f7qf = simulation.calculate('f7qf', period)
        f7qg = simulation.calculate('f7qg', period)
        f7qh = simulation.calculate('f7qh', period)
        f7qi = simulation.calculate('f7qi', period)
        f7qj = simulation.calculate('f7qj', period)
        f7qo = simulation.calculate('f7qo', period)
        f7qp = simulation.calculate('f7qp', period)
        f7qq = simulation.calculate('f7qq', period)
        f7qr = simulation.calculate('f7qr', period)
        f7qs = simulation.calculate('f7qs', period)
        f7mm = simulation.calculate('f7mm', period)
        f7ma = simulation.calculate('f7ma', period)
        f7lg = simulation.calculate('f7lg', period)
        f7ks = simulation.calculate('f7ks', period)
        f7ls = simulation.calculate('f7ls', period)

        return period, (f7oz + f7pz + f7qz + f7rz + f7qe + f7qf + f7qg + f7qh + f7qi + f7qj + f7qo + f7qp + f7qq + f7qr + f7qs +
                    f7mm + f7ma + f7lg + f7ks + f7ls)

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Investissements dans les DOM-TOM dans le cadre d'une entrepise.
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ks = simulation.calculate('f7ks', period)
        f7kt = simulation.calculate('f7kt', period)
        f7ku = simulation.calculate('f7ku', period)
        f7lg = simulation.calculate('f7lg', period)
        f7lh = simulation.calculate('f7lh', period)
        f7li = simulation.calculate('f7li', period)
        f7mm = simulation.calculate('f7mm', period)
        f7ma = simulation.calculate('f7ma', period)
        f7mb = simulation.calculate('f7mb', period)
        f7mc = simulation.calculate('f7mc', period)
        f7mn = simulation.calculate('f7mn', period)
        f7oz = simulation.calculate('f7oz', period)
        f7pa = simulation.calculate('f7pa', period)
        f7pb = simulation.calculate('f7pb', period)
        f7pd = simulation.calculate('f7pd', period)
        f7pe = simulation.calculate('f7pe', period)
        f7pf = simulation.calculate('f7pf', period)
        f7ph = simulation.calculate('f7ph', period)
        f7pi = simulation.calculate('f7pi', period)
        f7pj = simulation.calculate('f7pj', period)
        f7pl = simulation.calculate('f7pl', period)
        f7pz = simulation.calculate('f7pz', period)
        f7qz = simulation.calculate('f7qz', period)
        f7qe = simulation.calculate('f7qe', period)
        f7qf = simulation.calculate('f7qf', period)
        f7qg = simulation.calculate('f7qg', period)
        f7qh = simulation.calculate('f7qh', period)
        f7qi = simulation.calculate('f7qi', period)
        f7qo = simulation.calculate('f7qo', period)
        f7qp = simulation.calculate('f7qp', period)
        f7qq = simulation.calculate('f7qq', period)
        f7qr = simulation.calculate('f7qr', period)
        f7qv = simulation.calculate('f7qv', period)

        return period, (f7ks + f7kt + f7ku + f7lg + f7lh + f7li + f7mb + f7mn + f7mc + f7mm + f7ma +  f7oz + f7pa + f7pb + f7pd +
                    f7pe + f7pf + f7ph + f7pi + f7pj + f7pl + f7pz + f7qz + f7qf + f7qg + f7qh + f7qi + f7qo +
                    f7qp + f7qq + f7qr + f7qe + f7qv)

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Investissements dans les DOM-TOM dans le cadre d'une entrepise.
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ks = simulation.calculate('f7ks', period)
        f7kt = simulation.calculate('f7kt', period)
        f7ku = simulation.calculate('f7ku', period)
        f7lg = simulation.calculate('f7lg', period)
        f7lh = simulation.calculate('f7lh', period)
        f7li = simulation.calculate('f7li', period)
        f7ma = simulation.calculate('f7ma', period)
        f7mb = simulation.calculate('f7mb', period)
        f7mc = simulation.calculate('f7mc', period)
        f7mm = simulation.calculate('f7mm', period)
        f7mn = simulation.calculate('f7mn', period)
        f7nu = simulation.calculate('f7nu', period)
        f7nv = simulation.calculate('f7nv', period)
        f7nw = simulation.calculate('f7nw', period)
        f7ny = simulation.calculate('f7ny', period)
        f7pa = simulation.calculate('f7pa', period)
        f7pb = simulation.calculate('f7pb', period)
        f7pd = simulation.calculate('f7pd', period)
        f7pe = simulation.calculate('f7pe', period)
        f7pf = simulation.calculate('f7pf', period)
        f7ph = simulation.calculate('f7ph', period)
        f7pi = simulation.calculate('f7pi', period)
        f7pj = simulation.calculate('f7pj', period)
        f7pl = simulation.calculate('f7pl', period)
        f7pm = simulation.calculate('f7pm', period)
        f7pn = simulation.calculate('f7pn', period)
        f7po = simulation.calculate('f7po', period)
        f7pp = simulation.calculate('f7pp', period)
        f7pr = simulation.calculate('f7pr', period)
        f7ps = simulation.calculate('f7ps', period)
        f7pt = simulation.calculate('f7pt', period)
        f7pu = simulation.calculate('f7pu', period)
        f7pw = simulation.calculate('f7pw', period)
        f7px = simulation.calculate('f7px', period)
        f7py = simulation.calculate('f7py', period)
        f7pz = simulation.calculate('f7pz', period)
        f7qe = simulation.calculate('f7qe', period)
        f7qf = simulation.calculate('f7qf', period)
        f7qg = simulation.calculate('f7qg', period)
        f7qi = simulation.calculate('f7qi', period)
        f7qo = simulation.calculate('f7qo', period)
        f7qp = simulation.calculate('f7qp', period)
        f7qr = simulation.calculate('f7qr', period)
        f7qv = simulation.calculate('f7qv', period)
        f7qz = simulation.calculate('f7qz', period)
        f7rg = simulation.calculate('f7rg', period)
        f7ri = simulation.calculate('f7ri', period)
        f7rj = simulation.calculate('f7rj', period)
        f7rk = simulation.calculate('f7rk', period)
        f7rl = simulation.calculate('f7rl', period)
        f7rm = simulation.calculate('f7rm', period)
        f7ro = simulation.calculate('f7ro', period)
        f7rp = simulation.calculate('f7rp', period)
        f7rq = simulation.calculate('f7rq', period)
        f7rr = simulation.calculate('f7rr', period)
        f7rt = simulation.calculate('f7rt', period)
        f7ru = simulation.calculate('f7ru', period)
        f7rv = simulation.calculate('f7rv', period)
        f7rw = simulation.calculate('f7rw', period)
        f7rx = simulation.calculate('f7rx', period)
        f7ry = simulation.calculate('f7ry', period)

        return period, (f7ks + f7kt + f7ku + f7lg + f7lh + f7li + f7ma + f7mb + f7mc + f7mm + f7mn +  f7pz + f7nu + f7nv + f7nw +
                    f7ny + f7pa + f7pb + f7pd + f7pe + f7pf + f7ph + f7pi + f7pj + f7pl + f7pm + f7pn + f7po + f7pp + f7pr +
                    f7ps + f7pt + f7pu + f7pw + f7px + f7py + f7qe + f7qf + f7qg + f7qi + f7qo + f7qp + f7qr + f7qv + f7qz +
                    f7rg + f7ri + f7rj + f7rk + f7rl + f7rm + f7ro + f7rp + f7rq + f7rr + f7rt + f7ru + f7rv + f7rw)

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Investissements dans les DOM-TOM dans le cadre d'une entrepise.
        '''
        period = period.start.offset('first-of', 'year').period('year')
        fhsa = simulation.calculate('fhsa', period)
        fhsb = simulation.calculate('fhsb', period)
        fhsf = simulation.calculate('fhsf', period)
        fhsg = simulation.calculate('fhsg', period)
        fhsc = simulation.calculate('fhsc', period)
        fhsh = simulation.calculate('fhsh', period)
        fhse = simulation.calculate('fhse', period)
        fhsj = simulation.calculate('fhsj', period)
        fhsk = simulation.calculate('fhsk', period)
        fhsl = simulation.calculate('fhsl', period)
        fhsp = simulation.calculate('fhsp', period)
        fhsq = simulation.calculate('fhsq', period)
        fhsm = simulation.calculate('fhsm', period)
        fhsr = simulation.calculate('fhsr', period)
        fhso = simulation.calculate('fhso', period)
        fhst = simulation.calculate('fhst', period)
        fhsu = simulation.calculate('fhsu', period)
        fhsv = simulation.calculate('fhsv', period)
        fhsw = simulation.calculate('fhsw', period)
        fhsz = simulation.calculate('fhsz', period)
        fhta = simulation.calculate('fhta', period)
        fhtb = simulation.calculate('fhtb', period)
        fhtd = simulation.calculate('fhtd', period)
        f7ks = simulation.calculate('f7ks', period)
        f7kt = simulation.calculate('f7kt', period)
        f7ku = simulation.calculate('f7ku', period)
        f7lg = simulation.calculate('f7lg', period)
        f7lh = simulation.calculate('f7lh', period)
        f7li = simulation.calculate('f7li', period)
        f7ma = simulation.calculate('f7ma', period)
        f7mb = simulation.calculate('f7mb', period)
        f7mc = simulation.calculate('f7mc', period)
        f7mm = simulation.calculate('f7mm', period)
        f7mn = simulation.calculate('f7mn', period)
        f7nu = simulation.calculate('f7nu', period)
        f7nv = simulation.calculate('f7nv', period)
        f7nw = simulation.calculate('f7nw', period)
        f7ny = simulation.calculate('f7ny', period)
        f7pa = simulation.calculate('f7pa', period)
        f7pb = simulation.calculate('f7pb', period)
        f7pd = simulation.calculate('f7pd', period)
        f7pe = simulation.calculate('f7pe', period)
        f7pf = simulation.calculate('f7pf', period)
        f7ph = simulation.calculate('f7ph', period)
        f7pi = simulation.calculate('f7pi', period)
        f7pj = simulation.calculate('f7pj', period)
        f7pl = simulation.calculate('f7pl', period)
        f7pm = simulation.calculate('f7pm', period)
        f7pn = simulation.calculate('f7pn', period)
        f7po = simulation.calculate('f7po', period)
        f7pp = simulation.calculate('f7pp', period)
        f7pr = simulation.calculate('f7pr', period)
        f7ps = simulation.calculate('f7ps', period)
        f7pt = simulation.calculate('f7pt', period)
        f7pu = simulation.calculate('f7pu', period)
        f7pw = simulation.calculate('f7pw', period)
        f7px = simulation.calculate('f7px', period)
        f7py = simulation.calculate('f7py', period)
        f7qe = simulation.calculate('f7qe', period)
        f7qf = simulation.calculate('f7qf', period)
        f7qg = simulation.calculate('f7qg', period)
        f7qi = simulation.calculate('f7qi', period)
        f7qo = simulation.calculate('f7qo', period)
        f7qp = simulation.calculate('f7qp', period)
        f7qr = simulation.calculate('f7qr', period)
        f7qv = simulation.calculate('f7qv', period)
        f7qz = simulation.calculate('f7qz', period)
        f7rg = simulation.calculate('f7rg', period)
        f7ri = simulation.calculate('f7ri', period)
        f7rj = simulation.calculate('f7rj', period)
        f7rk = simulation.calculate('f7rk', period)
        f7rl = simulation.calculate('f7rl', period)
        f7rm = simulation.calculate('f7rm', period)
        f7ro = simulation.calculate('f7ro', period)
        f7rp = simulation.calculate('f7rp', period)
        f7rq = simulation.calculate('f7rq', period)
        f7rr = simulation.calculate('f7rr', period)
        f7rt = simulation.calculate('f7rt', period)
        f7ru = simulation.calculate('f7ru', period)
        f7rv = simulation.calculate('f7rv', period)
        f7rw = simulation.calculate('f7rw', period)
        f7ry = simulation.calculate('f7ry', period)

        return period, (fhsa + fhsb + fhsf + fhsg + fhsc + fhsh + fhse + fhsj + fhsk + fhsl + fhsp + fhsq + fhsm + fhsr + fhso +
                    fhst + fhsu + fhsv + fhsw + fhsz + fhta + fhtb + fhtd + f7ks + f7kt + f7ku + f7lg + f7lh + f7li + f7ma +
                    f7mb + f7mc + f7mm + f7mn + f7nu + f7nv + f7nw + f7ny + f7pa + f7pb + f7pd + f7pe + f7pf + f7ph + f7pi +
                    f7pj + f7pl + f7pm + f7pn + f7po + f7pp + f7pr + f7ps + f7pt + f7pu + f7pw + f7px + f7py + f7qe + f7qf +
                    f7qg + f7qi + f7qo + f7qp + f7qr + f7qv + f7qz + f7rg + f7ri + f7rj + f7rk + f7rl + f7rm + f7ro + f7rp +
                    f7rq + f7rr + f7rt + f7ru + f7rv + f7rw)


#TODO: vérifier pour 2002
#TODO: pb 7ul 2005-2009 (ITRED = 0 au lieu de 20€ (forfaitaire), dû à ça : Cochez [7UL] si vous déclarez en ligne pour
#la première fois vos revenus 2008 et si vous utilisez un moyen automatique de paiement (prélèvement mensuel ou à
#l'échéance ou paiement par voie électronique))


#TODO: vérifier les dates des variables de doment et domsoc (y sont-elles encore en 2013 par ex ?)

@reference_formula
class domlog(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"domlog"

    @dated_function(start = date(2002, 1, 1), stop = date(2002, 12, 31))
    def function_20020101_20021231(self, simulation, period):
        '''
        Investissements OUTRE-MER dans le secteur du logement et autres secteurs d’activité
        2002
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ua = simulation.calculate('f7ua', period)
        f7ub = simulation.calculate('f7ub', period)
        f7uc = simulation.calculate('f7uc', period)
        f7uj = simulation.calculate('f7uj', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.domlog

        return period, P.taux1 * f7uj + P.taux2 * (f7ua + f7ub + f7uc)

    @dated_function(start = date(2003, 1, 1), stop = date(2004, 12, 31))
    def function_20030101_20041231(self, simulation, period):
        '''
        Investissements OUTRE-MER dans le secteur du logement et autres secteurs d’activité
        2003-2004
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ua = simulation.calculate('f7ua', period)
        f7ub = simulation.calculate('f7ub', period)
        f7uc = simulation.calculate('f7uc', period)
        f7ui = simulation.calculate('f7ui', period)
        f7uj = simulation.calculate('f7uj', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.domlog

        return period, P.taux1 * f7uj + P.taux2 * (f7ua + f7ub + f7uc) + f7ui

    @dated_function(start = date(2005, 1, 1), stop = date(2007, 12, 31))
    def function_20050101_20071231(self, simulation, period):
        '''
        Investissements OUTRE-MER dans le secteur du logement et autres secteurs d’activité
        2005-2007
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ua = simulation.calculate('f7ua', period)
        f7ub = simulation.calculate('f7ub', period)
        f7uc = simulation.calculate('f7uc', period)
        f7ui = simulation.calculate('f7ui', period)
        f7uj = simulation.calculate('f7uj', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.domlog

        return period, P.taux1 * f7uj + P.taux2 * (f7ua + f7ub) + f7ui

    @dated_function(start = date(2008, 1, 1), stop = date(2008, 12, 31))
    def function_20080101_20081231(self, simulation, period):
        '''
        Investissements OUTRE-MER dans le secteur du logement et autres secteurs d’activité
        2008
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ui = simulation.calculate('f7ui', period)

        return period, f7ui

    @dated_function(start = date(2009, 1, 1), stop = date(2009, 12, 31))
    def function_20090101_20091231(self, simulation, period):
        '''
        Investissements OUTRE-MER dans le secteur du logement et autres secteurs d’activité
        2009
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7qb = simulation.calculate('f7qb', period)
        f7qc = simulation.calculate('f7qc', period)
        f7qd = simulation.calculate('f7qd', period)
        f7qk = simulation.calculate('f7qk', period)

        return period, f7qb + f7qc + f7qd + f7qk / 2

    @dated_function(start = date(2010, 1, 1), stop = date(2010, 12, 31))
    def function_20100101_20101231(self, simulation, period):
        '''
        Investissements OUTRE-MER dans le secteur du logement et autres secteurs d’activité
        2010
        TODO: Plafonnement sur la notice
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7qb = simulation.calculate('f7qb', period)
        f7qc = simulation.calculate('f7qc', period)
        f7qd = simulation.calculate('f7qd', period)
        f7ql = simulation.calculate('f7ql', period)
        f7qt = simulation.calculate('f7qt', period)
        f7qm = simulation.calculate('f7qm', period)

        return period, f7qb + f7qc + f7qd + f7ql + f7qt + f7qm

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Investissements OUTRE-MER dans le secteur du logement et autres secteurs d’activité
        2011
        TODO: Plafonnement sur la notice
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7qb = simulation.calculate('f7qb', period)
        f7qc = simulation.calculate('f7qc', period)
        f7qd = simulation.calculate('f7qd', period)
        f7ql = simulation.calculate('f7ql', period)
        f7qm = simulation.calculate('f7qm', period)
        f7qt = simulation.calculate('f7qt', period)
        f7oa = simulation.calculate('f7oa', period)
        f7ob = simulation.calculate('f7ob', period)
        f7oc = simulation.calculate('f7oc', period)
        f7oh = simulation.calculate('f7oh', period)
        f7oi = simulation.calculate('f7oi', period)
        f7oj = simulation.calculate('f7oj', period)
        f7ok = simulation.calculate('f7ok', period)

        return period, f7qb + f7qc + f7qd + f7ql + f7qm + f7qt + f7oa + f7ob + f7oc + f7oh + f7oi + f7oj + f7ok

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Investissements OUTRE-MER dans le secteur du logement et autres secteurs d’activité
        2012
        TODO: Plafonnement sur la notice
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7qb = simulation.calculate('f7qb', period)
        f7qc = simulation.calculate('f7qc', period)
        f7qd = simulation.calculate('f7qd', period)
        f7ql = simulation.calculate('f7ql', period)
        f7qm = simulation.calculate('f7qm', period)
        f7qt = simulation.calculate('f7qt', period)
        f7oa = simulation.calculate('f7oa', period)
        f7ob = simulation.calculate('f7ob', period)
        f7oc = simulation.calculate('f7oc', period)
        f7oh = simulation.calculate('f7oh', period)
        f7oi = simulation.calculate('f7oi', period)
        f7oj = simulation.calculate('f7oj', period)
        f7ok = simulation.calculate('f7ok', period)
        f7ol = simulation.calculate('f7ol', period)
        f7om = simulation.calculate('f7om', period)
        f7on = simulation.calculate('f7on', period)
        f7oo = simulation.calculate('f7oo', period)
        f7op = simulation.calculate('f7op', period)
        f7oq = simulation.calculate('f7oq', period)
        f7or = simulation.calculate('f7or', period)
        f7os = simulation.calculate('f7os', period)
        f7ot = simulation.calculate('f7ot', period)
        f7ou = simulation.calculate('f7ou', period)
        f7ov = simulation.calculate('f7ov', period)
        f7ow = simulation.calculate('f7ow', period)

        return period, (f7qb + f7qc + f7qd + f7ql + f7qm + f7qt + f7oa + f7ob + f7oc + f7oh + f7oi + f7oj + f7ok + f7ol + f7om +
                    f7on + f7oo + f7op + f7oq + f7or + f7os + f7ot + f7ou + f7ov + f7ow)

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Investissements OUTRE-MER dans le secteur du logement et autres secteurs d’activité
        2013
        TODO: Plafonnement sur la notice
        '''
        period = period.start.offset('first-of', 'year').period('year')
        fhod = simulation.calculate('fhod', period)
        fhoe = simulation.calculate('fhoe', period)
        fhof = simulation.calculate('fhof', period)
        fhog = simulation.calculate('fhog', period)
        fhox = simulation.calculate('fhox', period)
        fhoy = simulation.calculate('fhoy', period)
        fhoz = simulation.calculate('fhoz', period)
        f7qb = simulation.calculate('f7qb', period)
        f7qc = simulation.calculate('f7qc', period)
        f7qd = simulation.calculate('f7qd', period)
        f7ql = simulation.calculate('f7ql', period)
        f7qm = simulation.calculate('f7qm', period)
        f7qt = simulation.calculate('f7qt', period)
        f7oa = simulation.calculate('f7oa', period)
        f7ob = simulation.calculate('f7ob', period)
        f7oc = simulation.calculate('f7oc', period)
        f7oh = simulation.calculate('f7oh', period)
        f7oi = simulation.calculate('f7oi', period)
        f7oj = simulation.calculate('f7oj', period)
        f7ok = simulation.calculate('f7ok', period)
        f7ol = simulation.calculate('f7ol', period)
        f7om = simulation.calculate('f7om', period)
        f7on = simulation.calculate('f7on', period)
        f7oo = simulation.calculate('f7oo', period)
        f7op = simulation.calculate('f7op', period)
        f7oq = simulation.calculate('f7oq', period)
        f7or = simulation.calculate('f7or', period)
        f7os = simulation.calculate('f7os', period)
        f7ot = simulation.calculate('f7ot', period)
        f7ou = simulation.calculate('f7ou', period)
        f7ov = simulation.calculate('f7ov', period)
        f7ow = simulation.calculate('f7ow', period)

        return period, (f7qb + f7qc + f7qd + f7ql + f7qm + f7qt + f7oa + f7ob + f7oc + f7oh + f7oi + f7oj + f7ok + f7ol + f7om +
                    f7on + f7oo + f7op + f7oq + f7or + f7os + f7ot + f7ou + f7ov + f7ow + fhod + fhoe +
                    fhof + fhog + fhox + fhoy + fhoz)


#En accord avec la DGFiP mais pas de 7ub et 7uj dans la notice


@reference_formula
class domsoc(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"domsoc"

    @dated_function(start = date(2010, 1, 1), stop = date(2012, 12, 31))
    def function_20100101_20121231(self, simulation, period):
        '''
        Investissements outre-mer dans le logement social (déclaration n°2042 IOM)
        2010-
        TODO plafonnement à 15% f7qa / liens avec autres investissments ?
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7qn = simulation.calculate('f7qn', period)
        f7qk = simulation.calculate('f7qk', period)
        f7qu = simulation.calculate('f7qu', period)
        f7kg = simulation.calculate('f7kg', period)
        f7kh = simulation.calculate('f7kh', period)
        f7ki = simulation.calculate('f7ki', period)
        f7qj = simulation.calculate('f7qj', period)
        f7qs = simulation.calculate('f7qs', period)
        f7qw = simulation.calculate('f7qw', period)
        f7qx = simulation.calculate('f7qx', period)

        return period,  f7qn + f7qk + f7qu + f7kg + f7kh + f7ki + f7qj + f7qs + f7qw + f7qx

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Investissements outre-mer dans le logement social (déclaration n°2042 IOM)
        2013
        TODO plafonnement à 15% f7qa / liens avec autres investissments ?
        '''
        period = period.start.offset('first-of', 'year').period('year')
        fhra = simulation.calculate('fhra', period)
        fhrb = simulation.calculate('fhrb', period)
        fhrc = simulation.calculate('fhrc', period)
        fhrd = simulation.calculate('fhrd', period)
        f7qn = simulation.calculate('f7qn', period)
        f7qk = simulation.calculate('f7qk', period)
        f7qu = simulation.calculate('f7qu', period)
        f7kg = simulation.calculate('f7kg', period)
        f7kh = simulation.calculate('f7kh', period)
        f7ki = simulation.calculate('f7ki', period)
        f7qj = simulation.calculate('f7qj', period)
        f7qs = simulation.calculate('f7qs', period)
        f7qw = simulation.calculate('f7qw', period)
        f7qx = simulation.calculate('f7qx', period)

        return period,  fhra + fhrb + fhrc + fhrd + f7qn + f7qk + f7qu + f7kg + f7kh + f7ki + f7qj + f7qs + f7qw + f7qx


@reference_formula
class donapd(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"donapd"

    @dated_function(start = date(2002, 1, 1), stop = date(2010, 12, 31))
    def function_20020101_20101231(self, simulation, period):
        '''
        Dons effectués à  des organises d'aide aux personnes en difficulté (2002-2010)
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ud = simulation.calculate('f7ud', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.donapd

        return period, P.taux * min_(f7ud, P.max)

    @dated_function(start = date(2011, 1, 1), stop = date(2013, 12, 31))
    def function_20110101_20131231(self, simulation, period):
        '''
        Dons effectués à  des organises d'aide aux personnes en difficulté (2011-2013)
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ud = simulation.calculate('f7ud', period)
        f7va = simulation.calculate('f7va', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.donapd

        return period, P.taux * min_(f7ud + f7va, P.max)


@reference_formula
class duflot(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"duflot"
    start_date = date(2013, 1, 1)

    def function(self, simulation, period):
        '''
        Investissements locatifs interméiaires (loi Duflot)
        2013-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7gh = simulation.calculate('f7gh', period)
        f7gi = simulation.calculate('f7gi', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.duflot

        return period, min_(P.plafond, P.taux_m * f7gh + P.taux_om * f7gi) / 9


#TODO: / 5 dans trois TOM

@reference_formula
class ecodev(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"ecodev"
    start_date = date(2009, 1, 1)
    stop_date = date(2009, 12, 31)

    def function(self, simulation, period):
        '''
        Sommes versées sur un compte épargne codéveloppement (case 7UH)
        2009
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7uh = simulation.calculate('f7uh', period)
        rbg_int = simulation.calculate('rbg_int', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.ecodev

        return period, min_(f7uh * P.taux, min_(P.base * rbg_int, P.max))  # page3 ligne 18


@reference_formula
class ecpess(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"ecpess"

    def function(self, simulation, period):
        '''
        Réduction d'impôt au titre des enfants à charge poursuivant leurs études secondaires ou supérieures
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ea = simulation.calculate('f7ea', period)
        f7eb = simulation.calculate('f7eb', period)
        f7ec = simulation.calculate('f7ec', period)
        f7ed = simulation.calculate('f7ed', period)
        f7ef = simulation.calculate('f7ef', period)
        f7eg = simulation.calculate('f7eg', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.ecpess

        return period, (P.col * (f7ea + f7eb / 2) +
                P.lyc * (f7ec + f7ed / 2) +
                P.sup * (f7ef + f7eg / 2))


@reference_formula
class garext(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"garext"

    @dated_function(start = date(2002, 1, 1), stop = date(2002, 12, 31))
    def function_20020101_20021231(self, simulation, period):
        '''
        Frais de garde des enfants à l’extérieur du domicile (cases GA, GB, GC de la 2042)
        et GE, GF, GG
        2002
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ga = simulation.calculate('f7ga', period)
        f7gb = simulation.calculate('f7gb', period)
        f7gc = simulation.calculate('f7gc', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.garext

        max1 = P.max
        return period, P.taux * (min_(f7ga, max1) + min_(f7gb, max1) + min_(f7gc, max1))

    @dated_function(start = date(2003, 1, 1), stop = date(2005, 12, 31))
    def function_20030101_20051231(self, simulation, period):
        '''
        Frais de garde des enfants à l’extérieur du domicile (cases GA, GB, GC de la 2042)
        et GE, GF, GG
        2003-2005
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ga = simulation.calculate('f7ga', period)
        f7gb = simulation.calculate('f7gb', period)
        f7gc = simulation.calculate('f7gc', period)
        f7ge = simulation.calculate('f7ge', period)
        f7gf = simulation.calculate('f7gf', period)
        f7gg = simulation.calculate('f7gg', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.garext

        max1 = P.max
        max2 = P.max / 2
        return period, P.taux * (min_(f7ga, max1) +
                           min_(f7gb, max1) +
                           min_(f7gc, max1) +
                           min_(f7ge, max2) +
                           min_(f7gf, max2) +
                           min_(f7gg, max2))


@reference_formula
class intagr(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"intagr"
    start_date = date(2005, 1, 1)

    def function(self, simulation, period):
        '''
        Intérêts pour paiement différé accordé aux agriculteurs
        2005-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7um = simulation.calculate('f7um', period)
        marpac = simulation.calculate('marpac', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.intagr

        max1 = P.max * (1 + marpac)
        return period, P.taux * min_(f7um, max1)


@reference_formula
class intcon(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"intcon"
    start_date = date(2004, 1, 1)
    stop_date = date(2005, 12, 31)

    def function(self, simulation, period):
        '''
        Intérêts des prêts à la consommation (case UH)
        2004-2005
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7uh = simulation.calculate('f7uh', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.intcon

        max1 = P.max
        return period, P.taux * min_(f7uh, max1)


@reference_formula
class intemp(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"intemp"
    start_date = date(2002, 1, 1)
    stop_date = date(2003, 12, 31)

    def function(self, simulation, period):
        '''
        Intérêts d'emprunts
        2002-2003
        '''
        period = period.start.offset('first-of', 'year').period('year')
        nb_pac = simulation.calculate('nb_pac', period)
        f7wg = simulation.calculate('f7wg', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.intemp

        max1 = P.max + P.pac * nb_pac
        return period, P.taux * min_(f7wg, max1)


@reference_formula
class invfor(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"invfor"

    @dated_function(start = date(2002, 1, 1), stop = date(2005, 12, 31))
    def function_20020101_20051231(self, simulation, period):
        '''
        Investissements forestiers pour 2002-2005
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7un = simulation.calculate('f7un', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invfor

        seuil = P.seuil * (marpac + 1)
        return period, P.taux * min_(f7un, seuil)

    @dated_function(start = date(2006, 1, 1), stop = date(2008, 12, 31))
    def function_20060101_20081231(self, simulation, period):
        '''
        Investissements forestiers pour 2006-2008
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7un = simulation.calculate('f7un', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invfor

        return period, P.taux * f7un

    @dated_function(start = date(2009, 1, 1), stop = date(2009, 12, 31))
    def function_20090101_20091231(self, simulation, period):
        '''
        Investissements forestiers pour 2009
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7un = simulation.calculate('f7un', period)
        f7up = simulation.calculate('f7up', period)
        f7uq = simulation.calculate('f7uq', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invfor

        return period, P.taux * (min_(f7un, P.seuil * (marpac + 1)) + min_(f7up, P.ifortra_seuil * (marpac + 1)) +
                min_(f7uq, P.iforges_seuil * (marpac + 1)))

    @dated_function(start = date(2010, 1, 1), stop = date(2010, 12, 31))
    def function_20100101_20101231(self, simulation, period):
        '''
        Investissements forestiers pour 2010
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7te = simulation.calculate('f7te', period)
        f7un = simulation.calculate('f7un', period)
        f7up = simulation.calculate('f7up', period)
        f7uq = simulation.calculate('f7uq', period)
        f7uu = simulation.calculate('f7uu', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invfor

        return period, (P.taux * (
            min_(f7un, P.seuil * (marpac + 1)) +
            min_(f7up + f7uu + f7te, P.ifortra_seuil * (marpac + 1)) +
            min_(f7uq, P.iforges_seuil * (marpac + 1))))

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Investissements forestiers pour 2011 cf. 2041 GK
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7te = simulation.calculate('f7te', period)
        f7tf = simulation.calculate('f7tf', period)
        f7ul = simulation.calculate('f7ul', period)
        f7un = simulation.calculate('f7un', period)
        f7up = simulation.calculate('f7up', period)
        f7uq = simulation.calculate('f7uq', period)
        f7uu = simulation.calculate('f7uu', period)
        f7uv = simulation.calculate('f7uv', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invfor

        max0 = max_(0, P.ifortra_seuil * (marpac + 1) - f7ul)
        max1 = max_(0, max0 - f7uu + f7te + f7uv + f7tf)
        return period, (P.taux * (
            min_(f7un, P.seuil * (marpac + 1)) +
            min_(f7up, max1) +
            min_(f7uq, P.iforges_seuil * (marpac + 1))) +
            P.report10 * min_(f7uu + f7te + f7uv + f7tf, max0) +
            P.taux_ass * min_(f7ul, P.ifortra_seuil * (marpac + 1)))

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Investissements forestiers pour 2012 cf. 2041 GK
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7te = simulation.calculate('f7te', period)
        f7tf = simulation.calculate('f7tf', period)
        f7tg = simulation.calculate('f7tg', period)
        f7ul = simulation.calculate('f7ul', period)
        f7un = simulation.calculate('f7un', period)
        f7up = simulation.calculate('f7up', period)
        f7uq = simulation.calculate('f7uq', period)
        f7uu = simulation.calculate('f7uu', period)
        f7uv = simulation.calculate('f7uv', period)
        f7uw = simulation.calculate('f7uw', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invfor

        max0 = max_(0, P.ifortra_seuil * (marpac + 1) - f7ul)
        max1 = max_(0, max0 - f7uu + f7te + f7uv + f7tf)
        max2 = max_(0, max1 - f7tg - f7uw)
        return period, (P.taux * (
            min_(f7un, P.seuil * (marpac + 1)) +
            min_(f7up, max2) +
            min_(f7uq, P.iforges_seuil * (marpac + 1))) +
            P.report10 * min_(f7uu + f7te + f7uv + f7tf, max0) +
            P.report11 * min_(f7tg + f7uw, max1) +
            P.taux_ass * min_(f7ul, P.ifortra_seuil * (marpac + 1)))

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Investissements forestiers pour 2013 cf. 2041 GK
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7te = simulation.calculate('f7te', period)
        f7tf = simulation.calculate('f7tf', period)
        f7tg = simulation.calculate('f7tg', period)
        f7th = simulation.calculate('f7th', period)
        f7ul = simulation.calculate('f7ul', period)
        f7un = simulation.calculate('f7un', period)
        f7up = simulation.calculate('f7up', period)
        f7uq = simulation.calculate('f7uq', period)
        f7uu = simulation.calculate('f7uu', period)
        f7uv = simulation.calculate('f7uv', period)
        f7uw = simulation.calculate('f7uw', period)
        f7ux = simulation.calculate('f7ux', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invfor

        max0 = max_(0, P.ifortra_seuil * (marpac + 1) - f7ul)
        max1 = max_(0, max0 - f7uu + f7te + f7uv + f7tf)
        max2 = max_(0, max1 - f7tg - f7uw)
        max3 = max_(0, max2 - f7th - f7ux)
        return period, (P.taux * (
            min_(f7un, P.seuil * (marpac + 1)) +
            min_(f7up, max3) +
            min_(f7uq, P.iforges_seuil * (marpac + 1))) +
            P.report10 * min_(f7uu + f7te + f7uv + f7tf, max0) +
            P.report11 * min_(f7tg + f7uw, max1) +
            P.report12 * min_(f7th + f7ux, max2) +
            P.taux_ass * min_(f7ul, P.ifortra_seuil * (marpac + 1)))


@reference_formula
class invlst(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"invlst"

    @dated_function(start = date(2004, 1, 1), stop = date(2004, 12, 31))
    def function_20040101_20041231(self, simulation, period):
        '''
        Investissements locatifs dans le secteur touristique
        2004
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7xc = simulation.calculate('f7xc', period)
        f7xd = simulation.calculate('f7xd', period)
        f7xe = simulation.calculate('f7xe', period)
        f7xf = simulation.calculate('f7xf', period)
        f7xg = simulation.calculate('f7xg', period)
        f7xh = simulation.calculate('f7xh', period)
        f7xi = simulation.calculate('f7xi', period)
        f7xj = simulation.calculate('f7xj', period)
        f7xk = simulation.calculate('f7xk', period)
        f7xl = simulation.calculate('f7xl', period)
        f7xm = simulation.calculate('f7xm', period)
        f7xn = simulation.calculate('f7xn', period)
        f7xo = simulation.calculate('f7xo', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invlst

        seuil1 = P.seuil1 * (1 + marpac)
        seuil2 = P.seuil2 * (1 + marpac)
        seuil3 = P.seuil3 * (1 + marpac)

        xc = P.taux_xc * min_(f7xc, seuil1 / 4)
        xd = P.taux_xd * f7xd
        xe = P.taux_xe * min_(f7xe, seuil1 / 6)
        xf = P.taux_xf * f7xf
        xg = P.taux_xg * min_(f7xg, seuil2)
        xh = P.taux_xh * min_(f7xh, seuil3)
        xi = P.taux_xi * min_(f7xi, seuil1 / 4)
        xj = P.taux_xj * f7xj
        xk = P.taux_xk * f7xk
        xl = P.taux_xl * min_(f7xl, seuil1 / 6)
        xm = P.taux_xm * f7xm
        xn = P.taux_xn * min_(f7xn, seuil1 / 6)
        xo = P.taux_xo * f7xo

        return period, around(xc + xd + xe + xf + xg + xh + xi + xj + xk + xl + xm + xn + xo)

    @dated_function(start = date(2005, 1, 1), stop = date(2010, 12, 31))
    def function_20050101_20101231(self, simulation, period):
        '''
        Investissements locatifs dans le secteur touristique
        2005-2010
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7xc = simulation.calculate('f7xc', period)
        f7xd = simulation.calculate('f7xd', period)
        f7xe = simulation.calculate('f7xe', period)
        f7xf = simulation.calculate('f7xf', period)
        f7xg = simulation.calculate('f7xg', period)
        f7xh = simulation.calculate('f7xh', period)
        f7xi = simulation.calculate('f7xi', period)
        f7xj = simulation.calculate('f7xj', period)
        f7xk = simulation.calculate('f7xk', period)
        f7xl = simulation.calculate('f7xl', period)
        f7xm = simulation.calculate('f7xm', period)
        f7xn = simulation.calculate('f7xn', period)
        f7xo = simulation.calculate('f7xo', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invlst

        seuil1 = P.seuil1 * (1 + marpac)
        seuil2 = P.seuil2 * (1 + marpac)
        seuil3 = P.seuil3 * (1 + marpac)

        xc = P.taux_xc * min_(f7xc, seuil1 / 6)
        xd = P.taux_xd * f7xd
        xe = P.taux_xe * min_(f7xe, seuil1 / 6)
        xf = P.taux_xf * f7xf
        xg = P.taux_xg * min_(f7xg, seuil2)
        xh = P.taux_xh * min_(f7xh, seuil2 - f7xg)
        xi = P.taux_xi * f7xi
        xj = P.taux_xj * f7xj
        xk = P.taux_xk * f7xk
        xl = P.taux_xl * min_(f7xl, seuil1 / 6)
        xm = P.taux_xm * f7xm
        xn = P.taux_xn * min_(f7xn, seuil1 / 6)
        xo = P.taux_xo * f7xo

        return period, around(xc + xd + xe + xf + xg + xh + xi + xj + xk + xl + xm + xn + xo)

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Investissements locatifs dans le secteur touristique
        2011
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7xa = simulation.calculate('f7xa', period)
        f7xb = simulation.calculate('f7xb', period)
        f7xc = simulation.calculate('f7xc', period)
        f7xd = simulation.calculate('f7xd', period)
        f7xe = simulation.calculate('f7xe', period)
        f7xf = simulation.calculate('f7xf', period)
        f7xg = simulation.calculate('f7xg', period)
        f7xh = simulation.calculate('f7xh', period)
        f7xi = simulation.calculate('f7xi', period)
        f7xj = simulation.calculate('f7xj', period)
        f7xk = simulation.calculate('f7xk', period)
        f7xl = simulation.calculate('f7xl', period)
        f7xm = simulation.calculate('f7xm', period)
        f7xn = simulation.calculate('f7xn', period)
        f7xo = simulation.calculate('f7xo', period)
        f7xp = simulation.calculate('f7xp', period)
        f7xq = simulation.calculate('f7xq', period)
        f7xr = simulation.calculate('f7xr', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invlst

        seuil1 = P.seuil1 * (1 + marpac)
        seuil2 = P.seuil2 * (1 + marpac)
        seuil3 = P.seuil3 * (1 + marpac)

        xc = P.taux_xc * min_(f7xc, seuil1 / 6)
        xa = P.taux_xa * min_(f7xa, seuil2)
        xg = P.taux_xg * min_(f7xg, seuil2 - f7xa)
        xb = P.taux_xb * min_(f7xb, seuil2 - f7xa - f7xg)
        xh = P.taux_xh * min_(f7xh, seuil2 - f7xa - f7xg - f7xb)
        xi = P.taux_xi * (f7xf + f7xi + f7xp)
        xj = P.taux_xj * (f7xm + f7xj + f7xq)
        xl = P.taux_xl * min_(f7xl, seuil1 / 6)
        xo = P.taux_xo * (f7xk + f7xo + f7xr)

        return period, around(xc + xa + xg + xb + xh + xi + xj + xl + xo)

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Investissements locatifs dans le secteur touristique
        2012
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7xa = simulation.calculate('f7xa', period)
        f7xb = simulation.calculate('f7xb', period)
        f7xc = simulation.calculate('f7xc', period)
        f7xd = simulation.calculate('f7xd', period)
        f7xe = simulation.calculate('f7xe', period)
        f7xf = simulation.calculate('f7xf', period)
        f7xg = simulation.calculate('f7xg', period)
        f7xh = simulation.calculate('f7xh', period)
        f7xi = simulation.calculate('f7xi', period)
        f7xj = simulation.calculate('f7xj', period)
        f7xk = simulation.calculate('f7xk', period)
        f7xl = simulation.calculate('f7xl', period)
        f7xm = simulation.calculate('f7xm', period)
        f7xn = simulation.calculate('f7xn', period)
        f7xo = simulation.calculate('f7xo', period)
        f7xp = simulation.calculate('f7xp', period)
        f7xq = simulation.calculate('f7xq', period)
        f7xr = simulation.calculate('f7xr', period)
        f7xv = simulation.calculate('f7xv', period)
        f7xx = simulation.calculate('f7xx', period)
        f7xz = simulation.calculate('f7xz', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invlst

        seuil1 = P.seuil1 * (1 + marpac)
        seuil2 = P.seuil2 * (1 + marpac)
        seuil3 = P.seuil3 * (1 + marpac)

        xc = P.taux_xc * min_(f7xc, seuil1 / 6)
        xa = P.taux_xa * min_(f7xa, seuil2)
        xg = P.taux_xg * min_(f7xg, seuil2 - f7xa)
        xx = P.taux_xx * min_(f7xx, seuil2 - f7xa - f7xg)
        xb = P.taux_xb * min_(f7xb, seuil2 - f7xa - f7xg - f7xx)
        xh = P.taux_xh * min_(f7xh, seuil2 - f7xa - f7xg - f7xb - f7xx)
        xz = P.taux_xz * min_(f7xz, seuil2 - f7xa - f7xg - f7xb - f7xx - f7xh)
        xi = P.taux_xi * (f7xf + f7xi + f7xp + f7xn)
        xj = P.taux_xj * (f7xm + f7xj + f7xq + f7xv)
        xl = P.taux_xl * min_(f7xl, seuil1 / 6)
        xo = P.taux_xo * (f7xk + f7xo + f7xr)

        return period, around(xc + xa + xg + xx + xb + xz + xh + xi + xj + xl + xo)

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Investissements locatifs dans le secteur touristique
        2013
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7uy = simulation.calculate('f7uy', period)
        f7uz = simulation.calculate('f7uz', period)
        f7xf = simulation.calculate('f7xf', period)
        f7xi = simulation.calculate('f7xi', period)
        f7xj = simulation.calculate('f7xj', period)
        f7xk = simulation.calculate('f7xk', period)
        f7xm = simulation.calculate('f7xm', period)
        f7xn = simulation.calculate('f7xn', period)
        f7xo = simulation.calculate('f7xo', period)
        f7xp = simulation.calculate('f7xp', period)
        f7xq = simulation.calculate('f7xq', period)
        f7xr = simulation.calculate('f7xr', period)
        f7xv = simulation.calculate('f7xv', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invlst

        xi = P.taux_xi * (f7xf + f7xi + f7xp + f7xn + f7uy)
        xj = P.taux_xj * (f7xm + f7xj + f7xq + f7xv + f7uz)
        xo = P.taux_xo * (f7xk + f7xo + f7xr)

        return period, around(xi + xj + xo)


@reference_formula
class invrev(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"invrev"
    start_date = date(2002, 1, 1)
    stop_date = date(2003, 12, 31)

    def function(self, simulation, period):
        '''
        Investissements locatifs dans les résidences de tourisme situées dans une zone de
        revitalisation rurale (cases GS, GT, XG, GU et GV)
        2002-2003
        TODO 1/4 codé en dur
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7gs = simulation.calculate('f7gs', period)
        f7gt = simulation.calculate('f7gt', period)
        f7xg = simulation.calculate('f7xg', period)
        f7gu = simulation.calculate('f7gu', period)
        f7gv = simulation.calculate('f7gv', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.invrev

        return period, (P.taux_gs * min_(f7gs, P.seuil_gs * (1 + marpac)) / 4 +
                 P.taux_gu * min_(f7gu, P.seuil_gu * (1 + marpac)) / 4 +
                 P.taux_xg * min_(f7xg, P.seuil_xg * (1 + marpac)) / 4 +
                 P.taux_gt * f7gt + P.taux_gt * f7gv)


@reference_formula
class locmeu(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"locmeu"

    @dated_function(start = date(2009, 1, 1), stop = date(2009, 12, 31))
    def function_20090101_20091231(self, simulation, period):
        '''
        Investissement en vue de la location meublée non professionnelle dans certains établissements ou résidences
        2009
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ij = simulation.calculate('f7ij', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.locmeu

        return period, P.taux * min_(P.max, f7ij) / 9

    @dated_function(start = date(2010, 1, 1), stop = date(2010, 12, 31))
    def function_20100101_20101231(self, simulation, period):
        '''
        Investissement en vue de la location meublée non professionnelle dans certains établissements ou résidences
        2010
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ij = simulation.calculate('f7ij', period)
        f7ik = simulation.calculate('f7ik', period)
        f7il = simulation.calculate('f7il', period)
        f7im = simulation.calculate('f7im', period)
        f7is = simulation.calculate('f7is', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.locmeu

        return period, ((min_(P.max, max_(f7ij, f7il)) + min_(P.max, f7im)) / 9 + f7ik) * P.taux + f7is

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Investissement en vue de la location meublée non professionnelle dans certains établissements ou résidences
        2011
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ij = simulation.calculate('f7ij', period)
        f7ik = simulation.calculate('f7ik', period)
        f7il = simulation.calculate('f7il', period)
        f7im = simulation.calculate('f7im', period)
        f7in = simulation.calculate('f7in', period)
        f7io = simulation.calculate('f7io', period)
        f7ip = simulation.calculate('f7ip', period)
        f7iq = simulation.calculate('f7iq', period)
        f7ir = simulation.calculate('f7ir', period)
        f7is = simulation.calculate('f7is', period)
        f7it = simulation.calculate('f7it', period)
        f7iu = simulation.calculate('f7iu', period)
        f7iv = simulation.calculate('f7iv', period)
        f7iw = simulation.calculate('f7iw', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.locmeu

        m20 = (maxi(f7ij, f7il, f7in, f7iv) == max_(f7il, f7in))
        return period, ((min_(P.max, maxi(f7ij, f7il, f7in, f7iv)) * (P.taux20 * m20 + P.taux18 * not_(m20)) +
                P.taux * (min_(P.max, max_(f7im, f7iw)) + min_(P.max, f7io))) / 9 +
            P.taux * max_(f7ik, f7ip + f7ir + f7iq) +
            f7is + f7iu + f7it)

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Investissement en vue de la location meublée non professionnelle dans certains établissements ou résidences
        2012
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ia = simulation.calculate('f7ia', period)
        f7ib = simulation.calculate('f7ib', period)
        f7ic = simulation.calculate('f7ic', period)
        f7id = simulation.calculate('f7id', period)
        f7ie = simulation.calculate('f7ie', period)
        f7if = simulation.calculate('f7if', period)
        f7ig = simulation.calculate('f7ig', period)
        f7ih = simulation.calculate('f7ih', period)
        f7ij = simulation.calculate('f7ij', period)
        f7ik = simulation.calculate('f7ik', period)
        f7il = simulation.calculate('f7il', period)
        f7im = simulation.calculate('f7im', period)
        f7in = simulation.calculate('f7in', period)
        f7io = simulation.calculate('f7io', period)
        f7ip = simulation.calculate('f7ip', period)
        f7iq = simulation.calculate('f7iq', period)
        f7ir = simulation.calculate('f7ir', period)
        f7is = simulation.calculate('f7is', period)
        f7it = simulation.calculate('f7it', period)
        f7iu = simulation.calculate('f7iu', period)
        f7iv = simulation.calculate('f7iv', period)
        f7iw = simulation.calculate('f7iw', period)
        f7ix = simulation.calculate('f7ix', period)
        f7iz = simulation.calculate('f7iz', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.locmeu

        m18 = (maxi(f7id, f7ie, f7if, f7ig) == max_(f7ie, f7if))
        m20 = (maxi(f7ij, f7il, f7in, f7iv) == max_(f7il, f7in))
        return period, ((min_(P.max, maxi(f7ij, f7il, f7in, f7iv)) * (P.taux20 * m20 + P.taux18 * not_(m20)) +
                min_(P.max, maxi(f7id, f7ie, f7if, f7ig)) * (P.taux18 * m18 + P.taux11 * not_(m18)) +
                P.taux * (min_(P.max, max_(f7im, f7iw)) + min_(P.max, f7io))) / 9 +
            P.taux * max_(f7ik + f7ip, f7ir + f7iq) +
            f7ia + f7ib + f7ic + f7ih + f7is + f7iu + f7it + f7ix + f7iz)

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Investissement en vue de la location meublée non professionnelle dans certains établissements ou résidences
        2013
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ia = simulation.calculate('f7ia', period)
        f7ib = simulation.calculate('f7ib', period)
        f7ic = simulation.calculate('f7ic', period)
        f7id = simulation.calculate('f7id', period)
        f7ie = simulation.calculate('f7ie', period)
        f7if = simulation.calculate('f7if', period)
        f7ig = simulation.calculate('f7ig', period)
        f7ih = simulation.calculate('f7ih', period)
        f7ij = simulation.calculate('f7ij', period)
        f7ik = simulation.calculate('f7ik', period)
        f7il = simulation.calculate('f7il', period)
        f7im = simulation.calculate('f7im', period)
        f7in = simulation.calculate('f7in', period)
        f7io = simulation.calculate('f7io', period)
        f7ip = simulation.calculate('f7ip', period)
        f7iq = simulation.calculate('f7iq', period)
        f7ir = simulation.calculate('f7ir', period)
        f7is = simulation.calculate('f7is', period)
        f7it = simulation.calculate('f7it', period)
        f7iu = simulation.calculate('f7iu', period)
        f7iv = simulation.calculate('f7iv', period)
        f7iw = simulation.calculate('f7iw', period)
        f7ix = simulation.calculate('f7ix', period)
        f7iy = simulation.calculate('f7iy', period)
        f7iz = simulation.calculate('f7iz', period)
        f7jc = simulation.calculate('f7jc', period)
        f7ji = simulation.calculate('f7ji', period)
        f7js = simulation.calculate('f7js', period)
        f7jt = simulation.calculate('f7jt', period)
        f7ju = simulation.calculate('f7ju', period)
        f7jv = simulation.calculate('f7jv', period)
        f7jw = simulation.calculate('f7jw', period)
        f7jx = simulation.calculate('f7jx', period)
        f7jy = simulation.calculate('f7jy', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.locmeu

        m18 = (maxi(f7id, f7ie, f7if, f7ig) == max_(f7ie, f7if))
        m20 = (maxi(f7ij, f7il, f7in, f7iv) == max_(f7il, f7in))
        return period, ((min_(P.max, maxi(f7ij, f7il, f7in, f7iv)) * (P.taux20 * m20 + P.taux18 * not_(m20)) +
                min_(P.max, maxi(f7id, f7ie, f7if, f7ig)) * (P.taux18 * m18 + P.taux11 * not_(m18)) +
                P.taux11 * min_(P.max, f7jt + f7ju) +
                P.taux * (min_(P.max, max_(f7im, f7iw)) + min_(P.max, f7io))) / 9 +
            P.taux * max_(f7ik + f7ip, f7ir + f7iq) +
            f7ia + f7ib + f7ic + f7ih + f7is + f7iu + f7it + f7ix + f7iy + f7iz + f7jv + f7jw + f7jx + f7jy + f7jc +
                f7ji + f7js)


@reference_formula
class mohist(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"mohist"
    start_date = date(2008, 1, 1)

    def function(self, simulation, period):
        '''
        Travaux de conservation et de restauration d’objets classés monuments historiques (case NZ)
        2008-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7nz = simulation.calculate('f7nz', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.mohist

        return period, P.taux * min_(f7nz, P.max)


@reference_formula
class patnat(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"patnat"

    @dated_function(start = date(2010, 1, 1), stop = date(2010, 12, 31))
    def function_20100101_20101231(self, simulation, period):
        '''
        Dépenses de protections du patrimoine naturel (case 7KA)
        2010
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ka = simulation.calculate('f7ka', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.patnat

        max1 = P.max
        return period, P.taux * min_(f7ka, max1)

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Dépenses de protections du patrimoine naturel (case 7KA, 7KB)
        2011
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ka = simulation.calculate('f7ka', period)
        f7kb = simulation.calculate('f7kb', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.patnat

        max1 = P.max
        return period, P.taux * min_(f7ka, max1) + f7kb

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Dépenses de protections du patrimoine naturel (case 7KA, 7KB, 7KC)
        2012
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ka = simulation.calculate('f7ka', period)
        f7kb = simulation.calculate('f7kb', period)
        f7kc = simulation.calculate('f7kc', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.patnat

        max1 = P.max
        return period, P.taux * min_(f7ka, max1) + f7kb + f7kc

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Dépenses de protections du patrimoine naturel (case 7KA, 7KB, 7KC)
        2013
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ka = simulation.calculate('f7ka', period)
        f7kb = simulation.calculate('f7kb', period)
        f7kc = simulation.calculate('f7kc', period)
        f7kd = simulation.calculate('f7kd', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.patnat

        max1 = P.max
        return period, P.taux * min_(f7ka, max1) + f7kb + f7kc + f7kd


@reference_formula
class prcomp(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"prcomp"

    def function(self, simulation, period):
        '''
        Prestations compensatoires
        2002-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7wm = simulation.calculate('f7wm', period)
        f7wn = simulation.calculate('f7wn', period)
        f7wo = simulation.calculate('f7wo', period)
        f7wp = simulation.calculate('f7wp', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.prcomp

        div = (f7wo == 0) * 1 + f7wo  # Pour éviter les divisions par zéro

        return period, ((f7wm == 0) * ((f7wn == f7wo) * P.taux * min_(f7wn, P.seuil) +
                                  (f7wn < f7wo) * (f7wo <= P.seuil) * P.taux * f7wn +
                                  max_(0, (f7wn < f7wo) * (f7wo > P.seuil) * P.taux * P.seuil * f7wn / div)) +
                (f7wm != 0) * ((f7wn == f7wm) * (f7wo <= P.seuil) * P.taux * f7wm +
                                  max_(0, (f7wn == f7wm) * (f7wo >= P.seuil) * P.taux * f7wm / div) +
                                  (f7wn > f7wm) * (f7wo <= P.seuil) * P.taux * f7wn +
                                  max_(0, (f7wn > f7wm) * (f7wo >= P.seuil) * P.taux * f7wn / div)) +
                 P.taux * f7wp)


@reference_formula
class repsoc(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"repsoc"
    start_date = date(2003, 1, 1)

    def function(self, simulation, period):
        '''
        Intérèts d'emprunts pour reprises de société
        2003-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7fh = simulation.calculate('f7fh', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.repsoc

        seuil = P.seuil * (marpac + 1)
        return period, P.taux * min_(f7fh, seuil)


@reference_formula
class resimm(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"resimm"

    @dated_function(start = date(2009, 1, 1), stop = date(2010, 12, 31))
    def function_20090101_20101231(self, simulation, period):
        '''
        Travaux de restauration immobilière (cases 7RA et 7RB)
        2009-2010
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ra = simulation.calculate('f7ra', period)
        f7rb = simulation.calculate('f7rb', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.resimm

        max1 = P.max
        max2 = max_(max1 - f7rb, 0)
        return period, P.taux_rb * min_(f7rb, max1) + P.taux_ra * min_(f7ra, max2)

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Travaux de restauration immobilière (cases 7RA, 7RB, 7RC, 7RD)
        2011
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ra = simulation.calculate('f7ra', period)
        f7rb = simulation.calculate('f7rb', period)
        f7rc = simulation.calculate('f7rc', period)
        f7rd = simulation.calculate('f7rd', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.resimm

        max1 = P.max
        max2 = max_(max1 - f7rd, 0)
        max3 = max_(max2 - f7rb, 0)
        max4 = max_(max3 - f7rc, 0)
        return period, (P.taux_rd * min_(f7rd, max1) + P.taux_rb * min_(f7rb, max2) + P.taux_rc * min_(f7rc, max3) +
                P.taux_ra * min_(f7ra, max4))

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Travaux de restauration immobilière (cases 7RA, 7RB, 7RC, 7RD, 7RE, 7RF)
        2012
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ra = simulation.calculate('f7ra', period)
        f7rb = simulation.calculate('f7rb', period)
        f7rc = simulation.calculate('f7rc', period)
        f7rd = simulation.calculate('f7rd', period)
        f7re = simulation.calculate('f7re', period)
        f7rf = simulation.calculate('f7rf', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.resimm

        max1 = P.max
        max2 = max_(max1 - f7rd, 0)
        max3 = max_(max2 - f7rb, 0)
        max4 = max_(max3 - f7rc - f7rf, 0)
        max5 = max_(max4 - f7ra, 0)
        return period, (P.taux_rd * min_(f7rd, max1) + P.taux_rb * min_(f7rb, max2) + P.taux_rc * min_(f7rc + f7rf, max3) +
                P.taux_ra * min_(f7ra, max4) + P.taux_re * min_(f7re, max5))

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Travaux de restauration immobilière (cases 7RA, 7RB, 7RC, 7RD, 7RE, 7RF, 7SX, 7SY)
        2012
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ra = simulation.calculate('f7ra', period)
        f7rb = simulation.calculate('f7rb', period)
        f7rc = simulation.calculate('f7rc', period)
        f7rd = simulation.calculate('f7rd', period)
        f7re = simulation.calculate('f7re', period)
        f7rf = simulation.calculate('f7rf', period)
        f7sx = simulation.calculate('f7sx', period)
        f7sy = simulation.calculate('f7sy', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.resimm

        max1 = P.max
        max2 = max_(max1 - f7rd, 0)
        max3 = max_(max2 - f7rb, 0)
        max4 = max_(max3 - f7rc - f7sy - f7rf, 0)
        max5 = max_(max4 - f7ra, 0)
        return period, (P.taux_rd * min_(f7rd, max1) + P.taux_rb * min_(f7rb, max2) + P.taux_rc * min_(f7sy + f7rf + f7rc, max3) +
                P.taux_ra * min_(f7ra, max4) + P.taux_re * min_(f7re + f7sx, max5))


@reference_formula
class rsceha(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"rsceha"

    def function(self, simulation, period):
        '''
        Rentes de survie et contrats d'épargne handicap
        2002-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        nb_pac2 = simulation.calculate('nb_pac2', period)
        nbR = simulation.calculate('nbR', period)
        f7gz = simulation.calculate('f7gz', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.rsceha

        max1 = P.seuil1 + (nb_pac2 - nbR) * P.seuil2
        return period, P.taux * min_(f7gz, max1)


@reference_formula
class saldom(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"saldom"

    @dated_function(start = date(2002, 1, 1), stop = date(2004, 12, 31))
    def function_20020101_20041231(self, simulation, period):
        '''
        Sommes versées pour l'emploi d'un salariés à  domicile
        2002-2004
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7df = simulation.calculate('f7df', period)
        f7dg = simulation.calculate('f7dg', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.saldom

        isinvalid = f7dg
        max1 = P.max1 * not_(isinvalid) + P.max3 * isinvalid
        return period, P.taux * min_(f7df, max1)

    @dated_function(start = date(2005, 1, 1), stop = date(2006, 12, 31))
    def function_20050101_20061231(self, simulation, period):
        '''
        Sommes versées pour l'emploi d'un salariés à  domicile
        2005-2006
        '''
        period = period.start.offset('first-of', 'year').period('year')
        nb_pac2 = simulation.calculate('nb_pac2', period)
        f7df = simulation.calculate('f7df', period)
        f7dl = simulation.calculate('f7dl', period)
        f7dg = simulation.calculate('f7dg', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.saldom

        isinvalid = f7dg
        nbpacmin = nb_pac2 + f7dl
        maxBase = P.max1
        maxDuMaxNonInv = P.max2
        maxNonInv = min_(maxBase + P.pac * nbpacmin, maxDuMaxNonInv)
        max1 = maxNonInv * not_(isinvalid) + P.max3 * isinvalid
        return period, P.taux * min_(f7df, max1)

    @dated_function(start = date(2007, 1, 1), stop = date(2008, 12, 31))
    def function_20070101_20081231(self, simulation, period):
        '''
        Sommes versées pour l'emploi d'un salariés à  domicile
        2007-2008
        '''
        period = period.start.offset('first-of', 'year').period('year')
        nb_pac2 = simulation.calculate('nb_pac2', period)
        f7db = simulation.calculate('f7db', period)
        f7df = simulation.calculate('f7df', period)
        f7dl = simulation.calculate('f7dl', period)
        f7dg = simulation.calculate('f7dg', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.saldom

        isinvalid = f7dg
        nbpacmin = nb_pac2 + f7dl
        maxBase = P.max1
        maxDuMaxNonInv = P.max2
        maxNonInv = min_(maxBase + P.pac * nbpacmin, maxDuMaxNonInv)
        maxEffectif = maxNonInv * not_(isinvalid) + P.max3 * isinvalid
        max1 = maxEffectif - min_(f7db, maxEffectif)
        return period, P.taux * min_(f7df, max1)

    @dated_function(start = date(2009, 1, 1), stop = date(2013, 12, 31))
    def function_20090101_20131231(self, simulation, period):
        '''
        Sommes versées pour l'emploi d'un salariés à  domicile
        2009-2013
        '''
        period = period.start.offset('first-of', 'year').period('year')
        nb_pac2 = simulation.calculate('nb_pac2', period)
        f7db = simulation.calculate('f7db', period)
        f7df = simulation.calculate('f7df', period)
        f7dl = simulation.calculate('f7dl', period)
        f7dq = simulation.calculate('f7dq', period)
        f7dg = simulation.calculate('f7dg', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.saldom

        isinvalid = f7dg
        annee1 = f7dq
        nbpacmin = nb_pac2 + f7dl
        maxBase = P.max1 * not_(annee1) + P.max1_1ereAnnee * annee1
        maxDuMaxNonInv = P.max2 * not_(annee1) + P.max2_1ereAnnee * annee1
        maxNonInv = min_(maxBase + P.pac * nbpacmin, maxDuMaxNonInv)
        maxEffectif = maxNonInv * not_(isinvalid) + P.max3 * isinvalid
        max1 = maxEffectif - min_(f7db, maxEffectif)
        return period, P.taux * min_(f7df, max1)


@reference_formula
class scelli(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"scelli"

    @dated_function(start = date(2009, 1, 1), stop = date(2009, 12, 31))
    def function_20090101_20091231(self, simulation, period):
        '''
        Investissements locatif neufs : Dispositif Scellier (cases 7HJ et 7HK)
        2009
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7hj = simulation.calculate('f7hj', period)
        f7hk = simulation.calculate('f7hk', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.scelli

        return period, max_(P.taux1 * min_(P.max, f7hj), P.taux2 * min_(P.max, f7hk)) / 9

    @dated_function(start = date(2010, 1, 1), stop = date(2010, 12, 31))
    def function_20100101_20101231(self, simulation, period):
        '''
        Investissements locatif neufs : Dispositif Scellier
        2010
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7hj = simulation.calculate('f7hj', period)
        f7hk = simulation.calculate('f7hk', period)
        f7hn = simulation.calculate('f7hn', period)
        f7ho = simulation.calculate('f7ho', period)
        f7hl = simulation.calculate('f7hl', period)
        f7hm = simulation.calculate('f7hm', period)
        f7hr = simulation.calculate('f7hr', period)
        f7hs = simulation.calculate('f7hs', period)
        f7la = simulation.calculate('f7la', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.scelli

        return period, (max_(
                    max_(P.taux1 * min_(P.max, f7hj),
                    P.taux2 * min_(P.max, f7hk)),
                    max_(P.taux1 * min_(P.max, f7hn),
                    P.taux2 * min_(P.max, f7ho))) / 9 +
                max_(
                    P.taux1 * min_(P.max, f7hl),
                    P.taux2 * min_(P.max, f7hm)) / 9 +
                max_(P.taux1 * f7hr, P.taux2 * f7hs) +
                f7la)

    @dated_function(start = date(2011, 1, 1), stop = date(2011, 12, 31))
    def function_20110101_20111231(self, simulation, period):
        '''
        Investissements locatif neufs : Dispositif Scellier
        2011
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7hj = simulation.calculate('f7hj', period)
        f7hk = simulation.calculate('f7hk', period)
        f7hl = simulation.calculate('f7hl', period)
        f7hm = simulation.calculate('f7hm', period)
        f7hn = simulation.calculate('f7hn', period)
        f7ho = simulation.calculate('f7ho', period)
        f7hr = simulation.calculate('f7hr', period)
        f7hs = simulation.calculate('f7hs', period)
        f7ht = simulation.calculate('f7ht', period)
        f7hu = simulation.calculate('f7hu', period)
        f7hv = simulation.calculate('f7hv', period)
        f7hw = simulation.calculate('f7hw', period)
        f7hx = simulation.calculate('f7hx', period)
        f7hz = simulation.calculate('f7hz', period)
        f7la = simulation.calculate('f7la', period)
        f7lb = simulation.calculate('f7lb', period)
        f7lc = simulation.calculate('f7lc', period)
        f7na = simulation.calculate('f7na', period)
        f7nb = simulation.calculate('f7nb', period)
        f7nc = simulation.calculate('f7nc', period)
        f7nd = simulation.calculate('f7nd', period)
        f7ne = simulation.calculate('f7ne', period)
        f7nf = simulation.calculate('f7nf', period)
        f7ng = simulation.calculate('f7ng', period)
        f7nh = simulation.calculate('f7nh', period)
        f7ni = simulation.calculate('f7ni', period)
        f7nj = simulation.calculate('f7nj', period)
        f7nk = simulation.calculate('f7nk', period)
        f7nl = simulation.calculate('f7nl', period)
        f7nm = simulation.calculate('f7nm', period)
        f7nn = simulation.calculate('f7nn', period)
        f7no = simulation.calculate('f7no', period)
        f7np = simulation.calculate('f7np', period)
        f7nq = simulation.calculate('f7nq', period)
        f7nr = simulation.calculate('f7nr', period)
        f7ns = simulation.calculate('f7ns', period)
        f7nt = simulation.calculate('f7nt', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.scelli

        return period, (min_(P.max, maxi(
                    P.taux13 * max_(f7nf, f7nj) / 9,
                    P.taux15 * max_(f7ng, f7ni) / 9,
                    P.taux22 * max_(f7na, f7ne) / 9,
                    P.taux1 * maxi(f7nb, f7nc, f7nd, f7nh) / 9,
                    P.taux36 * maxi(f7nk / 9, f7no / 9, f7np / 5, f7nt / 5),
                    P.taux2 * maxi(f7nl / 9, f7nm / 9, f7nn / 9, f7nq / 5, f7nr / 5, f7ns / 5))) +
                min_(P.max, maxi(
                    P.taux1 * max_(f7hj, f7hn),
                    P.taux2 * max_(f7hk, f7ho))) / 9 +
                min_(P.max, max_(P.taux1 * f7hl, P.taux2 * f7hm)) / 9 +
                min_(P.max, maxi(P.taux1 * f7hv, P.taux1 * f7hx, P.taux2 * f7hw, P.taux2 * f7hz)) +
                min_(P.max, max_(P.taux1 * f7ht, P.taux2 * f7hu)) +
                min_(P.max, max_(P.taux1 * f7hr, P.taux2 * f7hs)) +
                f7la + f7lb + f7lc
                )

    @dated_function(start = date(2012, 1, 1), stop = date(2012, 12, 31))
    def function_20120101_20121231(self, simulation, period):
        '''
        Investissements locatif neufs : Dispositif Scellier
        2012
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7ha = simulation.calculate('f7ha', period)
        f7hb = simulation.calculate('f7hb', period)
        f7hg = simulation.calculate('f7hg', period)
        f7hh = simulation.calculate('f7hh', period)
        f7hd = simulation.calculate('f7hd', period)
        f7he = simulation.calculate('f7he', period)
        f7hf = simulation.calculate('f7hf', period)
        f7hj = simulation.calculate('f7hj', period)
        f7hk = simulation.calculate('f7hk', period)
        f7hl = simulation.calculate('f7hl', period)
        f7hm = simulation.calculate('f7hm', period)
        f7hn = simulation.calculate('f7hn', period)
        f7ho = simulation.calculate('f7ho', period)
        f7hr = simulation.calculate('f7hr', period)
        f7hs = simulation.calculate('f7hs', period)
        f7ht = simulation.calculate('f7ht', period)
        f7hu = simulation.calculate('f7hu', period)
        f7hv = simulation.calculate('f7hv', period)
        f7hw = simulation.calculate('f7hw', period)
        f7hx = simulation.calculate('f7hx', period)
        f7hz = simulation.calculate('f7hz', period)
        f7ja = simulation.calculate('f7ja', period)
        f7jb = simulation.calculate('f7jb', period)
        f7jd = simulation.calculate('f7jd', period)
        f7je = simulation.calculate('f7je', period)
        f7jf = simulation.calculate('f7jf', period)
        f7jg = simulation.calculate('f7jg', period)
        f7jh = simulation.calculate('f7jh', period)
        f7jj = simulation.calculate('f7jj', period)
        f7jk = simulation.calculate('f7jk', period)
        f7jl = simulation.calculate('f7jl', period)
        f7jm = simulation.calculate('f7jm', period)
        f7jn = simulation.calculate('f7jn', period)
        f7jo = simulation.calculate('f7jo', period)
        f7jp = simulation.calculate('f7jp', period)
        f7jq = simulation.calculate('f7jq', period)
        f7jr = simulation.calculate('f7jr', period)
        f7la = simulation.calculate('f7la', period)
        f7lb = simulation.calculate('f7lb', period)
        f7lc = simulation.calculate('f7lc', period)
        f7ld = simulation.calculate('f7ld', period)
        f7le = simulation.calculate('f7le', period)
        f7lf = simulation.calculate('f7lf', period)
        f7na = simulation.calculate('f7na', period)
        f7nb = simulation.calculate('f7nb', period)
        f7nc = simulation.calculate('f7nc', period)
        f7nd = simulation.calculate('f7nd', period)
        f7ne = simulation.calculate('f7ne', period)
        f7nf = simulation.calculate('f7nf', period)
        f7ng = simulation.calculate('f7ng', period)
        f7nh = simulation.calculate('f7nh', period)
        f7ni = simulation.calculate('f7ni', period)
        f7nj = simulation.calculate('f7nj', period)
        f7nk = simulation.calculate('f7nk', period)
        f7nl = simulation.calculate('f7nl', period)
        f7nm = simulation.calculate('f7nm', period)
        f7nn = simulation.calculate('f7nn', period)
        f7no = simulation.calculate('f7no', period)
        f7np = simulation.calculate('f7np', period)
        f7nq = simulation.calculate('f7nq', period)
        f7nr = simulation.calculate('f7nr', period)
        f7ns = simulation.calculate('f7ns', period)
        f7nt = simulation.calculate('f7nt', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.scelli

        return period, (min_(P.max, maxi(
                    P.taux13 * max_(f7nf, f7nj) / 9,
                    P.taux15 * max_(f7ng, f7ni) / 9,
                    P.taux22 * max_(f7na, f7ne) / 9,
                    P.taux1 * maxi(f7nb, f7nc, f7nd, f7nh) / 9,
                    P.taux36 * maxi(f7nk / 9, f7no / 9, f7np / 5, f7nt / 5),
                    P.taux2 * maxi(f7nl / 9, f7nm / 9, f7nn / 9, f7nq / 5, f7nr / 5, f7ns / 5))) +
                min_(P.max, maxi(
                    P.taux1 * max_(f7hj, f7hn),
                    P.taux2 * max_(f7hk, f7ho))) / 9 +
                min_(P.max, max_(P.taux1 * f7hl, P.taux2 * f7hm)) / 9 +
                min_(P.max, maxi(P.taux1 * f7hv, P.taux1 * f7hx, P.taux2 * f7hw, P.taux2 * f7hz)) +
                min_(P.max, max_(P.taux1 * f7ht, P.taux2 * f7hu)) +
                min_(P.max, max_(P.taux1 * f7hr, P.taux2 * f7hs)) +
                f7la + f7lb + f7lc + f7ld + f7le + f7lf +
                f7ha + f7hb + f7hg + f7hh + f7hd + f7he + f7hf +
                min_(P.max, maxi(
                    P.taux6 * max_(f7jf, f7jj) / 9,
                    P.taux13 * maxi(f7ja, f7je, f7jg, f7jh) / 9,
                    P.taux22 * maxi(f7jb, f7jd) / 9,
                    P.taux24 * maxi(f7jk / 9, f7jn / 9, f7jo / 5, f7jr / 5),
                    P.taux36 * maxi(f7jl / 9, f7jm / 9, f7jp / 5, f7jq / 5)))
                )

    @dated_function(start = date(2013, 1, 1), stop = date(2013, 12, 31))
    def function_20130101_20131231(self, simulation, period):
        '''
        Investissements locatif neufs : Dispositif Scellier
        2013
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7fa = simulation.calculate('f7fa', period)
        f7fb = simulation.calculate('f7fb', period)
        f7fc = simulation.calculate('f7fc', period)
        f7fd = simulation.calculate('f7fd', period)
        f7gj = simulation.calculate('f7gj', period)
        f7gk = simulation.calculate('f7gk', period)
        f7gl = simulation.calculate('f7gl', period)
        f7gp = simulation.calculate('f7gp', period)
        f7gs = simulation.calculate('f7gs', period)
        f7gt = simulation.calculate('f7gt', period)
        f7gu = simulation.calculate('f7gu', period)
        f7gv = simulation.calculate('f7gv', period)
        f7gw = simulation.calculate('f7gw', period)
        f7gx = simulation.calculate('f7gx', period)
        f7ha = simulation.calculate('f7ha', period)
        f7hb = simulation.calculate('f7hb', period)
        f7hg = simulation.calculate('f7hg', period)
        f7hh = simulation.calculate('f7hh', period)
        f7hd = simulation.calculate('f7hd', period)
        f7he = simulation.calculate('f7he', period)
        f7hf = simulation.calculate('f7hf', period)
        f7hj = simulation.calculate('f7hj', period)
        f7hk = simulation.calculate('f7hk', period)
        f7hl = simulation.calculate('f7hl', period)
        f7hm = simulation.calculate('f7hm', period)
        f7hn = simulation.calculate('f7hn', period)
        f7ho = simulation.calculate('f7ho', period)
        f7hr = simulation.calculate('f7hr', period)
        f7hs = simulation.calculate('f7hs', period)
        f7ht = simulation.calculate('f7ht', period)
        f7hu = simulation.calculate('f7hu', period)
        f7hv = simulation.calculate('f7hv', period)
        f7hw = simulation.calculate('f7hw', period)
        f7hx = simulation.calculate('f7hx', period)
        f7hz = simulation.calculate('f7hz', period)
        f7ja = simulation.calculate('f7ja', period)
        f7jb = simulation.calculate('f7jb', period)
        f7jd = simulation.calculate('f7jd', period)
        f7je = simulation.calculate('f7je', period)
        f7jf = simulation.calculate('f7jf', period)
        f7jg = simulation.calculate('f7jg', period)
        f7jh = simulation.calculate('f7jh', period)
        f7jj = simulation.calculate('f7jj', period)
        f7jk = simulation.calculate('f7jk', period)
        f7jl = simulation.calculate('f7jl', period)
        f7jm = simulation.calculate('f7jm', period)
        f7jn = simulation.calculate('f7jn', period)
        f7jo = simulation.calculate('f7jo', period)
        f7jp = simulation.calculate('f7jp', period)
        f7jq = simulation.calculate('f7jq', period)
        f7jr = simulation.calculate('f7jr', period)
        f7la = simulation.calculate('f7la', period)
        f7lb = simulation.calculate('f7lb', period)
        f7lc = simulation.calculate('f7lc', period)
        f7ld = simulation.calculate('f7ld', period)
        f7le = simulation.calculate('f7le', period)
        f7lf = simulation.calculate('f7lf', period)
        f7lm = simulation.calculate('f7lm', period)
        f7ls = simulation.calculate('f7ls', period)
        f7lz = simulation.calculate('f7lz', period)
        f7mg = simulation.calculate('f7mg', period)
        f7na = simulation.calculate('f7na', period)
        f7nb = simulation.calculate('f7nb', period)
        f7nc = simulation.calculate('f7nc', period)
        f7nd = simulation.calculate('f7nd', period)
        f7ne = simulation.calculate('f7ne', period)
        f7nf = simulation.calculate('f7nf', period)
        f7ng = simulation.calculate('f7ng', period)
        f7nh = simulation.calculate('f7nh', period)
        f7ni = simulation.calculate('f7ni', period)
        f7nj = simulation.calculate('f7nj', period)
        f7nk = simulation.calculate('f7nk', period)
        f7nl = simulation.calculate('f7nl', period)
        f7nm = simulation.calculate('f7nm', period)
        f7nn = simulation.calculate('f7nn', period)
        f7no = simulation.calculate('f7no', period)
        f7np = simulation.calculate('f7np', period)
        f7nq = simulation.calculate('f7nq', period)
        f7nr = simulation.calculate('f7nr', period)
        f7ns = simulation.calculate('f7ns', period)
        f7nt = simulation.calculate('f7nt', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.scelli

        return period, (min_(P.max, maxi(
                    P.taux13 * max_(f7nf, f7nj) / 9,
                    P.taux15 * max_(f7ng, f7ni) / 9,
                    P.taux22 * max_(f7na, f7ne) / 9,
                    P.taux1 * maxi(f7nb, f7nc, f7nd, f7nh) / 9,
                    P.taux36 * maxi(f7nk / 9, f7no / 9, f7np / 5, f7nt / 5),
                    P.taux2 * maxi(f7nl / 9, f7nm / 9, f7nn / 9, f7nq / 5, f7nr / 5, f7ns / 5))) +
                min_(P.max, maxi(
                    P.taux1 * max_(f7hj, f7hn),
                    P.taux2 * max_(f7hk, f7ho))) / 9 +
                min_(P.max, max_(P.taux1 * f7hl, P.taux2 * f7hm)) / 9 +
                min_(P.max, maxi(P.taux1 * f7hv, P.taux1 * f7hx, P.taux2 * f7hw, P.taux2 * f7hz)) +
                min_(P.max, max_(P.taux1 * f7ht, P.taux2 * f7hu)) +
                min_(P.max, max_(P.taux1 * f7hr, P.taux2 * f7hs)) +
                min_(P.max, maxi(
                    P.taux6 * maxi(f7jf, f7jj, f7fb) / 9,
                    P.taux13 * maxi(f7ja, f7je, f7jg, f7jh, f7fa) / 9,
                    P.taux22 * maxi(f7jb, f7jd) / 9,
                    P.taux24 * maxi(f7jk / 9, f7jn / 9, f7jo / 5, f7jr / 5, f7fc / 9, f7fd / 5),
                    P.taux36 * maxi(f7jl / 9, f7jm / 9, f7jp / 5, f7jq / 5))) +
                f7la + f7lb + f7lc + f7ld + f7le + f7lf + f7lm + f7ls + f7lz + f7mg +
                f7ha + f7hb + f7hg + f7hh + f7hd + f7he + f7hf +
                f7gj + f7gk + f7gl + f7gp + f7gs + f7gt + f7gu + f7gv + f7gx + f7gw
                )


@reference_formula
class sofica(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"sofica"
    start_date = date(2006, 1, 1)

    def function(self, simulation, period):
        '''
        Souscriptions au capital de SOFICA
        2006-
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7gn = simulation.calculate('f7gn', period)
        f7fn = simulation.calculate('f7fn', period)
        rng = simulation.calculate('rng', period)
        P = simulation.legislation_at(period.start).ir.reductions_impots.sofica

        max0 = min_(P.taux1 * max_(rng, 0), P.max)
        max1 = max_(0, max0 - f7gn)
        return period, P.taux2 * min_(f7gn, max0) + P.taux3 * min_(f7fn, max1)


@reference_formula
class sofipe(SimpleFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"sofipe"
    start_date = date(2009, 1, 1)
    stop_date = date(2011, 1, 1)

    def function(self, simulation, period):
        """
        Souscription au capital d’une SOFIPECHE (case 7GS)
        2009-2011
        """
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        rbg_int = simulation.calculate('rbg_int', period)
        f7gs = simulation.calculate('f7gs', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.sofipe

        max1 = min_(P.max * (marpac + 1), P.base * rbg_int)  # page3 ligne 18
        return period, P.taux * min_(f7gs, max1)


@reference_formula
class spfcpi(DatedFormulaColumn):
    column = FloatCol(default = 0)
    entity_class = FoyersFiscaux
    label = u"spfcpi"

    @dated_function(start = date(2002, 1, 1), stop = date(2002, 12, 31))
    def function_20020101_20021231(self, simulation, period):
        '''
        Souscription de parts de fonds communs de placement dans l'innovation,
        de fonds d'investissement de proximité
        2002
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7gq = simulation.calculate('f7gq', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.spfcpi

        max1 = P.max * (marpac + 1)
        return period, P.taux1 * min_(f7gq, max1)

    @dated_function(start = date(2003, 1, 1), stop = date(2006, 12, 31))
    def function_20030101_20061231(self, simulation, period):
        '''
        Souscription de parts de fonds communs de placement dans l'innovation,
        de fonds d'investissement de proximité
        2003-2006
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7gq = simulation.calculate('f7gq', period)
        f7fq = simulation.calculate('f7fq', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.spfcpi

        max1 = P.max * (marpac + 1)
        return period, (P.taux1 * min_(f7gq, max1) + P.taux1 * min_(f7fq, max1))

    @dated_function(start = date(2007, 1, 1), stop = date(2010, 12, 31))
    def function_20070101_20101231(self, simulation, period):
        '''
        Souscription de parts de fonds communs de placement dans l'innovation,
        de fonds d'investissement de proximité
        2007-2010
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7gq = simulation.calculate('f7gq', period)
        f7fq = simulation.calculate('f7fq', period)
        f7fm = simulation.calculate('f7fm', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.spfcpi

        max1 = P.max * (marpac + 1)
        return period, (P.taux1 * min_(f7gq, max1) +
                    P.taux1 * min_(f7fq, max1) +
                    P.taux2 * min_(f7fm, max1))

    @dated_function(start = date(2011, 1, 1), stop = date(2013, 12, 31))
    def function_20110101_20131231(self, simulation, period):
        '''
        Souscription de parts de fonds communs de placement dans l'innovation,
        de fonds d'investissement de proximité
        2011-2013
        '''
        period = period.start.offset('first-of', 'year').period('year')
        marpac = simulation.calculate('marpac', period)
        f7gq = simulation.calculate('f7gq', period)
        f7fq = simulation.calculate('f7fq', period)
        f7fm = simulation.calculate('f7fm', period)
        f7fl = simulation.calculate('f7fl', period)
        _P = simulation.legislation_at(period.start)
        P = simulation.legislation_at(period.start).ir.reductions_impots.spfcpi

        max1 = P.max * (marpac + 1)
        return period, (P.taux1 * min_(f7gq, max1) + P.taux1 * min_(f7fq, max1) + P.taux2 * min_(f7fm, max1) +
                P.taux3 * min_(f7fl, max1))

    @dated_function(start = date(2014, 1, 1), stop = date(2014, 12, 31))
    def function_20140101_20141231(self, simulation, period):
        '''
        Souscription de parts de fonds communs de placement dans l'innovation,
        de fonds d'investissement de proximité
        2014
        '''
        period = period.start.offset('first-of', 'year').period('year')
        f7gq = simulation.calculate('f7gq', period)

        return period, f7gq * 0


def mini(a, b, *args):
    if not args:
        return min_(a, b)
    else:
        return min_(a, mini(b, *args))


def maxi(a, b, *args):
    if not args:
        return max_(a, b)
    else:
        return max_(a, maxi(b, *args))
