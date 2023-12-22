---
title: طرق مختلفة لفتح الملفات
linktitle: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

مع Aspose.Cells من الممكن فتح الملفات، على سبيل المثال لاسترداد البيانات، أو استخدام قالب مصمم لتسريع عملية التطوير. يمكن لـ Aspose.Cells فتح مجموعة من الملفات المختلفة، مثل Microsoft جداول بيانات Excel (XLS، XLSX، XLSM، XLSB)، CSV أو TabDelimited ملف.

{{% /alert %}} 
##  **فتح ملف عبر المسار**
 يمكن للمطورين فتح ملف Excel Microsoft باستخدام مسار الملف الخاص به على الكمبيوتر المحلي عن طريق تحديده في[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)منشئ الطبقة. ما عليك سوى تمرير المسار في المُنشئ كسلسلة. Aspose.Cells سيكتشف تلقائيًا نوع تنسيق الملف.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

##  **فتح ملف باستخدام الدفق**
 من الممكن أيضًا فتح ملف Excel كدفق. للقيام بذلك، استخدم نسخة مثقلة من المنشئ الذي يأخذ*تدفق*الكائن الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

