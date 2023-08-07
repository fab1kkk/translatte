<template>
    <div class="navbar">
        <AppNavbar />
    </div>
    <div class="content-wrapper">
        <slot></slot>
    </div>
    <AppFooter />
</template>


<script>
import AppFooter from '@/components/AppFooter.vue';
import AppNavbar from '@/components/AppNavbar.vue';

export default {
    name: 'PageLayout',
    components: {
        AppNavbar,
        AppFooter
    }
}
</script>

<style scoped>
.navbar {
    background-color: rgba(33,33,33, 0.1);
}
.content-wrapper {
    max-width: 1444px;
    margin: 0 auto;
    padding: 0 10px;

}
</style>