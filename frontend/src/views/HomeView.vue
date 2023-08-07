<template>
    <Layout>
        <div class="home">
            <div class="child1">
                <StoryContent />
            </div>
            <div class="child2">
                <!-- <StoryContent /> -->
            </div>
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

<style scoped>
.home {
    display: flex;
    flex-direction: row;
    gap: 20px;
    margin-top: 20px;
    text-align: center;
}

.child1 {
    width: 50%;
}

.child2 {
    width: 50%;
}

@media (max-width: 768px) {
    .home {
        flex-direction: column;
    }

    .child1, .child2 {
        width: 100%;
    }

    .child1 {
        text-align: center;
    }
}
</style>