<template>
  <div class="shadow-md rounded-md hover:bg-gray-400 hover:text-white">
    <a :href="this.url" target="_blank">
      <img :src="this.icon_url" class="w-8 pt-2 pl-2" alt="" />
      <div class="p-4">
        <h5 class="text-xl font-semibold mb-2">{{ name }}</h5>
        <p class="mb-4">{{ description }}</p>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: "ServiceCard",
  props: {
    name: String,
    description: String,
    url: String,
    icon_url: String,
  },
};
</script>