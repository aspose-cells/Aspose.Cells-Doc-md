---
title: تعديل مستوى ضغط دفتر العمل مع Golang عبر C++
linktitle: ضبط مستوى ضغط ملف العمل
type: docs
weight: 180
url: /ar/go-cpp/adjust-workbook-compression-level/
description: تعلم كيفية ضبط مستوى ضغط ملف العمل باستخدام Aspose.Cells for C++ لتحسين حجم الملف ووقت المعالجة.
---

## **ضبط مستوى ضغط الورقة العمل**

يمكن للمطورين تعديل مستوى الضغط لسجل العمل عند العمل مع سجلات عمل أكبر حجمًا. قد يضع المطورون حجم الملفات الأصغر أولويةً على وقت المعالجة أو العكس. توفر Aspose.Cells تعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) الذي يمكنك استخدامه لتعيين مستوى الضغط لسجل العمل. توفر التعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) الأعضاء التالية.

- المستوى 1: أسرع ولكن أقل فعالية في الضغط.
- المستوى 2: أبطأ قليلاً، ولكن أفضل من المستوى 1.
- المستوى 3: أبطأ قليلاً، ولكن أفضل من المستوى 2.
- المستوى 4: أبطأ قليلاً، ولكن أفضل من المستوى 3.
- المستوى 5: أبطأ قليلاً من المستوى 4، لكن مع ضغط أفضل.
- المستوى 6: توازن جيد بين السرعة وكفاءة الضغط.
- المستوى 7: ضغط جيد جدًا!
- المستوى8: ضغط أفضل من المستوى7!
- المستوى9: الضغط "الأفضل"، حيث الأفضل يعني أكبر حجم للاختزال في تيار بيانات الإدخال. هذا أيضًا الضغط الأبطأ.

يوضح الشريحة الكودية التالية استخدام تعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) ومقارنة وقت التحويل للمستوى 1 والمستوى 6 والمستوى 9. يمكنك أيضًا مقارنة أحجام الملفات المولدة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AdjustWorkbookCompressionLevel.go" >}}
