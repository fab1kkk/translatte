<template>
    <Layout>
        <div class="home">
            <StoryContent />
        </div>
    </Layout>
</template>


<script>
import StoryContent from "@/components/StoryContent.vue";
import Layout from "@/layout/Layout.vue";


export default {
    name: "HomeView",
    components: {
        StoryContent,
        Layout
    },
};
</script>

<style>
.home {
    max-width: 1444px;
    margin: 0 auto;
    padding: 0 10px;
}
</style>