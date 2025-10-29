---
title: حفظ ملف ODS وفق مواصفات ODF 1.1 و 1.2 و 1.3 باستخدام Golang عبر C++
linktitle: الحفظ كـ ODF 1.1 و 1.2 و 1.3
description: تحويل Excel إلى ODF 1.1 و 1.2 و 1.3 باستخدام Aspose.Cells باستخدام C++.
type: docs
weight: 230
url: /ar/go-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells حفظ ملف ODS (**جداول بيانات المستند المفتوح**) بصيغة ODF (**صيغة المستند المفتوح**) وفقًا لمواصفات 1.1 و 1.2 و 1.3. لدى Aspose.Cells خاصية [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/go-cpp/odssaveoptions/getodfstrictversion/) التي تحدد إصدار ODF لحفظ ملفات ODS. القيمة الافتراضية لهذه الخاصية هي [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/)، لذلك الملف ODS المحفوظ بدون ضبط هذه الخاصية يستخدم مواصفات 1.2.

{{% /alert %}}

يفترض الكود النموذجي أدناه إنشاء كائن عمل، يضيف قيمة إلى الخلية A1 في الورقة الأولى ثم يقوم بحفظ ملف ODS وفقًا لمواصفات ODF 1.1 و 1.2 و 1.3. بشكل افتراضي، يتم حفظ ملف ODS بمواصفات ODF 1.2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveOdsFileInOdf11And12Specifications.go" >}}
