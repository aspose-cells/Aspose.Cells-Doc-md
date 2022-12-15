---
title: Konvertera JSON till CSV
type: docs
weight: 210
url: /sv/net/convert-json-to-csv/
---
## **Konvertera JSON till CSV**

Aspose.Cells stöder konvertering av enkel såväl som kapslad JSON till CSV. För detta tillhandahåller API**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)** och**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** klasser. De**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**klass ger alternativen för JSON-layout som**[IgnoreArrayTitle](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**(ignorerar titeln om arrayen är en egenskap hos ett objekt) eller**[ArrayAsTable](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)**(behandlar arrayen som en tabell). De**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**klass bearbetar JSON med hjälp av layoutalternativen som ställts in med**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**klass.

Följande kodexempel visar användningen av**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**och**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**klasser för att ladda[käll JSON-fil](104398869.json) och genererar[utdata CSV-fil](104398870.csv).

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
