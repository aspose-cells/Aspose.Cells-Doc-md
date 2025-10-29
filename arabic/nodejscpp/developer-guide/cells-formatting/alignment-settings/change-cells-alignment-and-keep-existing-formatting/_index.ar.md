---
title: تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية
linktitle: تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية
description: استخدم مكتبة Aspose.Cells لتغيير محاذاة الخلية والحفاظ على التنسيق الحالي في Node.js عبر C++
keywords: Aspose.Cells، Node.js عبر C++، محاذاة الخلية، الحفاظ على التنسيق الحالي
type: docs
weight: 340
url: /ar/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، ترغب في تغيير محاذاة عدة خلايا ولكنك تريد أيضًا الاحتفاظ بالتنسيق الحالي. تتيح لك Aspose.Cells for Node.js via C++ القيام بذلك باستخدام طريقة [**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-). إذا قمت بضبطه على **true**، فسيتم تطبيق تغييرات المحاذاة، وإلا فلن يتم ذلك. يرجى ملاحظة أن كائن [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) يُمرر كمعامل إلى طريقة [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-) التي تطبق التنسيق فعليًا على نطاق من الخلايا.

## **تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية**

الكود النموذجي التالي يقوم بتحميل الملف الإكسل النموذجي، ينشئ المدى ويضبط توسيطه أفقيا وعموديا ويحتفظ بالتنسيق الحالي. الصورة النموذجية التالية تقارن ملف الإكسل النموذجي وملف الإكسل الناتج وتُظهر أن جميع التنسيقات الحالية للخلايا هي نفسها باستثناء أن الخلايا الآن موجهة في منتصف الخط أفقيًا وعموديًا.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
