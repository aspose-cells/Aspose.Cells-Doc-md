---
title: Konvertera JSON till CSV
type: docs
weight: 210
url: /sv/net/convert-json-to-csv/
---

## **Konvertera JSON till CSV**

Aspose.Cells stödjer konvertering av enkel såväl som inbäddad JSON till CSV. För detta tillhandahåller API:et [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) och [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)-klasserna. [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)-klassen ger alternativ för JSON-layout som [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)(ignorerar titeln om arrayen är en egenskap till ett objekt) eller [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)(behandlar arrayen som en tabell). [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)-klassen bearbetar JSON med de layoutalternativ som är inställda med [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)-klassen.

Följande kodexempel demonstrerar användningen av [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) och [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) klasser för att läsa in den [ursprungliga JSON-filen](104398869.json) och generera [utdata-CSV-filen](104398870.csv).

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
