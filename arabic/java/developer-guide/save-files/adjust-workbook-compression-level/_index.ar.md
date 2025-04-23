---
title: ضبط مستوى ضغط الورقة العمل
type: docs
weight: 130
url: /ar/java/adjust-workbook-compression-level/
---

## **ضبط مستوى ضغط الورقة العمل**

يمكن للمطورين ضبط مستوى الضغط لدفتر العمل عند العمل مع دفاتر العمل الكبيرة. يمكن للمطورين إعطاء الأولوية لأحجام الملفات الأصغر على مدى الوقت والتجهيز أو العكس. توفر Aspose.Cells فئة [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) التي يمكنك استخدامها لتعيين مستوى الضغط لدفتر العمل. توفر فئة [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) الأعضاء التالية.

- [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-1): أسرع ولكن ضغط أقل.
- [**LEVEL_2**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-2): أبطأ قليلا، ولكن أفضل من المستوى 1.
- [**LEVEL_3**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-3): أبطأ قليلا، لكن أفضل من المستوى 2.
- [**LEVEL_4**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-4): أبطأ قليلا، لكن أفضل من المستوى 3.
- [**LEVEL_5**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-5): أبطأ قليلا من المستوى 4، ولكن بضغط أفضل.
- [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-6): توازن جيد بين السرعة وكفاءة الضغط.
- [**LEVEL_7**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-7): ضغط جيد جدا!
- [**LEVEL_8**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-8): ضغط أفضل من المستوى 7!
- [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-9): أفضل الضغط، حيث يعني الأفضل أكبر تقليل في حجم تدفق البيانات الإدخالية. هذا أيضا الضغط الأبطأ.

الكود العيني التالي يظهر استخدام فئة [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) ويقارن وقت التحويل لـ [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-1), [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-6), و [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-9). يمكنك أيضا مقارنة أحجام الملفات المولدة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
{{< app/cells/assistant language="java" >}}
