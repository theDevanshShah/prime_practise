import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Parameters
years = 27
months = years * 12
start_sip = 5000
annual_return = 0.13  # 13% CAGR (Conservative for Flexi Cap)
monthly_rate = (1 + annual_return)**(1/12) - 1

# Arrays to store data
month_indices = np.arange(1, months + 1)
ages = 23 + month_indices / 12

# Scenario A: User's Ask (10% Step-up every 6 Months)
sip_aggressive = []
portfolio_aggressive = []
current_corpus_agg = 0
current_sip_agg = start_sip

# Scenario B: Realistic (10% Step-up Annually)
sip_realistic = []
portfolio_realistic = []
current_corpus_real = 0
current_sip_real = start_sip

for m in range(1, months + 1):
    # --- Aggressive Calculation ---
    current_corpus_agg = (current_corpus_agg + current_sip_agg) * (1 + monthly_rate)
    portfolio_aggressive.append(current_corpus_agg)
    sip_aggressive.append(current_sip_agg)
    
    # Increase SIP every 6 months
    if m % 6 == 0:
        current_sip_agg *= 1.10

    # --- Realistic Calculation ---
    current_corpus_real = (current_corpus_real + current_sip_real) * (1 + monthly_rate)
    portfolio_realistic.append(current_corpus_real)
    sip_realistic.append(current_sip_real)
    
    # Increase SIP every 12 months
    if m % 12 == 0:
        current_sip_real *= 1.10

# Convert to Crores for plotting
portfolio_aggressive_cr = np.array(portfolio_aggressive) / 10000000
portfolio_realistic_cr = np.array(portfolio_realistic) / 10000000

# --- PLOTTING ---
plt.figure(figsize=(12, 7), dpi=120)
plt.style.use('dark_background')

# Plot Lines
plt.plot(ages, portfolio_aggressive_cr, color='#00e676', linewidth=2.5, label="Your Plan (10% hike / 6mo)")
plt.plot(ages, portfolio_realistic_cr, color='#2979ff', linewidth=2.5, linestyle='--', label="Standard Plan (10% hike / 1yr)")

# Fill area under User's Plan
plt.fill_between(ages, portfolio_aggressive_cr, color='#00e676', alpha=0.1)

# Highlight Final Values
final_agg = portfolio_aggressive_cr[-1]
final_real = portfolio_realistic_cr[-1]

plt.scatter([50], [final_agg], color='#00e676', s=100, zorder=5)
plt.text(46, final_agg, f'₹ {final_agg:.1f} Cr', color='#00e676', fontsize=14, fontweight='bold', ha='right')

plt.scatter([50], [final_real], color='#2979ff', s=100, zorder=5)
plt.text(50.5, final_real, f'₹ {final_real:.1f} Cr', color='#2979ff', fontsize=12, fontweight='bold')

# Annotations for SIP Reality Check
mid_sip_agg = sip_aggressive[int(months/2)]
end_sip_agg = sip_aggressive[-1]
plt.annotate(f'Required Monthly SIP:\n₹ {end_sip_agg/100000:.1f} Lakhs/mo', 
             xy=(50, final_agg), xytext=(42, final_agg*0.6),
             arrowprops=dict(arrowstyle="->", color='white', lw=1),
             color='white', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="#263238", ec="white"))

# Titles and Labels
plt.title('Wealth Projection: Age 23 to 50', fontsize=18, fontweight='bold', pad=20, color='white')
plt.xlabel('Age', fontsize=12, color='#cfd8dc')
plt.ylabel('Portfolio Value (₹ Crores)', fontsize=12, color='#cfd8dc')
plt.grid(color='#37474f', linestyle=':', linewidth=0.5)
plt.legend(loc='upper left', fontsize=11)

# Formatting Axes
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('₹%.0f Cr'))

plt.tight_layout()
plt.savefig('portfolio_projection.png')