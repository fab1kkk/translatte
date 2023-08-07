<template>
    <section>
        <button @click="returnDummy" :disabled="loading"
            :class="[style.button.wrapper, loading ? style.button.loading : style.button.getStory]">
            {{ loading ? 'Loading...' : 'Generate useless story!' }}
        </button>
        <div v-if="loading" :class="style.animation.spinner"> </div>
        <div ref="textAreaRef" class="textarea-wrapper">
            <textarea id="cont" :class="style.textarea.data" v-if="storyData" v-model="storyData"
                :style="{ height: style.textarea.height + 'px' }">
                Story..</textarea>
        </div>
    </section>
</template>

<script>
import ApiService from '@/services/apiService';

export default {
    name: 'StoryContent',
    data() {
        return {
            storyData: '',
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
        async fetchStory() {
            this.loading = !this.loading
            const response = await ApiService.get('/api/get-story')
            let story = response.choices[0].message.content
            let i = 0;
            let interval = setInterval(() => {
                if (i < story.length) {
                    this.storyData += story[i];
                    i++;
                    if (i % 3 === 0) {
                        this.style.textarea.height += 1.5;
                    }
                } else {
                    clearInterval(interval)
                }
            }, 3);
            this.loading = !this.loading
        },
        returnDummy() {
            this.storyData = '';
            this.style.textarea.height = 0;
            let story = 'To mi się przypomniała dobra historia, byłem raz z moimi kumplami na nasypie, mocno wstawiony po alkoholu. Wszyscy byliśmy w takim euforycznym nastroju, że postanowiliśmy wspiąć się na tor kolejowy i zacząć biegać po szynach. Może nie był to najmądrzejszy pomysł, ale w tamtym momencie wydawał się niezwykle zabawny. Biegnąc po szynach, czułem się jak równy zawodnik na olimpijskim torze. Miałem wrażenie, że jestem najszybszym człowiekiem na świecie. Mój umysł był jednak na tyle zamroczony, że nie zauważyłem zbliżającego się pociągu. W pewnym momencie usłyszałem dźwięk syreny, który wprawił mnie w lekką panikę. Szybko spojrzałem w kierunku nadjeżdżającego pociągu i zobaczyłem go coraz bliżej. Wszyscy zaczęliśmy krzyczeć i biec w przeciwnym kierunku, ale nogi odmówiły mi posłuszeństwa. Upadłem na torowisko, a pociąg zbliżał się coraz bardziej. W ostatniej chwili zdołałem się odsunąć na bok, a pociąg przejechał tuż obok mnie, zostawiając tylko kilka centymetrów od mojego nosa. Po tym przeżyciu, moje towarzystwo i ja usiedliśmy na ziemi, trzęsącymi się nogami i próbując złapać oddech. Byliśmy przerażeni, ale jednocześnie nasz strach zmieszał się z ogromnym ulgą. Przeżyłem prawie śmierć przez własną głupotę. To doświadczenie nauczyło mnie, że nawet w najbardziej beztroskich chwilach powinniśmy zachować zdrowy rozsądek. Bieganie po torach kolejowych to nie żart, to niebezpieczne i nieodpowiedzialne. Od tego dnia obiecałem sobie, że nigdy więcej nie narazę swojego życia w taki sposób. Ostatecznie, ta historia skończyła się szczęśliwie, ale mogła się skończyć tragicznie. Byłem wdzięczny, że dostałem drugą szansę i od tego czasu staram się cieszyć życiem z większą odpowiedzialnością.';
            let i = 0;
            let interval = setInterval(() => {
                if (i < story.length) {
                    this.storyData += story[i];
                    i++;
                    if (i % 3 === 0) {
                        this.style.textarea.height += 1.5;
                    }
                } else {
                    clearInterval(interval)
                }
            }, 3);
        },
    },
    computed: {
        computeTextAreaHeight() {
            if (this.$refs.textAreaRef) {
                return `${this.$refs.textAreaRef.scrollHeight}px`;
            } else {
                return 'auto';
            }
        }
    },
}
</script>

<style scoped> .button-wrapper {
     transition: 0.4s linear;
     background: rgba(255, 0, 0, 0.5);
     font-size: 20px;
     border: none;
     border-radius: 0;
     padding: 3px 15px;
 }

 .button-getStory {
     width: 300px;
     cursor: pointer;
 }

 .button-loading {
     background: transparent;
     pointer-events: none;
     width: 200px;
 }

 .animation-spinner {
     border: 4px solid white;
     border-left-color: brown;
     border-right-color: lightcoral;
     border-radius: 50%;
     width: 30px;
     height: 30px;
     animation: spin 1.5s ease-in-out infinite;
     margin: 20px auto;
 }

 .textarea-wrapper {
     height: auto;
     width: 100%;
 }

 .textarea-data {
     width: 100%;
     box-sizing: border-box;
     border: none;
     padding: 30px;
     transition: height 0.3s;
     margin-top: 20px;
     font-size: 18px;
     resize: none;
     outline: none;
     background-color: rgba(0, 0, 0, 0.05);
     border-radius: 5px;
     overflow: hidden;
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