<template>
    <Layout>
        <div class="home">
            <FIleUploadButton @fileUploaded="handleFileUploaded" />
            <StoryContent :uploadedContent="uploadedContent" />
        </div>
    </Layout>
</template>


<script>
import FIleUploadButton from "@/components/FIleUploadButton.vue";
import StoryContent from "@/components/StoryContent.vue";
import Layout from "@/layout/Layout.vue";


export default {
    name: "HomeView",
    components: {
        StoryContent,
        Layout,
        FIleUploadButton,
    },
    data() {
        return {
            uploadedContent: '',
        }
    },
    methods: {
        handleFileUploaded(content) {
            this.uploadedContent = content;
        }
    }
    
};
</script>

<style>
.home {
    max-width: 1444px;
    margin: 0 auto;
    padding: 0 10px;
}
</style>