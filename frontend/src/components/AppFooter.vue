<template>
    <footer>
        <div :class="style.footer.copyright">
            <span>
                &copy; {{ currentYear }}. {{ copyright }}
            </span>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'AppFooter',
    data() {
        return {
            currentYear: new Date().getFullYear(),
            appName: 'Piglord',
            style: {
                footer: {
                    copyright: "footer-copyright",
                }
            }
        };
    },
    computed: {
        copyright() {
            return 'All rights reserved.';
        },
    }
}
</script>

<style scoped>

.footer-copyright {
    max-width: 1444px;
    margin: 0 auto;
    text-align: center;
    padding: 20px 5px;
}
</style>