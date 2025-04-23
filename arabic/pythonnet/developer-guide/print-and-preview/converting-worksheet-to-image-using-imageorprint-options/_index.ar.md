---
title: تحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة
type: docs
weight: 90
url: /ar/python-net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

هذا المستند مصمم لتوفير فهم مفصل حول كيفية تحويل ورقة العمل إلى ملف صورة وتطبيق خيارات مختلفة للصورة وخيارات الطباعة للصورة، مثل الدقة وضغط TIFF وتنسيق الصورة وجودة الصفحة وغيرها.

{{% /alert %}}

## **حفظ الأوراق العمل إلى صور - نهج مختلفة**

أحيانًا، قد تحتاج إلى عرض أوراق عملك كممثل تصويري. تحتاج إلى عرض صور أوراق العمل في تطبيقاتك أو صفحات الويب الخاصة بك. قد تحتاج إلى إدراج الصور في مستند Word، أو ملف PDF، أو عرض تقديمي PowerPoint، أو استخدامها في سيناريو آخر. ببساطة، تريد أن يتم عرض ورقة العمل كصورة لاستخدامها في مكان آخر. يدعم Aspose.Cells للبايثون via .NET تحويل أوراق العمل في ملفات Excel إلى صور. كما يدعم Aspose.Cells للبايثون via .NET تعيين خيارات مختلفة مثل تنسيق الصورة، الدقة (رأسياً وأفقياً)، جودة الصورة، وخيارات أخرى للطباعة والصورة.

قد تحاول Office Automation لكن لديها عيوبها الخاصة. هناك عدة أسباب وقضايا متورطة: على سبيل المثال، الأمان، الاستقرار، التوسعة، السرعة، السعر والميزات. بإختصار، هناك العديد من الأسباب، مع أن أهمها أن Microsoft نفسها توصي بشدة ضد استخدام التشغيل التلقائي لحلول البرمجيات.

توضح هذه المقالة كيفية إنشاء تطبيق وحدة تحكم في Visual Studio .NET، وتنفيذ تحويل ورقة العمل إلى صورة باستخدام خيارات صورة وطباعة مختلفة مع بعض خطوط الكود البسيطة باستخدام واجهة برمجة تطبيقات Aspose.Cells للبايثون via .NET.

تحتاج إلى استيراد النطاق الزمني [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) إلى برنامج/مشروعك. يوجد لديها العديد من الفئات القيمة، على سبيل المثال، [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)، [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)، وما إلى ذلك.

الفئة [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) تمثل ورقة عمل لإنشاء صور للورقة العمل، لديها طريقة [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) مكدسة يمكنها تحويل ورقة عمل مباشرة إلى ملف صورة أو ملفات (بصورة) بالسمات أو الخيارات المطلوبة. يمكن استرجاع كائن System.Drawing.Bitmap ويمكنك حفظ ملف الصورة على القرص/التيار. هناك العديد من تنسيقات الصور المدعومة، على سبيل المثال، BMP، PNG، GIF، JPEG، TIFF، EMF وهكذا.

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى صورة باستخدام خيارات ImageOrPrint**

### **إنشاء ملف عمل قالب في Microsoft Excel**

لقد أنشأت ورق عمل جديد في MS Excel وأضافت بعض البيانات في الورقة العمل الأولى. الآن، سأقوم بتحويل ورقة العمل في ملف القالب "Sheet1" إلى ملف صورة "SheetImage.tiff" وسأطبق خيارات الصور المختلفة مثل الدقة الأفقية والعمودية وضغط Tiff وما إلى ذلك.

### **تحويل ورقة العمل إلى ملف صورة**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}


## **تحويل الصور باستخدام WorkbookRender**

يمكن أن يحتوي ملف الصورة TIFF على أكثر من إطار واحد. يمكنك حفظ ورقة العمل بأكملها في صورة TIFF واحدة بإطارات أو صفحات متعددة:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

