<template>
    <footer class="br-footer">
        <div class="br-footer-logo">
            <img src="~/assets/images/logo.png" alt="Logo" />
        </div>
        <h2 class="br-footer-title">Contacta con nosotros</h2>
        <h3 class="br-footer-subtitle">Tienes alguna duda</h3>
        <div class="br-footer-description">
            Estaremos encantados de poder ayudarte, detrás de cualquier método
            de contacto habrá uno de nosotros esperándote
        </div>
        <Social />
        <nav class="br-footer-nav">
            <ul class="br-footer-nav-list">
                <li class="br-footer-nav-list-item">
                    <NuxtLink to="/footer-links/legal">Aviso legal</NuxtLink>
                </li>
                <li class="br-footer-nav-list-item">
                    <NuxtLink to="/footer-links/privacy">Política de privacidad</NuxtLink>
                </li>
                <li class="br-footer-nav-list-item">
                    <NuxtLink to="/footer-links/cookies">Política de cookies</NuxtLink>
                </li>
                <li class="br-footer-nav-list-item">
                    <NuxtLink to="/footer-links/terms-condition"
                        >Terminos y condiciones
                    </NuxtLink>
                </li>
                <li class="br-footer-nav-list-item">
                    <NuxtLink to="/footer-links/state-grants">Subvenciones</NuxtLink>
                </li>
            </ul>
        </nav>
    </footer>
</template>
<script>
import Social from "~/components/reusable/Social.vue";

export default {
    name: "Footer",
    components: {
        Social,
    },
};
</script>
<style lang="scss" scoped>
.br-footer {
    background-color: $color-primary-blue;
    color: $color-white;
    padding: 2rem;
    text-align: center;
    &-logo {
        margin-bottom: 1rem;
        & > img {
            width: 84px;
        }
    }
    &-description {
        margin: 0 auto;
        max-width: 350px;
    }

    &-nav {
        margin-top: 2rem;
        @include mobile-layout {
            margin-top: 3rem;
        }
        &-list {
            display: flex;
            flex-flow: row wrap;
            justify-content: center;
            align-items: center;
            list-style: none;
            margin: 0;
            padding: 0;

            @include mobile-layout {
                flex-direction: column;
                gap: 16px;
            }

            &-item {
                &:not(:last-child) {
                    margin-right: 1rem;
                }
                & > a {
                    color: $color-white;
                    border-bottom: unset;
                    transition: border-bottom 2ms linear;
                    &:hover {
                        border-bottom: 1.5px solid $color-white;
                        padding-bottom: 3px;
                    }
                }
            }
        }
    }
}
</style>