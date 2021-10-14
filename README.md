#  Q
Q: "Le meilleur site de Q du MONDE ENTIER"

![preview.png preview](https://raw.githubusercontent.com/valentinpx/Q/master/preview.png)

Site réalisé dans le cadre d'un test technique afin de réaliser mon stage de fin de première année à [la Quincaillerie](https://la-quincaillerie.fr/).

## API
###  List all of "Q" images sorted by popularity
***Definition***
- `GET /api`

***Response***
- `200 OK` on success
```json
[
    {
        "id" : 42,
        "url": "https://cdn.dribbble.com/users/230124/screenshots/4296888/qampersand1.png",
        "votes": {
            "up" : 100,
            "down" : 2
        }
    },
    {
        "id" : 12,
        "url": "https://cdn.dribbble.com/users/297873/screenshots/6358046/q-06_final_dribbble_4x.jpg",
        "votes": {
            "up" : 314,
            "down" : 420
        }
    }
]
```

### Get a specified "Q" image
***Definition***
- `GET /api/42`

***Response***
- `200 OK` on success
```json
{
    "id" : 42,
    "url": "https://cdn.dribbble.com/users/230124/screenshots/4296888/qampersand1.png",
    "votes": {
        "up" : 100,
        "down" : 2
    }
}
```
- `404 Not Found` if "Q" does not exist

### Get a random "Q" image
***Definition***
- `GET /api/random-q`

***Response***
- `200 OK` on success
```json
{
    "id" : 42,
    "url": "https://cdn.dribbble.com/users/230124/screenshots/4296888/qampersand1.png",
    "votes": {
        "up" : 100,
        "down" : 2
    }
}
```
### Upvote or downvote a "Q" image
***Definition***
- `POST /api/<id>/vote`

***Arguments***
- `"up":string` "true" if it is an upvote or "false" for downvote

***Response***
- `200 OK` on success
```json
{
    "id" : 42,
    "url": "https://cdn.dribbble.com/users/230124/screenshots/4296888/qampersand1.png",
    "votes": {
        "up" : 101,
        "down" : 2
    }
}
```
- `404 Not Found` if "Q" does not exist
