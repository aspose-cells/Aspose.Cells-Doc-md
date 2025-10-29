---
title: البدء
type: docs
weight: 10
url: /ar/net/getting-started/
---

{{% alert color="primary" %}} 

ستعرض لك هذه الصفحة كيفية تثبيت Aspose Cells وإنشاء تطبيق Hello World.

{{% /alert %}}

## **التثبيت**

### **ثبت Aspose.Cells عبر NuGet**

NuGet هو أسهل طريقة لتنزيل وتثبيت Aspose.Cells for .NET. 

1. افتح Microsoft Visual Studio ومدير حزم NuGet. 
1. ابحث عن "aspose.cells" للعثور على Aspose.Cells for .NET المطلوبة. 
1. انقر فوق "تثبيت"، سيتم تنزيل Aspose.Cells for .NET والإشارة إليها في مشروعك.
**![ثبت Aspose Cells عبر NuGet](install-through-nuget.png)**

يمكنك أيضًا تنزيله من صفحة الويب nuget ل aspose.cells: 
[حزمة NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/)

[المزيد من التفاصيل](/cells/ar/net/installation/)

### **ثبت Aspose.Cells على نظام التشغيل Windows**

1. قم بتنزيل Aspose.Cells.msi من الصفحة التالية:
[تنزيل Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. انقر نقرًا مزدوجًا على Aspose Cells msi واتبع التعليمات لتثبيته:

**![تثبيت Aspose Cells على نظام التشغيل Windows](install-on-windows.png)**

[المزيد من التفاصيل](/cells/ar/net/installing-aspose-cells-on-windows/)

### **تثبيت Aspose.Cells على نظام التشغيل لينكس**

في هذا المثال، استخدم Ubuntu لأظهر كيفية البدء باستخدام Aspose.Cells على نظام التشغيل لينكس.

1. قم بإنشاء تطبيق .netcore، وسمه "AsposeCellsTest".
2. افتح ملف "AsposeCellsTest.csproj"، وأضف الأسطر التالية إليه للإشارة إلى حزمة Aspose.Cells:
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="25.10" />
  </ItemGroup>
{{< /highlight >}}
3. افتح المشروع باستخدام VSCode على Ubuntu:
**![تثبيت Aspose Cells على نظام التشغيل لينكس](install-on-linux.png)**
4. قم بتشغيل الاختبار باستخدام الكود التالي:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

ملاحظة: Aspose.Cells لـ .NetStandard يمكن أن تدعم متطلباتك على نظام التشغيل لينكس.

ينطبق على: NetStandard2.0، NetCore2.1، NetCore3.1، Net5.0، Net6.0 والإصدار المتقدم.

### **تثبيت Aspose.Cells على نظام التشغيل macOS**

في هذا المثال، استخدم macOS High Sierra لأظهر كيفية البدء باستخدام Aspose.Cells على نظام التشغيل macOS.

1. قم بإنشاء تطبيق .netcore، وسمه "AsposeCellsTest".
2. افتح التطبيق باستخدام Visual Studio for Mac، ثم قم بتثبيت Aspose Cells من خلال NuGet:
**![تثبيت Aspose Cells على نظام التشغيل macOS](install-on-mac-os.png)**
3. قم بتشغيل الاختبار باستخدام الكود التالي:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. إذا كنت بحاجة إلى استخدام ميزات تتعلق بالرسومات، يرجى تثبيت libgdiplus في نظام التشغيل macOS، انظر:
[كيفية تثبيت libgdiplus في نظام التشغيل macOS](/cells/ar/net/how-to-install-libgdiplus-in-macos/)

ملاحظة: Aspose.Cells لـ .NetStandard يمكن أن تدعم متطلباتك على نظام التشغيل macOS.

ينطبق على: NetStandard2.0، NetCore2.1، NetCore3.1، Net5.0، Net6.0 والإصدار المتقدم.

### [**Run Aspose Cells in Docker**](/cells/ar/net/how-to-run-aspose-cells-in-docker/)

### **كيفية استخدام مكتبة الرسومات على منصات غير ويندوز مع Net6**

يستخدم Aspose.Cells for Net6 الآن SkiaSharp كمكتبة الرسومات، كما هو موصى به في [بيان رسمي من مايكروسوفت](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md). لمزيد من التفاصيل حول استخدام Aspose.Cells مع NET6، يرجى الاطلاع على [كيفية تشغيل Aspose.Cells لـ .Net6](/cells/ar/net/how-to-run-aspose-cells-for-net6/).

## **إنشاء تطبيق مرحبًا بالعالم**

تقوم الخطوات التالية بإنشاء تطبيق مرحبًا بالعالم باستخدام واجهة برمجة التطبيقات لـ Aspose.Cells:

1. إذا كان لديك ترخيص، ثم [قم بتطبيقه](/cells/ar/net/licensing/).
   إذا كنت تستخدم النسخة التجريبية، فتخطى خطوط الكود المتعلقة بالترخيص.
1. إنشاء مثيل من فئة [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) لإنشاء ملف إكسل جديد، أو فتح ملف إكسل موجود.
١. الوصول إلى أي خلية مرغوبة في ورقة العمل في ملف إكسل.
1. إدراج كلمات **Hello World!** في الخلية التي تم الوصول إليها.
1. إنشاء ملف Microsoft Excel المعدل.

يتم توضيح تنفيذ الخطوات أعلاه في الأمثلة أدناه.

### **مثال على الشفرة: إنشاء مصنف جديد**

يُنشئ المثال التالي مصنفًا جديدًا من البداية، يدرج "مرحبا بالعالم!" في الخلية A1 في الصفحة العمل الأولى، ويحفظ كملف Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **مثال على الشفرة: فتح ملف موجود**

يُفتح المثال التالي ملف قالب Microsoft Excel موجود "Sample.xlsx"، يدرج "مرحبا بالعالم!" في الخلية A1 في الصفحة العمل الأولى، ويحفظ كملف Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
