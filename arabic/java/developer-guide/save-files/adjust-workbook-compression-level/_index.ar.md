---
title: ضبط مستوى ضغط المصنف
type: docs
weight: 130
url: /ar/java/adjust-workbook-compression-level/
---
## **ضبط مستوى ضغط المصنف**

يمكن للمطورين ضبط مستوى الضغط للمصنف عند العمل مع المصنفات الأكبر حجمًا. قد يعطي المطورون الأولوية لأحجام الملفات الأصغر على وقت المعالجة أو العكس. يوفر Aspose.Cells**[OoxmlCompressionType] (https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)**التعداد الذي يمكنك استخدامه لتعيين مستوى ضغط المصنف. ال**[OoxmlCompressionType] (https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** يوفر التعداد الأعضاء التالية.

- **[LEVEL_1] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**: الضغط الأسرع والأقل فعالية.
- **[LEVEL_2] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2)**: أبطأ قليلاً ، لكن أفضل من المستوى 1.
- **[LEVEL_3] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3)**أبطأ قليلاً ، لكن أفضل من المستوى 2.
- **[LEVEL_4] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4)**: أبطأ قليلاً ، لكن أفضل من المستوى 3.
- **[LEVEL_5] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5)**: أبطأ قليلاً من المستوى 4 ، لكن بضغط أفضل.
- **[LEVEL_6] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)**: توازن جيد بين السرعة وكفاءة الضغط.
- **[LEVEL_7] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)**: ضغط جيد جدا!
- **[LEVEL_8] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8)**: ضغط أفضل من المستوى 7!
- **[LEVEL_9] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**الضغط "الأفضل" ، حيث يعني أفضل تقليل في حجم دفق بيانات الإدخال. هذا أيضًا هو أبطأ ضغط.

يوضح مقتطف الشفرة التالي استخدام**[OoxmlCompressionType] (https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** التعداد ويقارن وقت التحويل لـ**[LEVEL_1] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**, **[LEVEL_6] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)** ، و**[LEVEL_9] (https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**. يمكنك أيضًا مقارنة أحجام الملفات التي تم إنشاؤها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
