---
title: Använda FormelText funktionen i Aspose.Cells med Golang via C++
linktitle: Använda FormelText funktionen
description: Denna artikel introducerar hur man använder FormulaText funktionen i Aspose.Cells biblioteket för att bearbeta formler i Microsoft Excel. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda metoden som tillhandahålls av Aspose.Cells för att få och ställa in formeltexten för cellen och få resultatet. Till slut sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, FormulaText funktioner
type: docs
weight: 60
url: /sv/go-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText är en funktion i Excel 2013 och senare. Den stöds inte av tidigare versioner som Excel 2010 eller 2007 etc. Som namnet antyder skriver den ut texten i formeln som finns i en given cell. Den här artikeln kommer att visa dig hur du använder den här funktionen med Aspose.Cells.

{{% /alert %}} 

Följande exempelkod visar användningen av FormulaText med Aspose.Cells. Koden skriver först en formel i cell A1 och skriver sedan ut texten för formeln med FormulaText i cell A2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingFormulatextFunctionInAsposeCells.go" >}}
## **Konsoloutput**
Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
