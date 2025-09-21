---
title: Convert JSON to CSV with Golang via C++
linktitle: Convert JSON to CSV
type: docs
weight: 210
url: /go-cpp/convert-json-to-csv/
description: Learn how to convert JSON to CSV using Aspose.Cells for C++ with simple and nested JSON examples.
---

## **Convert JSON to CSV**

Aspose.Cells supports converting simple as well as nested JSON to CSV. For this, the API provides [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) and [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) classes. The [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) class provides the options for JSON layout like [**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/)(ignores the title if the array is a property of an object) or [**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/)(processes the array as a table). The [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) class processes the JSON using the layout options set with the [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) class.

The following code sample demonstrates the use of [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) and [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) classes to load the [source JSON file](104398869.json) and generates the [output CSV file](104398870.csv).

### **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}