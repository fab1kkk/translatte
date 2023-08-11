<template>
    
    <div class="file-upload-container">
        <form @submit.prevent="submitForm" class="upload-form">
            <label for="fileInput" :class="[style.label.default, selectedFile.content ? 'filled' : '']">{{
                selectedFile.object ?
                selectedFile.object.name : 'Upload a file' }}</label>
            <input type="file" name="fileInput" id="fileInput" ref="fileInput" @change="handleFileChange" class="file-input"
                accept="text/plain, application/pdf">
            <button type="submit" :class="['upload-button', selectedFile.content ? 'filled' : '']"
                v-if="selectedFile.object">{{ selectedFile.content ? 'Loaded' : 'Translate' }}</button>
            </form>
            <button v-if="selectedFile.exists" @click="resetForm">Reset</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            selectedFile: {
                object: null,
                content: '',
                exists: false,
            },
            style: {
                label: {
                    default: 'file-label',
                    filled: 'file-label-filled',
                },
            },
        };
    },
    methods: {
        async submitForm() {
            if (this.selectedFile) {
                let formData = new FormData();
                formData.append('file', this.selectedFile.object);
                try {
                    const response = await axios.post('http://127.0.0.1:8000/uploadfile/', formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data',
                        }
                    });
                    this.selectedFile.content = response.data.content;
                    this.$emit("fileUploaded", response.data.content);
                } catch (error) {
                    console.error('Error uploading file: ', error);
                }
            } else {
                console.log('No file provided');
            }
        },
        handleFileChange(event) {
            console.log(event)
            this.selectedFile.object = event.target.files[0];
            this.selectedFile.exists = true;
        },

        resetForm() {
            this.$refs.fileInput.value = '';
            this.selectedFile.object = null;
            this.selectedFile.content = '';
            this.$emit("fileUploaded", null);
            this.selectedFile.exists = false;
        },
    }

}
</script>

<style scoped>
.file-upload-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
}


.upload-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: auto;
}

.file-label {
    font-size: 20px;
    padding: 15px;
    background-color: rgba(0, 136, 169, 1);
    color: white;
    border-radius: 5px;
    width: 150px;
    text-align: center;
    cursor: pointer;
    transition: background-color 0.4s;
}

.filled {
    background-color: rgba(0, 169, 37, 0.7) !important;
}

.file-input {
    display: none;
}

.upload-button {
    color: white;
    background-color: #666;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.4s;
    transition: opacity 0.5s;
    margin: 5px 0;
    height: 35px;
    width: 100%;
}
</style>