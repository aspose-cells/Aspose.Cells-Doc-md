---
title: 获取创建Excel文档的应用程序的版本号
type: docs
weight: 150
url: /zh/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

通常需要知道创建Microsoft Excel文档的应用程序的版本号。Aspose.Cells提供了[**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)属性以实现此目的。

{{% /alert %}}

以下示例代码演示了[**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)属性的使用。它加载由Microsoft Excel 2003、2007、2010和2013创建的Excel文件，并打印创建这些Excel文档的应用程序的版本号。

作为参考，以下是示例代码创建的控制台输出。

{{< highlight java >}}

Excel 2003 XLS Version: 726502

Excel 2007 XLS Version: 786432

Excel 2010 XLS Version: 917504

Excel 2013 XLS Version: 983040

Excel 2007 XLSX Version: 12.0000

Excel 2010 XLSX Version: 14.0300

Excel 2013 XLSX Version: 15.0300

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetVersionNumberofApplication-GetVersionNumberofApplication.java" >}}
{{< app/cells/assistant language="java" >}}
