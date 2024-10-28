from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date

class RiskFactors(BaseModel):
    description: str = Field(..., description="A description of risk factors affecting the company")
    impact: str = Field(..., description="How these risk factors might impact the company's operations or financials")

class BusinessDescription(BaseModel):
    overview: str = Field(..., description="Overview of the business operations")
    products_and_services: str = Field(..., description="A list of products and services offered by the company")
    subsidiaries: Optional[List[str]] = Field(None, description="A list of company subsidiaries")
    industry: str = Field(..., description="Industry in which the company operates")

class LegalProceedings(BaseModel):
    description: str = Field(..., description="Any ongoing or past legal proceedings involving the company")

class FinancialStatements(BaseModel):
    income_statement: str = Field(..., description="Summary of the company's income statement")
    balance_sheet: str = Field(..., description="Summary of the company's balance sheet")
    cash_flow_statement: str = Field(..., description="Summary of the company's cash flow statement")
    footnotes: Optional[str] = Field(None, description="Additional footnotes or commentary on the financials")

class ManagementDiscussionAnalysis(BaseModel):
    financial_conditions: str = Field(..., description="Discussion of the financial condition of the company")
    operations: str = Field(..., description="Discussion of the results of operations for the reporting period")
    liquidity_and_capital_resources: str = Field(..., description="Liquidity and capital resources discussion")

class ExecutiveCompensation(BaseModel):
    name: str = Field(..., description="Executive name")
    title: str = Field(..., description="Executive title")
    salary: float = Field(..., description="Base salary of the executive")
    bonus: Optional[float] = Field(None, description="Any bonuses received by the executive")
    stock_options: Optional[float] = Field(None, description="Stock options granted to the executive")
    total_compensation: float = Field(..., description="Total compensation received by the executive")

class FinancialSummary(BaseModel):
    revenue: float = Field(..., description="Total revenue for the reporting period")
    net_income: float = Field(..., description="Net income for the reporting period")
    total_assets: float = Field(..., description="Total assets held by the company")
    total_liabilities: float = Field(..., description="Total liabilities of the company")

class TenKForm(BaseModel):
    company_name: str = Field(..., description="The name of the company filing the 10-K")
    fiscal_year_end: str = Field(..., description="The fiscal year-end date for the report")
    risk_factors: Optional[List[RiskFactors]] = Field(None, description="Risk factors discussed in the report")
    business_description: BusinessDescription = Field(..., description="A description of the company's business")
    legal_proceedings: Optional[List[LegalProceedings]] = Field(None, description="Any legal proceedings involving the company")
    financial_statements: FinancialStatements = Field(..., description="The company's financial statements")
    management_discussion_analysis: ManagementDiscussionAnalysis = Field(..., description="Management's discussion and analysis of financial conditions")
    executive_compensation: Optional[List[ExecutiveCompensation]] = Field(None, description="Compensation details for company executives")
    financial_summary: FinancialSummary = Field(..., description="A summary of key financial metrics for the company")