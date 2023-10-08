<template>
    <header class="br-header">
        <ul class="br-header-menu-list">
            <li class="br-header-menu-list-item logo">
                <NuxtLink href="/">
                    <img src="~/assets/images/logo.png" alt="Logo" />
                </NuxtLink>
            </li>
            <li class="br-header-menu-list-item">
                <NuxtLink href="/about">Quienes somos</NuxtLink>
            </li>
            <li class="br-header-menu-list-item">
                <NuxtLink href="/shop">Tienda</NuxtLink>
            </li>
            <li class="br-header-menu-list-item">
                <NuxtLink href="/help">Ayuda</NuxtLink>
            </li>
            <li class="br-header-menu-list-item">
                <NuxtLink href="/contact">Contacto</NuxtLink>
            </li>
        </ul>
    </header>
</template>

<style lang="scss">
.br-header {
    &-menu-list {
        display: flex;

        &-item {
            &:not(:last-child) {
                margin-right: 1rem;
            }

            &.logo {
                img {
                    width: 35px;
                }
            }
        }
    }
}
</style>