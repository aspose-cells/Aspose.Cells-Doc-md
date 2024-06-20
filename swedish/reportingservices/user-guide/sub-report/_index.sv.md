---
title: Delrapport
type: docs
weight: 90
url: /sv/reportingservices/sub-report/
---

{{% alert color="primary" %}} 

En underrapport kan bäddas in i en tabellpost. Formatet är: &=subreport{ReportName=din rapportnamn; parameter1 namn = parameter1 värde; parameter2 namn = parameter2 värde; ...}

**En underrapport i en rapportdefinition** 

![todo:image_alt_text](sub-report_1.png)

I exemplet är namnet på underrapporten "Försäljningsorderdetalj". Den har en parameter, SalesOrderNumber. Värdet på parametern är EmpSalesDetail.SalesOrderNumber.
### **Begränsningar för underrapporter**
1. Underrapporten ska utformas med Aspose.Cells.ReportingServices Designer.
1. Underrapporten kan bara bäddas in i tabellgruppraden, och gruppraden får inte innehålla några element utom underrapporten. Det är inte tillåtet att bädda in en underrapport i tabellens detalj- eller sidfotsrader.
1. För närvarande stöds inte inbäddning på fler än en nivå. Underrapporten kan inte innehålla en inbäddad rapport.

{{% /alert %}} 
###### **Denna avsnitt innehåller följande ämnen:** 
- [Skapa tabellpost](/cells/sv/reportingservices/creating-table-item/)
- [Lägg till underrapportspost](/cells/sv/reportingservices/add-sub-report-item/)
