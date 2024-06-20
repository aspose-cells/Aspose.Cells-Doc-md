---
title: حفظ ملف ODS بمواصفات ODF 1.1 و 1.2
linktitle: حفظ كـ ODF 1.1 و 1.2 
description: تحويل Excel إلى مواصفات ODF 1.1 و 1.2 باستخدام Aspose.Cells.
type: docs
weight: 230
url: /ar/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells حفظ ملف ODS (جداول بيانات مستند مفتوح) في مواصفات ODF (تنسيق مستند مفتوح) 1.1 و 1.2. لدى Aspose.Cells خصائص [**OdsSaveOptions.IsStrictSchema11**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/properties/isstrictschema11) التي تحدد استخدام مواصفات ODF 1.1 لحفظ ملفات ODS. القيمة الافتراضية لهذه الخاصية هي **خاطئة**, لذا يتم حفظ ملف ODS دون هذا الإعداد باستخدام المواصفات 1.2.

{{% /alert %}}

الكود العيني أدناه ينشئ كائن ورقة عمل، يضيف قيمة إلى الخلية A1 في الورقة العمل الأولى ثم يحفظ ملف ODS في مواصفات ODF 1.1 و 1.2. بشكل افتراضي، يتم حفظ الملف ODS بمواصفة 1.2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
