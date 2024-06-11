---
title: 在ODF 1.1和1.2规范中保存ODS文件
linktitle: 保存为ODF 1.1和1.2 
description: 使用Aspose.Cells将Excel转换为ODF 1.1和1.2规范。
type: docs
weight: 230
url: /zh/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells支持在ODF（OpenDocument Format）1.1和1.2规范中保存ODS文件（OpenDocument Spreadsheet）。 Aspose.Cells具有[**OdsSaveOptions.IsStrictSchema11**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/properties/isstrictschema11)属性，该属性指定保存ODS文件时使用ODF 1.1规范。 此属性的默认值为**false**，因此未使用此设置保存的ODS文件使用1.2规范。

{{% /alert %}}

下面的示例代码创建一个工作簿对象，在第一个工作表的单元A1中添加一些值，然后以ODF 1.1和1.2规范保存ODS文件。默认情况下，ODS文件以ODF 1.2规范保存。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
