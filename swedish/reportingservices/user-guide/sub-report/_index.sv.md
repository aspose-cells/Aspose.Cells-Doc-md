---
title: Delrapport
type: docs
weight: 90
url: /sv/reportingservices/sub-report/
---
{{% alert color="primary" %}} 

En delrapport kan bäddas in i en tabellpost. Formatet är: &=subreport{ReportName=ditt rapportnamn; parameter1 namn = parameter1 värde; parameter2 namn = parameter2 värde; ...}

**En delrapport i en rapportdefinition** 

![todo:image_alt_text](sub-report_1.png)

I exemplet är namnet på underrapporten "Försäljningsorderdetalj". Den har en parameter, SalesOrderNumber. Värdet på parametern är EmpSalesDetail.SalesOrderNumber.
### **Restriktioner för delrapporter**
1. Delrapporten ska utformas med Aspose.Cells.ReportingServices Designer.
1. Underrapporten kan bara bäddas in i tabellgruppsraden och gruppraden kan inte innehålla några element förutom underrapporten. Det är inte tillåtet att bädda in en delrapport i raderna med tabelldetaljer eller sidfotsrader.
1. För närvarande stöds inte kapsling av mer än en nivå. Delrapporten kan inte innehålla en inbäddad rapport.

{{% /alert %}} 
###### **Det här avsnittet innehåller följande ämnen:**
- [Skapar tabellobjekt](/cells/sv/reportingservices/creating-table-item/)
- [Lägg till underrapportobjekt](/cells/sv/reportingservices/add-sub-report-item/)
