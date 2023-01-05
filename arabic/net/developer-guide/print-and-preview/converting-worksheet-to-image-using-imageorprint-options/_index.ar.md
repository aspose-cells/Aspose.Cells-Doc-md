---
title: تحويل ورقة العمل إلى صورة باستخدام خيارات ImageOrPrint
type: docs
weight: 90
url: /ar/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

تم تصميم هذا المستند لتوفير فهم تفصيلي لكيفية تحويل ورقة العمل إلى ملف صورة وتطبيق خيارات مختلفة للصورة والطباعة ، وخيارات مثل الدقة ، وضغط TIFF ، وتنسيق الصورة وجودة الصفحة.

{{% /alert %}}

## **حفظ أوراق العمل في الصور - مناهج مختلفة**

في بعض الأحيان ، قد تحتاج إلى تقديم أوراق العمل الخاصة بك كتمثيل تصويري. أنت بحاجة إلى تقديم صور ورقة العمل في تطبيقاتك أو صفحات الويب الخاصة بك. قد تحتاج إلى إدراج الصور في مستند Word أو ملف PDF أو عرض تقديمي PowerPoint أو استخدامها في سيناريو آخر. ما عليك سوى عرض ورقة العمل كصورة بحيث يمكنك استخدامها في مكان آخر. يدعم Aspose.Cells تحويل أوراق العمل في ملفات Excel إلى صور. كما يدعم Aspose.Cells تعيين خيارات مختلفة مثل تنسيق الصورة ودقة الوضوح (الرأسية والأفقية) وجودة الصورة وخيارات الصورة والطباعة الأخرى.

يمكنك تجربة أتمتة Office ولكن أتمتة Office لها عيوبها الخاصة. هناك العديد من الأسباب والمشكلات المعنية: على سبيل المثال ، الأمان والاستقرار وقابلية التوسع والسرعة والسعر والميزات. باختصار ، هناك العديد من الأسباب ، أهمها أن Microsoft يوصون بشدة ضد أتمتة المكاتب من حلول البرمجيات.

توضح هذه المقالة كيفية إنشاء تطبيق وحدة التحكم في Visual Studio .NET ، وإجراء تحويل ورقة العمل إلى صورة باستخدام خيارات مختلفة للصور والطباعة مع بضعة أسطر وأبسط من التعليمات البرمجية باستخدام Aspose.Cells API.

 تحتاج إلى الاستيراد[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)إلى برنامجك / مشروعك. لديها عدة فئات قيمة ، على سبيل المثال ،[**عرض الورقة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**عرض المصنف**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)إلخ.

ال[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) تمثل class ورقة عمل لعرض الصور لورقة العمل ، فهي تحتوي على ملف[**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)الطريقة التي يمكنها تحويل ورقة عمل مباشرة إلى ملف (ملفات) صورة محددة بالسمات أو الخيارات التي تريدها. يمكنه إرجاع كائن System.Drawing.Bitmap ويمكنك حفظ ملف صورة على القرص / الدفق. هناك العديد من تنسيقات الصور المدعومة ، على سبيل المثال BMP ، PNG ، GIFF ، JPEG ، TIFF ، EMF وما إلى ذلك.

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى صورة باستخدام خيارات ImageOrPrint.**

### **إنشاء مصنف قالب في Microsoft Excel**

لقد أنشأت مصنفًا جديدًا في MS Excel وأضفت بعض البيانات في ورقة العمل الأولى. الآن ، سأقوم بتحويل ورقة عمل ملف القالب "Sheet1" إلى ملف صورة "SheetImage.tiff" وسأطبق خيارات مختلفة للصور مثل الدقة الأفقية والرأسية ، و TiffCompression وما إلى ذلك.

### **قم بتنزيل وتثبيت Aspose.Cells**

 أولا ، أنت بحاجة إلى[تحميل](https://downloads.aspose.com/cells/net) Aspose.Cells لـ .Net. قم بتثبيته على جهاز الكمبيوتر الخاص بك. الجميع[Aspose](http://www.aspose.com/) المكونات ، عند تثبيتها ، تعمل في وضع التقييم. لا يوجد حد زمني لوضع التقييم ويقوم فقط بحقن العلامات المائية في المستندات المنتجة.

### **أنشئ مشروعًا**

ابدأ تشغيل Visual Studio. صافي وإنشاء تطبيق وحدة تحكم جديد. سيعرض هذا المثال تطبيق وحدة تحكم C# ، ولكن يمكنك استخدام VB.NET أيضًا.

### **أضف المراجع**

سيستخدم هذا المشروع Aspose.Cells. لذلك ، يجب عليك إضافة مرجع إلى مكون Aspose.Cells في مشروعك. على سبيل المثال ، أضف مرجعًا إلى…. \ Program Files \ Aspose \ Aspose.Cells for .NET \ Bin \ Net1.0 \ Aspose.Cells.dll

### **تحويل ورقة العمل إلى ملف صورة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **خيارات التحويل**

من الممكن حفظ صفحات معينة على الصورة. الكود التالي يحول أوراق العمل الأولى والثانية في مصنف إلى صور JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **تحويل الصور باستخدام WorkbookRender**

يمكنك التنقل خلال المصنف وتقديم كل ورقة عمل فيه إلى صورة منفصلة:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

