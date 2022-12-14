---
title: Delrapporter
type: docs
weight: 20
url: /sv/reportingservices/sub-reports/
---
{{% alert color="primary" %}} 

Vi inkorporerade stöd för att bädda in en delrapport i en tabellgruppsrad. Formatet är:

&=subreport{ReportName=ditt rapportnamn; parameter1 namn = parameter1 värde; parameter2 namn = parameter2 värde;......} 

{{% /alert %}} 
### **Exempel**
**En delrapport i en tabell** 

![todo:image_alt_text](sub-reports_1.png)

 I exemplet är namnet på underrapporten "Försäljningsorderdetalj". Den har en parameter,*Försäljningsordernummer* . Värdet på parametern är*EmpSalesDetail.SalesOrderNumber.*
#### **Restriktioner för användning av underrapporter**
- Delrapporten bör utformas med verktyget Aspose.Cells.Reporting Services Designer.
- Underrapporten kan bara bäddas in i tabellgruppsraden och gruppraden kan inte innehålla andra element förutom underrapporten. Det är inte tillåtet att bädda in en delrapport i raderna med tabelldetaljer eller sidfotsrader.
- För närvarande stöds inte kapsling av mer än en nivå. Delrapporten kan inte innehålla inbäddad rapport.
