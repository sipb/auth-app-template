<template>
  <v-app>
    <v-content>
      <v-container class="text-center">
        <v-row>
          <v-col class="my-4">
            <h1 class="display-2 font-weight-bold mb-3">
              SIPB Wireless Internet Service Provider
            </h1>

            <p class="subheading font-weight-regular">
              A way for off-campus members of the MIT community to access free,
              high speed internet.
            </p>
          </v-col>
        </v-row>

        <v-row
          v-if="kerb === ''"
        >
          <v-col>
            <h2 class="headline font-weight-bold mb-3">
              Please log in to manage your internet access
            </h2>

            <v-btn
              href="https://wisp.mit.edu:444/"
              outlined
              color="primary"
            >
              Login
            </v-btn>
          </v-col>
        </v-row>

        <v-row v-else>
          <v-col cols="12">
            <h2 class="headline font-weight-bold mb-3">
              Important Links
            </h2>

            <v-row justify="center">
              <a
                v-for="(link, i) in importantLinks"
                :key="i"
                :href="link.href"
                class="subheading mx-3"
                target="_blank"
              >
                {{ link.text }}
              </a>
            </v-row>
          </v-col>

          <v-col
            class="mb-5"
            cols="12"
          >
            <h2 class="headline font-weight-bold mb-3">
              Ecosystem
            </h2>

            <v-row justify="center">
              <a
                v-for="(eco, i) in ecosystem"
                :key="i"
                :href="eco.href"
                class="subheading mx-3"
                target="_blank"
              >
                {{ eco.text }}
              </a>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    kerb: '',
    ecosystem: [
      {
        text: 'vuetify-loader',
        href: 'https://github.com/vuetifyjs/vuetify-loader',
      },
      {
        text: 'github',
        href: 'https://github.com/vuetifyjs/vuetify',
      },
      {
        text: 'awesome-vuetify',
        href: 'https://github.com/vuetifyjs/awesome-vuetify',
      },
    ],
    importantLinks: [
      {
        text: 'Documentation',
        href: 'https://vuetifyjs.com',
      },
      {
        text: 'Chat',
        href: 'https://community.vuetifyjs.com',
      },
      {
        text: 'Made with Vuetify',
        href: 'https://madewithvuejs.com/vuetify',
      },
      {
        text: 'Twitter',
        href: 'https://twitter.com/vuetifyjs',
      },
      {
        text: 'Articles',
        href: 'https://medium.com/vuetify',
      },
    ],
  }),
  created() {
    fetch('backend.py')
      .then((response) => response.json())
      .then((j) => {
        this.kerb = j.kerb;
      })
      .catch((err) => {
        console.log('Got this error trying to get kerb from backend.'
                  + ' Probably means you need to go to :444');
        console.warn(err);
      });
  },
};
</script>
