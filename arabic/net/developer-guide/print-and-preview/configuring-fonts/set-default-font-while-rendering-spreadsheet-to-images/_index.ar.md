---
title: تعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور
type: docs
weight: 360
url: /ar/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

يرجى استخدام خاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) لتعيين الخط الافتراضي أثناء تقديم جداول البيانات إلى الصور. ستكون هذه الخاصية فعالة فقط عندما لا يمكن للخط الافتراضي للدفتر تقديم حروفك. يتم استخدام الخط الافتراضي المحدد بواسطة الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) لجميع تلك الخلايا التي تحتوي على خطوط غير صحيحة أو غير موجودة.

{{% /alert %}}

## تعيين الخط الافتراضي أثناء تقديم جداول البيانات إلى الصور

الشيفرة النموذجية التالية تنشئ دفتر عمل، تضيف بعض النص في الخلية A4 من الورقة العمل الأولى، وتعين خطه إلى خط غير صحيح أو غير موجود. ثم، تأخذ صورتين للورقة العمل. تُأخذ الصورة الأولى من خلال تعيين الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) إلى *Courier New* وتُأخذ الصورة الثانية من خلال تعيين الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) إلى *Times New Roman*.

هذه الصورة الناتجة بعد تعيين الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) إلى *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

هذه الصورة الناتجة بعد تعيين الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) إلى *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## كود عينة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
