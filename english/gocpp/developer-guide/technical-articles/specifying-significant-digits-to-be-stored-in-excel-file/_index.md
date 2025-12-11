---
title: Specifying Significant Digits to be Stored in Excel File with Golang via C++
linktitle: Specifying Significant Digits
type: docs
weight: 30
url: /go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Learn how to specify significant digits to be stored in Excel files using Aspose.Cells with Golang via C++.
---

## **Possible Usage Scenarios**

By default, Aspose.Cells stores 17 significant digits of double values inside the Excel file, unlike MS-Excel which stores only 15 significant digits. You can change the default behavior of Aspose.Cells from 17 significant digits to 15 significant digits using the [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) property.

## **Specifying Significant Digits to Be Stored in an Excel File**

The following sample code forces Aspose.Cells to use 15 significant digits while storing double values inside the Excel file. Please check the [output Excel file](22774105.xlsx). Change its extension to .zip, unzip it, and you will see that only 15 significant digits are stored in the Excel file. The following screenshot explains the effect of the [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) property on the output Excel file.

![Screenshot showing 15 significant digits stored in the Excel file](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}