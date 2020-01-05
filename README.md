#  Q

Q: "Le meilleur site de Q du MONDE ENTIER"

Q is a modest "Q" site allowing you to vote for "Q" images.
You can also see the list of all "Q" images sorted by popularity.

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
- `"up":booleen` "True" if it is an upvote or "False" for downvote

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
