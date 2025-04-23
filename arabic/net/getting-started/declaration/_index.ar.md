---
title: الإعلان
type: docs
weight: 30
url: /ar/net/declaration/
---

{{% alert color="primary" %}} 

بشكل عام، جميع مكونات Aspose .NET تتطلب إعدادات أمان Full Trust. السبب في ذلك هو أن مكونات Aspose ل .NET تحتاج إلى الوصول إلى إعدادات التسجيل وملفات النظام بخلاف الدليل الظاهري لعمليات معينة مثل تحليل الخطوط وما إلى ذلك. علاوة على ذلك، تعتمد مكونات Aspose ل .NET (بما في ذلك Aspose.Cells for .NET) على فئات النظام الأساسي .NET التي تتطلب أيضًا إعدادات Full Trust في كثير من الحالات.

{{% /alert %}} 
## **تحدي الثقة الجزئية / الثقة المتوسطة**
يفرض معظم مزودي خدمة الإنترنت مستوى أمان الثقة المتوسطة عند استضافة تطبيقات متعددة من شركات مختلفة. علاوة على ذلك، في بعض الأحيان تحتاج إلى استضافة تطبيقات متعددة على خادم مشترك، مثل في مزود الخدمة الإنترنت أو سناريوهات أخرى، يجب أن تستخدم مستوى الثقة المتوسطة لتقييد التطبيقات. يوفر مستوى الثقة المتوسطة في ASP.NET بيئة تنفيذ مقيدة تكون مناسبة لعزل التطبيقات المتعددة المستضافة على خوادم مزودي الخدمة الإنترنت. في حالة .NET 2.0، يمكن أن يحدد مثل هذا المستوى الأماني القيود التالية التي يمكن أن تؤثر على قدرة Aspose.Cells for .NET على الأداء بشكل صحيح، على سبيل المثال:

- **لا تتوفر إذنات السجل**. يعني هذا أنه لا يمكنك الوصول إلى سجل التسجيل، والذي يُطلب لتعداد الخطوط المثبتة عند تقديم جداول بيانات أو وثائق أخرى.
- **تقييد إذنات FileIOPermission**. يعني هذا أنه يمكنك فقط الوصول إلى الملفات في تسلسل الدليل الظاهري لتطبيقك. يعني هذا بشكل محتمل أنه لا يمكن قراءة الخطوط خلال التصدير.
## **استخدام Aspose.Cells for .NET بمجموعة إذنات الثقة المتوسطة**
يمكنك اتباع بعض التوصيات لتشغيل Aspose.Cells for .NET على مستوى الثقة المتوسطة أو بيئة الخادم المشتركة:

- لتعيين ملف ترخيص في كودك، من الأفضل أن تقوم بالاتصال بطريقة License.SetLicense(Stream) بعد الحصول على ملف الترخيص إلى تدفق.
- يجب تعيين مجلد الخطوط (الذي يمكن الوصول إليه بإذن). إذا لم يكن هناك طريقة للوصول إلى الملف على الخادم، يرجى إضافة ملفات الخطوط اللازمة إلى تطبيقك.
- في وضع الثقة الجزئية، لا يتم دعم تحويل الشكل إلى EMF، لذا قم بتعيين نوع الصورة المصدر (للأشكال) إلى صيغ صور أخرى.

انظر إلى المثال التالي الذي يوضح كيفية استخدام/تشغيل Aspose.Cells for .NET في وضع الثقة المتوسطة.

{{< highlight csharp >}}

 // Instantiate the License object

Aspose.Cells.License lic = new Aspose.Cells.License();

// Get the license file into stream

System.IO.Stream stream = System.IO.File.OpenRead(MapPath("~") + @"\Aspose.Cells.lic");

// Set the License stream

lic.SetLicense(stream);

// Close the stream

stream.Close();

// Set the fonts directory

CellsHelper.FontDir = MapPath("~") + @"\Fonts";

//Open the template file

Workbook workbook = new Workbook(MapPath("~") + @"\test.xlsx");

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

// Set the image type to other format instead of using the default image type, that is, EMF

pdfSaveOptions.ImageType = System.Drawing.Imaging.ImageFormat.Png;

// Save the PDF file

workbook.Save(MapPath("~") + @"\dest.pdf", pdfSaveOptions);

// Save the XLSX file

workbook.Save(MapPath("~") + @"\dest.xlsx");



{{< /highlight >}}





{{< app/cells/assistant language="csharp" >}}
