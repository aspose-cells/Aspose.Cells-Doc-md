---
title: Omvandling mellan cellnamn och rad/kolumnindex
linktitle: Cellnamn och Index Omvandling
type: docs
weight: 5
url: /sv/java/names-and-indices/
description: Lär dig hur man får omvandlingsresultat mellan cellnamn och rad/kolumnindex med Aspose.Cells for Java API er.
keywords: Java Konvertera cellindex till namn, Konvertera cellnamn till rad/kolumnindex med java api er, Hur man får cellnamn från rad och kolumnindex med java, Java Hur man får rad och kolumnindex från cellnamn.
---

## **Hur man får cellnamn från rad- och kolumnindex**
Det är möjligt att hitta ett cells namn med rad- och kolumnindex. Den här artikeln förklarar hur.

Aspose.Cells tillhandahåller metoden [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) som tillåter utvecklare att få namnet på en cell om de tillhandahåller rad- och kolumnindex.

{{% alert color="primary" %}} 

Microsoft Excel börjar räkna rad- och kolumnindex från 1. Till skillnad från Microsoft Excel börjar Aspose.Cells räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempelkod illustrerar hur man använder [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) för att komma åt cellens namn vid ett känt rad- och kolumnindex. Koden genererar följande utdata.

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Hur man får rad- och kolumnindex från cellnamn**
Det är möjligt att hitta en rad- och kolumnindex för cellen från dess namn. Denna artikel förklarar hur.

Aspose.Cells tillhandahåller metoden [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) som tillåter utvecklare att få rad- och kolumnindex från cellens namn.

{{% alert color="primary" %}} 

Microsoft Excel börjar räkna rad- och kolumnindex från 1. Till skillnad från Microsoft Excel börjar Aspose.Cells räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempelkod illustrerar hur man använder [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) för att få rad- och kolumnindex från cellens namn. Koden genererar följande utdata.

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Hur man skapar säkra kalkylbladsnamn**
Ibland finns det ett behov av att tilldela kalkylbladsnamnet under körningstid. I detta scenario kan det finnas kalkylbladsnamn som kan innehålla vissa ytterligare tecken som <>+(?”. Det finns ett behov av att ersätta sådana tecken, som inte är tillåtna som ett kalkylbladsnamn, med något förinställt tecken som tillhandahålls av användaren. På samma sätt kan längden öka till mer än 31 tecken vilket behöver bli avkortat. Apache POI tillhandahåller vissa funktioner för att skapa säkra namn, därför erbjuds liknande funktion av Aspose.Cells för att hantera alla dessa problem. Följande exempelkod demonstrerar denna funktion:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Konsolutdata**

Det här är det första namnet som skapas

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
