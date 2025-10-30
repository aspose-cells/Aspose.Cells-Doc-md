---
title: Få cellerindex
type: docs
weight: 600
url: /sv/nodejs-cpp/get-cells-index/
description: Lär dig hur man får rad eller kolumn genom namnet på raden, kolumnen eller cellerna. Konvertera namnet på cellen till rad och kolumnindex nollbaserat.
keywords: Få radindex och kolumnindex efter namnet på cellen, Få kolumnindex efter namnet på kolumnen, Få radindex efter namnet på raden, Få index efter namnet på cellen. 
---

{{% alert color="primary" %}}
Standardvyn i Excel är A1-stilreferens, där varje kolumn är definierad som A, B, C ... och cellerna namnges som A1, B2, C3 ... och så vidare.
Du kan vilja veta vilken rad och kolumn är denna cell i.

{{% /alert %}}


## **Möjliga användningsscenario**
När du bara behöver manipulera en specifik data på arbetsbladet genom rad- och kolumnindex behöver du veta kolumn- och kolumnindex för den specifika cellen. 
Aspose.Cells for Node.js via C++ erbjuder denna funktion för att få rad- och kolumnindex efter namnet på raden, kolumnen och cellen. 
Aspose.Cells for Node.js via C++ tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

Obs: Indextypen är nollbaserad i Aspose.Cells for Node.js via C++, men id för rad är ettbaserat i MS Excel.

## **Hämta cellernas index med Aspose.Cells for Node.js via C++**
Detta exempel visar hur man:

1. Skapa en arbetsbok och lägg till lite data.
1. Hitta den specifika cellen i det första arbetsbladet.
1. Få radindex och kolumnindex efter namnet på cellen.
1. Få kolumnindex efter namnet på kolumnen.
1. Få radindex efter namnet på raden.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
