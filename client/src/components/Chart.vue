<template>
  <div>
    <svg width="500" height="500">
      <g
        class="modeld"
        v-for="modeld in layoutData.children"
        :key="modeld.data.name"
        :style="{
          transform: `translate(${modeld.x}px, ${modeld.y}px)`
        }"
      >
        <circle class="modeld__circle" :r="modeld.r" :fill="modeld.data.color"></circle>
        <text class="modeld__label">{{ modeld.data.name }}</text>
      </g>
    </svg>
  </div>
</template>

<script>

import { hierarchy, pack } from 'd3-hierarchy';
import axios from 'axios';

export default {
  data() {
    return {
      models: [
      ],
    };
  },
  methods: {
    getModels() {
      const path = 'http://localhost:5000/data';
      axios.get(path)
        .then((res) => {
          this.models = res.data.models;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  computed: {
    transformedmodeldData() {
      return {
        name: 'Top Level',
        children: this.models.map(modeld => ({
          ...modeld,
          size: modeld.count,
          parent: 'Top Level',
        })),
      };
    },

    layoutData() {
      // Generate a D3 hierarchy
      const rootHierarchy = hierarchy(this.transformedmodeldData)
        .sum(d => d.size)
        .sort((a, b) => b.value - a.value);

      // Pack the circles inside the viewbox
      return pack()
        .size([500, 500])
        .padding(10)(rootHierarchy);
    },
  },
  created() {
    this.getModels();
    setInterval(() => {
      this.getModels();
    }, 10000);
  },
};
</script>

<style>
body {
  font: 16px -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica,
    Arial, sans-serif;
}

svg {
  display: block;
  margin: 0 auto;
}

.modeld {
  transition: transform 0.2s ease-in-out;
  text-anchor: middle;
}

.modeld__circle {
  transition: r 0.2s ease-in-out;
}

.modeld__label {
  fill: #fff;
  font-weight: bold;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.controls {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.control {
  display: inline-flex;
  flex-direction: column;
  margin: 0 4px;
}

.control label {
  font-size: 14px;
  font-weight: bold;
  margin-bottom: 4px;
}

.control input {
  display: block;
  font: inherit;
  width: 100px;
}
</style>
