---
title: Convert JSON to CSV
type: docs
weight: 210
url: /net/convert-json-to-csv/
---

## **Convert JSON to CSV**

Aspose.Cells supports converting simple as well as nested JSON to CSV. For this, the API provides [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) and [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) classes. The [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) class provides the options for JSON layout like [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)(ignores the title if the array is a property of an object) or [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)(processes the array as a table). The [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) class processes the JSON using the layout options set with the [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) class.

The following code sample demonstrates the use of [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) and [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) classes to load the [source JSON file](104398869.json) and generates the [output CSV file](104398870.csv).

### **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
