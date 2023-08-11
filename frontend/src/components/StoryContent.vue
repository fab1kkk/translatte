<template>
    <div class="story-content-container">
        <div class="read-btn-wrapper">
            <button @click="returnDummy" :disabled="loading || !uploadedContent"
                :class="[style.button.wrapper, loading ? style.button.loading : style.button.getStory]">
                {{ loading ? 'Reading...' : 'Translatte' }}
            </button>
        </div>
        <div class="story-content-wrapper" v-if="uploadedContent">
            <div class="input">
                <div v-if="loading" :class="style.animation.spinner"> </div>
                <div ref="textAreaRef" class="textarea-wrapper">
                    <textarea id="cont" :class="style.textarea.data" v-model="originalText"
                        :style="{ height: style.textarea.height + 'px' }">
            </textarea>
                </div>
            </div>
            <div class="output">
                <div v-if="loading" :class="style.animation.spinner"> </div>
                <div ref="textAreaRef" class="textarea-wrapper">
                    <textarea id="cont" :class="style.textarea.data" v-model="translatedText"
                        :style="{ height: style.textarea.height + 'px' }">
        </textarea>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'StoryContent',
    data() {
        return {
            originalText: '',
            translatedText: '',
            loading: false,
            style: {
                button: {
                    wrapper: 'button-wrapper',
                    getStory: 'button-getStory',
                    loading: 'button-loading',
                },
                textarea: {
                    data: 'textarea-data',
                    height: 100,
                },
                animation: {
                    spinner: 'animation-spinner',
                }
            }
        };
    },
    methods: {
        returnDummy() {
            this.loading = !this.loading;
            console.log(this.uploadedContent)
            this.originalText = this.uploadedContent.original;
            this.translatedText = this.uploadedContent.translated;
            this.loading = !this.loading;
        }
    },
    computed: {
        computeTextAreaHeight() {
            if (this.$refs.textAreaRef) {
                return `${this.$refs.textAreaRef.scrollHeight}px`;
            }
            else {
                return 'auto';
            }
        }
    },
    props: {
        uploadedContent: String,
    }
}
</script>

<style scoped> .story-content-container {
     margin-top: 15px;
 }

 .story-content-wrapper {
     display: flex;
     flex-direction: row;
     gap: 20px;
     margin-top: 20px;
     text-align: center;
 }

 .input,
 .output {
     width: 50%;
 }

 .read-btn-wrapper {
     display: flex;
     justify-content: center;
 }

 .button-wrapper {
     transition: 0.4s linear;
     background: rgba(255, 0, 0, 0.4);
     font-size: 20px;
     border: none;
     border-radius: 0;
     padding: 3px 15px;
     width: 300px;
     border-radius: 5px;
 }

 .button-getStory {
     cursor: pointer;
 }

 .button-loading {
     background: transparent;
     pointer-events: none;
     width: 200px;
 }

 .animation-spinner {
     border: 4px solid white;
     border-left-color: rgb(27, 174, 219);
     border-right-color: lightcoral;
     border-radius: 50%;
     width: 15px;
     height: 15px;
     animation: spin 1.5s ease-in-out infinite;
     margin: 5px auto;
 }

 .textarea-wrapper {
     width: 100%;
 }

 .textarea-data {
     width: 100%;
     box-sizing: border-box;
     border: none;
     padding: 30px;
     margin-top: 20px;
     font-size: 18px;
     resize: vertical;
     outline: none;
     background-color: rgba(0, 0, 0, 0.05);
     border-radius: 5px;
 }

 @media (max-width: 768px) {
     .story-content-wrapper {
         flex-direction: column;
     }

     .input,
     .output {
         width: 100%;
     }
 }

 @keyframes spin {
     0% {
         transform: rotate(0deg);
     }

     100% {
         transform: rotate(720deg);
     }
 }
</style>