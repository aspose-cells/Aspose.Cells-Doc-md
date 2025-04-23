---
title: إنشاء بيانات شكل معايرة شريطية للصور
linktitle: إنشاء بيانات شكل معايرة شريطية للصور
description: Aspose.Cells هي مكتبة Node.js للعمل مع ملفات جداول البيانات. تدعم إنشاء أشرطة بيانات وصور ذات تنسيق شرطي، مما يسمح للمستخدمين بتخصيص عرض جدول البيانات استنادًا إلى قيمة الخلايا. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لإنشاء أشرطة بيانات وصور ذات تنسيق شرطي.
keywords: Aspose.Cells، التنسيق الشرطي، أشرطة البيانات، الصور، جداول البيانات، Node.js عبر C++
type: docs
weight: 40
url: /ar/nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

أحيانًا ، تحتاج إلى إنشاء صور شرائط البيانات التنسيقية الشرطية. يمكنك استخدام طريقة Aspose.Cells [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) لإنشاء هذه الصور. توضح هذه المقالة كيفية إنشاء صورة DataBar باستخدام Aspose.Cells.

{{% /alert %}}

ينتج رمز العينة التالي صورة DataBar للخلية C1. أولاً، يقوم بالوصول إلى كائن شرط التنسيق للخلية، ومن ذلك الكائن، يصل إلى [**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar) ويستخدم طريقة [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) لإنشاء صورة الخلية. أخيرًا، يحفظ الصورة على القرص.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}

