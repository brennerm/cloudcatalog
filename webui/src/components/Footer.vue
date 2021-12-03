<template>
  <footer class="body-font w-full">
    <div class="text-gray-800 bg-gray-300">
      <div
        class="
          container
          mx-auto
          py-2
          flex flex-wrap flex-col
          md:flex-row
          justify-between
          text-sm
        "
      >
        <p class="text-center">
          Built with
          <span class="text-red-600"><HeartIcon class="inline w-4 h-4" /></span>
          by
          <a
            href="https://shipit.dev/about.html"
            class="text-blue-700"
            target="_blank"
            >brennerm</a
          >
        </p>
        <p>Service <a href="https://github.com/brennerm/cloudcatalog/issues/new?assignees=&labels=&template=new-service.md&title=%5BNEW+SERVICE%5D" target="_blank" class="text-blue-700">missing?</a></p>
        <p class="">
          Cloud Catalog is not associated with any cloud provider.
        </p>
      </div>
    </div>
  </footer>
</template>

<script>
import { HeartIcon } from "@heroicons/vue/solid";

export default {
  name: "Footer",
  props: {},
  components: {
    HeartIcon,
  },
};
</script>