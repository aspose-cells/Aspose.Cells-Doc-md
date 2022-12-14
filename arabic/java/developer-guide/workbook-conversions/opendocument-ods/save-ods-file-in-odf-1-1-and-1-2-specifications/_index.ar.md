---
title: حفظ ملف ODS في مواصفات ODF 1.1 و 1.2
type: docs
weight: 170
url: /ar/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---
{{% alert color="primary" %}}

Aspose.Cells يدعم الحفظ (**جدول بيانات OpenDocument**) ملف ODS في (**تنسيق OpenDocument** ) مواصفات ODF 1.1 و ODF 1.2. تمت إضافة Aspose.Cells[**OdsSaveOptions.setStrictSchema11 ()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) الخاصية لاستخدام مواصفات ODF 1.1 لحفظ ملفات ODS. القيمة الافتراضية لهذه الخاصية هي**خاطئة**، لذا فإن ملف ODS المحفوظ بدون هذه الإعدادات الخاصة سيستخدم المواصفات 1.2.

{{% /alert %}}

ينشئ نموذج التعليمات البرمجية أدناه كائن المصنف ، ويضيف بعض القيمة في الخلية A1 من ورقة العمل الأولى ثم يحفظ ملف ODS في مواصفات ODF 1.1 و 1.2. بشكل افتراضي ، يتم حفظ ملف ODS في مواصفات ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
