---
title: Convert Excel to NumPy
type: docs
weight: 30
url: /python-net/convert-excel-to-numpy/
description: Convert Excel to NumPy by using Aspose.Cells for Python via .NET API.
keywords: Python Convert Excel to NumPy array, Export Excel to NumPy array in Python via NET, Python Convert xlsx to  NumPy array, Excel to NumPy array using Python.
---

{{% alert color="primary" %}}

Using Aspose.Cells for Python via .NET API, you can convert Excel, TSV, CSV, Json and many different formats to Numpy data.


{{% /alert %}}

## **Convert Excel Workbook to NumPy ndarray**
Here's an example code snippet to demonstrate how to export excel data to a NumPy array using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Traverse excel data and export data to NumPy ndarray using Aspose.Cells for Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

The output result:
```
['City' 'Region' 'Store' 'Chicago' 'Central' '3055' 'New York' 'East'
 '3036' 'Detroit' 'Central' '3074' 'City2' 'Region2' 'Store3' 'Seattle'
 'West' '3000' 'philadelph' 'East' '3082' 'Detroit' 'Central' '3074'
 'City3' 'Region3' 'Store3' 'Seattle' 'West' '3166' 'New York' 'East'
 '3090' 'Chicago' 'Central' '3055' 'New York' 'East' '3090']
```

## **How to Convert Worksheet to NumPy ndarray**
Here's an example code snippet to demonstrate how to export worksheet data to Numpy ndarray using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Convert worksheet data to Numpy ndarray using Aspose.Cells for Python Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

The output result:
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **How to Convert a Range of Excel to NumPy ndarray**
Here's an example code snippet to demonstrate how to export range data to NumPy ndarray using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Create the Range.
1. Convert Range data to NumPy ndarray using Aspose.Cells for Python Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

The output result:
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **How to Convert a ListObject of Excel to NumPy ndarray**
Here's an example code snippet to demonstrate how to export ListObject data to NumPy ndarray using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Create ListObject object.
1. Convert ListObject data to NumPy ndarray using Aspose.Cells for Python Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

The output result:
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **How to Convert a Row of Excel to NumPy ndarray**
Here's an example code snippet to demonstrate how to export Row data to NumPy ndarray using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Get Row object by row index.
1. Convert Row data to NumPy ndarray using Aspose.Cells for Python Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

The output result:
```
['Detroit' 'Central' '3074']
```

## **How to Convert a Column of Excel to NumPy ndarray**
Here's an example code snippet to demonstrate how to export Column data to NumPy ndarray using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Get Column object by column index.
1. Convert Column data to NumPy ndarray using Aspose.Cells for Python Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

The output result:
```
['Store' '3055' '3036' '3074']
```