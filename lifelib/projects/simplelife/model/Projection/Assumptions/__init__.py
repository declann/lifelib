"""Assumption input and calculations for individual policies.

This Space is a child Space of :mod:`~simplelife.model.Projection`,
and it holds assumption parameters and rates used
by the :mod:`~simplelife.model.Projection` Space.

.. figure:: /images/projects/simplelife/model/Assumptions/diagram1.png

.. rubric:: Parameters

Since :mod:`~simplelife.model.Projection` is parameterized with
:attr:`PolicyID` and :attr:`ScenID`, this Space is also
parameterized as a child space of :mod:`~simplelife.model.Projection`.
For example, ``simplelife.Projection[1].Assumptions.ExpsMaintSA()``
represents the expense maintenance per sum assured for Policy 1.

Attributes:
    PolicyID(:obj:`int`): Policy ID
    ScenID(:obj:`int`, optional): Scenario ID, defaults to 1.

.. rubric:: References

Attributes:
    AssumptionTables: `ExcelRange`_ object holding data read from the
        Excel range *AssumptionTable* in *input.xlsx*.

    MortalityTable: `ExcelRange`_ object holding mortality tables.
        The data is read from *MortalityTables* range in *input.xlsx*.

    prod: Alias for :func:`simplelife.Projection.Policy.Product`
    polt: Alias for :func:`simplelife.Projection.Policy.PolicyType`
    gen: Alias for :func:`simplelife.Projection.Policy.Gen`
    sex: Alias for :func:`simplelife.Projection.Policy.Sex`
    AsmpLookup: Alias for :func:`simplelife.Input.AsmpLookup`

.. _ExcelRange:
   https://docs.modelx.io/en/latest/reference/dataclient.html#excelrange

"""

from modelx.serialize.jsonvalues import *

_formula = None

_bases = []

_allow_none = None

_spaces = []

# ---------------------------------------------------------------------------
# Cells

def BaseMortRate(x):
    """Bae mortality rate"""

    table_id = AsmpLookup.match("BaseMort", prod(), polt(), gen()).value
    return MortalityTables[table_id, sex(), x]


def CnsmpTax():
    """Consumption tax rate"""
    return AsmpLookup("CnsmpTax")


def CommInitPrem():
    """Initial commission per premium"""
    result = AsmpLookup.match("CommInitPrem", prod(), polt(), gen()).value

    if result is not None:
        return result
    else:
        raise ValueError('CommInitPrem not found')


def CommRenPrem():
    """Renewal commission per premium"""
    result = AsmpLookup.match("CommRenPrem", prod(), polt(), gen()).value

    if result is not None:
        return  result
    else:
        raise ValueError('CommRenPrem not found')


def CommRenTerm():
    """Renewal commission term"""
    result = AsmpLookup.match("CommRenTerm", prod(), polt(), gen()).value

    if result is not None:
        return result
    else:
        raise ValueError('CommRenTerm not found')


def ExpsAcqAnnPrem():
    """Acquisition expense per annualized premium"""
    return AsmpLookup.match("ExpsAcqAnnPrem", prod(), polt(), gen()).value


def ExpsAcqPol():
    """Acquisition expense per policy"""
    return AsmpLookup.match("ExpsAcqPol", prod(), polt(), gen()).value


def ExpsAcqSA():
    """Acquisition expense per sum assured"""
    return AsmpLookup.match("ExpsAcqSA", prod(), polt(), gen()).value


def ExpsMaintAnnPrem():
    """Maintenance expense per annualized premium"""
    return AsmpLookup.match("ExpsMaintPrem", prod(), polt(), gen()).value


def ExpsMaintPol():
    """Maintenance expense per policy"""
    return AsmpLookup.match("ExpsMaintPol", prod(), polt(), gen()).value


def ExpsMaintSA():
    """Maintenance expense per sum assured"""
    return AsmpLookup.match("ExpsMaintSA", prod(), polt(), gen()).value


def InflRate():
    """Inflation rate"""
    return AsmpLookup("InflRate")


def LastAge():
    """Age at which mortality becomes 1"""
    x = 0
    while True:
        if BaseMortRate(x) == 1:
            return x
        x += 1


def MortFactor(y):
    """Mortality factor"""
    table = AsmpLookup.match("MortFactor", prod(), polt(), gen()).value

    if table is None:
        raise ValueError('MortFactor not found')

    result = AssumptionTables.get((table, y), None)

    if result is None:
        return MortFactor(y-1)
    else:
        return result


def MortTable():
    """Mortality Table"""
    result = AsmpLookup.match("BaseMort", prod(), polt(), gen()).value

    if result is not None:
        return MortalityTables(result).MortalityTable
    else:
        raise ValueError('MortTable not found')


def SurrRate(y):
    """Surrender Rate"""
    table = AsmpLookup.match("Surrender", prod(), polt(), gen()).value

    if table is None:
        raise ValueError('Surrender not found')

    result =  AssumptionTables.get((table, y), None)

    if result is None:
        return SurrRate(y-1)
    else:
        return result


# ---------------------------------------------------------------------------
# References

AsmpLookup = ("Interface", ("...", "Input", "AsmpLookup"), "auto")

AssumptionTables = ("Pickle", 2325077011464)

MortalityTables = ("Pickle", 2325070426248)

gen = ("Interface", ("..", "Policy", "Gen"), "auto")

polt = ("Interface", ("..", "Policy", "PolicyType"), "auto")

prod = ("Interface", ("..", "Policy", "Product"), "auto")

sex = ("Interface", ("..", "Policy", "Sex"), "auto")