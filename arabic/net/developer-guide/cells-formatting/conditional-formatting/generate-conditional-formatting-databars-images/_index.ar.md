---
title: إنشاء بيانات شكل معايرة شريطية للصور
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات. تدعم إنشاء شرائط بيانات مُنسقة تنسيقيًا والصور، مما يتيح للمستخدمين تخصيص عرض جدول البيانات استنادًا إلى قيمة الخلايا. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لإنشاء شرائط بيانات مُنسقة تنسيقيًا والصور.
keywords: Aspose.Cells، التنسيق الشرطي، شرائط بيانات، صور، جداول بيانات
type: docs
weight: 40
url: /ar/net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

أحيانًا ، تحتاج إلى إنشاء صور شرائط البيانات التنسيقية الشرطية. يمكنك استخدام طريقة Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) لإنشاء هذه الصور. توضح هذه المقالة كيفية إنشاء صورة DataBar باستخدام Aspose.Cells.

{{% /alert %}}

يُنشئ الشفرة النموذجية التالية صورة DataBar للخلية C1. أولاً، يصل إلى كائن شرط التنسيق للخلية، ومن ثم من ذلك الكائن، يصل إلى الكائن [**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) ويستخدم طريقة [**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) لإنشاء صورة الخلية. في النهاية، يقوم بحفظ الصورة على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
