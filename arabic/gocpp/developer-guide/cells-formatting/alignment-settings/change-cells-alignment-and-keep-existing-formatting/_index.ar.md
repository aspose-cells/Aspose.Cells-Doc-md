---
title: تغيير محاذاة الخلايا والحفاظ على التنسيق الموجود باستخدام Golang عبر C++
description: استخدم مكتبة Aspose.Cells لتغيير توجيه الخلية والحفاظ على التنسيق الحالي
keywords: Aspose.Cells، C++، محاذاة الخلايا، الحفاظ على التنسيق الحالي
type: docs
weight: 340
url: /ar/go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **سيناريوهات الاستخدام المحتملة**

 في بعض الأحيان، تريد تغيير محاذاة عدة خلايا مع الاحتفاظ بالتنسيق الحالي. تتيح لك Aspose.Cells القيام بذلك باستخدام خاصية [**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/). إذا قمت بضبطها على **true**، ستتم التغييرات في المحاذاة، وإلا فلن تكون. يرجى ملاحظة أن كائن [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) يُمرر كمعامل للطريقة [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) التي تطبق التنسيق على نطاق من الخلايا.

## **تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية**

الكود النموذجي التالي يقوم بتحميل الملف الإكسل النموذجي، ينشئ المدى ويضبط توسيطه أفقيا وعموديا ويحتفظ بالتنسيق الحالي. الصورة النموذجية التالية تقارن ملف الإكسل النموذجي وملف الإكسل الناتج وتُظهر أن جميع التنسيقات الحالية للخلايا هي نفسها باستثناء أن الخلايا الآن موجهة في منتصف الخط أفقيًا وعموديًا.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}
