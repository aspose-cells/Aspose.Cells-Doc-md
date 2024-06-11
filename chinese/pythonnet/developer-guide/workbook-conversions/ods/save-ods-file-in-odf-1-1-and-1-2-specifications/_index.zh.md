---
title: 在ODF 1.1和1.2规范中保存ODS文件
linktitle: 保存为ODF 1.1和1.2 
description: 使用Aspose.Cells将Excel转换为ODF 1.1和1.2规范。
type: docs
weight: 230
url: /zh/python-net/save-ods-file-in-odf-1-1-and-1-2-specifications/
description: 如何使用Aspose.Cells for Python via .NET API保存ODS文件在ODF 1.1和1.2规范中。
keywords: Python保存ODS文件至ODF 1.1和1.2规范，将ODS文件保存至ODF 1.1和1.2规范，Python via NET。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET支持在ODF（OpenDocument Format）1.1和1.2规范中保存ODS文件（OpenDocument电子表格）。Aspose.Cells for Python via .NET具有[**OdsSaveOptions.is_strict_schema11**](https://reference.aspose.com/cells/python-net/aspose.cells/odssaveoptions/is_strict_schema11/)属性，用于指定保存ODS文件时使用ODF 1.1规范。此属性的默认值为**false**，因此没有设置的ODS文件使用1.2规范保存。

{{% /alert %}}

下面的示例代码创建一个工作簿对象，在第一个工作表的单元A1中添加一些值，然后以ODF 1.1和1.2规范保存ODS文件。默认情况下，ODS文件以ODF 1.2规范保存。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.py" >}}
