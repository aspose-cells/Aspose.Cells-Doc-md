---
title: دمج الملفات
type: docs
weight: 10
url: /ar/java/merge-files/
---
## **مقدمة**

 يوفر Aspose.Cells طرقًا مختلفة لدمج الملفات. بالنسبة إلى الملفات البسيطة التي تحتوي على بيانات وتنسيقات وصيغ ، فإن ملف[**Workbook.combine ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook) ) لدمج عدة مصنفات ، و[**Worksheet.copy (**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)لنسخ أوراق العمل إلى مصنف جديد. هذه الطرق سهلة الاستخدام وفعالة ، ولكن إذا كان لديك الكثير من الملفات لدمجها ، فقد تجد أنها تتطلب الكثير من موارد النظام. لتجنب ذلك ، استخدم الطريقة الثابتة CellsHelper.mergeFiles ، وهي طريقة أكثر فاعلية لدمج عدة ملفات.

## **دمج الملفات باستخدام Aspose.Cells**

يوضح نموذج التعليمات البرمجية التالي كيفية دمج الملفات الكبيرة باستخدام أسلوب CellsHelper.mergeFiles. يتطلب الأمر ملفين بسيطين لكن كبيرين ، MyBook1.xls و MyBook2.xls. تحتوي الملفات على بيانات وصيغ منسقة فقط.

{{% alert color="primary" %}}

لا تدعم طريقة CellsHelper.mergeFiles سوى دمج البيانات والأنماط والتنسيق والصيغ. قد لا يتم دمج الكائنات مثل المخططات أو الصور أو التعليقات أو الكائنات الأخرى باستخدام هذه الطريقة. علاوة على ذلك ، يتم استخدام ملف مخبأ لتخزين البيانات المؤقتة للعملية.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
