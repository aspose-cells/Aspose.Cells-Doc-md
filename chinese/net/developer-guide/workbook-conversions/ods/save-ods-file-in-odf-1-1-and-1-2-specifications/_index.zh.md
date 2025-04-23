---
title: 将ODS文件保存为ODF 1.1、1.2和1.3规范
linktitle: 以ODF 1.1、1.2和1.3保存
description: 使用Aspose.Cells转换Excel为ODF 1.1、1.2和1.3规范。
type: docs
weight: 230
url: /zh/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

 Aspose.Cells 支持将 ODS 文件（**OpenDocument Spreadsheet**）保存为符合 ODF（**OpenDocument Format**） 1.1、1.2 和 1.3 规格的文件。Aspose.Cells 有 [**OdsSaveOptions.OdfStrictVersion**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/odfstrictversion/) 属性，用于指定保存 ODS 文件的 ODF 版本。该属性默认值为 [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/net/aspose.cells.ods/opendocumentformatversiontype/)，因此未设置此属性保存的 ODS 文件默认使用 1.2 规范。

{{% /alert %}}

 以下示例代码创建了一个工作簿对象，向第一个工作表的单元格 A1 添加了一些值，然后以 ODF 1.1、1.2 和 1.3 规范保存 ODS 文件。默认情况下，ODS 文件以 ODF 1.2 规范保存。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
{{< app/cells/assistant language="csharp" >}}
