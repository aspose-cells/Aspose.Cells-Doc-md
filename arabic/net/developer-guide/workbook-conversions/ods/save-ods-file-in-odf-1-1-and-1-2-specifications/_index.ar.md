---
title: احفظ ملف ODS في مواصفات ODF 1.1 و 1.2 و 1.3
linktitle: احفظ كملف ODF 1.1 و 1.2 و 1.3
description: حول Excel إلى مواصفات ODF 1.1 و 1.2 و 1.3 باستخدام Aspose.Cells.
type: docs
weight: 230
url: /ar/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells حفظ ملف ODS (**جداول بيانات المستند المفتوح**) بصيغة ODF (**صيغة المستند المفتوح**) وفقًا لمواصفات 1.1 و 1.2 و 1.3. لدى Aspose.Cells خاصية [**OdsSaveOptions.OdfStrictVersion**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/odfstrictversion/) التي تحدد إصدار ODF لحفظ ملفات ODS. القيمة الافتراضية لهذه الخاصية هي [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/net/aspose.cells.ods/opendocumentformatversiontype/)، لذلك الملف ODS المحفوظ بدون ضبط هذه الخاصية يستخدم مواصفات 1.2.

{{% /alert %}}

يفترض الكود النموذجي أدناه إنشاء كائن عمل، يضيف قيمة إلى الخلية A1 في الورقة الأولى ثم يقوم بحفظ ملف ODS وفقًا لمواصفات ODF 1.1 و 1.2 و 1.3. بشكل افتراضي، يتم حفظ ملف ODS بمواصفات ODF 1.2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
{{< app/cells/assistant language="csharp" >}}
