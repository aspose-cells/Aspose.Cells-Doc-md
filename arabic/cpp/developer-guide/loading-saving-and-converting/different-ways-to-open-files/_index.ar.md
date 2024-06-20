---
title: طرق مختلفة لفتح الملفات
linktitle: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

مع Aspose.Cells من الممكن فتح الملفات، على سبيل المثال لاسترداد البيانات، أو استخدام قالب مصمم لتسريع عملية التطوير. يمكن لـAspose.Cells فتح مجموعة متنوعة من الملفات المختلفة، مثل ورقات العمل Microsoft Excel (XLS، XLSX، XLSM، XLSB)، ملفات CSV أو TabDelimited.

{{% /alert %}} 
## **فتح ملف عبر مسار**
يمكن للمطورين فتح ملف Microsoft Excel باستخدام مساره في الكمبيوتر المحلي عن طريق تحديده في مُنشئ فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) ببساطة قم بتمرير المسار في المُنشئ كسلسلة نص. سوف Aspose.Cells يكتشف نوع تنسيق الملف تلقائياً.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **فتح ملف باستخدام تيار**
من الممكن أيضاً فتح ملف Excel كتيار. للقيام بذلك، استخدم الإصدار المحدث من المُنشئ الذي يأخذ كائن *Stream* الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

