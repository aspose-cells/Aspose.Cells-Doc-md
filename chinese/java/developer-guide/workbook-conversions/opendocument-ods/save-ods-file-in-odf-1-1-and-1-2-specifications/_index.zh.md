---
title: 以 ODF 1.1、1.2 和 1.3 规范保存ODS文件
type: docs
weight: 170
url: /zh/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells支持将（**OpenDocument Spreadsheet**）ODS文件保存为（**OpenDocument Format**）符合ODF 1.1、1.2和 1.3 规范。Aspose.Cells已添加 [**OdsSaveOptions.setOdfStrictVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions/#setOdfStrictVersion-int-) 属性，用于指定保存的ODF版本。此属性的默认值为 [**OpenDocumentFormatVersionType.ODF_12**](https://reference.aspose.com/cells/java/com.aspose.cells/opendocumentformatversiontype/#ODF-12)，因此未进行特殊设置的ODS文件将使用1.2规范。

{{% /alert %}}

下面的示例代码创建工作簿对象，在第一个工作表的A1单元格中添加一些值，然后按照ODF 1.1和1.2规范保存ODS文件。默认情况下，ODS文件保存在ODF 1.2规范中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
{{< app/cells/assistant language="java" >}}
