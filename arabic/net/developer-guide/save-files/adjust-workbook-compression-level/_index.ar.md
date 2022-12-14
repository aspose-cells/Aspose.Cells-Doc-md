---
title: ضبط مستوى ضغط المصنف
type: docs
weight: 180
url: /ar/net/adjust-workbook-compression-level/
---
## **ضبط مستوى ضغط المصنف**

يمكن للمطورين ضبط مستوى الضغط للمصنف عند العمل مع المصنفات الأكبر حجمًا. قد يعطي المطورون الأولوية لأحجام الملفات الأصغر على وقت المعالجة أو العكس. يوفر Aspose.Cells**[OoxmlCompressionType] (https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** التعداد الذي يمكنك استخدامه لتعيين مستوى ضغط المصنف. ال**[OoxmlCompressionType] (https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** يوفر التعداد الأعضاء التالية.

- المستوى 1: الضغط الأسرع والأقل فعالية.
- المستوى 2: أبطأ قليلاً ، لكن أفضل ، من المستوى 1.
- المستوى 3: أبطأ قليلاً ، لكن أفضل ، من المستوى 2.
- المستوى 4: أبطأ قليلاً ، لكن أفضل من المستوى 3.
- المستوى 5: أبطأ قليلاً من المستوى 4 ، لكن بضغط أفضل.
- المستوى 6: توازن جيد بين السرعة وكفاءة الضغط.
- المستوى 7: ضغط جيد جدًا!
- المستوى 8: ضغط أفضل من المستوى 7!
- المستوى 9: الضغط "الأفضل" ، حيث يعني أفضل تقليل في حجم دفق بيانات الإدخال. هذا أيضًا هو أبطأ ضغط.

 يوضح مقتطف الشفرة التالي استخدام**[OoxmlCompressionType] (https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**التعداد ويقارن وقت التحويل للمستوى 1 والمستوى 6 والمستوى 9. يمكنك أيضًا مقارنة أحجام الملفات التي تم إنشاؤها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
