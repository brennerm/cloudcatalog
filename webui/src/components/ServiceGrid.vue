<template>
  <div class="overflow-y-auto">
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-4">
      <ServiceCard
        v-for="service in this.serviceData"
        :key="service.key"
        :name="service.name"
        :description="service.short_description"
        :url="service.link"
        :icon_url="this.providers[service.key.split('_')[0]].icon"
        :title="this.providers[service.key.split('_')[0]].name"
      />
    </div>
    <div v-show="this.serviceData.length == 0">
      <div class="text-center">
        There are no results that match your criteria.
      </div>
    </div>
  </div>
</template>

<script>
import ServiceCard from "./ServiceCard.vue";

export default {
  name: "ServiceGrid",
  props: {
    serviceData: Array,
    providers: Object,
  },
  components: {
    ServiceCard,
  },
};
</script>