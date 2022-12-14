---
title: Importera DataView till GridWeb
type: docs
weight: 60
url: /sv/net/import-dataview-to-gridweb/
---
{{% alert color="primary" %}} 

Med lanseringen av Microsoft .NET Framework introducerades ett nytt sätt att lagra data. Nu DataSet, DataTable och DataView objekt som lagrar data i offlineläge. Dessa objekt är mycket praktiska som datalager. Med Aspose.Cells.GridWeb är det möjligt att importera data från antingen DataTable- eller DataView-objekt till kalkylblad. Aspose.Cells.GridWeb stöder endast import av data från en DataView. objekt men ett DataTable-objekt kan också användas indirekt. Låt oss diskutera denna funktion i detalj.

{{% /alert %}} 
## **Importera data från DataView**
Importera data från ett DataView-objekt med hjälp av GridWorsheetCollections ImportDataView-metod i GridWeb-kontrollen. Skicka DataView-objektet som du vill importera data från till ImportDataView-metoden. Det är möjligt att ange kolumnrubrik och datastilar under import.

{{% alert color="primary" %}} 

När data importeras från ett DataView-objekt skapas ett nytt kalkylblad för att hålla den importerade datan. Arbetsbladet har samma namn som DataTable.

{{% /alert %}} 

**Utdata: Data importeras från en DataView till ett nytt kalkylblad** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

 Bredden på kolumnerna justeras för att visa all data de innehåller. När data importeras från DataView justeras inte kolumnbredderna automatiskt. Användare måste justera dem själva. För att justera kolumnbredderna programmatiskt, se[Ändra storlek på rader och kolumner](/cells/sv/net/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

En överbelastad version av ImportDataView-metoden tillåter utvecklare att ange namnet på arket som innehåller de importerade data och ett specifikt antal rader och kolumner som ska importeras från DataView-objektet.

{{% /alert %}}
