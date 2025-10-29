---
title: الحصول على رقم الإصدار للتطبيق الذي أنشأ مستند Excel
type: docs
weight: 210
url: /ar/python-net/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

غالباً ما تحتاج إلى معرفة رقم إصدار التطبيق الذي أنشأ مستند Microsoft Excel. يوفر Aspose.Cells for Python via .NET الخاصية [**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version) لهذا الغرض.

{{% /alert %}}

الكود النموذجي التالي يظهر استخدام خاصية [**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version). يقوم بتحميل ملفات Excel التي تم إنشاؤها باستخدام Microsoft Excel 2003 و 2007 و 2010 و 2013 ويقوم بطباعة رقم الإصدار للتطبيق الذي أنشأ هذه المستندات في Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-GetApplicationVersion-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
