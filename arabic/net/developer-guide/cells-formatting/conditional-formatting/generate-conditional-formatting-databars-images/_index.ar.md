---
title: إنشاء صور لأشرطة البيانات ذات التنسيق الشرطي
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات. وهو يدعم إنشاء أشرطة وصور بيانات منسقة بشكل مشروط، مما يسمح للمستخدمين بتخصيص عرض جدول البيانات بناءً على قيمة الخلايا. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لإنشاء أشرطة وصور بيانات منسقة بشكل مشروط.
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /ar/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 في بعض الأحيان، تحتاج إلى إنشاء صور لأشرطة بيانات التنسيق الشرطي. يمكنك استخدام Aspose.Cells[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) طريقة توليد هذه الصور توضح هذه المقالة كيفية إنشاء صورة DataBar باستخدام Aspose.Cells.

{{% /alert %}}

 نموذج التعليمات البرمجية التالي ينشئ صورة DataBar للخلية C1. أولاً، يصل إلى كائن شرط التنسيق الخاص بالخلية، ثم من هذا الكائن، يصل إلى[**شريط البيانات**](https://reference.aspose.com/cells/net/aspose.cells/databar) الكائن ويستخدمه[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)طريقة توليد صورة الخلية وأخيرا، فإنه يحفظ الصورة على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
