---
title: 在ODF 1.1和1.2规范中保存ODS文件
type: docs
weight: 170
url: /zh/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells支持使用ODF 1.1规范和ODF 1.2规范保存（**OpenDocument Format**）ODS文件。Aspose.Cells已经添加了[**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11)属性以使用ODF 1.1规范保存ODS文件。此属性的默认值为**false**，因此未使用此特殊设置保存的ODS文件将使用1.2规范。

{{% /alert %}}

下面的示例代码创建工作簿对象，在第一个工作表的A1单元格中添加一些值，然后按照ODF 1.1和1.2规范保存ODS文件。默认情况下，ODS文件保存在ODF 1.2规范中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
