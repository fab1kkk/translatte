<template>
    <div class="file-upload-container">
        <form @submit.prevent="submitForm" class="upload-form">
            <label for="fileInput" :class="[style.label.default, selectedFile ? 'filled' : '']">{{ selectedFile ? selectedFile.name : 'Upload file' }}</label>
            <input type="file" name="fileInput" id="fileInput" ref="fileInput" @change="handleFileChange" class="file-input"
                accept="text/plain, application/pdf">
            <button type="submit" class="upload-button">Process</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            selectedFile: null,
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
            console.log(this.selectedFile)
        },
        handleFileChange(event) {
            this.selectedFile = event.target.files[0]
            console.log(this.selectedFile.name)
        }
    }

}
</script>

<style scoped>
.file-upload-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

.title {
    font-size: 24px;
    margin-bottom: 20px;
}

.upload-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.file-label {
    font-size: 18px;
    padding: 15px;
    border: 2px solid rgba(0, 136, 169, 1);
    border-radius: 5px;
    margin-bottom: 10px;
    cursor: pointer;
    transition: all 0.4s;
}
.filled { 
    background-color: rgba(22, 204, 37, 0.5);
}
.file-label:hover {
    background-color: rgba(0, 136, 169, 0.8);
}

.file-input {
    margin-bottom: 10px;
    display: none;
}

.upload-button {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.2s;
}

.upload-button:hover {
    background-color: #0056b3;
}
</style>