---
title: احصل على رقم إصدار التطبيق الذي أنشأ مستند Excel
type: docs
weight: 150
url: /ar/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---
{{% alert color="primary" %}}

 غالبًا ما تحتاج إلى معرفة رقم إصدار التطبيق الذي أنشأ مستند Excel Microsoft. يوفر Aspose.Cells ملف[**Workbook.getBuiltInDocumentProperties (). getVersion ()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) خاصية لهذا الغرض.

{{% /alert %}}

 يوضح نموذج التعليمات البرمجية التالي استخدام[**Workbook.getBuiltInDocumentProperties (). getVersion ()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)منشأه. يقوم بتحميل ملفات Excel التي تم إنشاؤها باستخدام Microsoft Excel 2003 و 2007 و 2010 و 2013 ويطبع رقم إصدار التطبيق الذي أنشأ مستندات Excel هذه.

كمرجع لك ، يوجد أدناه إخراج وحدة التحكم الذي ينشئه نموذج التعليمات البرمجية.

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
