---
title: Convert JSON to CSV
type: docs
weight: 210
url: /python-net/convert-json-to-csv/
description: Learn how to convert json to csv file with Aspose.Cells for Python via .NET API.
keywords: Python Convert json to csv, Convert json to csv Pyton via NET, Export json to csv, Convert json to csv
---

## **Convert JSON to CSV**

Aspose.Cells for Python via .NET supports converting simple as well as nested JSON to CSV. For this, the API provides [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) and [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) classes. The [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) class provides the options for JSON layout like [**ignore_array_title**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/)(ignores the title if the array is a property of an object) or [**array_as_table**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/)(processes the array as a table). The [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) class processes the JSON using the layout options set with the [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) class.

The following code sample demonstrates the use of [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) and [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) classes to load the [source JSON file](104398869.json) and generates the [output CSV file](104398870.csv).

### **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}
