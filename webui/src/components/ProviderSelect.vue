<template>
  <div class="flex w-full">
    <button
      v-for="(value, name, index) in this.providerToggles"
      :key="name"
      class="
        flex-grow
        bg-transparent
        border-t border-b border-gray-400
        font-bold
        text-sm
        outline-none
        focus:outline-none
        ease-linear
        transition-all
        duration-150
        py-3
      "
      :class="{
        'text-white': value,
        'rounded-l': index === 0,
        'rounded-r': index === Object.keys(this.providerToggles).length - 1,
        'border-l': index < Object.keys(this.providerToggles).length - 1,
        'border-r': index > 0,
      }"
      :style="{
        'background-color': value
          ? this.providers[name].primaryColor
          : '#FFFFFF',
      }"
      :title="this.providers[name].name"
      @click="this.$emit('providerToggleChanged', name, !value)"
      type="button"
    >
      {{ providers[name].short_name ? providers[name].short_name : providers[name].name }}
    </button>
  </div>
</template>

<script>
export default {
  name: "ProviderSelect",
  props: {
    providerToggles: Object,
    providers: Object,
  },
};
</script>