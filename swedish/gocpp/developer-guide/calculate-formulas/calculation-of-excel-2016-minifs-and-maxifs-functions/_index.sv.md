---
title: Beräkning av Excel 2016 MINIFS och MAXIFS funktioner med Golang via C++
description: Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att beräkna MINIFS och MAXIFS funktioner i Microsoft Excel 2016 med C++.
keywords: Aspose.Cells, Excel, 2016, MINIFS funktion, MAXIFS funktion, beräkning
type: docs
weight: 300
url: /sv/go-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Möjliga användningsscenario**
Microsoft Excel 2016 stöder MINIFS och MAXIFS funktioner. Dessa funktioner stöds inte i Excel 2013 eller tidigare versioner. Aspose.Cells stöder också beräkning av dessa funktioner. Följande skärmdump illustrerar användningen av dessa funktioner. Läs de röda kommentarerna i skärmbilden för att förstå hur dessa funktioner fungerar.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Beräkning av Excel 2016 MINIFS och MAXIFS funktioner**
Följande exempelkod laddar [exempel excel filen](5115149.xlsx) och anropar [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) metoden för att utföra formelberäkningen via Aspose.Cells och sparar sedan resultaten i [utgångs PDF](5115154.pdf).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfExcel2016MinifsAndMaxifsFunctions.go" >}}
