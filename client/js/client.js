let api_path = "http://localhost:8888"

new Vue({
    el: '#app',
    data: {
        id: null,
        url: null,
        upvotes: null,
        downvotes: null
    },
    methods: {
        get_random() {
            axios.get(api_path.concat("/api/random-q"))
            .then(response => {
                this.id = response.data.id
                this.url = response.data.url
                this.votes.up = response.data.upvotes
                this.votes.down = response.data.downvotes
                console.log(this.id)
            })
        },
        vote(id, up) {
            console.log(up)
        }
    },
    mounted: function() {
        this.get_random()
    }
})
