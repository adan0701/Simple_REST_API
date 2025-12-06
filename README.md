# Simple quotes REST API

## Fonctionnement : 

- Utilisation de la librairie flask pour gérer l'API.
- Utilisation de JSON pour gérer une base de données locale.

## Routes :

- /quotes (GET)
- /quotes/random (GET)
- /quotes/add (POST)
- /quotes/<id> (PATCH)
- /quotes/<id> (DELETE)
- /health (GET)

### /quotes :

- Méthode : GET
- Retourne toutes les citations au format JSON : "text", "author" et "id" (*Voir format base de données JSON*).
- Si un argument est donné : `?author=Einstein` (*uniquement l'auteur fonctionne*) renvoie uniquement les citations de cet auteur.

### /quotes/random : 

- Méthode : GET
- Retourne une citation aléatoire au format JSON : "text", "author" et "id" (*Voir format base de données JSON*).

### /quotes/add : 

- Méthode : POST
- Ajoute la citation fournie dans la requête qui doit être au format JSON (*Voir format base de données JSON*).
- Retourne "Citation ajoutée" si la requête s'est exécutée sans erreur.
- Incremente l'id automatiquement.
- Retourne une erreur 400 si les conditions suivantes ne sont pas remplies : 
    - Il y a une requête avec un fichier json
    - Les clés "text" et "author" et uniquement celle-ci sont présentes
    - Les clés ci-dessus ne sont pas vides

### /quotes/<id> : 

- Méthode : PATCH
- Modifie la citation avec l'id dans la requête, l'id est nécessaire.
- Retourne une erreur 400 si les conditions suivantes ne sont pas remplies : 
    - Il y a une requête avec un fichier json
    - Les clés "text" et/ou "author" et uniquement celle-ci sont présentes
    - La/les clés ci-dessus ne sont pas vides


### /quotes/<id> : 

- Méthode : DELETE
- Supprime la citation avec l'id dans la requête, l'id est nécessaire.

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
        "author": "Auteur",
        "id": 0
    }
]
```

## Exemple d'utilisation : 

`127.0.0.1:5000/quotes/random` retournera : 

```json
{
  "author": "Confucius",
  "id": 5,
  "text": "Choisis un travail que tu aimes, et tu n'auras pas à travailler un seul jour de ta vie."
}
```
## Librairie nécessaire :
- Flask
- Random
- JSON

Toutes les librairies nécessaires peuvent être ajoutées à l'aide de `pip` et du fichier `requirements.txt`