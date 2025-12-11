---
title: Convert Excel to Python Data
type: docs
weight: 30
url: /python-net/convert-excel-to-list/
description: Convert Excel to List by using Aspose.Cells for Python via .NET API.
keywords: Convert Excel to Dictionary Using Python Excel Library, Convert Workbook to Dictionary Using Python Excel Library, Convert Row object to List Using Python Excel Library, How to Convert ListObject to List, Convert Column Object to List Using Python Excel Library, Convert Range to List Using Python Excel Library, Convert Worksheet to List Using Python Excel Library.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Using Aspose.Cells for Python via .NET API, you can convert Workbook, Worksheet, Range, Row, Column and other Excel data to Python lists.

{{% /alert %}}

## **How to Convert Excel Workbook to Dictionary**
Here's an example code snippet to demonstrate how to export Excel data to a dictionary using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Traverse all worksheets and convert the workbook to a dictionary using Aspose.Cells for Python via .NET library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

The output result:
```python
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]],
 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['Philadelphia', 'East', 3082], ['Detroit', 'Central', 3074]],
 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **How to Convert Excel Workbook to List**
Here's an example code snippet to demonstrate how to export Excel data to a list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Traverse all worksheets and convert the workbook to a list using Aspose.Cells for Python via .NET library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

The output result:
```python
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]],
 [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['Philadelphia', 'East', 3082], ['Detroit', 'Central', 3074]],
 [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]]
```

## **How to Convert Worksheet to List**
Here's an example code snippet to demonstrate how to export worksheet data to a list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Convert worksheet data to a list using Aspose.Cells for Python via .NET library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

The output result:
```python
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **How to Convert a ListObject of Excel to List**
Here's an example code snippet to demonstrate how to export ListObject data to a list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Create a ListObject.
1. Convert ListObject data to a list using Aspose.Cells for Python via .NET library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

The output result:
```python
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **How to Convert a Row of Excel to List**
Here's an example code snippet to demonstrate how to export Row data to a list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Get the Row object by row index.
1. Convert Row data to a list using Aspose.Cells for Python via .NET library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

The output result:
```python
['Detroit', 'Central', 3074]
```

## **How to Convert a Column of Excel to List**
Here's an example code snippet to demonstrate how to export Column data to a list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Get the Column object by column index.
1. Convert Column data to a list using Aspose.Cells for Python via .NET library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

The output result:
```python
['Store', 3055, 3036, 3074]
```

## **How to Convert a Range of Excel to List**
Here's an example code snippet to demonstrate how to export range data to a list using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Create the Range.
1. Convert Range data to a list using Aspose.Cells for Python via .NET library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

The output result:
```python
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
{{< app/cells/assistant language="python-net" >}}
