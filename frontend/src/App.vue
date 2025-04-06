<template>
  <div class="bg-black min-h-screen flex flex-col ">
    <AppNav />
    <main class="flex-grow w-[80%] lg:w-[50%] mx-auto">
      <router-view />
    </main>
    <AppFooter />
  </div>
  <!-- <v-app>
      <v-app-bar class="bg-primary">
        <v-toolbar-title>Movie Review Analyzer</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn text @click="$router.push('/')">Home</v-btn>
        <v-btn text @click="$router.push('/admin')">Admin</v-btn>
      </v-app-bar>
    <v-main class="space-y-12" style="margin-top: 1rem;">
      <v-container fluid style="height: 100vh;">
        <v-row justify="center" align="center" class="min-h-screen">
          <v-col cols="12" md="8" lg="6">
            <v-card class="elevation-26 pa-4" color="black">
              <router-view />
            </v-card>
          </v-col>
        </v-row>
      </v-container>            
    </v-main>
    <v-footer class="bg-primary" app>
      <v-container>
        <v-row justify="center">
          <v-col cols="12" class="text-center">
            <p class="white--text">&copy; 2025 Movie Review Analyzer</p>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
  </v-app> -->
</template>

<script setup>
import AppFooter from './components/AppFooter.vue';
import AppNav from './components/AppNav.vue';

  //
</script>
