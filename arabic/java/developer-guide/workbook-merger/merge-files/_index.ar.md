---
title: دمج الملفات
type: docs
weight: 10
url: /ar/java/merge-files/
---

## **مقدمة**

يوفر Aspose.Cells طرقًا مختلفة لدمج الملفات. يمكن استخدام الـ [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)) لدمج العديد من دفاتر العمل للملفات البسيطة بالبيانات والتنسيق والصيغ، ويمكن استخدام الـ [Worksheet.copy](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) لنسخ الصفحات العمل في دفتر عمل جديد. هذه الطرق سهلة الاستخدام وفعالة، ولكن إذا كان هناك الكثير من الملفات لدمجها، قد تجد أنها تستهلك الكثير من موارد النظام. لتجنب ذلك، استخدم الطريقة الثابتة CellsHelper.mergeFiles، وهي طريقة أكثر فاعلية لدمج العديد من الملفات.

## **دمج الملفات باستخدام Aspose.Cells**

الرمز المصدري التالي يوضح كيفية دمج الملفات الكبيرة باستخدام طريقة CellsHelper.mergeFiles. يأخذ الملفان الكبيران البسيطان، MyBook1.xls وMyBook2.xls، واللذان يحتويا على بيانات مُنسَقة وصُيغ فقط.

{{% alert color="primary" %}}

الطريقة CellsHelper.mergeFiles تدعم فقط دمج البيانات، الأنماط، التنسيق والصيغ. لم يتم ربط الكائنات مثل الرسوم البيانية، الصور، التعليقات أو أي كائنات أخرى باستخدام هذه الطريقة. علاوة على ذلك، يتم استخدام ملف مؤقت لتخزين البيانات المؤقتة للعملية.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
