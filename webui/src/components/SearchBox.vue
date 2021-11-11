<template>
  <div class="flex w-full">
    <span
      class="
        z-10
        leading-snug
        font-normal
        absolute
        text-center text-gray-400
        absolute
        bg-transparent
        rounded
        text-base
        items-center
        justify-center
        w-8
        pl-3
        py-3
      "
    >
    <SearchIcon/>
    </span>
    <input
      type="text"
      placeholder="Search"
      v-bind:value="query"
      @input="this.$emit('queryChanged', $event.target.value)"
      class="
        py-3
        placeholder-gray-400
        text-gray-600
        relative
        bg-white bg-white
        rounded
        text-sm
        border border-gray-400
        outline-none
        focus:outline-none focus:ring
        w-full
        pl-10
        pr-14
      "
    />
    <span class="
      z-10
      leading-snug
      font-normal
      right-5
      text-center text-white
      absolute
      bg-gray-500
      rounded-full
      text-xs
      mt-3
      py-0.5
      px-2">
      {{ numberOfResults }}
    </span>
  </div>
</template>

<script>
import { SearchIcon } from '@heroicons/vue/solid'

export default {
  name: "SearchBox",
  props: {
    query: String,
    numberOfResults: Number,
  },
  components: {
    SearchIcon
  },
};
</script>