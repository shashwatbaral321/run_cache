import matplotlib.pyplot as plt

# Example data from simulation
cache_sizes = ["32kB", "64kB", "128kB"]
hit_rates = [85, 88, 90]  # Example hit rates
miss_rates = [15, 12, 10]  # Example miss rates
latencies = [50, 45, 40]  # Example memory access latencies

# Plot Cache Hit Rates and Miss Rates
plt.figure(figsize=(10, 5))
plt.plot(cache_sizes, hit_rates, marker="o", label="Hit Rate (%)")
plt.plot(cache_sizes, miss_rates, marker="o", label="Miss Rate (%)")
plt.xlabel("Cache Size")
plt.ylabel("Percentage")
plt.title("Cache Hit and Miss Rate vs. Cache Size")
plt.legend()
plt.grid(True)
plt.savefig("cache_hit_miss_rates.png")  # Save plot as PNG file

# Plot Memory Access Latency
plt.figure(figsize=(10, 5))
plt.plot(
    cache_sizes, latencies, marker="o", color="green", label="Latency (cycles)"
)
plt.xlabel("Cache Size")
plt.ylabel("Latency (cycles)")
plt.title("Average Memory Access Latency vs. Cache Size")
plt.legend()
plt.grid(True)
plt.savefig("memory_access_latency.png")  # Save plot as PNG file
