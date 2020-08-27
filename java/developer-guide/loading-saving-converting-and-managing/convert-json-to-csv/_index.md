---
title: Convert JSON to CSV
type: docs
weight: 160
url: /java/convert-json-to-csv/
---

Aspose.Cells supports converting simple as well as nested JSON to CSV. For this, the API provides [**JsonLayoutOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) and [**JsonUtility**](https://apireference.aspose.com/cells/java/com.aspose.cells/JsonUtility) classes. The [**JsonLayoutOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) class provides the options for JSON layout like [**IgnoreArrayTitle**](https://apireference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(ignores the title if the array is a property of an object) or [**ArrayAsTable**](https://apireference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(processes the array as a table). The [**JsonUtility**](https://apireference.aspose.com/cells/java/com.aspose.cells/JsonUtility) class processes the JSON using the layout options set with the [**JsonLayoutOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) class.

The following code sample demonstrates the use of [**JsonLayoutOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) and [**JsonUtility**](https://apireference.aspose.com/cells/java/com.aspose.cells/JsonUtility) classes to load the [source JSON file](SampleJson.json) and generates the [output CSV file](SampleJson_out.csv).

## Sample Code

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
