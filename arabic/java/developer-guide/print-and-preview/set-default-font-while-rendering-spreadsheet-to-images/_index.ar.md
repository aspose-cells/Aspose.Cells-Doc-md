---
title: تعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور
type: docs
weight: 840
url: /ar/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

الرجاء استخدام خاصية [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) لتعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور. ستكون هذه الخاصية فعالة فقط عندما لا يمكن أن يقوم الخط الافتراضي للدفتر بتقديم الشخصيات الخاصة بك. يتم استخدام الخط الافتراضي المحدد باستخدام الخاصية [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) لجميع تلك الخلايا التي تحتوي على خطوط غير صالحة أو غير موجودة.

{{% /alert %}} 
## **تعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور**
الكود المرجعي التالي ينشئ دفتر عمل ، يضيف بعض النص في الخلية A4 من الورقة العمل الأولى ويعين خطه إلى خط غير صالح أو غير موجود. ثم يأخذ صورتين من الورقة العمل. تم أخذ الصورة الأولى عن طريق تعيين [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) الخاصية إلى *Courier New* وتم أخذ الصورة الثانية عن طريق تعيين [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) الخاصية إلى *Times New Roman*.

هذه هي الصورة الناتجة بعد تعيين [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) الخاصية إلى *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

هذه هي الصورة الناتجة بعد تعيين [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) الخاصية إلى *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
{{< app/cells/assistant language="java" >}}
