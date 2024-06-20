---
title: Importera DataView till GridWeb
type: docs
weight: 60
url: /sv/net/aspose-cells-gridweb/import-dataview-to-gridweb/
keywords: GridWeb, import
description: Den här artikeln introducerar hur man importerar data i GridWeb.
---

{{% alert color="primary" %}} 

Med frisläppandet av Microsoft .NET Framework introducerades ett nytt sätt att lagra data. Nu finns DataSet-, DataTable- och DataView-objekt som lagrar data i offline-läge. Dessa objekt är mycket praktiska som datarepositories. Med Aspose.Cells.GridWeb är det möjligt att importera data från antingen DataTable- eller DataView-objekt till kalkylblad. Aspose.Cells.GridWeb stöder endast import av data från ett DataView-objekt, men ett DataTable-objekt kan också användas indirekt. Låt oss diskutera den här funktionen i detalj.

{{% /alert %}} 
## **Importera data från DataView**
Importera data från ett DataView-objekt med hjälp av GridWorsheetCollectionns ImportDataView-metod i GridWeb-kontrollen. Skicka DataView-objektet som du vill importera data från till ImportDataView-metoden. Det är möjligt att specificera kolumnrubrik och datastilar vid import.

{{% alert color="primary" %}} 

När data importeras från ett DataView-objekt skapas ett nytt kalkylblad för att hålla den importerade datan. Kalkylbladet har samma namn som DataTable.

{{% /alert %}} 

**Utmatning: Data importerad från ett DataView till ett nytt kalkylblad** 

![todo:image_alt_text](import-dataview-to-gridweb_1.png)

Kolumnbredderna justeras för att visa all den data de innehåller. När data importeras från DataView justeras inte kolumnbredderna automatiskt. Användarna behöver justera dem själva. För att justera kolumnbredderna programmatiskt, se [Ändra storlek på rader och kolumner](/cells/sv/net/aspose-cells-gridweb/resize-rows-and-columns/).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ImportDataView.aspx-ImportDataView.cs" >}}

{{% alert color="primary" %}} 

En överbelastad version av ImportDataView-metoden tillåter utvecklare att specificera namnet på arket som håller den importerade datan och ett specifikt antal rader och kolumner att importera från DataView-objektet.

{{% /alert %}}
