# How To Run Referrals
subtitle: A Guide to Building Successful Referral Programs By [!Boaz Sobrado](www.boazsobrado.com)

## Table of Contents
1. [Understanding Referrals](#understanding-referrals)
    - [Should You Run A Refer A Friend Campaign?](#should-you-run-a-refer-a-friend-campaign)
    - [Case Studies](#case-study-refer-a-friend-schemes-in-the-wild)
    - [Definitions](#definitions-what-is-a-refer-a-friend-scheme)
    - [Who Refers, Who Gets Referred, Why And How?](#who-refers-who-gets-referred-why-and-how)
2. [Design Principles of Referrals](#design-principles-of-referrals-schemes)
    - [Quality vs Quantity Tradeoff](#the-quality-versus-quantity-tradeoff)
    - [Rewards](#rewards)
    - [Qualification Criteria](#on-the-qualification-criteria)
3. [Operating A Referrals Scheme](#operations)


## Introduction

<div class="epigraph">
  <blockquote>
    <p>We gave new customers $10 for joining, and we gave them $10 more every time they referred a friend.</p>
    <footer>Peter Thiel, <cite>Zero to One</cite> (2014)</footer>
  </blockquote>
</div>

<span class="newthought">Refer-A-Friend</span>, whereby existing users are encouraged to refer new customers to the product, is one of the most important and efficient user acquisition channels for digital consumer companies.

Fintech companies such as Revolut, Paypal or Wise acquire over half of their via incentivised or organic "word of mouth" campaigns [^sn: Just over half of users coming from "word of mouth" or "referrals" seems to be the industry standard for FinTech companies.]. Referrals campaigns are not just effective for fintech companies. Nikita Bier, currently the CPO of X (formerly Twitter) has made a career out of organically growing "viral" referral based apps such as YikYak and Gas. Evidently, RAF schemes have the potential to acquire a large volume users.

The best known referral campaign I've been involved in was Zilch's in 2021. Zilch is a UK based consumer-finance app that reached the top of the App store in late 2021, off the back of a well-executed viral referral campaign.

[!trends:keyword:Zilch,geo:GB,time:2021-01-01 2021-12-31]

The Google trends chart below shows how fast Zilch grew. When I joined Zilch in summer of 2021, we had less than 1 million registered customers. In September, we hit 1 million registered customers. By March 2022 we had exceeded 2 million registered customers. In December 2021 alone, we acquired 425k new registrations, primarily off the back of our Refer-A-Friend programme[^mn: This is all publically available information based on [Zilch Press Releases](https://www.zilch.com/news/zilch-continues-unprecedented-fintech-disruption-reaching-2-million-users-in-record-time/)].

And yet, we were not doing anything radically new. We were running a playbook analogous to that of PayPal in 1999. PayPal's meteoric rise via the Refer-A-Friend programme is not exactly a secret.[^mn: See Elon Musk [on the topic](https://www.youtube.com/watch?v=vDwzmJpI4io&t=680s
) on Youtube] Peter Thiel wrote about it in his bestselling book Zero To One which was published in 2014. This is curious given how much technology has changed since 1999. Nobody serious would run online advertising campaigns like they were run 25 years ago. So in a world with dwindling attention spans and consumers who are saturated by advertising, why are old Refer-A-Friend tactics still successful?

As always, the devil is in the details. But fundamentally, the human desire to share and be social is constant. The goal with this essay is to show the underlying mechanics, tactics and methods with which effective Refer-A-Friend campaigns can be run. I have run Refer-A-Friend campaigns in various B2C fintech companies (including Zilch) and have consulted on the topic. Throughout the essay I show various charts with data. Unless otherwise mentioned, this is synthetic data.

## Understanding Referrals

### Should You Even Run A Refer A Friend Campaign?

<div class="epigraph">
  <blockquote>
    <p>The degree to which you're successful approximates the degree to which you build a product that is so good, people spontaneously tell their friends about it.</p>
    <footer>Sam Altman</footer>
  </blockquote>
</div>


Mobile gaming companies (think Candy Crush or Monopoly Go) are muscular performance marketing ad spenders. In 2025 they are projected [^sn: [InsightTracker](https://blog.insightrackr.com/en/docs/Global-Mobile-Gaming-UA-Trends-Strategy-Report)] to generate over $100bn in revenue, with about 25% of revenue going towards [^sn:[2024 Bain Mobile Gaming Report](https://s3.amazonaws.com/media.mediapost.com/uploads/BAIN-report_gaming-report-2024.pdf)] advertising. They are clearly experts at digital marketing, otherwise they wouldn't survive. But they don't spend nearly as much on referrals as Fintech companies do. Why?

Not all products are suitable for high volume, paid Refer-A-Friend schemes. Just because PayPal, Revolut and Wise acquired a large fraction of their users through a RAF schemes doesn't mean your company will. The following companies are likely to struggle with a Refer-A-Friend scheme: a company with 0 users, a socially sensitive product (e.g. erectile dysfunction pills or credit cards for people with bad credit) or a niche product such that potential customers are unlikely to know each other (e.g. clients of a funeral home) is unlikely to be successful at a Refer-A-Friend scheme. 

The characteristics of your product (or service) impact the likelihood of success in running a successful RAF scheme:

1. **Network Effects**. Revolut, PayPal and Wise grew fast on RAF schemes because their business ("peer to peer payments") is inherently a social product. Most transactions have two parties, the person sending the money and the person receiving it. Users of payments businesses generally have a strong incentive to refer their friends onto the platform, as the platform then becomes more valuable to them the more of their counterparties use them.
2. **Customer Base Size**. If you are just starting out with user acquisition RAF is unlikely to be helpful. RAF requires a large number of customers to start with, because only a subset of them will go on to refer new users.
3. **Product & Customer Base Sociality**. Is your product something people would talk about? People are much more likely to share information about good places to eat than they are treatment options for genital warts. Customer demographics matter too. For instance, young people tend to refer more.
4. **Product Trust Requirements**. Do your customers need to trust your product? People tend to trust things their friends trust, and far more trust is required for a financial app than a video game.
5. **User Lifetime Values (LTVs)**. Are your customers in the RAF LTV sweet spot? If your business has users who are on average worth very little, you probably have little room to offer financial incentives to refer friends. I'll happily refer a friend to a product if I'll get 100 USD for it, but I'd be insulted if someone offered me 10 cents. Conversely, if your customers are worth a lot, you might want to have professional sales and accounts managers involved in the process, which negates the purpose of a productised RAF experience.

### Case Study: Refer-A-Friend Schemes In The Wild

Lets look at a few examples of modern, successful RAF campaigns for Revolut, Robinhood, Wise and Monzo.

**Revolut**

<figure>
  <img src="https://web-tips.co.uk/media/2019/09/revolut-referral-code-voucher-discount-10-498x1024.jpg" alt="First image" style="width: 48%; display: inline-block; margin-right: 2%;">
  <img src="https://web-tips.co.uk/media/2019/09/revolut-referral-code-voucher-discount-10-498x1024.jpg" alt="Second image" style="width: 48%; display: inline-block;">
  <figcaption>Caption for both images</figcaption>
</figure>

In its 2024 shareholder report, fintech giant Revolut claims that 65% of retail customers are acquired via word of mouth or referrals. This is at a significant scale too, they grew 38% year on year to 52.5m customers, see [Revolut 2024 Annual Report](https://www.revolut.com/news/record_growth_and_diverse_product_offering_drive_revolut_to_1_4bn_profit_in_2024/)

Like most companies, Revolut has experimented extensively on their referral programme, but the iteration above shows a limited time offer whereby both the referrer and the person referred gets $10.

There's two things to point out:

- the equal split of the reward of the referrer and the referee [^mn: This has become the most common best practice but is by no means [set in stone](#splitting-rewards)]
- the limited time deal which adds some urgency to the user

**Robinhood**

<figure style="max-width: 27.5%;">  <!-- 50% of 55% -->
   <img src="https://babysteps2onlinesuccess.com/wp-content/uploads/2020/05/Robinhood-Share-min-scaled.jpg" alt="An example of Robinhood's Variable Reward scheme">
 </figure>

In Robinhood's [S1 filing](https://www.sec.gov/Archives/edgar/data/1783879/000162828021013318/robinhoods-1.htm) in 2021, Robinhood boasts that:

> "a majority of our new customers join our platform organically or through the Robinhood Referral Program...These channels were responsible for over 80% of the new Funded Accounts".

Robinhood's key differentiation is the variable reward offer, whereby users can receive "up to $200". But if you read the terms and conditions of the referral campaign, you'll find that:

> The cash value you receive could be anywhere between $5 and $200. Keep in mind, approximately 99% of customers will get stock worth $5. You can use this reward to claim a fractional share of a stock.

Variable rewards have been very successful for Robinhood, but the exact same scheme may not be appropriate for all other products.

**Wise**

<div class="epigraph">
  <blockquote>
    <p>The stat I'm most proud of, and the hardest thing to make happen out of all of that was we acquired 70% of the users that found out about Wise last month through word of mouth.</p>
    <footer>Nilan Peris - Wise CPO</footer>
  </blockquote>
</div>

Similarly, Wise (formerly known as Transferwise) is on record explaining that roughly 70% of their customers come from referrals [^sn: at least according to this [job ad](https://wise.jobs/job/senior-growth-manager-word-of-mouth-in-london-jid-993) on their website].

<figure style="max-width: 27.5%;">  <!-- 50% of 55% -->
   <img src="https://www.cloudsponge.com/wp-content/uploads/2021/07/2021-07-28_13-24-58.jpg" alt="Description">
 </figure>

The example above is similar to Robinhood in that a large number gets shown to the user for a referral, whereas the "true" number is much lower.

Key to understanding Wise's referral programme is that their customer lifetime values are significantly lower than Robinhood's or Revolut's, meaning that they cannot afford to pay as much per user. For this reason they batch their referral programme via this step function. This way they can lower their costs by introducing "breakage", i.e. "free" referrals that they do not have to pay for because the referrer never reaches the 3 user unlock.

### Definitions: What is a Refer-A-Friend Scheme?

<div class="epigraph">
  <blockquote>
    <p>If you do build a great experience, customers tell each other about that. Word of mouth is very powerful.</p>
    <footer>Jeff Bezos</footer>
  </blockquote>
</div>


<span class="newthought">People are social </span> creatures. People have a natural tendency to talk, and Refer-A-Friend as a user acquisition channel aims to leverage natural social behaviour of your users in order to acquire new customers. In other words:

> <p class="sans">A Refer-A-Friend scheme is a structured program where existing users recruit new customers to a product.</p>

There are two types of users involved in Refer-A-Friend schemes:

- **referrer**: an existing user that invites a new user
- **a referee**: the new user being referred to use your product

Likewise, there are two categories of referrals:

- **incentivised**: this is when you provide your customers with a **reward** for successfully referring someone
- **unincentivised**: when you do not provide your customers with an incentive for successfully referring others

The **qualification criteria** are the requirements your users (either **referrer** or **referree** or both) need to hit in order receive a **reward**.

There are two broad categories of **rewards**:

- **cash incentives**: whereby you offer users cash or cash equivalents (e.g. Amazon gift cards).
- **non-cash incentives**: non-cash incentives which have low marginal costs, like extra lives in video games (e.g. Candy Crush) or free premium features (e.g. DuoLingo)

It is important to also clarify a few things that are similar to RAF schemes but have some important differences.

Giving new users a **reward** if they meet a certain **qualification criteria**,  if they haven't been referred by an existing user, is a **sign-on bonus**. Sign-on bonuses have similar dynamics than referrals, but are sufficiently different that they should be structured differently.

Similarly, when a single **referrer** gets compensated for referring a large volume (think hundreds) of **referees**, he is not so much a **referrer** but an **affiliate**.

Operationally, there are two important terms you must be aware of:

- **Fraud**: when professionals, often in organised groups, are trying to rip you off. They could be using stolen / bought identities, bot farms, etc.
- **Abuse**: Abuse is simply when everyday people decide to try to take your money. This means a group of college kids who all sign up and refer each other for the rewards.


### Who Refers, Who Gets Referred, Why And How?

<div class="epigraph">
  <blockquote>
    <p>For every social app I’ve ever built, number of invitations sent per user drops 20% for every additional year of age—from 13 years old to 18</p>
    <footer>Nikita Bier, <cite>CPO of X</cite> (2014)</footer>
  </blockquote>
</div>

<span class="newthought">Good begets good. </span> Generally, people refer people like themselves. There are various other factors which influence the likelihood someone will refer or be referred to your product. The single most important insight is that good users are also the best referrers.

Not only do good clients usually refer the most users (under normal circumstances) but they also refer the highest quality users. Keep an eye on your power users and try to figure out what you can do to to encourage them to refer.  Unfortunately, it is also the case that the minority of referees who are referred by low value clients tend to be low value clients themselves.

**comment add in chart**

Yet it is no coincidence that most "viral" apps tend to start with teenagers or college aged individuals. Demographics play an important role, as the quote above implies. Generally,  younger users tend to refer more. But whereas social media networks want you to refer more new people because of the strengthening of network effects and a relatively low cost to service users, most businesses (particularly fintech businesses) want more of the *right* users.

**comment add in chart**

The chart above shows that referred users tend to skew young, but most of the value generated by the referral programme doesn't come from the youngest referred users. The sweet spot is somewhere in the middle, where you still get valuable users but at a high enough volume.

If, like Nikita Bier, your goal is to acquire as many users as possible, then by all means try to skew as young as possible. If, on the other hand, you want to get as much value as possible from referrals as a user acquisition channel, you need to appeal to the right demographic.

### Most Users Refer Only One Or Two Users

![Referrals Per Referrer](/Users/boazsobrado/Desktop/codes/raf/img/referrals_per_referrer.png)

As the title implies, the vast majority of users who refer (keep in mind most users do not refer anyone) only successfully refer one or two users.

From this it follows that the **single most important referral is the first one**. In other words, the biggest leverage you have on a referrals programme is increasing the percentage of users who make at least one referral. It depends on your product, but it is unlikely for the user to "know" enough people who will convert dozens of people to your product.

If your distribution doesn't look like this, but rather has a number of "superreferrers" referring a large percentage of users, you need to carefully inspect who these users are and who they are bringing in. This is not necessarily a problem, and can be a good source of new user acquisition, but I would argue that these are no longer really referrers, but rather affiliates.

Affiliates require far more stringent monitoring. If left unmonitored you may be exposing yourself to risks like: affiliates increasing your marketing costs by bidding on your keywords, running reputationaly risky black-hat marketing campaigns or even individuals running fraud rings using your referrals scheme to monetise. [^mn: see more under [Referrals & Affiliates](#Referrals and Affiliate)]

### Referred Users Are Highly Likely To Convert

In terms of conversion rates, referred users are both more likely to convert and convert faster than users acquired from other channels.

There's a few reasons for this:
- If incentivised, they have much higher motivation than your regular users.
- Chances are their friends already sold or explained your product to them, and are effectively "warm" leads. The referrer has already done a lot of the work for you by the time they hit the onboarding flow. [^sn: Consider testing a separate onboarding flow for referred users.]

If the conversion rate for your referred customers isn't multiples of your overall onboarding funnel, you need to double check something hasn't broken.

## Design Principles of Referrals Schemes

###The Quality versus Quantity Tradeoff

Every referral program faces the same tradeoff: **quality versus quantity**. Each lever you adjust, be it reward amounts, qualification criteria or even onboarding friction, will have an impact on this balance.

A typical example can be seen below:

<figure class="fullwidth">
  <img src="/Users/boazsobrado/Desktop/codes/raf/img/referral_dynamics_2.png" alt="Quality versus quantity in referrals">
  <figcaption>The dilemma of balancing quantity versus quantity in refer-a-friend programmes</figcaption>
</figure>

The key intuition is that the less incentive (or more friction) there is for people to refer, the better quality the of the users acquired through the acquisition channel will be. If referring is difficult and is unincentivised, only your most loyal users will refer, and they too will only refer people for whom they know the product is a good match. On the other hand, if referring is easy and highly incentivised, your users may be driven to make money by referring customers who are unlikely to be good clients.

### Rewards

<span class="newthought">The more you pay out </span> the more users you acquire. Like for all channels, the relationship between payouts and user acquisition increases linearly at first, and then tends to tail of as the incremental cost per new customer rises.

Moreover, if you increase rewards you tend to find that the average quality of an acquired user goes down. This is because you get a larger percentage of "reward chasers" rather than genuine, interested users of the platform. A lot of running a RAF campaigns has to do with being successful in scaling volumes while not compromising on quality.

### Rewards: Cash vs Non-cash Incentives

<figure style="max-width: 55%;">  <!-- 50% of 55% -->
   <img src="/Users/boazsobrado/Desktop/codes/raf/img/alltrails_referral_tree.png" alt="An example of Robinhood's Variable Reward scheme">
 </figure>
Casual gaming companies like CandyCrush, Monopoly Go or DuoLingo tend to offer non-cash incentives for their referral schemes. If the average LTV of their users is less than $1, then it is impractical to offer cash incentives for referrals. Instead, they tend to offer non-cash incentives like in-game currency, extra lives and premium product features to entice users to refer new customers.

The advantages of non-cash incentives are that they tend to attract high quality customers, have low marginal costs and have far lower transaction costs than cash incentives. Moreover, in cases when cash incentives are not an option due to low LTVs or regulatory reasons (such as for example cash-incentivised referrals payouts for CFD products, which are banned in the European Union), non-cash incentives allow products to run referrals campaigns.

The disadvantage of non-cash incentives is that they can be hard to stack and thus to scale. If you give a user a free premium feature for referring a customer, what incentive will they have to refer more than one? Moreover, you will get a selection effect in a way that you do not with cash incentives. $50 is $50 for everyone, but your premium feature may be more attractive for some users than others. This is of particular concern with the **referee**. Even if the **referrer** values the "extra life" in a game they receive as a reward for onboarding their friend, it is unlikely the **referee** will value it as highly.

[^mn:<img src="https://cdn.prod.website-files.com/5ecfee3d3c78d12514ee78db/659fd5147dc3b23241e4e607_Untitled%2010.webp" alt="Revolut Non-Cash Incentive" style="max-height: 500px; width: auto;"> Revoluts ran a non-cash incentive scheme for their metal card]

Cash incentives (or at least incentives with a clear monetary value) tend to lead to greater volume because they are more attractive to both referrer and referee, and because they are infinitely stackable. By stackable I mean that if you get 50 dollars for referring a friend, and you refer 5 friends, then 250 dollars is 5 times better than 50. However, they do attract certain people who want to take the money and run.

### Rewards: Splitting Rewards

The industry has converged towards the best practice of offering both users a reward. Moreover, the referrer and the referee tend to get an equal sized reward. The reason for this is more psychological than economic. It turns out users are much more likely to want to give a "gift" to their friends than to be seen to be "making money" off a friend.

[^mn:![OnePay Uneven Incentive](/Users/boazsobrado/Downloads/onepay_raf.PNG) Uneven sided referral programme by OnePay]

That being said, while it is best practice for most products it is by no means inevitable for it to be like this. Single sided referrals programmes also work, and may even be somewhat more effective depending on the user group. Generally, cash strapped users (such as those using OnePay), or users who refer people who are less close to themselves (e.g. micro-influencers), may want to help themselves to a larger percentage of the reward.

### Rewards: Variable vs Non-Variable

Generally, rewards  ought to be as simple as possible. The more you increase the complexity of the reward, the harder it is for the referrer to explain and for the referee to understand. The only reason why you would increase complexity is to make the scheme easier to market.

We know that the higher the reward you advertise, the more volume of referrals you get. One way in which you can advertise a high reward without compromising profitability is by offering variable rewards.  For example, take Robinhood's referrals programme. Their terms and conditions tells us that:

> The cash value you receive could be anywhere between $5 and $200. Keep in mind, approximately 99% of customers will get stock worth $5. You can use this reward to claim a fractional share of a stock.

Why would Robinhood do this? The hope is that the prospective (or existing) user will read the high number and be anchored towards it.  In other words, variable rewards are a way of being able to market potential rewards to users and assume that they will either not read carefully or will "hope" for the big reward.

In an interview, Robinhood employees claim they have AB tested dozens of different reward schemes and have yet to find something more effective than this. Nevertheless, the option might not be available to everyone given compliance limitations, and it is probably more suitable to some products than others.


### Rewards: Cliffs, Bonuses and Limits

Another way in which you can market a higher number is by introducing limits, cliffs or bonuses that make "real" payouts smaller than "marketing" figures.

An important thing to realise is that the user often has limited control over how many users they refer. They can invite a friend, but whether they sign up and they meet the qualification criteria or not is often beyond their control. Their friend may be too lazy to sign up, or might not understand your app. For this reason, varying the value paid out based on the number of people they refer can be another way in which you can introduce variance into payout amounts.

For example, Wise's campaign offers a payout ONLY if the user refers three individual separate new clients. This introduces breakage,  which means that a lot of referrals will not get paid out ever. The purpose of this is to save on costs. The image below illustrates just how much:

![Referrals Per Referrer](/Users/boazsobrado/Desktop/codes/raf/img/wise_breakage_stacked.png)

Assuming a distribution of referees per referrer, Wise can cut costs by up to 90% through this payout scheme.

Another option is to limit the amount of users a single individual can be paid for. This also serves as a cost saving measure, but can help limit fraud and removes incentives for abuse too.

One of the best tactics I have found is to add a bonus incentive for the *first* referral. Referrers tend to refer multiple people, knowing that there is no guarantee any particular user will convert. By paying double for the first referral, you often can buy multiple referrals at a good price. Moreover, it makes it more likely for an individual to make their first referral, which increases the amount of referrals considerably.

### On The Qualification Criteria

**add images to illustrate**


Examples of qualification criteria:

- Capital.com: 200 USD deposit and 3 trades
- Wise: three friends who do X
- Public.com: Buy 1000 worth of stocks

The reason why you are setting up **qualification criteria** for a referred user to hit is because you want to make sure you are getting a valuable user for your money. Here too you have to balance on the *quality vs quantity* tradeoff.

If you make it a bit too easy to meet the criteria, you'll end up flooded by users who simply to take your money. If you make it too hard, you'll end up acquiring very few incremental new users. Tightening the quality criteria is often analogous to paying less. You'll acquire fewer users, but of average better quality.[^mn: This is not always true, but most of the time it is.]


<p class="sans">A good qualification criteria is generally a heuristic that predicts a high user lifetime value.</p>

My favourite qualification criteria was the one we used at Zilch. We ran a simple regression that showed that adding a card to a mobile wallet was one of the best predictors of higher user LTV. We realised that once a user added a Zilch card to their device wallet, it was very sticky. Very few users would go through the effort of deleting the card, which meant that sooner or later they were likely to use it. 

Our qualification criteria then became: "The new user must spend using ApplePay / GooglePay to get your rewards". We even made the referrer rewards only spendable via mobile wallet, ensuring both users were more likely to be retained. 

The qualification criteria should "predict" LTV, not "be" LTV. There is sometimes a temptation to try to keep qualification criteria tight, effectively turning referrals rewards into a fee rebate. For example, a business will calculate that $100 in user spend generates $30 in profit, so they will "give" back some of the profit (i.e 30 USD) to the user. The argument is sometimes made that this will make abuse and fraud impossible. I generally advise against this, because most users can see through the transactional nature of this arrangement. They want a reward in anticipation of their business, not a discount on existing transactions.

Make the criteria as simple as possible. Not only do your referrers need to be able to understand it, they also need to be able to **explain it** to the referees, who understand your product even less than they do. Do not use internal jargon ("registered customer", "lead", etc) and assume the user will understand. Along these lines, a good qualification criteria needs to **seem** easy to do. It doesn't necessarily have to be easy, but it needs to seem simple enough to the user. A good example of this is Robinhood's 'invite a friend and link a bank account to get a stock'. This seems easy enough to do, but does not say anything about risk checks, KYC verification, eligibility questionnaires and other things which might be necessary to link an account.

### Qualification: Time Limits and Limited Time Offers

Like in the Revolut example above, often referrals programmes will introduce limited time offers with a higher bonus structure than before. This serves two purposes, first to give people an incentive to refer now as opposed to procrastinating and deferring it to some endless point in the future. Instilling a sense of urgency for action is key.

Second, it can be used to manage flows and campaigns. Because referrrals campaigns can have uncertain outcomes (e.g. due to the introduction of a new qualification criteria or a higher reward) limiting the duration of the campaign can limit the potential cost of a campaign. If from outset the campaign is set to expire after a limited amount of time, you can avoid changing terms and conditions on users at the last minute.  If the new offer is for unlimited time, the campaign could easily grow more than expected and would potentially acquire a cohort of low value customers. By limiting the duration of the campaign, it allows for a manageable post-campaign analysis to review the cohort's value.

Third, it can help capitalise on certain events or seasonality. A "Christmas campaign" may encourage people to share the product with their families when they are at home.

### Referrals UI - UX

**comment: draft, bring up to speed with examples from the site where you need to pay, add ALEX's comments here maybe?**
A well-designed refer-a-friend scheme has the following elements:

1. Referral hub / entry point
The main screen where you land. Shows your unique link or code, maybe a headline like "Earn £50 per friend." Often has a prominent share button and a summary of your stats (invited: X, earned: £Y).
2. Share/invite screen
Where you actually distribute the link. Usually presents options: copy link, share via WhatsApp, SMS, email, social media. Sometimes includes a QR code. Revolut does this as a modal; Wise keeps it inline.
3. Status tracker
Shows progression of each referral. Typically columns or cards with states like: "Invited" → "Signed up" → "Completed action" → "Reward unlocked." This is where users check if their friend actually qualified.
4. Rewards / earnings screen
Your payout history and pending amounts. Shows what you've earned, when it was credited, and any rewards still waiting to unlock. PayPal tends to show this as a transaction-style list; Revolut uses a more visual summary.
5. Terms / how it works
Explains qualification criteria. What counts as a "qualifying action"—first transfer, card spend, verification, etc. Usually a separate detail page or expandable section.

Omitting any of these pages is asking for trouble later. If you don't have a "status tracker" for example, your customer support will be inundated with people asking. 

## Operations

###  Metrics To Monitor

A successful refer-a-friend scheme acquires a large number of high quality users. To do this, you need to monitor the quantity of users acquired, their quality, and the virality of referral scheme. 

I'd like to emphasise that monitoring the quality of users acquired via RAF is absolutely key, especially if you are giving away cash or cash equivalents. You should monitor their performance daily, particularly if you see a sudden increase in volume of users. It is of great importance you monitor the spread of the channel by geography or nationality. See more on this on the fraud section.

I have found the following (non-exhaustive) list of metrics useful:

- Quantity:
  - Number of new leads via referrals
  - Number of new qualified leads via referrals
  - Number of transacting new customers
  - % of user acquisition that comes in via referrals
  
- Quality: 
  - The converision funnel steps of referred users (click -> lead -> registered customer -> active customer)
  - Their LTV curves

- Virality: 
  - Number of clicks on referral links
  - Number of shares of referral links
  - Referral rate (w)
  - Referral rate of new customers
  - Number of users referred per customer

### Running A RAF Scheme

Do not underestimate the complexity of a simple change to the referral programme. Say you want to change the payout amoutn for  You need to change:

- email comms to both referrer and referee
- App and Web UI for both referrer and refereee
- push comms for both referrer and referee
- publicly available materials on the webpage, in FAQs, on support ticket responses etc.

Perhaps this seems obvious, but it happens surprisingly often that one or more of these are out of whack with each other. This inevitably leads to user complaints and customer support tickets. Part of the reason for this is that generally different teams tend to own these functions, and they tend to run with different providers. For this reason, a high quality referral campaigns will require collaboration across various teams in a tech company. You will need to work with: 
- the product & engineering team (to change referral logic, screens and features)
- the marketing & CRM team (to notify your customers about the programme and referral campaigns)
- the legal team (to draft the terms & conditions of the programme)
- the customer support team (to update FAQs and deal with the inevitable inquiries and complaints around the programme)
- finance or backoffice support team to deal with payouts
- the fraud team to deal with potential issues (more on this later)

If you are building out a scheme, or even modifying an existing scheme, it is highly recommended you notify all these teams. 

Due to the potential virality of referral schemes and the large amount of users for whom this is the first interaction with your product, it is important to minimise the number of users who are dissapointed by the scheme. Otherwise, you'll be flooded by people complaining in customer support tickets. It is surprising how often people get upset about free money.

From this it follows that its important to keep in mind while building out the referral scheme ensure it is "easy" to change things. Ideally, you want to be in a position where means all of the items above can easily changed at the flick of a button.

#### CASE STUDY: PUBLIC
It would be unworthy of me to pick on a company with a terrible RAF scheme, so instead I picked a good one that is nonetheless facing some of the most common issues. Public runs a tightly managed refer a friend promotion with simple qualification criteria, and a limited time offer. Nevertheless, I experienced the following isues as a referrer: 

- Email comms goes out
- App says one thing
- Link on app says another
- Landing page has a 404
-etc

#### CASE STUDY: ZILCH

One of the problems we faced at Zilch was that our referral programmes paid out based on when the user created the account.

Lets say I invite a friend when the referrals campaign pays out $5 per user and they create an account, but do not qualify for the referral bonus. A month later, the referral amount increases to $10 dollars for a limited time, and Zilch emails their customers about it. I call my friend and ask him to finish the process, and he ends up qualifying. But we both get $5 instead of the $10 we were expecting, because he created his account under the previous campaign!

This also lead to financial reporting issues, because inevitably we'd have users being paid a wide range of referral bonuses in a given month as they qualify, but the financial models had stricter assumptoins. 

Generally, we would increase the payout if people complained via customer support but a more long term solution would be to make referral offers time limited. 

### International Refer-A-Friend Programmes

Cross-border referrals, i.e. where a customer in one country refers a customer in another country, can get very complicated. 

First, there might be a different payout amount. Digital products tend to cost more in the United States than say in India. For this reason, often RAF schemes have different payouts for referrals in India than in the United States. So then, if a user in India refers a user in the United States, should this user receive the Swiss reward or the American reward?

Second, although the user usually sees a single product, the legal entities underlying the product may be different from country to country as they sit under a different regulatory regime. Incentivised referrals may be legal under one jurisdiction for a financial product, but illegal in another. Perhaps your user referred a customer in a state where he cannot legally be paid for a referral. They'll blame you unless you explain it to them. 

My advice is generally to try to keep the programme as simple as possible and avoid using "country of residence" distinctions when setting qualification criteria or reward. If it is unavoidable, simplify the situation by allowing customers to only refer people in their own countries, as this should cover most cases anyway. 

### Going Viral

<div class="epigraph">
  <blockquote>
    <p>It's just like bacteria in a Petri dish. So what you want to do is try to have one customer generate like two customers. OK? Or something like that. Maybe three customers, ideally. And then you want that to happen really fast.</p>
    <footer>Elon Musk <cite>SpaceX, Tesla, Paypal</cite> (2014)</footer>
  </blockquote>
</div>

Virality coefficient: Number of users referred by the average user * conversion rate.
$$ N_avg_referrals * P_Referral $$

If it is greater than 1, then you have an exponentially increasing virality coefficient and will go viral.

The more you incentivise and push users to Refer A Friend, the worse the quality of the acquired user.

Assuming you want to at least make your money back, the equation generally boils down to[^mn: This might not always be the case. The initial cohorts of the viral PayPal RAF acquisition likely never paid back, but the resulting network effects were valuable in themselves]:

Expected_LTV >= Reward Paid Out

Reward Paid Out = P(Meeting Qualification Criteria) * Expected

= P(Meeting Qualification Criteria) * Expected_LTV_Given_Meets Conversion Crtiteria

$$P(Conversion | Qualification Criteria) * E(Value| Conversion) = Reward <= expected LTV $$


probs remove the below 
The reward of an incentivised RAF scheme can vary across companies and industries. It can be extra product features, a discount or even a cash bonus. Generally, you wish to balance the reward you pay with the value of the users you attract, so that you end up paying less than what the user you are acquiring is worth. Similarly, the qualification criteria can also vary: it can be as little as registering to your product (e.g. signing up to an email list or downloading your app), but it might also be as onerous as making several large transactions. Importantly, the qualification criteria and the reward are two sides of the same coin. The more onerous your qualification criteria is, the more you can afford to pay out as a reward.

### Fraud & Abuse

Generally, Refer a Friend is inevitably going to lead  to a lot of conversations around fraud and abuse within the company.

Many people have some memory about them personally (or someone they know) abusing a refer-a-friend scheme and feeling very clever about it. Second, the process around incentivised referrals usually involves teams that are not usually involved in marketing operations, such as finance, fraud,  customer support or operations teams. It is very difficult for finance team analysts or customer support specialists to spot millions of dollars wasted in ineffective Google Search ad spend, but they will easily notice that sometimes you pay out 50 USD for a user that ends up not coming back ever again. For many people, that money feels more "wasted" to them.

For this reason, it is important to establish everyone across the business from the outset that [^mn: I have stolen this phrase from an [excellent essay](https://www.bitsaboutmoney.com/archive/optimal-amount-of-fraud/) by Patio11]:

> The optimal amount of fraud and abuse on a refer a friend scheme is not 0

Some degree of abuse & fraud is fine, it is part of your CAC and you can bake it into your LTV calculations too. Point out that there will be wasted money on all marketing acquisition channels. As long the numbers make sense overall, it is fine.

That being said, every now and then you'll end up looking at a chart like this:

Chart image

This should scare you. If this happens you rapidly need to figure out which of 3 things has happened:

- You're a victim of abuse
- You're a victim of fraud
- You've gone viral
- Some combination of the above

You need to figure which of these it is, and quickly, because exponential growth will put your tech infrastructure under severe load, it'll swamp your customer support teams and generally all things will break. You need to figure out if its worth it.

As a sidenote, generally it is good practice to have an anti-fraud / anti-abuse mechanism online that can be finetuned at a moments notice, whereby you can slow down the pace of the referrals without the need for a release or to diverte valuable tech resource. Any friction you introduce (e.g. a 24 hour payout review period) will slow down the momentum down significantly.

Fraudsters are more likely than your users to read the T&Cs, and to think of ways to get around them.
Don't try to bake in every single possible exception to the rules into the T&Cs, just reserve the right to not pay out for inorganic behaviour.

Can usually be mitigated through simple anti-fraud methods involving monitoring the reuse of identities, addresses, payment methods, devices etc. Your anti-fraud method does not have to be perfect, it just has to be better than that of the latest FinTech that raised a lot VC of money. Much like how a gazelle in a hunted gazelle pack doesn't need to outrun a lion, but just outrun the slowest gazelle. For every little piece of friction you introduce to fraudsters, the less exploiting you is worth it to them, and the more it is worth exploiting your less capable competitors.


## Referrals And Affiliates

Wise's Refer-A-Friend T&Cs state:

>2.3. The referral program is solely for individual personal usage and not for any commercial usage.

> 2.4. If you wish to, or already use the Referral Program to, refer people as part of your business for commercial purposes, including referrals via a website or social media, or any kinds of advertising and marketing activities (or for other purposes outside the scope of this Agreement), at our sole and absolute discretion, we reserve the right to move you on to our marketing program (the “Partner Program”), subject to the terms of this Agreement, within the Wise app, or exercise our rights under clause 6. If you are moved to the Partner Program, you will be notified in writing.

> 2.5. If Wise elects to move you to our Partner Program, you will be subject to a different set of terms and conditions. If you do not want to join the Partner Program, but continue to refer people for commercial purposes, then Wise can exercise its rights under clause 6 of this Agreement.


## When to Reach out (CRM)

- Social proof the largest payouts
- Reach out regularly
- Reach out early during the funnel, after the first transaction, generally whenever is a good time to ask for a review is a good time to to ask for a referral
- Keep a refer a friend CTA in the footer of ALL your emails & customer comms to increase surface area. 

### Should I put Ads Behind My Refer-A-Friend Campaign?

![Ad spend behind Blueberry's referral campaign](/Users/boazsobrado/Desktop/codes/raf/img/raf_ad.png)

Often growth teams will be tempted to "seed" or "push" a referrals campaign with ad dollars.

This is generally a bad idea, for various reasons. Primarily because the quality of the users you attract with this sort of campaign is sub-par. Second, the conversion rates are far lower than acquiring new users, given that users have to a) register themselves b) refer a new user. You are better off focusing on acquiring new users, and incentivising the conversion to a referral further down the line.

## Customer Stickiness


## Unincentivised Referrals: You Are Already Acquiring Users Through Referrals

For most businesses, if you ask your new customers "where did you hear about us?" generally one of the most common answers you'll hear is "word of mouth" or "a referral from a friend". Even customers where you have a "clean" digital attribution and you can see that they clicked your Google search ad, even these customers will often tell you a friend referred them, particularly if your product is deliberative and has a long lead time. Chances are that yes, they clicked your ad, but they also spoke to their friend and/or had the product recommended to them beforehand.

Therein lies an opportunity. The key insight is that you want to make it as easy as possible for your users to talk about and advertise your product.

If you make it easier for users to refer each other to your product, then more users will get referred in. For this reason, I often recommend starting with setting up a simple, unincentivies refer a friend programme. Even if you cannot offer incentives to your users to refer others, they will still do it (assuming you have a good product, if you don't, please work on that first).

If there is no refer a friend scheme set up, I'll often recommend starting with an unincentivised programme. Just a few screens and clicks to make it easier for people to refer your product to a friend, something that they were likely to do anyway. This has the dual purposes of establishing a baseline of users who will come in via a refer a friend programme and helping you calculate the incremental value of incentives overall.

- Screenshots On LinkedIn
- Watermarks On TikTok & X
- "Sent from my iPhone"
