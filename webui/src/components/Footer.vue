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
            href="https://brennerm.github.io/about.html"
            class="text-blue-700"
            target="_blank"
            >brennerm</a
          >
        </p>
        <p>Service <a href="" class="text-blue-700">missing?</a></p>
        <p class="">
          <a href="" class="text-blue-700">cloudcatalog.dev</a> is not
          associated with any cloud provider.
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