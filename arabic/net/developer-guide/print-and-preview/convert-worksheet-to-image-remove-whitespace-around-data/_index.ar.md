---
title: تحويل ورقة العمل إلى صورة - إزالة المسافة البيضاء حول البيانات
type: docs
weight: 40
url: /ar/net/convert-worksheet-to-image-remove-whitespace-around-data/
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى تقديم صور ورقة العمل في التطبيقات أو صفحات الويب. على سبيل المثال ، قد تحتاج إلى إدراج صور في مستند Word أو ملف PDF أو عرض تقديمي PowerPoint أو مستند آخر. بشكل أساسي ، تريد عرض ورقة العمل كصورة بحيث يمكن لصقها في تطبيقات أخرى. Aspose.Cells يسمح لك بتحويل أوراق عمل Microsoft Excel إلى صور.

{{% /alert %}}

## **إزالة المسافة البيضاء حول البيانات**

 ال[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)API يحول ورقة العمل إلى ملف صورة مع أي سمات محددة ، على سبيل المثال ، تنسيق الصورة ، والأوراق المرقمة ، إلخ. يتم دعم العديد من تنسيقات الصور ، بما في ذلك BMP ، GIF ، JPG ، TIFF ، و EMF.

 عند استخدام ميزة من ورقة إلى صورة ، يكون للصورة الناتجة مسافة بيضاء ، أي حد ، حولها بشكل افتراضي. يمكنك إزالة هذا عن طريق تعيين هوامش إعداد الصفحة العلوية والسفلية واليسرى واليمنى لورقة العمل المصدر على 0 وتحديدها[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)السمات وفقًا لذلك.

يزيل مقتطف الشفرة التالي المسافة البيضاء حول البيانات في صورة الإخراج.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

