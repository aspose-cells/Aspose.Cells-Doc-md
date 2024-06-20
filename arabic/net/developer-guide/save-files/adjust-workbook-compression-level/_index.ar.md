---
title: ضبط مستوى ضغط الورقة العمل
type: docs
weight: 180
url: /ar/net/adjust-workbook-compression-level/
---

## **ضبط مستوى ضغط الورقة العمل**

يمكن للمطورين تعديل مستوى الضغط لسجل العمل عند العمل مع سجلات عمل أكبر حجمًا. قد يضع المطورون حجم الملفات الأصغر أولويةً على وقت المعالجة أو العكس. توفر Aspose.Cells تعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) الذي يمكنك استخدامه لتعيين مستوى الضغط لسجل العمل. توفر التعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) الأعضاء التالية.

- المستوى 1: أسرع ولكن أقل فعالية في الضغط.
- المستوى 2: أبطأ قليلاً، ولكن أفضل من المستوى 1.
- المستوى 3: أبطأ قليلاً، ولكن أفضل من المستوى 2.
- المستوى 4: أبطأ قليلاً، ولكن أفضل من المستوى 3.
- المستوى 5: أبطأ قليلاً من المستوى 4، لكن مع ضغط أفضل.
- المستوى 6: توازن جيد بين السرعة وكفاءة الضغط.
- المستوى 7: ضغط جيد جدًا!
- المستوى8: ضغط أفضل من المستوى7!
- المستوى9: الضغط "الأفضل"، حيث الأفضل يعني أكبر حجم للاختزال في تيار بيانات الإدخال. هذا أيضًا الضغط الأبطأ.

يوضح الشريحة الكودية التالية استخدام تعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) ومقارنة وقت التحويل للمستوى 1 والمستوى 6 والمستوى 9. يمكنك أيضًا مقارنة أحجام الملفات المولدة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
