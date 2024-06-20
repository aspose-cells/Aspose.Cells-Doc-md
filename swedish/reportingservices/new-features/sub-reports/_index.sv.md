---
title: Delrapporter
type: docs
weight: 20
url: /sv/reportingservices/sub-reports/
---

{{% alert color="primary" %}} 

Vi har inkorporerat stöd för att bädda in en delrapport i en tabellgruppsrad. Formatet är:

&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

{{% /alert %}} 
### **Exempel**
**En delrapport i en tabell** 

![todo:image_alt_text](sub-reports_1.png)

I exemplet är namnet på delrapporten ”Försäljningsorderdetaljer”. Den har en parameter, *SalesOrderNumber*. Värdet på parametern är *EmpSalesDetail.SalesOrderNumber.*
#### **Restriktioner för att använda delrapporter**
- Delrapporten ska utformas med verktyget Aspose.Cells.Reporting Services Designer.
- Delrapporten kan endast bäddas in i tabellgruppsraden och gruppraden får inte innehålla andra element än delrapporten. Att bädda in en delrapport i tabellens detalj- eller sidfotsrader är inte tillåtet.
- För närvarande stöds inte att bädda in mer än en nivå. Delrapporten kan inte innehålla inbäddad rapport.
