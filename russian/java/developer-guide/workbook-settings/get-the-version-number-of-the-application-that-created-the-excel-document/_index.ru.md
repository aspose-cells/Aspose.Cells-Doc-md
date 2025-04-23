---
title: Получить номер версии приложения, создавшего документ Excel
type: docs
weight: 150
url: /ru/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Часто вам нужно знать номер версии приложения, создавшего документ Microsoft Excel. Aspose.Cells предоставляет свойство [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) для этой цели.

{{% /alert %}}

Следующий образец кода демонстрирует использование свойства [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version). Он загружает файлы Excel, созданные в Microsoft Excel 2003, 2007, 2010 и 2013, и выводит номер версии приложения, создавшего эти документы Excel.

Для вашего ориентира ниже приведен вывод консоли образца кода.

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
