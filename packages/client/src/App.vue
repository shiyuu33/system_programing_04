<script setup lang="ts">
import { ref } from 'vue'

const statPlace = ref<string>('')
const endPlace = ref<string>('')
const results = ref<string[]>(['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh'])

const handleSearch = () => {}
</script>

<template>
  <div class="flex flex-col items-center p-6" style="background-color: #f8f9fa; min-height: 100vh">
    <div class="flex w-full max-w-lg space-x-4">
      <input
        v-model="statPlace"
        type="text"
        placeholder="始点"
        class="w-1/2 rounded-lg border border-gray-300 p-3 focus:outline-none focus:ring-2"
        style="color: #242323; border-color: #242323; focus:ring: #242323;"
      />
      <input
        v-model="endPlace"
        type="text"
        placeholder="終点"
        class="w-1/2 rounded-lg border border-gray-300 p-3 focus:outline-none focus:ring-2"
        style="color: #242323; border-color: #242323; focus:ring: #242323;"
      />
    </div>

    <button
      @click="handleSearch"
      class="mt-6 w-full max-w-lg rounded-lg px-5 py-3 font-semibold shadow-lg transition-colors duration-200 hover:shadow-xl focus:outline-none focus:ring-2 focus:ring-opacity-75"
      style="background-color: #242323; color: #f8f9fa; focus:ring: #242323; hover:bg-opacity-90;"
    >
      中間地点のお店を検索
    </button>

    <ul class="mt-8 w-full max-w-lg space-y-4">
      <li
        v-for="(result, index) in results"
        :key="index"
        class="rounded-lg border-2 p-4 shadow-md transition-shadow duration-200 hover:shadow-lg"
        style="border-color: #242323; background-color: #ffffff"
      >
        <div class="text-lg font-bold" style="color: #242323">{{ result }}</div>
        <p class="mt-1 text-sm" style="color: #242323">
          This is a brief description of {{ result }}.
        </p>
      </li>
    </ul>
  </div>
</template>
