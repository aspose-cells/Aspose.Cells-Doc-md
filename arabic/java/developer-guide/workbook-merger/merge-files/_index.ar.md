---
title: دمج الملفات
type: docs
weight: 10
url: /ar/java/merge-files/
---

## **مقدمة**

توفر Aspose.Cells طرقًا مختلفة لدمج الملفات. للملفات البسيطة التي تحتوي على بيانات وتنسيقات وصيغ، يمكن استخدام طريقة [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine-com.aspose.cells.Workbook-) لدمج عدة دفاتر عمل، ويمكن استخدام طريقة [**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy-com.aspose.cells.Worksheet-) لنسخ أوراق العمل إلى دفتر عمل جديد. هذه الطرق سهلة الاستخدام وفعالة، ولكن إذا كان لديك الكثير من الملفات التي تريد دمجها، فقد تجد أنها تستهلك الكثير من موارد النظام. لتجنب ذلك، استخدم الطريقة الثابتة CellsHelper.mergeFiles، وهي وسيلة أكثر كفاءة لدمج عدة ملفات.

## **دمج الملفات باستخدام Aspose.Cells**

الرمز المصدري التالي يوضح كيفية دمج الملفات الكبيرة باستخدام طريقة CellsHelper.mergeFiles. يأخذ الملفان الكبيران البسيطان، MyBook1.xls وMyBook2.xls، واللذان يحتويا على بيانات مُنسَقة وصُيغ فقط.

{{% alert color="primary" %}}

الطريقة CellsHelper.mergeFiles تدعم فقط دمج البيانات، الأنماط، التنسيق والصيغ. لم يتم ربط الكائنات مثل الرسوم البيانية، الصور، التعليقات أو أي كائنات أخرى باستخدام هذه الطريقة. علاوة على ذلك، يتم استخدام ملف مؤقت لتخزين البيانات المؤقتة للعملية.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
{{< app/cells/assistant language="java" >}}
