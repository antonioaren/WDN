<template>
    <div class="br-social">
        <div class="br-social-item">
            <!-- Facebook -->
            <a href="https://www.facebook.com/antonioaren" target="_blank">
                <img src="~/assets/svg/facebook.svg" alt="Facebook" />
            </a>
        </div>
        <div class="br-social-item">
            <!-- Instagram -->
            <a href="https://www.instagram.com/antonioaren" target="_blank">
                <img src="~/assets/svg/instagram.svg" alt="Instagram" />
            </a>
        </div>
        <div class="br-social-item">
            <!-- Linkedin -->
            <a href="https://www.linkedin.com/in/antonioaren" target="_blank">
                <img src="~/assets/svg/linkedin.svg" alt="Linkedin" />
            </a>
        </div>
        <div class="br-social-item">
            <!-- Mail -->
            <a href="mailto:antonioaren2@gmail.com" target="_blank">
                <img src="~/assets/svg/mail.svg" alt="Mail" />
            </a>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.br-social {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 3rem;

    &-item {
        display: flex;
        align-items: center;
        margin-right: 12px;

        & > a {
            display: flex;
            align-items: flex-end;
            justify-content: flex-end;
            border: 1px solid $color-white;
            border-radius: 50%;
            padding: 10px;
            & > img {
                width: 25px;
                height: 25px;
            }
        }
    }
}
</style>