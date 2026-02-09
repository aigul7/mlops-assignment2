# ML Energy Consumption Discussion

## 1. The ML.ENERGY Initiative

**Website:** https://ml.energy/

### Overview

The ML.ENERGY Initiative is a research effort focused on measuring and optimizing energy consumption in machine learning systems. They provide energy consumption benchmarks for ML models, tools to measure real-world usage, and research on sustainable AI practices.

### My Position: SUPPORT (with nuance)

#### Arguments FOR Energy Awareness

**1. Hidden Environmental Costs**

Training large models consumes massive energy. Research shows that training a single large language model can emit as much CO2 as 5 cars over their lifetime. Without measurement, we cannot optimize.

**2. Economic Impact**

Energy costs real money. In production, a model making millions of predictions daily can have significant electricity costs. Measuring helps optimize for both sustainability AND cost.

**3. Professional Responsibility**

As ML engineers, we should consider the broader impact of our work. Just as we care about model accuracy, we should care about environmental impact.

**4. Optimization Incentive**

What gets measured gets improved. Tracking energy encourages:
- More efficient algorithms
- Better hardware utilization
- Smarter model architectures

#### Arguments AGAINST (or Limitations)

**1. Measurement Overhead**

CodeCarbon itself uses resources to track emissions. For small projects, the overhead might outweigh benefits.

**2. Context Matters**

- My experiments: 0.000007 kg CO2 (negligible)
- GPT-4 training: Thousands of tons CO2 (critical to measure)

The scale matters tremendously.

**3. Misleading Comparisons**

Comparing energy across different hardware, regions, and scales can be misleading without proper context.

**4. Training vs Inference**

Most focus is on training energy, but for deployed models, inference energy over time is often MORE significant.

### My Conclusion

**For Research/Learning:** Energy tracking is valuable for awareness and building good habits.

**For Production:** Energy tracking is CRITICAL - both for cost optimization and environmental responsibility.

**Best Practice:** Track energy, but focus on it when it matters (production scale, large models, high-frequency inference).

---

## 2. CodeCarbon Methodology

**Website:** https://mlco2.github.io/codecarbon/methodology.html

### How CodeCarbon Works

CodeCarbon tracks carbon emissions using this formula:
```
CO2 (kg) = Energy (kWh) × Carbon Intensity (kg CO2/kWh)
```

#### Step 1: Measure Power Consumption

**CPU:**
- Linux: Uses RAPL (Running Average Power Limit)
- Windows: Uses TDP (Thermal Design Power) estimates
- macOS: Uses powermetrics

**GPU:**
- NVIDIA: nvidia-smi
- AMD: rocm-smi

**RAM:** Estimates based on memory usage

#### Step 2: Calculate Energy
```
Energy (kWh) = Power (W) × Time (h) / 1000
```

#### Step 3: Get Carbon Intensity

Carbon intensity varies by location:
- Coal-heavy grids: 0.9 kg CO2/kWh (e.g., Poland)
- Mixed grids: 0.4 kg CO2/kWh (e.g., USA average)
- Renewable grids: 0.02 kg CO2/kWh (e.g., Iceland)

CodeCarbon uses your location to estimate grid intensity.

### My Implementation

In this project:
- **Platform:** Databricks serverless compute
- **Tracking:** CodeCarbon wrapped around training loops
- **Results:** 0.000007 kg CO2 for best model

#### Limitations in My Setup

1. **Serverless Compute:** No direct hardware access, measurements are estimates
2. **Small Scale:** Dataset (1000 rows) is tiny - emissions are negligible
3. **No GPU:** CPU-only training is less energy-intensive but slower

### What I Learned

1. **Easy Integration:** Adding CodeCarbon took 3 lines of code
2. **Negligible Overhead:** No noticeable slowdown
3. **Awareness:** Even though emissions were tiny, it made me think about scale
4. **Production Implications:** At scale (millions of predictions), these tiny numbers multiply

---

## 3. Real-World Implications

### Scenario: Production Deployment

Imagine deploying exp4_v2_hp2 to production:
- 1 million predictions per day
- 0.000007 kg CO2 per training run
- Training: once per week
- Inference: continuous

**Annual Carbon Footprint:**
- Training: 0.000007 × 52 = 0.000364 kg CO2/year (negligible)
- Inference: Likely 100-1000x more (needs separate measurement)

**Lesson:** Training emissions are a one-time cost. Inference emissions accumulate over time and are often MORE important to optimize.

### What Would I Do Differently for Accurate Measurement

1. Use dedicated compute with hardware monitoring tools
2. Measure inference energy separately
3. Compare different model sizes (smaller model = lower inference energy)
4. Track over longer periods
5. Implement model compression (pruning, quantization)

---

## 4. Industry Context

### When Energy Tracking Matters Most

**High Priority:**
- Large language models (GPT, BERT, Claude)
- Computer vision (real-time video processing)
- Recommendation systems (millions of users)
- AutoML (training many models)

**Medium Priority:**
- Standard ML pipelines (like this project)
- Batch processing systems
- Research experiments

**Lower Priority:**
- One-off analyses
- Small datasets
- Proof-of-concept projects

### Maturity of AI Adoption

**Early Stage (Research/Learning):**
- Focus: Learning, experimentation
- Energy: Nice to track, not critical
- Tools: CodeCarbon for awareness

**Production Stage:**
- Focus: Performance, cost, sustainability
- Energy: CRITICAL to track and optimize
- Tools: Full energy monitoring, carbon accounting

---

## 5. My Experimental Results

From this assignment:

| Experiment | Carbon Emissions (kg CO2) |
|------------|--------------------------|
| exp1_v1_hp1 | 0.000009 |
| exp2_v1_hp2 | 0.000005 |
| exp3_v2_hp1 | 0.000006 |
| exp4_v2_hp2 | 0.000007 |

**Observations:**
1. All emissions are extremely low (expected for small dataset)
2. Variation exists even at this scale
3. More complex models (V2, HP2) don't necessarily use more energy
4. In production, these would scale linearly with data volume

---

## Conclusion

The ML.ENERGY Initiative and CodeCarbon are valuable tools for sustainable AI. While my project had negligible emissions, the practice of measuring is important for:

1. Building good engineering habits
2. Understanding scale implications
3. Preparing for production deployments
4. Contributing to sustainable AI practices

**Key Takeaway:** Measure energy, understand the context, optimize when it matters.

As ML practitioners, we have a responsibility to consider not just model performance, but also environmental impact. Starting with small projects like this builds the awareness and skills needed for responsible AI development at scale.

---

## References

1. ML.ENERGY Initiative: https://ml.energy/
2. CodeCarbon Methodology: https://mlco2.github.io/codecarbon/methodology.html
3. Strubell et al. (2019): "Energy and Policy Considerations for Deep Learning in NLP"
4. Patterson et al. (2021): "Carbon Emissions and Large Neural Network Training"
5. Luccioni et al. (2022): "Estimating the Carbon Footprint of BLOOM"