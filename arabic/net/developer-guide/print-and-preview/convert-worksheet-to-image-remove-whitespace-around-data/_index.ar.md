---
title: تحويل ورقة عمل إلى صورة  إزالة الفراغات حول البيانات
type: docs
weight: 40
url: /ar/net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

أحيانًا، قد تحتاج إلى عرض صور ورق العمل في التطبيقات أو صفحات الويب. على سبيل المثال، قد تحتاج إلى إدراج صور في مستند Word، ملف PDF، عرض PowerPoint، أو مستند آخر. بشكل أساسي، ترغب في عرض ورقة العمل كصورة بحيث يمكن لصقها في تطبيقات أخرى. تُسمح لك Aspose.Cells بتحويل جداول بيانات Microsoft Excel إلى صور.

{{% /alert %}}

## **إزالة الفراغات حول البيانات**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) API يحول ورقة عمل إلى ملف صورة مع أي سمات محددة، على سبيل المثال، تنسيق الصورة، الصفحات المقسمة، وما إلى ذلك. تدعم عدة صيغ للصور، بما في ذلك BMP، GIF، JPG، TIFF، و EMF.

عند استخدام ميزة الورقة إلى الصورة، يكون للصورة الناتجة فراغ حولها تلقائياً. يمكنك إزالة ذلك عن طريق تعيين الهوامش العلوية، السفلية، اليسرى واليمنى لتوجيه صفحة ورقة المصدر إلى 0 وتحديد [**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) بشكل مناسب.

الكود التالي يزيل الفراغات حول البيانات في الصورة الناتجة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

