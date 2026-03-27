# Referral Program Dynamics Visualization
# Tuftean Graphics Style
# By Boaz Sobrado - https://howtorunreferrals.com/

# Load required libraries
library(ggplot2)
library(ggthemes)
library(gridExtra)
library(scales)

# Set seed for reproducibility
set.seed(42)

# Generate data for 90 days
days <- 1:90

# 1. Referral Reward (Step Function)
# $10 for days 1-30, $15 for days 31-60, $20 for days 61-90
reward <- ifelse(days <= 30, 10,
                 ifelse(days <= 60, 15, 20))

# 2. Users Acquired Per Day
# Base rates with variance and bump effects around changes
users_acquired <- numeric(90)

for (i in 1:90) {
  if (i <= 30) {
    # Period 1: $10 reward, ~100 users/day
    base <- 100
    # Bump effect before change (days 25-30)
    if (i >= 25) {
      bump <- (i - 24) * 15
    } else {
      bump <- 0
    }
    users_acquired[i] <- base + bump + rnorm(1, 0, 8)
    
  } else if (i <= 60) {
    # Period 2: $15 reward, settling to ~150 users/day
    # Initial bump, then decay to baseline
    days_since_change <- i - 30
    if (days_since_change <= 5) {
      # High initial bump
      base <- 150 + (6 - days_since_change) * 20
    } else if (days_since_change <= 10) {
      # Decay period
      base <- 150 + (11 - days_since_change) * 8
    } else {
      base <- 150
    }
    
    # Bump before next change (days 55-60)
    if (i >= 55) {
      bump <- (i - 54) * 12
    } else {
      bump <- 0
    }
    users_acquired[i] <- base + bump + rnorm(1, 0, 10)
    
  } else {
    # Period 3: $20 reward, settling to ~180 users/day
    days_since_change <- i - 60
    if (days_since_change <= 5) {
      # High initial bump
      base <- 180 + (6 - days_since_change) * 18
    } else if (days_since_change <= 10) {
      # Decay period
      base <- 180 + (11 - days_since_change) * 7
    } else {
      base <- 180
    }
    users_acquired[i] <- base + rnorm(1, 0, 12)
  }
}

# Ensure no negative values
users_acquired <- pmax(users_acquired, 0)

# 3. Average User Value (Decreasing with higher rewards)
avg_user_value <- numeric(90)

for (i in 1:90) {
  if (i <= 30) {
    # Period 1: $10 reward, ~$20 avg value
    base <- 20
    avg_user_value[i] <- base + rnorm(1, 0, 1.5)
  } else if (i <= 60) {
    # Period 2: $15 reward, ~$18 avg value
    base <- 18
    avg_user_value[i] <- base + rnorm(1, 0, 1.5)
  } else {
    # Period 3: $20 reward, ~$14 avg value
    base <- 14
    avg_user_value[i] <- base + rnorm(1, 0, 1.5)
  }
}

# Create data frame
df <- data.frame(
  day = days,
  reward = reward,
  users = users_acquired,
  value = avg_user_value
)

# Plot 1: Referral Reward (Step Function)
p1 <- ggplot(df, aes(x = day, y = reward)) +
  geom_step(color = "black", size = 0.8) +
  scale_y_continuous(
    breaks = c(10, 15, 20),
    labels = dollar_format(prefix = "$"),
    limits = c(8, 22)
  ) +
  scale_x_continuous(breaks = seq(0, 90, 30)) +
  labs(
    title = "Referral Reward",
    y = "Reward",
    x = NULL
  ) +
  theme_tufte()

# Plot 2: Users Acquired Per Day
p2 <- ggplot(df, aes(x = day, y = users)) +
  geom_line(color = "black", size = 0.8) +
  scale_y_continuous(
    breaks = seq(50, 250, 50),
    limits = c(50, 260)
  ) +
  scale_x_continuous(breaks = seq(0, 90, 30)) +
  labs(
    title = "Users Acquired Per Day",
    y = "Users",
    x = NULL
  ) +
  theme_tufte()

# Plot 3: Average User Value
p3 <- ggplot(df, aes(x = day, y = value)) +
  geom_line(color = "black", size = 0.8) +
  scale_y_continuous(
    breaks = seq(10, 25, 5),
    labels = dollar_format(prefix = "$"),
    limits = c(10, 25)
  ) +
  scale_x_continuous(breaks = seq(0, 90, 30)) +
  labs(
    title = "Average User Value",
    y = "Value",
    x = "Day"
  ) +
  theme_tufte()

# Combine plots
png("referral_dynamics_2.png", 
    width = 8, height = 9, units = "in", res = 300)

grid.arrange(
  p1, p2, p3,
  ncol = 1,
  top = grid::textGrob(
    "The Trade-off Between Referral Rewards, Volume, and Quality",
    gp = grid::gpar(fontsize = 14, fontface = "bold"),
    just = "left",
    x = 0.05
  ),
  bottom = grid::textGrob(
    "https://howtorunreferrals.com/",
    gp = grid::gpar(fontsize = 9, col = "grey40"),
    just = "right",
    x = 0.95
  )
)

dev.off()

cat("Chart saved to referral_dynamics.png\n")

library(tidyverse)
library(ggthemes)

library(tidyverse)
library(ggthemes)

# Set parameters for synthetic data generation
set.seed(42)  # For reproducibility
exponent <- 3.25  # Power-law exponent tuned to approximate the chart's decay
max_k <- 1000  # Large enough to capture potential long tail
k_vec <- 1:max_k

# Compute unnormalized probabilities
unnorm_probs <- k_vec ^ (-exponent)

# Sum for normalization
sum_probs <- sum(unnorm_probs)

# Normalized probabilities
probs <- unnorm_probs / sum_probs

# Calculate total number of referrers to have expected ~9500 at k=1 for total_ftd (since total_ftd(1) = num(1) * 1)
n_referrers <- round(9500 * sum_probs)

# Sample FTD counts per referrer
ftd_samples <- sample(k_vec, size = n_referrers, replace = TRUE, prob = probs)

# Create data frame with counts
data <- tibble(ftd_per = ftd_samples) %>%
  count(ftd_per, name = "num_referrers") %>%
  mutate(total_ftd = ftd_per * num_referrers)

# Bin 50+
data_low <- data %>%
  filter(ftd_per < 50) %>%
  mutate(ftd_per_char = as.character(ftd_per))

data_high <- data %>%
  filter(ftd_per >= 50) %>%
  summarise(num_referrers = sum(num_referrers),
            total_ftd = sum(total_ftd)) %>%
  mutate(ftd_per_char = "50+")

# Combine
data_all <- bind_rows(data_low, data_high) %>%
  filter(num_referrers > 0) %>%
  mutate(ftd_per_char = factor(ftd_per_char, levels = c(as.character(1:49), "50+")))

# Plot the chart
ggplot(data_all, aes(x = ftd_per_char, y = total_ftd)) +
  geom_col(fill = "gray20") +
  scale_y_continuous(breaks = seq(0, 10000, by = 2500),
                     limits = c(0, 10000),
                     expand = c(0, 0)) +
  labs(x = "Referrals per Referrer",
       y = "Referrals",
       caption = "Synthetic data reproduction. Visit howtorunreferrals.com for more.") +
  theme_tufte() +
  theme(axis.text.x = element_text(angle = 45, vjust = 0.5, hjust = 1),
        panel.grid.major.y = element_line(color = "lightgray", size = 0.5),
        panel.grid.major.x = element_blank(),
        panel.grid.minor = element_blank())


## exponent analysis

library(tidyverse)
library(ggthemes)
library(gridExtra)

set.seed(42)
exponent <- 3.25
max_k <- 1000
k_vec <- 1:max_k

unnorm_probs <- k_vec ^ (-exponent)
probs <- unnorm_probs / sum(unnorm_probs)
n_referrers <- round(9500 * sum(unnorm_probs))

ftd_samples <- sample(k_vec, size = n_referrers, replace = TRUE, prob = probs)

data <- tibble(ftd_per = ftd_samples) %>%
  count(ftd_per, name = "num_referrers") %>%
  mutate(total_ftd = ftd_per * num_referrers)

# Payout parameters
payout_per_3 <- 115  # Wise pays $115 per 3 referrals
payout_per_ref <- payout_per_3 / 3  # ~$38.33 equivalent per referral

# Calculate payouts under each model
data <- data %>%
  mutate(
    # Model A: Pay for every referral ($38.33 each)
    payout_all = num_referrers * ftd_per * payout_per_ref,
    
    # Model B: Pay only if 3+ referrals, but then pay for all
    payout_threshold = num_referrers * ifelse(ftd_per >= 3, ftd_per * payout_per_ref, 0),
    
    # Model C: Wise model - pay $115 per complete batch of 3
    batches_of_3 = ftd_per %/% 3,
    payout_wise = num_referrers * batches_of_3 * payout_per_3,
    
    # Breakage analysis
    unpaid_referrals_wise = num_referrers * (ftd_per %% 3) + 
      num_referrers * ifelse(ftd_per < 3, ftd_per, 0) -
      num_referrers * ifelse(ftd_per < 3, ftd_per, 0),
    remainder_refs = ftd_per %% 3,
    paid_refs_wise = batches_of_3 * 3
  )

# Summary stats
total_refs <- sum(data$total_ftd)
cost_all <- sum(data$payout_all)
cost_threshold <- sum(data$payout_threshold)
cost_wise <- sum(data$payout_wise)

cat("=== Payout Model Comparison ===\n\n")
cat("Total referrals:", format(total_refs, big.mark = ","), "\n\n")

cat("Model A (pay all):        $", format(round(cost_all), big.mark = ","), "\n", sep = "")
cat("Model B (3+ threshold):   $", format(round(cost_threshold), big.mark = ","), 
    sprintf("  (%.1f%% savings)\n", 100 * (cost_all - cost_threshold) / cost_all), sep = "")
cat("Model C (Wise batches):   $", format(round(cost_wise), big.mark = ","),
    sprintf("  (%.1f%% savings)\n", 100 * (cost_all - cost_wise) / cost_all), sep = "")

# Build visualization data
# Show effective payout per referral under each model
viz_data <- data %>%
  filter(ftd_per <= 15) %>%
  mutate(
    eff_per_ref_all = payout_per_ref,
    eff_per_ref_threshold = ifelse(ftd_per >= 3, payout_per_ref, 0),
    eff_per_ref_wise = (batches_of_3 * payout_per_3) / ftd_per
  ) %>%
  select(ftd_per, eff_per_ref_all, eff_per_ref_threshold, eff_per_ref_wise) %>%
  pivot_longer(cols = starts_with("eff"), names_to = "model", values_to = "eff_payout") %>%
  mutate(model = case_when(
    model == "eff_per_ref_all" ~ "Pay all",
    model == "eff_per_ref_threshold" ~ "3+ threshold",
    model == "eff_per_ref_wise" ~ "Wise (batches of 3)"
  ))

# Plot 1: Effective payout per referral by model
p1 <- ggplot(viz_data, aes(x = ftd_per, y = eff_payout, color = model)) +
  geom_line(size = 1) +
  geom_point(size = 2) +
  scale_x_continuous(breaks = 1:15) +
  scale_y_continuous(labels = scales::dollar_format(), limits = c(0, 45)) +
  scale_color_manual(values = c("Pay all" = "gray60", 
                                "3+ threshold" = "steelblue", 
                                "Wise (batches of 3)" = "forestgreen")) +
  labs(
    title = "Effective Payout Per Referral",
    subtitle = "Wise's batch model creates sawtooth breakage",
    x = "Referrals per Referrer",
    y = "Effective $ per Referral",
    color = NULL
  ) +
  theme_tufte() +
  theme(legend.position = "bottom")

# Plot 2: Distribution of referrers with cumulative cost overlay
cost_by_bucket <- data %>%
  filter(ftd_per <= 20) %>%
  select(ftd_per, num_referrers, payout_all, payout_wise) %>%
  mutate(
    savings = payout_all - payout_wise,
    ftd_per_char = factor(ftd_per)
  )

p2 <- ggplot(cost_by_bucket, aes(x = ftd_per_char)) +
  geom_col(aes(y = payout_all / 1000), fill = "gray70", width = 0.7) +
  geom_col(aes(y = payout_wise / 1000), fill = "forestgreen", width = 0.7) +
  scale_y_continuous(labels = function(x) paste0("$", x, "k")) +
  labs(
    title = "Cost by Referral Bucket",
    subtitle = "Gray = pay-all model, Green = Wise batch model",
    x = "Referrals per Referrer",
    y = "Total Payout"
  ) +
  theme_tufte()

# Plot 3: Where does the savings come from?
breakage_detail <- data %>%
  mutate(
    type = case_when(
      ftd_per < 3 ~ "Never hit 3",
      ftd_per %% 3 == 0 ~ "Exact multiple",
      TRUE ~ "Remainder lost"
    )
  ) %>%
  group_by(type) %>%
  summarise(
    referrers = sum(num_referrers),
    referrals = sum(total_ftd),
    savings = sum(payout_all - payout_wise),
    .groups = "drop"
  ) %>%
  mutate(type = factor(type, levels = c("Never hit 3", "Remainder lost", "Exact multiple")))

p3 <- ggplot(breakage_detail, aes(x = type, y = savings / 1000)) +
  geom_col(fill = "coral", width = 0.6) +
  geom_text(aes(label = sprintf("$%.0fk", savings/1000)), vjust = -0.5, size = 3.5) +
  scale_y_continuous(labels = function(x) paste0("$", x, "k"), limits = c(0, max(breakage_detail$savings/1000) * 1.15)) +
  labs(
    title = "Sources of Breakage Savings",
    x = NULL,
    y = "Savings vs Pay-All"
  ) +
  theme_tufte()

# Combine
png("wise_breakage_analysis.png", width = 10, height = 10, units = "in", res = 300)
grid.arrange(
  p1, p2, p3,
  ncol = 1,
  top = grid::textGrob(
    "Wise Referral Program: Breakage Analysis",
    gp = grid::gpar(fontsize = 14, fontface = "bold"),
    just = "left", x = 0.05
  ),
  bottom = grid::textGrob(
    "howtorunreferrals.com",
    gp = grid::gpar(fontsize = 9, col = "grey40"),
    just = "right", x = 0.95
  )
)
dev.off()

cat("\nChart saved to wise_breakage_analysis.png\n")


library(tidyverse)
library(ggthemes)
library(gridExtra)

set.seed(42)
exponent <- 3.25
max_k <- 1000
k_vec <- 1:max_k

unnorm_probs <- k_vec ^ (-exponent)
probs <- unnorm_probs / sum(unnorm_probs)
n_referrers <- round(9500 * sum(unnorm_probs))

ftd_samples <- sample(k_vec, size = n_referrers, replace = TRUE, prob = probs)

data <- tibble(ftd_per = ftd_samples) %>%
  count(ftd_per, name = "num_referrers") %>%
  mutate(total_ftd = ftd_per * num_referrers)

# Payout parameters
payout_per_3 <- 115
payout_per_ref <- payout_per_3 / 3  # ~$38.33

# Calculate payouts under each model
data <- data %>%
  mutate(
    payout_all = num_referrers * ftd_per * payout_per_ref,
    batches_of_3 = ftd_per %/% 3,
    payout_wise = num_referrers * batches_of_3 * payout_per_3
  )

# Summary stats
total_refs <- sum(data$total_ftd)
cost_all <- sum(data$payout_all)
cost_wise <- sum(data$payout_wise)

cat("=== Payout Model Comparison ===\n\n")
cat("Total referrals:", format(total_refs, big.mark = ","), "\n\n")
cat("Model A (pay all):      $", format(round(cost_all), big.mark = ","), "\n", sep = "")
cat("Model B (Wise batches): $", format(round(cost_wise), big.mark = ","),
    sprintf("  (%.1f%% savings)\n", 100 * (cost_all - cost_wise) / cost_all), sep = "")

# Chart 1: Sawtooth - effective payout per referral
sawtooth_data <- tibble(ftd_per = 1:15) %>%
  mutate(
    eff_pay_all = payout_per_ref,
    eff_wise = ((ftd_per %/% 3) * payout_per_3) / ftd_per
  ) %>%
  pivot_longer(cols = c(eff_pay_all, eff_wise), names_to = "model", values_to = "eff_payout") %>%
  mutate(model = ifelse(model == "eff_pay_all", "Pay all", "Wise (batches of 3)"))

p1 <- ggplot(sawtooth_data, aes(x = ftd_per, y = eff_payout, color = model)) +
  geom_line(size = 1) +
  geom_point(size = 2) +
  scale_x_continuous(breaks = 1:15) +
  scale_y_continuous(labels = scales::dollar_format(), limits = c(0, 45)) +
  scale_color_manual(values = c("Pay all" = "gray50", "Wise (batches of 3)" = "#37B24D")) +
  labs(
    title = "Effective Payout Per Referral",
    x = "Referrals per Referrer",
    y = "$ per Referral",
    color = NULL
  ) +
  theme_tufte() +
  theme(legend.position = c(0.8, 0.25))

# Chart 2: Cumulative referrals and cumulative cost
cumulative_data <- data %>%
  arrange(ftd_per) %>%
  mutate(
    cum_referrals = cumsum(total_ftd),
    cum_cost_all = cumsum(payout_all),
    cum_cost_wise = cumsum(payout_wise)
  )

# Limit to where 95%+ of referrals are captured
cutoff <- cumulative_data %>% 
  
  filter(cum_referrals >= 0.99 * total_refs) %>% 
  slice(1) %>% 
  pull(ftd_per)

cumulative_data <- cumulative_data %>% filter(ftd_per <= cutoff)

# Scale factor to plot referrals and cost on same axis
max_refs <- max(cumulative_data$cum_referrals)
max_cost <- max(cumulative_data$cum_cost_all)
scale_factor <- max_refs / max_cost

p2 <- ggplot(cumulative_data, aes(x = ftd_per)) +
  # Cumulative referrals (gray area)
  geom_area(aes(y = cum_referrals), fill = "gray80", alpha = 0.5) +
  # Cumulative costs (lines)
  geom_line(aes(y = cum_cost_all * scale_factor, color = "Pay all"), size = 1) +
  geom_line(aes(y = cum_cost_wise * scale_factor, color = "Wise (batches of 3)"), size = 1) +
  scale_y_continuous(
    name = "Cumulative Referrals",
    labels = scales::comma,
    sec.axis = sec_axis(~ . / scale_factor / 1000, name = "Cumulative Cost ($k)", 
                        labels = function(x) paste0("$", round(x), "k"))
  ) +
  scale_x_continuous(breaks = seq(0, cutoff, by = 2)) +
  scale_color_manual(values = c("Pay all" = "gray40", "Wise (batches of 3)" = "#37B24D")) +
  labs(
    title = "Cumulative Referrals and Payout Cost",
    subtitle = sprintf("Shaded area = referrals. Gap between lines = %.0f%% savings", 
                       100 * (cost_all - cost_wise) / cost_all),
    x = "Referrals per Referrer",
    color = NULL
  ) +
  theme_tufte() +
  theme(
    legend.position = c(0.8, 0.3),
    axis.title.y.right = element_text(angle = 90)
  )

# Combine
png("wise_breakage_two_charts.png", width = 8, height = 9, units = "in", res = 300)
grid.arrange(
  p1, p2,
  ncol = 1,
  heights = c(1, 1.2),
  top = grid::textGrob(
    "Wise Referral Program: Batch Payout Breakage",
    gp = grid::gpar(fontsize = 14, fontface = "bold"),
    just = "left", x = 0.05
  ),
  bottom = grid::textGrob(
    "howtorunreferrals.com",
    gp = grid::gpar(fontsize = 9, col = "grey40"),
    just = "right", x = 0.95
  )
)
dev.off()

cat("\nChart saved to wise_breakage_two_charts.png\n")

library(tidyverse)
library(ggthemes)
library(gridExtra)

set.seed(42)
exponent <- 3.25
max_k <- 1000
k_vec <- 1:max_k

unnorm_probs <- k_vec ^ (-exponent)
probs <- unnorm_probs / sum(unnorm_probs)
n_referrers <- round(9500 * sum(unnorm_probs))

ftd_samples <- sample(k_vec, size = n_referrers, replace = TRUE, prob = probs)

data <- tibble(ftd_per = ftd_samples) %>%
  count(ftd_per, name = "num_referrers") %>%
  mutate(total_ftd = ftd_per * num_referrers)

# Payout parameters
payout_per_3 <- 115
payout_per_ref <- payout_per_3 / 3

# Calculate paid vs unpaid referrals under Wise model
data <- data %>%
  mutate(
    batches_of_3 = ftd_per %/% 3,
    remainder = ftd_per %% 3,
    # Referrals that count toward a payout
    paid_refs = batches_of_3 * 3 * num_referrers,
    # Referrals that don't (either never hit 3, or remainder)
    unpaid_refs = total_ftd - paid_refs
  )

# Summary
total_refs <- sum(data$total_ftd)
total_paid <- sum(data$paid_refs)
total_unpaid <- sum(data$unpaid_refs)

cat("=== Breakage Summary ===\n")
cat("Total referrals:", format(total_refs, big.mark = ","), "\n")
cat("Paid referrals:", format(total_paid, big.mark = ","), 
    sprintf(" (%.1f%%)\n", 100 * total_paid / total_refs))
cat("Unpaid referrals:", format(total_unpaid, big.mark = ","), 
    sprintf(" (%.1f%%)\n", 100 * total_unpaid / total_refs))

# Chart 1: Sawtooth (same as before)
sawtooth_data <- tibble(ftd_per = 1:15) %>%
  mutate(
    eff_pay_all = payout_per_ref,
    eff_wise = ((ftd_per %/% 3) * payout_per_3) / ftd_per
  ) %>%
  pivot_longer(cols = c(eff_pay_all, eff_wise), names_to = "model", values_to = "eff_payout") %>%
  mutate(model = ifelse(model == "eff_pay_all", "Pay all", "Wise (batches of 3)"))

p1 <- ggplot(sawtooth_data, aes(x = ftd_per, y = eff_payout, color = model)) +
  geom_line(size = 1) +
  geom_point(size = 2) +
  scale_x_continuous(breaks = 1:15) +
  scale_y_continuous(labels = scales::dollar_format(), limits = c(0, 45)) +
  scale_color_manual(values = c("Pay all" = "gray50", "Wise (batches of 3)" = "#37B24D")) +
  labs(
    title = "Effective Payout Per Referral",
    x = "Referrals per Referrer",
    y = "$ per Referral",
    color = NULL
  ) +
  theme_tufte() +
  theme(legend.position = c(0.8, 0.25))

# Chart 2: Stacked bar - paid vs unpaid referrals
stacked_data <- data %>%
  filter(ftd_per <= 15) %>%
  select(ftd_per, paid_refs, unpaid_refs) %>%
  pivot_longer(cols = c(paid_refs, unpaid_refs), names_to = "status", values_to = "referrals") %>%
  mutate(status = ifelse(status == "paid_refs", "Paid", "Unpaid (breakage)"))

p2 <- ggplot(stacked_data, aes(x = factor(ftd_per), y = referrals, fill = status)) +
  geom_col(width = 0.75) +
  scale_fill_manual(values = c("Paid" = "#37B24D", "Unpaid (breakage)" = "#E03131")) +
  scale_y_continuous(labels = scales::comma) +
  labs(
    title = "Referrals: Paid vs Unpaid Under Wise Model",
    subtitle = sprintf("%.0f%% of all referrals go unpaid", 100 * total_unpaid / total_refs),
    x = "Referrals per Referrer",
    y = "Total Referrals",
    fill = NULL
  ) +
  theme_tufte() +
  theme(legend.position = c(0.85, 0.85))

# Combine
png("wise_breakage_stacked.png", width = 8, height = 9, units = "in", res = 300)
grid.arrange(
  p1, p2,
  ncol = 1,
  heights = c(1, 1.2),
  top = grid::textGrob(
    "Wise Referral Program: Batch Payout Breakage",
    gp = grid::gpar(fontsize = 14, fontface = "bold"),
    just = "left", x = 0.05
  ),
  bottom = grid::textGrob(
    "howtorunreferrals.com",
    gp = grid::gpar(fontsize = 9, col = "grey40"),
    just = "right", x = 0.95
  )
)
dev.off()

cat("\nChart saved to wise_breakage_stacked.png\n")


library(ggplot2)
library(ggthemes)
library(gridExtra)

# Tufte theme setup
theme_tufte_custom <- function() {
  theme_tufte(base_family = "serif") +
    theme(
      plot.background = element_rect(fill = "#fffff8", color = NA),
      panel.background = element_rect(fill = "#fffff8", color = NA),
      text = element_text(color = "#111111"),
      axis.text = element_text(color = "#111111"),
      axis.title = element_text(size = 10),
      plot.title = element_text(size = 11, face = "plain"),
      axis.ticks.length = unit(0.2, "cm")
    )
}

ggplot(stacked_data, aes(x = factor(ftd_per), y = referrals, fill = status)) +
  geom_col(width = 0.75) +
  scale_fill_manual(values = c("Paid" = "#37B24D", "Unpaid (breakage)" = "#E03131")) +
  scale_y_continuous(labels = scales::comma) +
  labs(
    title = "Referrals: Paid vs Unpaid Under Wise Model",
    subtitle = sprintf("%.0f%% of all referrals go unpaid", 100 * total_unpaid / total_refs),
    x = "Referrals per Referrer",
    y = "Total Referrals",
    fill = NULL
  ) +
  theme_tufte_custom() +
  theme(legend.position = c(0.85, 0.85))



# Create synthetic data matching the pattern
age_groups <- c("18-20", "24-26", "30-32", "36-38", "42-44", 
                "48-50", "54-56", "60-62", "64-68", "72-74", "78-80")

# Synthetic data approximating the chart
df <- data.frame(
  age_group = factor(age_groups, levels = age_groups),
  all_users = c(0.22, 0.15, 0.10, 0.06, 0.04, 0.02, 0.01, 0.005, 0.003, 0.002, 0.001),
  activated_users = c(0.13, 0.12, 0.14, 0.105, 0.08, 0.04, 0.02, 0.01, 0.008, 0.005, 0.003),
  referrers = c(0.20, 0.16, 0.11, 0.075, 0.04, 0.025, 0.015, 0.008, 0.005, 0.003, 0.002)
)

# Reshape for ggplot
df_long <- df %>%
  pivot_longer(
    cols = c(all_users, activated_users, referrers),
    names_to = "metric",
    values_to = "percentage"
  ) %>%
  mutate(
    metric = factor(
      metric,
      levels = c("all_users", "activated_users", "referrers"),
      labels = c("All Users", "Activated Users", "Referrers")
    )
  )

# Create the plot
ggplot(df_long, aes(x = age_group, y = percentage, 
                    color = metric, group = metric)) +
  geom_line(linewidth = 1) +
  scale_y_continuous(
    labels = scales::percent_format(accuracy = 1),
    expand = expansion(mult = c(0, 0.05))
  ) +
  scale_color_manual(
    values = c(
      "All Referred Users" = "#FF6B6B",
      "Activated Referred Users" = "#51CF66", 
      "Referrers" = "#4DABF7"
    )
  ) +
  theme_tufte_custom() +
  theme(
    axis.text.x = element_text(angle = 0, hjust = 0.5),
    panel.grid.major.y = element_line(color = "#e0e0e0", linewidth = 0.3),
    panel.grid.major.x = element_blank()
  ) +
  labs(
    title = "New Users by Referrer Age at Account Creation",
    x = "Age At Account Creation",
    y = "Percentage"
  )

# Tufte theme
theme_tufte_custom <- function() {
  theme_tufte(base_family = "serif") +
    theme(
      plot.background = element_rect(fill = "#fffff8", color = NA),
      panel.background = element_rect(fill = "#fffff8", color = NA),
      text = element_text(color = "#111111"),
      axis.text = element_text(color = "#111111", size = 9),
      axis.title = element_text(size = 10),
      plot.title = element_text(size = 12, face = "plain"),
      axis.text.x = element_text(size = 9)
    )
}

# Synthetic data matching the pattern
df <- data.frame(
  quartile = factor(paste("Quartile", 1:4), 
                    levels = paste("Quartile", 1:4)),
  referee_revenue = c(3300000, 2800000, 4200000, 17500000)
)

# Create the plot
ggplot(df, aes(x = quartile, y = referee_revenue)) +
  geom_col(fill = "#4a4a4a", color = "#111111", linewidth = 0.3) +
  scale_y_continuous(
    labels = label_number(scale = 1e-6, suffix = "M"),
    expand = expansion(mult = c(0, 0.05))
  ) +
  geom_rangeframe(sides = "l") +
  theme_tufte_custom() +
  theme(
    panel.grid.major.y = element_line(color = "#e0e0e0", linewidth = 0.3),
    panel.grid.major.x = element_blank(),
    axis.ticks.x = element_blank()
  ) +
  labs(
    title = "Referee Revenue by Referrer Revenue Quartile",
    x = "Referrer Revenue at Day 7",
    y = "Referee Revenue Total"
  )


