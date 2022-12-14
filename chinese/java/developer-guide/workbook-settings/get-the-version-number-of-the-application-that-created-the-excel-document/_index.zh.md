---
title: 获取创建 Excel 文档的应用程序的版本号
type: docs
weight: 150
url: /zh/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---
{{% alert color="primary" %}}

通常您需要知道创建 Microsoft Excel 文档的应用程序的版本号。 Aspose.Cells 提供了[**工作簿.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)为此目的的财产。

{{% /alert %}}

下面的示例代码演示了使用[**工作簿.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)财产。它加载使用 Microsoft Excel 2003、2007、2010 和 2013 创建的 Excel 文件，并打印创建这些 Excel 文档的应用程序的版本号。

供您参考，下面是示例代码创建的控制台输出。

{{< highlight "java" >}}

Excel 2003 XLS Version: 726502

Excel 2007 XLS Version: 786432

Excel 2010 XLS Version: 917504

Excel 2013 XLS Version: 983040

Excel 2007 XLSX Version: 12.0000

Excel 2010 XLSX Version: 14.0300

Excel 2013 XLSX Version: 15.0300

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetVersionNumberofApplication-GetVersionNumberofApplication.java" >}}
