---
title: تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بصفحة
type: docs
weight: 80
url: /ar/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

تم تصميم هذا المستند لتزويد المطورين بفهم تفصيلي لكيفية تحويل ورقة العمل إلى ملف صورة وورقة عمل بها صفحات متعددة إلى ملف صورة لكل صفحة.

في بعض الأحيان ، قد تحتاج إلى تقديم أوراق العمل كصور ، على سبيل المثال ، لاستخدامها في التطبيقات أو صفحات الويب. قد تحتاج إلى إدراج الصور في مستند Word أو ملف PDF أو عرض تقديمي PowerPoint أو استخدامها في سيناريو آخر. ببساطة ، تريد تقديم ورقة العمل كصورة. يدعم Aspose.Cells تحويل أوراق العمل في Microsoft ملفات Excel إلى صور. كما يدعم Aspose.Cells تحويل مصنف إلى ملفات صور متعددة ، بمعدل واحد لكل صفحة.

يمكنك استخدام Office Automation لتحقيق ذلك ، ولكن أتمتة Office لها عيوبها الخاصة. هناك عدة أسباب ومشكلات متضمنة: على سبيل المثال الأمان والاستقرار وقابلية التوسع / السرعة والسعر والميزات. باختصار ، هناك العديد من الأسباب ، ولكن السبب الرئيسي هو أن Microsoft أنفسهم يوصون بشدة بعدم أتمتة Office.

{{% /alert %}}

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى ملف صورة**

توضح هذه المقالة كيفية إنشاء تطبيق وحدة تحكم في Visual Studio ، وتحويل ورقة عمل إلى صورة ، وتحويل ورقة عمل إلى صورة واحدة لكل ورقة عمل مع بضعة سطور بسيطة وأبسط من التعليمات البرمجية باستخدام Aspose.Cells API.

 تحتاج إلى استيراد ملف[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) إلى برنامجك / مشروعك. لديها العديد من الفئات القيمة ، مثل[**عرض الورقة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**عرض المصنف**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)، وهلم جرا. ال[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) فئة تمثل ورقة عمل لعرض الصور لورقة العمل ولديها تحميل زائد[**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)الطريقة التي يمكنها تحويل ورقة عمل إلى ملفات صور مباشرة مع أي سمات أو مجموعة خيارات. يمكنه إرجاع كائن System.Drawing.Bitmap ويمكنك حفظ ملف صورة على القرص / الدفق. يتم دعم العديد من تنسيقات الصور ، على سبيل المثال ، BMP و PNG و GIF و JPG و JPEG و TIFF و EMF وغيرها.

تشرح هذه المقالة كيفية:

- تحويل ورقة عمل إلى صورة
- قم بتحويل كل صفحة في ورقة العمل إلى صورة

توضح هذه المهمة كيفية استخدام Aspose.Cells لتحويل ورقة عمل من مصنف قالب إلى ملف صورة.

### **إعداد المشروع**

1.  أولاً،[تحميل Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1.  قم بتثبيته على جهاز الكمبيوتر الخاص بك. الجميع[Aspose](http://www.aspose.com/)المكونات ، عند تثبيتها ، تعمل في وضع التقييم. لا يوجد حد زمني لوضع التقييم ويقوم فقط بحقن العلامات المائية في المستندات المنتجة. ابدأ الآن Visual Studio.Net وأنشئ تطبيق وحدة تحكم جديد. يستخدم هذا المثال تطبيق وحدة تحكم C# ، ولكن يمكنك استخدام VB.NET أيضًا. قم بإضافة مرجع إلى Aspose.Cells في المشروع الذي تم إنشاؤه.

### **تحويل ورقة العمل إلى ملف الصورة**

 لقد أنشأت مصنفًا جديدًا في Microsoft Excel وأضفت بعض البيانات في ورقة العمل الأولى:**Testbook.xlsx** (1 ورقة عمل). بعد ذلك ، قم بتحويل ورقة عمل ملف القالب Sheet1 إلى ملف صورة يسمى SheetImage.jpg.

 فيما يلي الكود المستخدم من قبل المكون لإنجاز المهمة. يقوم بتحويل الورقة 1 بتنسيق**Testbook.xlsx** إلى ملف صورة لشرح مدى سهولة هذا التحويل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى ملف صورة حسب الصفحة**

يوضح هذا المثال كيفية استخدام Aspose.Cells لتحويل ورقة عمل من مصنف قالب يحتوي على عدة صفحات إلى ملف صورة واحد لكل صفحة.

### **تحويل ورقة العمل إلى صورة بالصفحة**

 لقد أنشأت مصنفًا جديدًا في Microsoft Excel وأضفت بعض البيانات في ورقة العمل الأولى:**Testbook2.xlsx** (1 ورقة عمل).

الآن ، قم بتحويل ورقة عمل ملف القالب Sheet1 إلى ملفات صور (ملف واحد لكل صفحة). نظرًا لأنني قمت بالفعل بإنشاء تطبيق وحدة التحكم لأداء مهمة النسخ ، فسوف أتخطى خطوات إنشاء تطبيق وحدة التحكم هذه وانتقل مباشرةً إلى خطوات تحويل ورقة العمل.

فيما يلي الكود المستخدم من قبل المكون لإنجاز المهمة. يقوم بتحويل الورقة 1 في Testbook2.xls إلى ملفات الصور حسب الصفحة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

