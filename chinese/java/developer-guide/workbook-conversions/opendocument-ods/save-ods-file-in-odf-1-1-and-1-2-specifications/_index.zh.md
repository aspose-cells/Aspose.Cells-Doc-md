---
title: 在ODF 1.1和1.2规范中保存ODS文件
type: docs
weight: 170
url: /zh/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells支持在(OpenDocument Format)ODF 1.1和ODF 1.2规范中保存(OpenDocument Spreadsheet)ODS文件。Aspose.Cells已添加[**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11)属性，用于使用ODF 1.1规范来保存ODS文件。此属性的默认值为**false**，因此未使用此特殊设置保存的ODS文件将使用1.2规范。

{{% /alert %}}

下面的示例代码创建工作簿对象，在第一个工作表的单元A1中添加一些值，然后将ODS文件保存在ODF 1.1和1.2规范中。默认情况下，ODS文件将以ODF 1.2规范保存。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
