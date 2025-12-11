---
title: Convert Excel to NumPy
type: docs
weight: 30
url: /python-net/convert-excel-to-numpy/
description: Convert Excel to NumPy by using Aspose.Cells for Python via .NET API.
keywords: Python Convert Excel to NumPy array, Export Workbook to NumPy array in Python via .NET, Python Convert Row to NumPy array, Python Convert Table to NumPy array, Export ListObject to NumPy array in Python via .NET, Python Convert Range to NumPy array, Column to NumPy array using Python.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction to NumPy**
NumPy (Numerical Python) is an open‑source numerical computation extension of Python. This tool can be used to store and process large matrices, which is much more efficient than Python's nested list structure (which can also be used to represent matrices). It supports a large number of dimensional arrays and matrix operations, and also provides a large number of mathematical function libraries for array operations. 

The main functions of NumPy:
1. Ndarray, a multidimensional array object, is a fast, flexible, and space‑saving data structure.
1. Linear algebra operations, including matrix multiplication, transposition, inversion, etc.
1. Fourier transform, performing a fast Fourier transform on an array.
1. Fast operation of floating‑point arrays.
1. Integrate C language code into Python to make it run faster.

Using Aspose.Cells for Python via .NET API, you can convert Excel, TSV, CSV, JSON and many different formats to NumPy ndarray.

## **How to Convert Excel Workbook to NumPy ndarray**
Here's an example code snippet to demonstrate how to export Excel data to a NumPy array using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Traverse Excel data and export data to NumPy ndarray using Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

The output result:
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['Philadelphia' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **How to Convert Worksheet to NumPy ndarray**
Here's an example code snippet to demonstrate how to export worksheet data to NumPy ndarray using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Convert worksheet data to NumPy ndarray using Aspose.Cells for Python via .NET Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

The output result:
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```

## **How to Convert a Range of Excel to a NumPy ndarray**
Here's an example code snippet to demonstrate how to export range data to NumPy ndarray using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Create the range.
1. Convert range data to NumPy ndarray using Aspose.Cells for Python via .NET Excel library.

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
1. Create a ListObject.
1. Convert ListObject data to NumPy ndarray using Aspose.Cells for Python via .NET Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

The output result:
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **How to Convert a Row of Excel to NumPy ndarray**
Here's an example code snippet to demonstrate how to export row data to NumPy ndarray using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Get the row object by row index.
1. Convert row data to NumPy ndarray using Aspose.Cells for Python via .NET Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

The output result:
```
['Detroit' 'Central' '3074']
```

## **How to Convert a Column of Excel to NumPy ndarray**
Here's an example code snippet to demonstrate how to export column data to NumPy ndarray using Aspose.Cells for Python via .NET:
1. Load the [sample file](sample_data.xlsx).
1. Get the first worksheet.
1. Get the column object by column index.
1. Convert column data to NumPy ndarray using Aspose.Cells for Python via .NET Excel library.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

The output result:
```
['Store' '3055' '3036' '3074']
```
{{< app/cells/assistant language="python-net" >}}
