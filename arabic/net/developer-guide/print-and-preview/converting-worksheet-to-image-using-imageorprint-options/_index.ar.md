---
title: تحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة
type: docs
weight: 90
url: /ar/net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

هذا المستند مصمم لتوفير فهم مفصل حول كيفية تحويل ورقة العمل إلى ملف صورة وتطبيق خيارات مختلفة للصورة وخيارات الطباعة للصورة، مثل الدقة وضغط TIFF وتنسيق الصورة وجودة الصفحة وغيرها.

{{% /alert %}}

## **حفظ الأوراق العمل إلى صور - نهج مختلفة**

في بعض الأحيان، قد تحتاج إلى عرض ورقات العمل الخاصة بك كتمثيل بصري. عليك حقاً تقديم صور ورقة العمل في تطبيقاتك أو صفحات الويب. قد تحتاج إلى إدراج الصور في وثيقة Word أو ملف PDF أو عرض PowerPoint، أو استخدامها في سيناريو آخر ما. ببساطة ترغب في عرض ورقة عمل مقدمة كصورة بحيث يمكنك استخدامها في مكان آخر. Aspose.Cells يدعم تحويل ورقات العمل في ملفات Excel إلى صور. أيضًا، يدعم Aspose.Cells ضبط خيارات مختلفة مثل تنسيق الصورة، الدقة (عمودي وأفقي على حد سواء)، جودة الصورة، وخيارات الصورة والطباعة الأخرى.

قد تحاول Office Automation لكن لديها عيوبها الخاصة. هناك عدة أسباب وقضايا متورطة: على سبيل المثال، الأمان، الاستقرار، التوسعة، السرعة، السعر والميزات. بإختصار، هناك العديد من الأسباب، مع أن أهمها أن Microsoft نفسها توصي بشدة ضد استخدام التشغيل التلقائي لحلول البرمجيات.

يوضح هذا المقال كيفية إنشاء تطبيق وحدة تحكم في Visual Studio .NET، وأداء تحويل ورقة العمل إلى صورة باستخدام خيارات مختلفة للصورة والطباعة ببضع وأبسط أسطر من الشفرة باستخدام API Aspose.Cells.

تحتاج إلى استيراد النطاق الزمني [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) إلى برنامج/مشروعك. يوجد لديها العديد من الفئات القيمة، على سبيل المثال، [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)، [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)، وما إلى ذلك.

الفئة [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) تمثل ورقة عمل لإنشاء صور للورقة العمل، لديها طريقة [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) مكدسة يمكنها تحويل ورقة عمل مباشرة إلى ملف صورة أو ملفات (بصورة) بالسمات أو الخيارات المطلوبة. يمكن استرجاع كائن System.Drawing.Bitmap ويمكنك حفظ ملف الصورة على القرص/التيار. هناك العديد من تنسيقات الصور المدعومة، على سبيل المثال، BMP، PNG، GIF، JPEG، TIFF، EMF وهكذا.

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة**

### **إنشاء ملف عمل قالب في Microsoft Excel**

لقد أنشأت ورق عمل جديد في MS Excel وأضافت بعض البيانات في الورقة العمل الأولى. الآن، سأقوم بتحويل ورقة العمل في ملف القالب "Sheet1" إلى ملف صورة "SheetImage.tiff" وسأطبق خيارات الصور المختلفة مثل الدقة الأفقية والعمودية وضغط Tiff وما إلى ذلك.

### **تنزيل وتثبيت Aspose.Cells**

أولاً، تحتاج إلى [تنزيل](https://downloads.aspose.com/cells/net) Aspose.Cells for .Net. قم بتثبيته على جهاز التطوير الخاص بك. كل عناصر [Aspose](http://www.aspose.com/)، عند التثبيت تعمل في وضع التقييم. يوجد لوضع التقييم حدود زمنية وهو يضع علامات مائية فقط في المستندات المنتجة.

### **إنشاء مشروع**

ابدأ Visual Studio. Net وأنشئ تطبيق وحدة التحكم الجديد. سيظهر هذا المثال تطبيق وحدة التحكم C#، ولكن يمكنك استخدام VB.NET أيضًا.

### **إضافة الإشارات**

سيستخدم هذا المشروع Aspose.Cells. لذا، يجب عليك إضافة الإشارة إلى مكون Aspose.Cells في مشروعك. على سبيل المثال، أضف إشارة إلى ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll

### **تحويل ورقة العمل إلى ملف صورة**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **خيارات التحويل**

من الممكن حفظ صفحات محددة إلى صورة. يحول الرمز التالي الصفحتين الأولى والثانية في دفتر عمل إلى صور JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **تحويل الصور باستخدام WorkbookRender**

يمكن أن يحتوي ملف الصورة TIFF على أكثر من إطار واحد. يمكنك حفظ ورقة العمل بأكملها في صورة TIFF واحدة بإطارات أو صفحات متعددة:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

