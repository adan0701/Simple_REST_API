# Simple quotes REST API

## Routes :

- /quote/all (GET)
- /quote/random (GET)
- /quote/add (POST)
- /health (GET)

### /quote/all :

- Méthode : GET
- Retourne toutes les citations au format JSON : "text" et "author"

### /quote/random : 

- Méthode : GET
- Retourne une citation aléatoire au format JSON : "text" et "author"

### /quote/add : 

- Méthode : POST
- Ajoute la citation fournie dans la requête au format JSON (*Voir format base de données JSON*)
- Retourne "Citation ajoutée" si la requête s'est exécutée sans erreur.

### /health : 

- Méthode : GET
- Retourne le statut de l'API au format JSON : "count" (Nombre de citation présente dans la base de données) et "status"

## Format de la base de donnée JSON : 

```json
[
    {
        "text": "Citation",
        "author": "Auteur"
    }
]
```

## Exemple d'utilisation : 

`127.0.0.1:5000/heath` retournera : 

```json
{
    "status": "ok",
    "count": 5
}
```