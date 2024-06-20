---
title: Exportera DataTable från GridWeb
type: docs
weight: 70
url: /sv/net/aspose-cells-gridweb/export-datatable-from-gridweb/
keywords: GridWeb, export
description: Den här artikeln introducerar hur man exporterar datatable i GridWeb.
---

{{% alert color="primary" %}} 

[Importera DataView till GridWeb](/cells/sv/net/aspose-cells-gridweb/import-dataview-to-gridweb/) handlade om att importera innehållet i en DataView till kontrollen Aspose.Cells.GridWeb. I den här artikeln diskuteras export av data från Aspose.Cells.GridWeb-kontrollen till en DataTable.

{{% /alert %}} 
## **Exportera kalkylbladsdata**
### **Till en specifik DataTable**
För att exportera kalkylbladsdata till en specifik DataTable-objekt:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
1. Skapa ett specifikt DataTable-objekt.
1. Exportera datan från de valda cellerna till det angivna DataTable-objektet.

Exemplet nedan skapar ett specifikt DataTable-objekt med fyra kolumner. Kalkylbladsdatan exporteras från den första cellen med alla rader och kolumner synliga i kalkylbladet till ett redan skapat DataTable-objekt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **Till en ny DataTable**
Ibland vill du inte skapa ett DataTable-objekt utan behöver helt enkelt exportera kalkylbladsdata till ett nytt DataTable-objekt.

Exemplet nedan försöker på ett annat sätt visa användningen av Export-metoden. Det tar referensen från det aktiva kalkylbladet och exporterar den kompletta datan från det kalkylbladet till ett nytt DataTable-objekt. DataTable-objektet kan nu användas på vilket sätt du vill. Det är till exempel möjligt att binda DataTable-objektet till en GridView för att visa datan.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
