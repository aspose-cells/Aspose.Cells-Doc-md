---
title: 用 Golang 通过 C++ 将工作簿保存为严格的 Open XML 电子表格格式。
linktitle: 将工作簿保存为严格的 Open XML 电子表格格式
type: docs
weight: 150
url: /zh/go-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: 了解如何使用Aspose.Cells for C++将工作簿保存为严格Open XML电子表格格式。
---

## **可能的使用场景**

Aspose.Cells允许你将工作簿保存为*严格Open XML电子表格*格式。为此，它提供了 [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/) 属性。如果将其值设置为 [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/)，那么输出的Excel文件将以严格Open XML电子表格格式保存。

## **将工作簿保存为严格的 Open XML 电子表格格式**

以下示例代码创建一个工作簿，并将 [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/) 属性值设为 [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/)，然后保存为 [输出Excel文件](67338272.xlsx)。如果你在Microsoft Excel中打开输出的Excel文件，选择另存为...，你将看到其格式为*严格Open XML电子表格*，如下截图所示。

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookToStrictOpenXmlSpreadsheetFormat.go" >}}
