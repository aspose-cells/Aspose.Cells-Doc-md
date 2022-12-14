---
title: Konvertering mellan cellnamn och rad-/kolumnindex
linktitle: Cell Namn och indexkonvertering
type: docs
weight: 5
url: /sv/java/names-and-indices/
---
## **Hämta Cell Namn från rad- och kolumnindex**
Det är möjligt att hitta en cells namn med tanke på rad- och kolumnindex. Den här artikeln förklarar hur.

 Aspose.Cells tillhandahåller[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) metod som tillåter utvecklare att få en cells namn om de tillhandahåller rad- och kolumnindex.

{{% alert color="primary" %}} 

Till skillnad från Microsoft Excel, där rad- och kolumnindexen börjar från 1, börjar Aspose.Cells räkna rad- och kolumnindex från 0.

{{% /alert %}} 

 Följande exempelkod illustrerar hur du använder[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) för att komma åt cellens namn som anges i ett känt rad- och kolumnindex. Koden genererar följande utdata.



Cell Namn på [0, 0]: A1

Cell Namn på [4, 0]: A5

Cell Namn på [0, 4]: E1

Cell Namn på [2, 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Hämta rad- och kolumnindex från Cell Namn**
Det är möjligt att hitta ett rad- och kolumnindex för cellen från dess namn. Den här artikeln förklarar hur.

 Aspose.Cells tillhandahåller[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) metod som låter utvecklare få ett rad- och kolumnindex från cellens namn.

{{% alert color="primary" %}} 

Till skillnad från Microsoft Excel, där rad- och kolumnindexen börjar från 1, börjar Aspose.Cells räkna rad- och kolumnindex från 0.

{{% /alert %}} 

 Följande exempelkod illustrerar hur du använder[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) för att hämta rad- och kolumnindex från cellens namn. Koden genererar följande utdata.



Radindex för Cell C6: 5

Kolumnindex för Cell C6: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Skapa säkra bladnamn**
Ibland finns det ett behov av att tilldela arknamnet vid körning. I det här scenariot kan det finnas arknamn som kan innehålla några ytterligare tecken som<>+(?”. Det finns ett behov av att ersätta alla sådana tecken, som inte är tillåtna som ett arknamn med något förinställt tecken som tillhandahålls av användaren. På samma sätt kan längden öka till mer än 31 tecken som måste trunkeras. Apache POI tillhandahåller vissa funktioner för att skapa säkra namn, därför tillhandahålls liknande funktion av Aspose.Cells för att hantera alla dessa problem. Följande exempelkod visar denna funktion:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Konsolutgång**

detta är förnamn som är cre

` `<> + (adj.Privat _ "Privat"
