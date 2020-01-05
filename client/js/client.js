let api_path = "http://localhost:8888"

new Vue({
    el: '#app',
    data: {
        id: null,
        url: null,
        votes: {
            up: null,
            down: null
        }
    },
    methods: {
        get_random() {
            axios.get(api_path.concat("/api/random-q"))
            .then(response => {
                this.id = response.data.id
                this.url = response.data.url
                this.votes = response.data.votes
            })
        },
        vote(id, up) {
            let dest = "False"

            if (up == true) {
                dest = "True"
                console.log("ui")
            }
            axios.post(api_path.concat("/api/", id, "/vote"), {up: dest})
        }
    },
    mounted: function() {
        this.get_random()
    }
})
