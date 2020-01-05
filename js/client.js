new Vue({
    el: '#app',
    data: {
        id: 1,
        url: "https://cdn.dribbble.com/users/1913212/screenshots/6414669/01.jpg",
        upvotes: 0,
        downvotes: 0
    },
    methods: {
        vote(id, up) {
            console.log(id)
            console.log(up)
        }
    }
})
