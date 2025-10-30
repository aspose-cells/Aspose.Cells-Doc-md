---
title: Konvertera JSON till CSV med Golang via C++
linktitle: Konvertera JSON till CSV
type: docs
weight: 210
url: /sv/go-cpp/convert-json-to-csv/
description: Lär dig hur man konverterar JSON till CSV med Aspose.Cells for C++ med enkla och inbäddade JSON exempel.
---

## **Konvertera JSON till CSV**

Aspose.Cells stöder konvertering av enkel och inbäddad JSON till CSV. För detta tillhandahåller API:n [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) och [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) klasser. Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) erbjuder val för JSON-layout, som [**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/) (ignorerar titeln om arrayen är en egenskap i ett objekt) eller [**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/) (behandlar arrayen som ett bord). Klassen [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) bearbetar JSON med layoutalternativ som ställts in med klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/).

Följande kodexempel visar användningen av klasserna [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) och [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) för att ladda [käljsonfil](104398869.json) och generera [utdata CSV-fil](104398870.csv).

### **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}
