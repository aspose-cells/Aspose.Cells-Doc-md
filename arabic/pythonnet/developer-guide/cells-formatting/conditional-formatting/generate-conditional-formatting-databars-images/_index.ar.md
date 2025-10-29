---
title: إنشاء بيانات شكل معايرة شريطية للصور
description: Aspose.Cells للبايثون via .NET هي مكتبة بايثون للعمل مع ملفات جداول البيانات. تدعم إنشاء أشرطة بيانات وصور ذات تنسيق شرطي، مما يسمح للمستخدمين بتخصيص عرض الجدول بناءً على قيمة الخلايا. ستقدم هذه المقالة مقدمة عن كيفية استخدام Aspose.Cells للبايثون لإنشاء أشرطة بيانات وصور ذات تنسيق شرطي.
keywords: Aspose.Cells للبايثون via .NET، التنسيق الشرطي، أشرطة البيانات، الصور، الجداول
type: docs
weight: 40
url: /ar/python-net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى إنشاء صور لأشرطة التنسيق الشرطي. يمكنك استخدام طريقة Aspose.Cells [**DataBar.to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) لإنشاء هذه الصور. يُظهر هذا المقال كيفية إنشاء صورة لشفرة البيانات باستخدام Aspose.Cells للبايثون via .NET.

{{% /alert %}}

يُنشئ الشفرة النموذجية التالية صورة DataBar للخلية C1. أولاً، يصل إلى كائن شرط التنسيق للخلية، ومن ثم من ذلك الكائن، يصل إلى الكائن [**DataBar**](https://reference.aspose.com/cells/python-net/aspose.cells/databar) ويستخدم طريقة [**to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) لإنشاء صورة الخلية. في النهاية، يقوم بحفظ الصورة على القرص.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GenerateDatabarImage-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
