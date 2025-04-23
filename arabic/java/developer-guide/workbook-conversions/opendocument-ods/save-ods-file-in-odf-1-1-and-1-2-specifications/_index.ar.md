---
title: حفظ ملف ODS وفقًا لمواصفات ODF 1.1، 1.2 و 1.3
type: docs
weight: 170
url: /ar/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells حفظ ملفات (**OpenDocument Spreadsheet**) بصيغة ODS وفقًا لمواصفات (**OpenDocument Format**) ODF 1.1، 1.2 و 1.3. أضف Aspose.Cells ملكية [**OdsSaveOptions.setOdfStrictVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions/#setOdfStrictVersion-int-) لاستخدام إصدار ODF عند حفظ ملفات ODS. القيمة الافتراضية لهذه الملكية [**OpenDocumentFormatVersionType.ODF_12**](https://reference.aspose.com/cells/java/com.aspose.cells/opendocumentformatversiontype/#ODF-12)، لذا فإن ملف ODS المحفوظ بدون هذه الإعدادات الخاصة سيستخدم مواصفة 1.2.

{{% /alert %}}

الكود العينة أدناه ينشئ كائن الدفتر، يضيف بعض القيم في الخلية A1 للورقة العمل الأولى ثم يحفظ ملف ODS في مواصفات ODF 1.1 و 1.2. بشكل افتراضي، يتم حفظ ملف ODS في مواصفات ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
{{< app/cells/assistant language="java" >}}
