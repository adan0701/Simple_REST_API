# Simple quotes REST API

## Fonctionnement : 

- Utilisation de la librairie flask pour gérer l'API.
- Utilisation de JSON pour gérer une base de données locale.

## Routes :

- /quote/all (GET)
- /quote/random (GET)
- /quote/add (POST)
- /health (GET)

### /quote/all :

- Méthode : GET
- Retourne toutes les citations au format JSON : "text" et "author" (*Voir format base de données JSON*).

### /quote/random : 

- Méthode : GET
- Retourne une citation aléatoire au format JSON : "text" et "author" (*Voir format base de données JSON*).

### /quote/add : 

- Méthode : POST
- Ajoute la citation fournie dans la requête qui doit être au format JSON (*Voir format base de données JSON*).
- Retourne "Citation ajoutée" si la requête s'est exécutée sans erreur.
- Retourne une erreur 400 si les conditions suivantes ne sont pas remplies : 
    - Il y a une requête avec un fichier json
    - Les clés "text" et "author" et uniquement celle-ci sont présentes
    - Les clés ci-dessus ne sont pas vides

### /health : 

- Méthode : GET
- Retourne le statut de l'API au format JSON : "count" (Nombre de citation présente dans la base de données) et "status".


## Gestion des erreurs : 

| Code erreur  | Erreur |
| ------------- | ------------- |
| 400  | Bad request  |
| 401  | Unauthorized  |
| 403  | Forbidden  |
| 404  | Route not found  |
| 405  | Method not allowed  |
| 409  | Conflict  |
| 500  | Server error |


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