<template>
    <!-- Navbar content -->
    <header>
        <router-link to="/"> <img src="../assets/dog_sunset.png" alt="logo here"></router-link>
        <nav class="navMenu">
            <ul class="nav__links">
                <li> <router-link to="/">Home</router-link> </li>
                <li> <router-link to="/about">About</router-link> </li>
                <li> <router-link to="/contact">Contact</router-link> </li>
            </ul>
        </nav>
        <router-link to="#"><button @click="getWidth">Login</button></router-link>
    </header>
    <hr style="border-color: rgba(0, 136, 169, 0.1);">
</template>


<script>
export default {
    name: 'AppNavbar',
    data() {
        return {
            url: '#',
        }
    },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap');

.router-link-active {
    color: rgba(0, 136, 169, 1);
    text-decoration: underline 0.1rem;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 25%;
}

img {
    border-radius: 50%;
    cursor: pointer;
    width: 75px;
    height: auto;
}

a,
button,
img {
    font-family: 'Montserrat', sans-serif;
    font-weight: 500;
    font-size: 18px;
    color: black;
    text-decoration: none;
}
.nav__links {
    list-style: none;
}

.nav__links li {
    display: inline;
    padding: 0 20px;
}

.nav__links li a {
    transition: all 0.3s ease 0s;
}

.nav__links li a:hover {
    color: #0088a9
}

button {
    padding: 3px 10px;
    background-color: rgba(0, 136, 169, 1);
    color: white;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease 0s;
}

button:hover {
    background-color: rgba(0, 136, 169, 0.8);
}

@media (max-width: 768px) {
    header {
        justify-content: center;
        padding: 15px;
    }
    img {
        display: none;
    }
    .nav__links {
        padding: 0;
        margin: 10px auto;
    }

}
</style>