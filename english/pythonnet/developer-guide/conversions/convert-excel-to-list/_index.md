---
title: Convert Excel to List
type: docs
weight: 30
url: /python-net/convert-excel-to-list/
description: Convert Excel to List by using Aspose.Cells for Python via .NET API.
keywords: Convert Excel to List Using Python Excel Library, Convert Workbook to List Using Python Excel Library, Convert Row object to List Using Python Excel Library, Convert COlumn Object to List Using Python Excel Library, Convert Range to List Using Python Excel Library, Convert Worksheet to List Using Python Excel Library.
---

{{% alert color="primary" %}}

Using Aspose.Cells for Python via .NET API, you can convert Workbook, Worksheet, Range, Row, Column and other excel data to Python list.

{{% /alert %}}

## **How to Convert Workbook to List**
Here's an example code snippet to demonstrate how to export excel data to list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Traverse all worksheets and convert workbook to list using Aspose.Cells for Python Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

The output result:
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055], ['New York', 'East', 3090]]]
```

## **How to Convert Worksheet to List**
Here's an example code snippet to demonstrate how to export worksheet data to list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Convert worksheet data to list using Aspose.Cells for Python Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

The output result:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **How to Convert Row to List**
Here's an example code snippet to demonstrate how to export Row data to list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Get Row object by row index.
1. Convert Row data to list using Aspose.Cells for Python Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

The output result:
```
['Chicago', 'Central', 3055]
```

## **How to Convert Column to List**
Here's an example code snippet to demonstrate how to export Column data to list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Get Column object by column index.
1. Convert Column data to list using Aspose.Cells for Python Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

The output result:
```
['Region', 'Central', 'East', 'Central']
```

## **How to Convert Range to List**
Here's an example code snippet to demonstrate how to export worksheet data to list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Create the Range.
1. Convert Range data to list using Aspose.Cells for Python Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

The output result:
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```