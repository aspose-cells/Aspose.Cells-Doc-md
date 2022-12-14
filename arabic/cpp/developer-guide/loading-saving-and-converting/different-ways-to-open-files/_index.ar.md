---
title: طرق مختلفة لفتح الملفات
linktitle: طرق مختلفة لفتح الملفات
type: docs
weight: 10
url: /ar/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

باستخدام Aspose.Cells ، يمكن فتح الملفات ، على سبيل المثال لاسترداد البيانات ، أو استخدام قالب المصمم لتسريع عملية التطوير. يمكن لـ Aspose.Cells فتح نطاق من الملفات المختلفة ، مثل Microsoft جداول بيانات Excel (XLS أو XLSX أو XLSM أو XLSB) أو ملفات CSV أو TabD limits.

{{% /alert %}} 
## **فتح ملف عبر مسار**
 يمكن للمطورين فتح ملف Excel Microsoft باستخدام مسار الملف الخاص به على الكمبيوتر المحلي عن طريق تحديده في ملف[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)منشئ الطبقة. ما عليك سوى تمرير المسار في المُنشئ كسلسلة. سوف يقوم Aspose.Cells باكتشاف نوع تنسيق الملف تلقائيًا.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath.cpp" >}}

## **فتح ملف باستخدام الدفق**
 من الممكن أيضًا فتح ملف Excel كتدفق. للقيام بذلك ، استخدم إصدارًا محملاً بشكل زائد من المُنشئ يأخذ الامتداد*مجرى*الكائن الذي يحتوي على الملف.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream.cpp" >}}

