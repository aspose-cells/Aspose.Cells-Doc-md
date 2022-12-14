---
title: Exportera DataTable från GridWeb
type: docs
weight: 70
url: /sv/net/export-datatable-from-gridweb/
---
{{% alert color="primary" %}} 

[Importera DataView till GridWeb](/cells/sv/net/import-dataview-to-gridweb/)talade om att importera innehållet i en DataView till Aspose.Cells.GridWeb-kontrollen. Det här ämnet diskuterar export av data från Aspose.Cells.GridWeb-kontrollen till en datatabell.

{{% /alert %}} 
## **Exportera kalkylbladsdata**
### **Till en specifik datatabell**
Så här exporterar du kalkylbladsdata till ett specifikt DataTable-objekt:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ditt webbformulär.
1. Skapa ett specifikt DataTable-objekt.
1. Exportera data från de markerade cellerna till det angivna DataTable-objektet.

Exemplet nedan skapar ett specifikt DataTable-objekt med fyra kolumner. Kalkylbladsdata exporteras med början från den första cellen med alla rader och kolumner synliga i kalkylbladet, till ett redan skapat DataTable-objekt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportDataTable.cs" >}}
### **Till en ny datatabell**
Ibland vill du inte skapa ett DataTable-objekt utan behöver helt enkelt exportera kalkylbladsdata till ett nytt DataTable-objekt.

Exemplet nedan försöker ett annat sätt att visa användningen av exportmetoden. Den tar referensen till det aktiva kalkylbladet och exporterar hela data från det kalkylbladet till ett nytt DataTable-objekt. DataTable-objektet kan nu användas på vilket sätt du vill. Det är till exempel möjligt att binda DataTable-objektet till en GridView för att se data.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ExportDataTable.aspx-ExportNewDataTable.cs" >}}
