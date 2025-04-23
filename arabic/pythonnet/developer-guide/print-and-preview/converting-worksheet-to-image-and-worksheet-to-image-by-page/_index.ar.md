---
title: تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بواسطة الصفحة
type: docs
weight: 80
url: /ar/python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

تم تصميم هذا المستند لتوفير للمطورين فهمًا مفصلًا حول كيفية تحويل ورقة العمل إلى ملف صورة وورقة العمل بصفحات متعددة إلى ملف صورة لكل صفحة.

أحيانًا، قد تحتاج إلى عرض أوراق العمل كصور، على سبيل المثال، لاستخدامها في التطبيقات أو صفحات الويب. قد تحتاج إلى إدراج الصور في مستند Word، أو ملف PDF، أو عرض PowerPoint، أو استخدام الحالات الأخرى. ببساطة، تريد عرض ورقة العمل كصورة. يدعم Aspose.Cells لـ Python via .NET تحويل أوراق العمل في ملفات إكسل إلى صور. كما يدعم Aspose.Cells لـ Python via .NET تحويل دفتر عمل إلى عدة ملفات صور، واحدة لكل صفحة.

قد تستخدم أتمتة Office لتحقيق هذا، ولكن أتمتة Office لها عيوبها الخاصة. هناك عدة أسباب وقضايا معقدة، على سبيل المثال الأمان والاستقرار والتوسعة / السرعة والسعر والميزات. بإختصار، هناك العديد من الأسباب، ولكن السبب الرئيسي هو أن شركة Microsoft نفسها توصي بشدة ضد أتمتة Office.

{{% /alert %}}

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى ملف صورة**

توضح هذه المقالة كيفية إنشاء تطبيق وحدة تحكم في Visual Studio، تحويل ورقة عمل إلى صورة، وتحويل ورقة عمل إلى صورة واحدة لكل ورقة عمل باستخدام واجهة برمجة التطبيقات Aspose.Cells للبايثون via .NET.

يجب أن تستورد مساحة الاسم [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) إلى البرنامج/المشروع الخاص بك. تحتوي على العديد من الفئات القيمة، مثل [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)، [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)، وما إلى ذلك. تمثل الفئة [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) ورقة العمل المطلوبة لتقديم الصور لورقة العمل ولها طريقة [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) مفتوحة يمكن أن تحول ورقة العمل إلى ملفات صور مباشرة باستخدام أي سمات أو خيارات. يمكنها إرجاع كائن System.Drawing.Bitmap ويمكنك حفظ ملف صورة في القرص/التدفق. تدعم العديد من تنسيقات الصور، على سبيل المثال، BMP، PNG، GIF، JPG، JPEG، TIFF، EMF، وغيرها.

تشرح هذه المقالة كيفية تحويل ورقة عمل إلى صورة. تُظهر هذه المهمة كيفية استخدام Aspose.Cells للبايثون via .NET لتحويل ورقة عمل من دفتر عمل قالب إلى ملف صورة.


### **تحويل ورقة العمل إلى ملف صورة**

أنشأت دفتر عمل جديد في Microsoft Excel وأضفت بعض البيانات في ورقة العمل الأولى: **Testbook.xlsx** (ورقة عمل واحدة). ثم قم بتحويل ورقة العمل في الملف القالب Sheet1 إلى ملف صورة يُعرف باسم SheetImage.jpg.

التالي هو الكود الذي استخدمته العنصر لإنجاز المهمة. يحول Sheet1 في **Testbook.xlsx** إلى ملف صورة لشرح سهولة هذا التحويل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى ملف صورة بواسطة الصفحة**

يُظهر هذا المثال كيفية استخدام Aspose.Cells للبايثون via .NET لتحويل ورقة عمل من دفتر عمل قالب يحتوي على عدة صفحات إلى ملف صورة لكل صفحة.

### **تحويل ورقة العمل إلى صورة حسب الصفحة**

لقد أنشأت ورق عمل جديد في Microsoft Excel وأضافت بعض البيانات في ورقة العمل الأولى: ملفTestbook2.xlsx (ورقة عمل واحدة).

الآن، قم بتحويل ورقة العمل Sheet1 في ملف القالب إلى ملفات صور (ملف واحد لكل صفحة). حيث أنني قمت بالفعل بإنشاء تطبيق الوحدة التحكم لأداء مهمة النسخ، سأتجاوز خطوات إنشاء تطبيق الوحدة التحكم تلك وأنتقل مباشرة إلى خطوات تحويل ورقة العمل.

الكود التالي تم استخدامه من قبل المكون لإنجاز المهمة. يقوم بتحويل Sheet1 في Testbook2.xls إلى ملفات صور حسب الصفحة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

