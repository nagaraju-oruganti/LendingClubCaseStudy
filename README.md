# LendingClub Defaults Exploration

> LendingClub is a consumer finance company which specialises in lending various types of loans to urban customers. When the company receives a loan application, the company has to make a decision for loan approval based on the applicant’s profile. The objective of the exploratory analysis to investigate variables driving the default rates.

## Table of Contents

- [General Info](#general-information)
- [Technologies Used](#technologies-used)
- [Conclusions](#conclusions)
- [Acknowledgements](#acknowledgements)

<!-- You can include any other section that is pertinent to your problem -->

## General Information

- Provide general information about your project here.
  Consumer default on loan payments is a loss to the lending business. In the project, our aim to investigate the factors that could assists in predicting default such that loan approval process can be improved to minimize loss.

- What is the background of your project?
  LeadingClub offers loans to the customers in 50 states in the US. The company grew exponentially between 2007 and 2011. This period coinsides with the great recession.

- What is the business probem that your project is trying to solve?
  Until 2010, the company reduced default rates to 12.9% but in the year 2011, the rate increased to 15.9%.

- What is the dataset that is being used?
The dataset is comparised of loan approved from 2007 to 2011. It included loan related attribtues and the borrower attributes.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Conclusions

1. The primary factor in the loan default are those applicants who secured loans on debt consolidation followed by small buiness, credit card, home improvements, and others. (Note that the records might have combined in others that do not fit in any of the rest 11 categories.)
2. Divergence between the mean funded to annual income ratio for the applicants defaults are higher. While the interest rate charged to them is also higher. It seems that the organization have some corrolary framework to assign interest rate on the risk they are acquiring from offering loan to those risky applicants. This is a normal process in lending business.
3. Contrary to the above observation, it is observed that there exist non-linear (expontential) relationship between interest charge and the funded amount irrespective of the riskiness of the default. The interest rates are as high as 25% are funded in 2011, which is about 500bps higher than 2010.
4. Over the years, as the business expanded, the risk appetite of it also increased. Until 2009, the funded amount to annual income ratio of the applicant was 0.15, and this increased to 0.2 in 2011.
5. Grading system employed by the business is effective. It is evident from the fact that with increase in letter grades from A to G, the default rate incrased. The sub-grades also follow the same trend. The number of approval also gradually dropped to a couple of hundred approval in grade G.
6. The business implementation of verification process can be improved. The default rate for those applicants' income verified by the business, and the income source verfied is significantly higher than non-verified. This observation is contrary to normal wisdom. Loan that are verified are expected to have low defaults that non-verfied. It is likely that the verfication could be aftermath of deliquency/default. In that case, verification process should be integrated in the application process.
7. Longterm loan of 60 months have higher defaults than 36 months. Applicants who defaulted took short term loan (36 months). While those who took long term loan (60 months) are defaulted when the funded amount is more than 0.2 of there income on average.

<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Technologies Used

- numpy - version 1.23.5
- pandas - version 1.5.3
- matplotlib - version 3.7
- seaborn - version 0.12.2

<!-- As the libraries versions keep on changing, it is recommended to mention the version of library used in this project -->

## Acknowledgements

Sayan for his ilustrative explaination in the live class

## Contact

Created by [@nagaraju-oruganti] - feel free to contact me!

<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
