---
title: حفظ ملف ODS في المواصفات ODF 1.1 و 1.2
type: docs
weight: 170
url: /ar/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

تدعم Aspose.Cells حفظ ملف ODS (OpenDocument Spreadsheet) في مواصفات ODF (OpenDocument Format) 1.1 و ODF 1.2. وقد أضافت Aspose.Cells خاصية [**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) لاستخدام مواصفات ODF 1.1 لحفظ ملفات ODS. القيمة الافتراضية لهذه الخاصية هي false، لذلك ستحفظ ملفات ODS بدون هذه الإعدادات الخاصة باستخدام المواصفات 1.2.

{{% /alert %}}

الكود العينة أدناه ينشئ كائن الدفتر، يضيف بعض القيم في الخلية A1 للورقة العمل الأولى ثم يحفظ ملف ODS في مواصفات ODF 1.1 و 1.2. بشكل افتراضي، يتم حفظ ملف ODS في مواصفات ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
