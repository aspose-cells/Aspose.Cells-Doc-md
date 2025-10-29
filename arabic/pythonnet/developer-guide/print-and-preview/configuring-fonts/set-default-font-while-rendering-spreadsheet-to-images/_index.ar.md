---
title: تعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور
type: docs
weight: 360
url: /ar/python-net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

يرجى استخدام خاصية [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) لتعيين الخط الافتراضي أثناء تقديم جداول البيانات إلى الصور. ستكون هذه الخاصية فعالة فقط عندما لا يمكن للخط الافتراضي للدفتر تقديم حروفك. يتم استخدام الخط الافتراضي المحدد بواسطة الخاصية [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) لجميع تلك الخلايا التي تحتوي على خطوط غير صحيحة أو غير موجودة.

{{% /alert %}}

## تعيين الخط الافتراضي أثناء تقديم جداول البيانات إلى الصور

الشيفرة النموذجية التالية تنشئ دفتر عمل، تضيف بعض النص في الخلية A4 من الورقة العمل الأولى، وتعين خطه إلى خط غير صحيح أو غير موجود. ثم، تأخذ صورتين للورقة العمل. تُأخذ الصورة الأولى من خلال تعيين الخاصية [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) إلى *Courier New* وتُأخذ الصورة الثانية من خلال تعيين الخاصية [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) إلى *Times New Roman*.

هذه الصورة الناتجة بعد تعيين الخاصية [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) إلى *Courier New*.

![todo:image_alt_text](1.png)

هذه الصورة الناتجة بعد تعيين الخاصية [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) إلى *Times New Roman*.

![todo:image_alt_text](2.png)

## كود عينة

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

{{< app/cells/assistant language="python-net" >}}
