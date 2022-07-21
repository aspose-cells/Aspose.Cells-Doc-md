---
title: Convert JSON to CSV
type: docs
weight: 160
url: /java/convert-json-to-csv/
---

Aspose.Cells supports converting simple as well as nested JSON to CSV. For this, the API provides [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) and [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) classes. The [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) class provides the options for JSON layout like [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(ignores the title if the array is a property of an object) or [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(processes the array as a table). The [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) class processes the JSON using the layout options set with the [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) class.

The following code sample demonstrates the use of [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) and [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) classes to load the [source JSON file](SampleJson.json) and generates the [output CSV file](SampleJson_out.csv).

## Sample Code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
