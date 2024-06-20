---
title: الحصول على رقم الإصدار للتطبيق الذي أنشأ مستند Excel
type: docs
weight: 150
url: /ar/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

غالبًا ما تحتاج إلى معرفة رقم الإصدار للتطبيق الذي أنشأ مستند Microsoft Excel. توفر Aspose.Cells الخاصية [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) لهذا الغرض.

{{% /alert %}}

الكود النموذجي التالي يظهر استخدام خاصية [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version). يقوم بتحميل ملفات Excel التي تم إنشاؤها باستخدام Microsoft Excel 2003 و 2007 و 2010 و 2013 ويقوم بطباعة رقم الإصدار للتطبيق الذي أنشأ هذه المستندات في Excel.

للرجوع إليها، إليك إخراج وحدة التحكم الذي ينشئه الكود العينة.

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
