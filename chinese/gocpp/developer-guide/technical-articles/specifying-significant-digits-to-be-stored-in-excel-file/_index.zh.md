---
title: 使用Golang通过C++在Excel文件中指定要存储的有效数字
linktitle: 指定有效数字
type: docs
weight: 30
url: /zh/go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: 学习如何使用Golang通过C++结合Aspose.Cells指定在Excel文件中存储的有效数字。
---

## **可能的使用场景**

默认情况下，Aspose.Cells在Excel文件中存储双精度数值时保留17位有效数字，不同于MS-Excel只存储15位有效数字。你可以使用[**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/)属性将Aspose.Cells的默认行为从17位改为15位。

## **指定要在Excel文件中存储的有效数字**

以下示例代码在将双精度值存储到Excel文件时强制使用15位有效数字。请检查[输出Excel文件](22774105.xlsx)，将其扩展名改为.zip并解压，即可见文件只存储了15位有效数字。下方截图说明[**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/)属性对输出文件的影响。

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}
