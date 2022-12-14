---
title: إعلان
type: docs
weight: 30
url: /ar/net/declaration/
---
{{% alert color="primary" %}} 

بشكل عام ، تتطلب كافة مكونات Aspose .NET تعيين أذونات ثقة كاملة. والسبب هو أن مكونات Aspose for .NET تحتاج إلى الوصول إلى إعدادات التسجيل وملفات النظام بخلاف الدليل الظاهري لعمليات معينة مثل تحليل الخطوط وما إلى ذلك. علاوة على ذلك ، تستند مكونات Aspose for .NET (بما في ذلك Aspose.Cells for .NET) إلى فئات النظام الأساسية .NET التي تتطلب أيضًا أذونات الثقة الكاملة مجموعة في كثير من الحالات.

{{% /alert %}} 
## **الثقة الجزئية / تحدي الثقة المتوسطة**
يقوم مقدمو خدمة الإنترنت الذين يستضيفون تطبيقات متعددة من شركات مختلفة في الغالب بفرض مستوى أمان متوسط الثقة. علاوة على ذلك ، في بعض الأحيان تحتاج إلى استضافة تطبيقات متعددة على خادم مشترك ، كما هو الحال في مزود خدمة الإنترنت أو سيناريوهات أخرى ، يجب عليك استخدام مستوى الثقة المتوسط لتقييد التطبيقات. يوفر مستوى الثقة المتوسط ASP.NET بيئة تنفيذ مقيدة مناسبة لعزل العديد من التطبيقات المستضافة على خوادم ISP. في حالة .NET 2.0 ، قد يحدد مستوى الأمان هذا القيود التالية التي قد تؤثر على قدرة Aspose.Cells for .NET على الأداء بشكل صحيح ، على سبيل المثال:

- **RegistryPermission غير متوفر**. هذا يعني أنه لا يمكنك الوصول إلى السجل ، وهو مطلوب لتعداد الخطوط المثبتة عند عرض جداول البيانات أو المستندات الأخرى.
- **FileIOPermission مقيد**هذا يعني أنه لا يمكنك الوصول إلا إلى الملفات الموجودة في التسلسل الهرمي للدليل الظاهري لتطبيقك. من المحتمل أن يعني هذا أنه لا يمكن قراءة الخطوط أثناء التصدير.
## **استخدم Aspose.Cells for .NET في مجموعة أذونات الثقة المتوسطة**
يمكنك اتباع بعض التوصيات لتشغيل Aspose.Cells for .NET على مستوى الثقة المتوسطة أو بيئة الخادم المشتركة:

- لتعيين ملف الترخيص في التعليمات البرمجية الخاصة بك ، من الأفضل أن تتصل بطريقة License.SetLicense (Stream) بدلاً من ذلك بعد الحصول على ملف الترخيص في التدفقات.
- يجب تعيين دليل الخطوط (الذي يمكن الوصول إليه بإذن). إذا لم تكن هناك طريقة للوصول إلى الملف على الخادم ، فيرجى إضافة ملفات الخطوط المطلوبة إلى التطبيق الخاص بك.
- في وضع الثقة الجزئية ، لا يتم دعم تحويل الشكل إلى EMF ، لذا قم بتعيين نوع الصورة المصدرة (للأشكال) إلى تنسيقات صور أخرى.

راجع المثال التالي الذي يوضح كيفية استخدام / تشغيل Aspose.Cells for .NET في وضع الثقة المتوسطة.

{{< highlight "csharp" >}}

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





