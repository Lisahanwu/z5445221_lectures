f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop("Randwick")
f_suburbs.pop("Kensington")
# 2. Ensure that your dictionary contains:
#
#     Fairfield: 18081
#     Fairfield East: 5273
#     Fairfield Heights: 7517
#     Fairfield West: 11575
#     Fairlight: 5840
#     Fiddletown: 233
#     Five Dock: 9356
#     Flemington: None
#     Forest Glen: None
#     Forest Lodge: 4583
#     Forestville: 8329
#     Freemans Reach: 1973
#     Frenchs Forest: 13473
#     Freshwater: 8866

# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.
new = {
    'Fairfield' : 18081,
    'Fairfield East' : 5273,
    'Fairfield Heights' : 7517,
    'Fairfield West' : 11575,
    'Fairlight' : 5840,
    'Fiddletown' : 233,
    'Five Dock' : 9356,
    'Flemington' : None,
    'Forest Glen' : None,
    'Forest Lodge' : 4583,
    'Forestville' : 8329,
    'Freemans Reach' : 1973,
    'Frenchs Forest' : 13473,
    'Freshwater' : 8866,
}
f_suburbs.update(new)