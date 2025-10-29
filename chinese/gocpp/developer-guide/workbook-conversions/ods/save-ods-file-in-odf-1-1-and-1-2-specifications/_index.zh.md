---
title: 使用 Golang 通过 C++ 将 ODS 文件保存为符合 ODF 1.1、1.2 和 1.3 规范的文件
linktitle: 以 ODF 1.1、1.2 和 1.3 版本保存
description: 使用 Aspose.Cells 和 C++ 将 Excel 转换为符合 ODF 1.1、1.2 和 1.3 规范的文件。
type: docs
weight: 230
url: /zh/go-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

 Aspose.Cells 支持将 ODS 文件（**OpenDocument Spreadsheet**）保存为符合 ODF（**OpenDocument Format**） 1.1、1.2 和 1.3 规格的文件。Aspose.Cells 有 [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/go-cpp/odssaveoptions/getodfstrictversion/) 属性，用于指定保存 ODS 文件的 ODF 版本。该属性默认值为 [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/)，因此未设置此属性保存的 ODS 文件默认使用 1.2 规范。

{{% /alert %}}

 以下示例代码创建了一个工作簿对象，向第一个工作表的单元格 A1 添加了一些值，然后以 ODF 1.1、1.2 和 1.3 规范保存 ODS 文件。默认情况下，ODS 文件以 ODF 1.2 规范保存。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveOdsFileInOdf11And12Specifications.go" >}}
