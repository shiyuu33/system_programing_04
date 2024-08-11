<script setup lang="ts">
import { Restaurant } from '@/services/restaurant'
import { ref } from 'vue'

const isLoading = ref<boolean>(false)
const startPlace = ref<string>('')
const endPlace = ref<string>('')
const results = ref<unknown[]>([])

const handleSearch = async () => {
  isLoading.value = true
  const restaurantService = new Restaurant()
  results.value = await restaurantService.getRestaurantsShopList({
    startPlace: startPlace.value,
    endPlace: endPlace.value
  })
  isLoading.value = false
}
</script>

<template>
  <div class="flex min-h-dvh flex-col items-center bg-[#f8f9fa] p-6">
    <div class="flex w-full max-w-lg space-x-4">
      <input
        v-model="startPlace"
        type="text"
        placeholder="始点"
        class="w-1/2 rounded-lg border border-gray-300 p-3 text-[#242323] focus:outline-none focus:ring-2"
      />
      <input
        v-model="endPlace"
        type="text"
        placeholder="終点"
        class="w-1/2 rounded-lg border border-gray-300 p-3 text-[#242323] focus:outline-none focus:ring-2"
      />
    </div>

    <button
      @click="handleSearch"
      class="mt-6 w-full max-w-lg rounded-lg bg-[#242323] px-5 py-3 font-semibold text-[#f8f9fa] shadow-lg transition-colors duration-200 hover:bg-opacity-90 hover:shadow-xl focus:outline-none focus:ring-2 focus:ring-opacity-75"
    >
      中間地点のお店を検索
    </button>

    <ul v-if="!isLoading" class="mt-8 w-full max-w-lg space-y-4">
      <li
        v-for="(result, index) in results"
        :key="index"
        class="rounded-lg border-2 border-[#242323] bg-[#ffffff] shadow-md transition-shadow duration-200 hover:shadow-lg"
      >
        <a
          class="flex w-full items-center gap-4 p-4"
          :href="result.urls.pc"
          target="_blank"
          rel="noreferrer"
        >
          <img class="inline-block shrink-0" :src="result.logo_image" />
          <div>
            <div class="text-lg font-bold text-[#242323]">{{ result.name }}</div>
            <p class="mt-1 text-sm text-[#242323]">{{ result.address }}.</p>
          </div>
        </a>
      </li>
    </ul>
  </div>
</template>
