# LendingClub Defaults Exploration

> LendingClub is a consumer finance company which specialises in lending various types of loans to urban customers. When the company receives a loan application, the company has to make a decision for loan approval based on the applicant’s profile. The objective of the exploratory analysis to investigate variables driving the default rates.

## Table of Contents

- [General Info](#general-information)
- [Technologies Used](#technologies-used)
- [Conclusions](#conclusions)
- [Acknowledgements](#acknowledgements)

<!-- You can include any other section that is pertinent to your problem -->

## General Information

- Consumer default on loan payments is a loss to the lending business. In the project, our aim is to investigate the factors that could assist in predicting default such that the loan approval process can be improved to minimize loss.

- LeadingClub offers loans to customers in 50 states in the US. The company grew exponentially between 2007 and 2011. This period coincides with the great recession.

- Until 2010, the company reduced default rates to 12.9% but in the year 2011, the rate increased to 15.9%.

- The dataset is comprised of loans approved from 2007 to 2011. It included loan-related attributes and borrower attributes.

## Conclusions

1. The primary factor in the loan default is those applicants who secured loans on debt consolidation followed by small businesses, credit cards, home improvements, and others. (Note that the records might have combined in others that do not fit in any of the rest 11 categories.)
2. Divergence between the mean funded to annual income ratio for the applicants' defaults is higher. While the interest rate charged to them is also higher. It seems that the organization has some corollary framework to assign interest rates on the risk they are acquiring from offering a loan to those risky applicants. This is a normal process in the lending business.
3. Contrary to the above observation, it is observed that there exists a non-linear (exponential) relationship between the interest charge and the funded amount irrespective of the riskiness of the default. Interest rates are as high as 25% funded in 2011, which is about 500bps higher than in 2010.
4. Over the years, as the business expanded, the risk appetite of it also increased. Until 2009, the funded amount to annual income ratio of the applicant was 0.15, and this increased to 0.2 in 2011.
5. Grading system employed by the business is effective. It is evident from the fact that with an increase in letter grades from A to G, the default rate increased. The sub-grades also follow the same trend. The number of approval also gradually dropped to a couple of hundred approval in grade G.
6. The business implementation of the verification process can be improved. The default rate for those applicants' income verified by the business, and the income source verified is significantly higher than non-verified. This observation is contrary to normal wisdom. Loans that are verified are expected to have low defaults than non-verified ones. It is likely that the verification could be an aftermath of delinquency/default. In that case, the verification process should be integrated into the application process.
7. Long-term loans of 60 months have higher defaults than 36 months. Applicants who defaulted took a short-term loan (36 months). While those who took long-term loans (60 months) defaulted when the funded amount is more than 0.2 of their income on average.

## Technologies Used

- numpy - version 1.23.5
- pandas - version 1.5.3
- matplotlib - version 3.7
- seaborn - version 0.12.2

## Acknowledgements

Sayan for his explanation in the live class

## Contact

Created by [@nagaraju-oruganti] - feel free to contact me!

<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
