<template>
  <div class="flex flex-col h-screen">
    <div class="pb-2 shadow">
    <Header/>
    <div class="flex flex-row flex-wrap gap-2 md:flex-nowrap pl-2 pr-2">
      <ProviderSelect
        :providerToggles="this.providerToggles"
        :providers="this.providers"
        @providerToggleChanged="this.providerToggleChanged"
      />
      <SearchBox :query="this.searchQuery" @queryChanged="this.queryChanged"/>
    </div>
    </div>
    <ServiceGrid :serviceData="this.filteredServiceData" :providers="this.providers" class="pt-3 pb-3 flex-grow"/>
    <Footer/>
  </div>
</template>

<script>
import Footer from "./components/Footer.vue";
import Header from "./components/Header.vue";
import ProviderSelect from "./components/ProviderSelect.vue";
import ServiceGrid from "./components/ServiceGrid.vue";
import SearchBox from "./components/SearchBox.vue";
import serviceData from "./assets/service_data.json";

export default {
  name: "App",
  components: {
    Footer,
    Header,
    ProviderSelect,
    SearchBox,
    ServiceGrid,
  },
  data() {
    return {
      serviceData: serviceData
        .sort(function (a, b) {
          const key_a = a.key.split("_", 2)[1]
          const key_b = b.key.split("_", 2)[1]

          if (key_a < key_b) {
            return -1;
          }
          if (key_a > key_b) {
            return 1;
          }
          return 0;
        }),
      searchQuery: "",
      providerToggles: {
        aws: true,
        alibaba: true,
        azure: true,
        digitalocean: true,
        gcp: true,
        ibm: true,
      },
      providers: {
        alibaba: {
          name: "Alibaba Cloud",
          short_name: "Alibaba",
          icon: "https://www.vectorlogo.zone/logos/alibabacloud/alibabacloud-icon.svg",
          primaryColor: "#FF6701",
        },
        aws: {
          name: "Amazon Web Services",
          short_name: "AWS",
          icon: "https://uxwing.com/wp-content/themes/uxwing/download/10-brands-and-social-media/aws.svg",
          primaryColor: "#FF9900",
        },
        azure: {
          name: "Microsoft Azure",
          short_name: "Azure",
          icon: "https://uxwing.com/wp-content/themes/uxwing/download/10-brands-and-social-media/azure.svg",
          primaryColor: "#008AD7",
        },
        digitalocean: {
          name: "DigitalOcean",
          icon: "https://cdn.icon-icons.com/icons2/2699/PNG/512/digitalocean_logo_icon_169273.png",
          primaryColor: "#0069FF",
        },
        gcp: {
          name: "Google Cloud Platform",
          short_name: "GCP",
          icon: "https://uxwing.com/wp-content/themes/uxwing/download/10-brands-and-social-media/google-cloud.svg",
          primaryColor: "#0F9D58",
        },
        ibm: {
          name: "IBM Cloud",
          short_name: "IBM",
          icon: "https://www.vectorlogo.zone/logos/ibm_cloud/ibm_cloud-icon.svg",
          primaryColor: "#008DEE",
        },
      },
    };
  },
  computed: {
    filteredServiceData: function () {
      var enabledProviders = [];

      for (var key in this.providerToggles) {
        if (this.providerToggles[key]) {
          enabledProviders.push(key);
        }
      }
      
      var filteredServiceData = this.serviceData.filter((service) =>
        Object.keys(service).some((k) =>
          service[k].toLowerCase().includes(this.searchQuery.toLowerCase())
        )
      );

      return filteredServiceData.filter((service) =>
        enabledProviders.some((provider) => service.key.startsWith(provider))
      );
    },
  },
  methods: {
    queryChanged: function (value) {
      this.searchQuery = value;
    },
    providerToggleChanged: function (provider, value) {
      this.providerToggles[provider] = value;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
