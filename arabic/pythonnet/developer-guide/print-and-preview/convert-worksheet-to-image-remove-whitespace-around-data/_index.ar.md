---
title: تحويل ورقة عمل إلى صورة  إزالة الفراغات حول البيانات
type: docs
weight: 40
url: /ar/python-net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى عرض صور ورقة العمل في التطبيقات أو صفحات الويب. على سبيل المثال، قد تحتاج إلى إدراج الصور في مستند Word، أو ملف PDF، أو عرض PowerPoint، أو مستند آخر. بشكل أساسي، ترغب في تحويل ورقة العمل إلى صورة بحيث يمكن لصقها في تطبيقات أخرى. يتيح لك Aspose.Cells لـ Python via .NET تحويل أوراق عمل إكسل إلى صور.

{{% /alert %}}

## **إزالة الفراغات حول البيانات**

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) API يحول ورقة عمل إلى ملف صورة مع أي سمات محددة، على سبيل المثال، تنسيق الصورة، الصفحات المقسمة، وما إلى ذلك. تدعم عدة صيغ للصور، بما في ذلك BMP، GIF، JPG، TIFF، و EMF.

عند استخدام ميزة الورقة إلى الصورة، يكون للصورة الناتجة فراغ حولها تلقائياً. يمكنك إزالة ذلك عن طريق تعيين الهوامش العلوية، السفلية، اليسرى واليمنى لتوجيه صفحة ورقة المصدر إلى 0 وتحديد [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) بشكل مناسب.

الكود التالي يزيل الفراغات حول البيانات في الصورة الناتجة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RemoveWhitespaceAroundData-1.py" >}}

