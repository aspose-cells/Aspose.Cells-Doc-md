---
title: تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بواسطة الصفحة
type: docs
weight: 80
url: /ar/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

تم تصميم هذا المستند لتوفير للمطورين فهمًا مفصلًا حول كيفية تحويل ورقة العمل إلى ملف صورة وورقة العمل بصفحات متعددة إلى ملف صورة لكل صفحة.

في بعض الأحيان قد تحتاج إلى تقديم ورقات العمل على شكل صور، على سبيل المثال، لاستخدامها في التطبيقات أو صفحات الويب. قد تحتاج إلى إدراج الصور في مستند Word أو ملف PDF أو عرض PowerPoint، أو استخدامها في سيناريو آخر. ببساطة، ترغب في عرض ورقة العمل على شكل صورة. تدعم Aspose.Cells تحويل ورقات العمل في ملفات Microsoft Excel إلى صور. بالإضافة إلى ذلك، تدعم Aspose.Cells تحويل دفتر العمل إلى عدة ملفات صور، واحدة لكل صفحة.

قد تستخدم أتمتة Office لتحقيق هذا، ولكن أتمتة Office لها عيوبها الخاصة. هناك عدة أسباب وقضايا معقدة، على سبيل المثال الأمان والاستقرار والتوسعة / السرعة والسعر والميزات. بإختصار، هناك العديد من الأسباب، ولكن السبب الرئيسي هو أن شركة Microsoft نفسها توصي بشدة ضد أتمتة Office.

{{% /alert %}}

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى ملف صورة**

يوضح هذا المقال كيفية إنشاء تطبيق وحدة التحكم في فيجوال ستوديو، وتحويل ورقة العمل إلى صورة، وتحويل ورقة العمل إلى صورة واحدة لكل ورقة بمجرد وصف بسيط باستخدام واجهة برمجة التطبيقات Aspose.Cells.

يجب أن تستورد مساحة الاسم [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) إلى البرنامج/المشروع الخاص بك. تحتوي على العديد من الفئات القيمة، مثل [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)، [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)، وما إلى ذلك. تمثل الفئة [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) ورقة العمل المطلوبة لتقديم الصور لورقة العمل ولها طريقة [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) مفتوحة يمكن أن تحول ورقة العمل إلى ملفات صور مباشرة باستخدام أي سمات أو خيارات. يمكنها إرجاع كائن System.Drawing.Bitmap ويمكنك حفظ ملف صورة في القرص/التدفق. تدعم العديد من تنسيقات الصور، على سبيل المثال، BMP، PNG، GIF، JPG، JPEG، TIFF، EMF، وغيرها.

يشرح هذا المقال كيفية:

- تحويل ورقة العمل إلى صورة
- تحويل كل صفحة في ورقة العمل إلى صورة

تظهر هذه المهمة كيفية استخدام Aspose.Cells لتحويل ورقة عمل من دفتر العمل القالب إلى ملف صورة.

### **إعداد المشروع**

1. أولاً، [حمّل Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
2. قم بتثبيته على جهاز الكمبيوتر الخاص بالتطوير الخاص بك. عند تثبيت جميع مكونات [Aspose](http://www.aspose.com/), تعمل في وضع التقييم. يتميز الوضع التجريبي بعدم وجود حد زمني وأنه يضيف فقط علامات مائية إلى المستندات المنتجة. الآن قم ببدء فيجوال ستوديو.نت وأنشئ تطبيق وحدة التحكم جديد. تستخدم هذا المثال تطبيق وحدة التحكم C#، ولكن يمكنك استخدام VB.NET أيضًا. أضف مرجع لـ Aspose.Cells إلى المشروع المُنشأ.

### **تحويل ورقة العمل إلى ملف صورة**

أنشأت دفتر عمل جديد في Microsoft Excel وأضفت بعض البيانات في ورقة العمل الأولى: **Testbook.xlsx** (ورقة عمل واحدة). ثم قم بتحويل ورقة العمل في الملف القالب Sheet1 إلى ملف صورة يُعرف باسم SheetImage.jpg.

التالي هو الكود الذي استخدمته العنصر لإنجاز المهمة. يحول Sheet1 في **Testbook.xlsx** إلى ملف صورة لشرح سهولة هذا التحويل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى ملف صورة بواسطة الصفحة**

يوضح هذا المثال كيفية استخدام Aspose.Cells لتحويل ورقة عمل من مصنف قوالب يحتوي على عدة صفحات إلى ملف صورة واحد لكل صفحة.

### **تحويل ورقة العمل إلى صورة حسب الصفحة**

لقد أنشأت ورق عمل جديد في Microsoft Excel وأضافت بعض البيانات في ورقة العمل الأولى: ملفTestbook2.xlsx (ورقة عمل واحدة).

الآن، قم بتحويل ورقة العمل Sheet1 في ملف القالب إلى ملفات صور (ملف واحد لكل صفحة). حيث أنني قمت بالفعل بإنشاء تطبيق الوحدة التحكم لأداء مهمة النسخ، سأتجاوز خطوات إنشاء تطبيق الوحدة التحكم تلك وأنتقل مباشرة إلى خطوات تحويل ورقة العمل.

الكود التالي تم استخدامه من قبل المكون لإنجاز المهمة. يقوم بتحويل Sheet1 في Testbook2.xls إلى ملفات صور حسب الصفحة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
