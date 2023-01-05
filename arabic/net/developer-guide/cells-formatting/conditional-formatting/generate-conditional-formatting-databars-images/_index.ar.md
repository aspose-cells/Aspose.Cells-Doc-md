---
title: إنشاء صور أشرطة بيانات التنسيق الشرطي
type: docs
weight: 40
url: /ar/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 في بعض الأحيان ، تحتاج إلى إنشاء صور لأشرطة بيانات التنسيق الشرطي. يمكنك استخدام Aspose.Cells[**DataBar.oImage ()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) طريقة لتوليد هذه الصور. يوضح هذا المقال كيفية إنشاء صورة DataBar باستخدام Aspose.Cells.

{{% /alert %}}

ينشئ نموذج التعليمات البرمجية التالي صورة DataBar للخلية C1. أولاً ، يصل إلى كائن شرط التنسيق للخلية ، ثم من هذا الكائن ، يصل إلى ملف[**شريط البيانات**](https://reference.aspose.com/cells/net/aspose.cells/databar) وجوه واستخداماته[**ToImage ()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)طريقة لتوليد صورة الخلية. أخيرًا ، يحفظ الصورة على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
