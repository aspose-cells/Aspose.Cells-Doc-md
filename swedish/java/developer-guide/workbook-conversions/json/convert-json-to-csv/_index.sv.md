---
title: Konvertera JSON till CSV
type: docs
weight: 160
url: /sv/java/convert-json-to-csv/
---

Aspose.Cells stöder konvertering av enkla såväl som inbäddade JSON till CSV. För detta tillhandahåller API:et klasserna [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) och [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). Klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) tillhandahåller alternativ för JSON-layout som [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle) (ignorerar titeln om arrayen är en egenskap hos ett objekt) eller [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable) (behandlar arrayen som en tabell). Klassen [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) behandlar JSON med användning av layoutalternativen som är inställda med hjälp av klassen [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions).

Följande kodexempel visar användningen av klasserna [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) och [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) för att ladda [käll-JSON-filen](SampleJson.json) och genererar [utdata-CSV-filen](SampleJson_out.csv).

## Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
