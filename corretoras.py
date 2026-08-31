#exc 01

portifolios = {
    "corretoras": [
        {
            "nome": "Ágora",
            "empresas": [
                {"nome": "Itaúsa", "ticket": "ITSA4"},
                {"nome": "Ecorodovias", "ticket": "ECOR3"},
                {"nome": "Taesa", "ticket": "TAEE11"},
                {"nome": "B3", "ticket": "B3SA3"},
                {"nome": "Vale", "ticket": "VALE3"}
            ]
        },
        {
            "nome": "Ativa",
            "empresas": [
                {"nome": "B3", "ticket": "B3SA3"},
                {"nome": "Bradesco", "ticket": "BBDC4"},
                {"nome": "BB Seguridade", "ticket": "BBSE3"},
                {"nome": "BR Distribuidora", "ticket": "BRDT3"},
                {"nome": "Taesa", "ticket": "TAEE11"},
                {"nome": "CTEEP", "ticket": "TRPL4"},
                {"nome": "Vale", "ticket": "VALE3"},
                {"nome": "Telefônica Brasil", "ticket": "VIVT3"}
            ]
        },
        {
            "nome": "Genial",
            "empresas": [
                {"nome": "CPFL", "ticket": "CPFE3"},
                {"nome": "Minerva", "ticket": "BEEF3"},
                {"nome": "Cyrela", "ticket": "CYRE3"},
                {"nome": "Randon", "ticket": "RAPT4"},
                {"nome": "CTEEP", "ticket": "TRPL4"}
            ]
        },
        {
            "nome": "Easyinvest",
            "empresas": [
                {"nome": "B3", "ticket": "B3SA3"},
                {"nome": "Brasil Agro", "ticket": "AGRO3"},
                {"nome": "Coca-cola", "ticket": "COCA34"},
                {"nome": "Taesa", "ticket": "TAEE11"},
                {"nome": "Vale", "ticket": "VALE3"},
                {"nome": "Copel", "ticket": "CPLE11"},
                {"nome": "Itaúsa", "ticket": "ITSA4"},
                {"nome": "Ambev", "ticket": "ABEV3"}
            ]
        },
        {
            "nome": "Elite",
            "empresas": [
                {"nome": "Bradesco", "ticket": "BBDC4"},
                {"nome": "BB Seguridade", "ticket": "BBSE3"},
                {"nome": "Banrisul", "ticket": "BRSR6"},
                {"nome": "Engie", "ticket": "EGIE3"},
                {"nome": "Itaúsa", "ticket": "ITSA4"},
                {"nome": "Sanepar", "ticket": "SAPR11"},
                {"nome": "Taesa", "ticket": "TAEE11"},
                {"nome": "CTEEP", "ticket": "TRPL4"},
                {"nome": "Telefônica Brasil", "ticket": "VIVT3"},
                {"nome": "Vale", "ticket": "VALE3"}
            ]
        },
        {
            "nome": "Guide",
            "empresas": [
                {"nome": "Alupar", "ticket": "ALUP11"},
                {"nome": "Banco do Brasil", "ticket": "BBAS3"},
                {"nome": "Cyrela", "ticket": "CYRE3"},
                {"nome": "CPFL", "ticket": "CPFE3"},
                {"nome": "Klabin", "ticket": "KLBN11"},
                {"nome": "Porto seguro", "ticket": "PSSA3"},
                {"nome": "Tim", "ticket": "TIMS3"},
                {"nome": "Vale", "ticket": "VALE3"}
            ]
        },
        {
            "nome": "Nova Futura",
            "empresas": [
                {"nome": "B3", "ticket": "B3SA3"},
                {"nome": "Cyrela", "ticket": "CYRE3"},
                {"nome": "Gerdau", "ticket": "GGBR4"},
                {"nome": "Vivo", "ticket": "VIVT3"},
                {"nome": "CTEEP", "ticket": "TRPL4"}
            ]
        },
        {
            "nome": "Órama",
            "empresas": [
                {"nome": "Banco ABC", "ticket": "ABCB4"},
                {"nome": "Bradesco", "ticket": "BBDC4"},
                {"nome": "Minerva", "ticket": "BEEF3"},
                {"nome": "CESP", "ticket": "CESP6"},
                {"nome": "Engie", "ticket": "EGIE3"}
            ]
        }
    ]
}


# exc 02

corretorasTradadas = [
    {
        "AgoraEmpresas": set(),
        "AgoraTickets": set()
    },
    {
        "AtivaEmpresas": set(),
        "AtivaTickets": set()
    },
    {
        "GenialEmpresas": set(),
        "GenialTickets": set()
    },
    {
        "EasyinvestEmpresas": set(),
        "EasyinvestTickets": set()
    },
    {
        "EliteEmpresas": set(),
        "EliteTickets": set()
    },
    {
        "GuideEmpresas": set(),
        "GuideTickets": set()
    },
    {
        "NovaFuturaEmpresas": set(),
        "NovaFuturaTickets": set()
    },
    {
        "OramaEmpresas": set(),
        "OramaTickets": set()
    }
]


for corretora in portifolios["corretoras"]:

    for empresa in corretora["empresas"]:

        if corretora["nome"] == "Ágora":
            corretorasTradadas[0]["AgoraEmpresas"].add(empresa["nome"])
            corretorasTradadas[0]["AgoraTickets"].add(empresa["ticket"])

        elif corretora["nome"] == "Ativa":
            corretorasTradadas[1]["AtivaEmpresas"].add(empresa["nome"])
            corretorasTradadas[1]["AtivaTickets"].add(empresa["ticket"])

        elif corretora["nome"] == "Genial":
            corretorasTradadas[2]["GenialEmpresas"].add(empresa["nome"])
            corretorasTradadas[2]["GenialTickets"].add(empresa["ticket"])

        elif corretora["nome"] == "Easyinvest":
            corretorasTradadas[3]["EasyinvestEmpresas"].add(empresa["nome"])
            corretorasTradadas[3]["EasyinvestTickets"].add(empresa["ticket"])

        elif corretora["nome"] == "Elite":
            corretorasTradadas[4]["EliteEmpresas"].add(empresa["nome"])
            corretorasTradadas[4]["EliteTickets"].add(empresa["ticket"])

        elif corretora["nome"] == "Guide":
            corretorasTradadas[5]["GuideEmpresas"].add(empresa["nome"])
            corretorasTradadas[5]["GuideTickets"].add(empresa["ticket"])

        elif corretora["nome"] == "Nova Futura":
            corretorasTradadas[6]["NovaFuturaEmpresas"].add(empresa["nome"])
            corretorasTradadas[6]["NovaFuturaTickets"].add(empresa["ticket"])

        elif corretora["nome"] == "Órama":
            corretorasTradadas[7]["OramaEmpresas"].add(empresa["nome"])
            corretorasTradadas[7]["OramaTickets"].add(empresa["ticket"])

# exc 03

resTodas = (corretorasTradadas[0]["AgoraTickets"] & corretorasTradadas[1]["AtivaTickets"] & corretorasTradadas[2]["GenialTickets"] & corretorasTradadas[3]["EasyinvestTickets"] & corretorasTradadas[4]["EliteTickets"] & corretorasTradadas[5]["GuideTickets"] & corretorasTradadas[6]["NovaFuturaTickets"] & corretorasTradadas[7]["OramaTickets"])

print("Ação em comum entre todas as corretoras:\n", "Nenhuma!" if not resTodas else resTodas )

#exc 04

# a) Ache se há alguma ação em comum a essas 4 corretoras

resA = (corretorasTradadas[0]["AgoraTickets"] & corretorasTradadas[1]["AtivaTickets"] & corretorasTradadas[4]["EliteTickets"] & corretorasTradadas[2]["GenialTickets"])

# print(corretorasTradadas[0]["AgoraTickets"])
# print(corretorasTradadas[1]["AtivaTickets"])
# print(corretorasTradadas[2]["EliteTickets"])
# print(corretorasTradadas[3]["GenialTickets"])

print("Ação em comum entre a 'Ágora', 'Ativa', 'Elite' e 'Genial' :\n", "Nenhuma!" if not resA else resA )

# b) Indique se há ações únicas para cada corretora 

resTicketsUnicos = (corretorasTradadas[0]["AgoraTickets"] - corretorasTradadas[1]["AtivaTickets"] - corretorasTradadas[4]["EliteTickets"] - corretorasTradadas[2]["GenialTickets"])

resTicketsUnicos2 = (corretorasTradadas[1]["AtivaTickets"] - corretorasTradadas[0]["AgoraTickets"] - corretorasTradadas[4]["EliteTickets"] - corretorasTradadas[2]["GenialTickets"])

resTicketsUnicos3 = (corretorasTradadas[4]["EliteTickets"] - corretorasTradadas[1]["AtivaTickets"] - corretorasTradadas[0]["AgoraTickets"] - corretorasTradadas[2]["GenialTickets"])

resTicketsUnicos4 = (corretorasTradadas[2]["GenialTickets"] - corretorasTradadas[1]["AtivaTickets"] - corretorasTradadas[0]["AgoraTickets"] - corretorasTradadas[4]["EliteTickets"])

print(f"Ação única em cada corretora: \n 'Ágora': {resTicketsUnicos}. \n 'Ativa': {resTicketsUnicos2}. \n 'Elite': {resTicketsUnicos3}. \n 'Genial': {resTicketsUnicos4}.")

# c) Determine as relações entre os portfólios das corretoras (subset ou superset)

resSubconjuntoAgora = corretorasTradadas[0]["AgoraTickets"] >= corretorasTradadas[1]["AtivaTickets"]
resSubconjuntoAgora2 = corretorasTradadas[0]["AgoraTickets"] >= corretorasTradadas[2]["GenialTickets"]
resSubconjuntoAgora3 = corretorasTradadas[0]["AgoraTickets"] >= corretorasTradadas[4]["EliteTickets"]

print(f"A corretora 'Ágora' é: \n Subconjunto da 'Ativa': {resSubconjuntoAgora}.")
print(f"A corretora 'Ágora' é: \n Subconjunto da 'Genial': {resSubconjuntoAgora2}.")
print(f"A corretora 'Ágora' é: \n Subconjunto da 'Elite': {resSubconjuntoAgora3}.")

resSubconjuntoAtiva = corretorasTradadas[1]["AtivaTickets"] >= corretorasTradadas[0]["AgoraTickets"]
resSubconjuntoAtiva2 = corretorasTradadas[1]["AtivaTickets"] >= corretorasTradadas[2]["GenialTickets"]
resSubconjuntoAtiva3 = corretorasTradadas[1]["AtivaTickets"] >= corretorasTradadas[4]["EliteTickets"]

print(f"A corretora 'Ativa' é: \n Subconjunto da 'Ágora': {resSubconjuntoAtiva}.")
print(f"A corretora 'Ativa' é: \n Subconjunto da 'Genial': {resSubconjuntoAtiva2}.")
print(f"A corretora 'Ativa' é: \n Subconjunto da 'Elite': {resSubconjuntoAtiva3}.")

resSubconjuntoGenial = corretorasTradadas[2]["GenialTickets"] >= corretorasTradadas[0]["AgoraTickets"]
resSubconjuntoGenial2 = corretorasTradadas[2]["GenialTickets"] >= corretorasTradadas[1]["AtivaTickets"]
resSubconjuntoGenial3 = corretorasTradadas[2]["GenialTickets"] >= corretorasTradadas[4]["EliteTickets"]

print(f"A corretora 'Genial' é: \n Subconjunto da 'Ágora': {resSubconjuntoGenial}.")
print(f"A corretora 'Genial' é: \n Subconjunto da 'Ativa': {resSubconjuntoGenial2}.")
print(f"A corretora 'Genial' é: \n Subconjunto da 'Elite': {resSubconjuntoGenial3}.")

resSubconjuntoElite = corretorasTradadas[4]["EliteTickets"] >= corretorasTradadas[0]["AgoraTickets"]
resSubconjuntoElite2 = corretorasTradadas[4]["EliteTickets"] >= corretorasTradadas[1]["AtivaTickets"]
resSubconjuntoElite3 = corretorasTradadas[4]["EliteTickets"] >= corretorasTradadas[2]["GenialTickets"]

print(f"A corretora 'Elite' é: \n Subconjunto da 'Ágora': {resSubconjuntoElite}.")
print(f"A corretora 'Elite' é: \n Subconjunto da 'Ativa': {resSubconjuntoElite2}.")
print(f"A corretora 'Elite' é: \n Subconjunto da 'Genial': {resSubconjuntoElite3}.")

#exc 04
