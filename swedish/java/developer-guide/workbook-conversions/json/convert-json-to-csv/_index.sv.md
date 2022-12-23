---
title: Konvertera JSON till CSV
type: docs
weight: 160
url: /sv/java/convert-json-to-csv/
---
Aspose.Cells stöder konvertering av såväl enkla som kapslade JSON till CSV. För detta tillhandahåller API[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)och[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)klasser. De[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)klass ger alternativen för JSON layout som[**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(ignorerar titeln om arrayen är en egenskap hos ett objekt) eller[**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(behandlar arrayen som en tabell). De[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)klass bearbetar JSON med hjälp av layoutalternativen som ställts in med[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)klass.

Följande kodexempel visar användningen av[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)och[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)klasser för att ladda[källfil JSON](SampleJson.json)och genererar[utgång CSV fil](SampleJson_out.csv).

## Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
