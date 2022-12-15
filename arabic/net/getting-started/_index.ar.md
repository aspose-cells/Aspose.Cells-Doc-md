---
title: ابدء
type: docs
weight: 10
url: /ar/net/getting-started/
---
{{% alert color="primary" %}} 

ستوضح لك هذه الصفحة كيفية تثبيت Aspose Cells وإنشاء تطبيق Hello World.

{{% /alert %}}

## **تثبيت**

### **قم بتثبيت Aspose.Cells حتى NuGet**

NuGet هو أسهل طريقة لتنزيل وتثبيت Aspose.Cells for .NET.

1.  افتح Microsoft Visual Studio و NuGet مدير الحزم.
1.  ابحث عن "aspose.cells" للعثور على Aspose.Cells for .NET المطلوب.
1. انقر فوق "تثبيت" ، سيتم تنزيل Aspose.Cells for .NET والإشارة إليه في مشروعك.
**!**

 يمكنك أيضًا تنزيله من صفحة الويب nuget لغرض معين.
[Aspose.Cells for .NET NuGet الحزمة](https://www.nuget.org/packages/Aspose.Cells/)

[مزيد من الخطوات للحصول على التفاصيل](/cells/ar/net/installation/)

### **قم بتثبيت Aspose.Cells على الويندوز**

1. تنزيل Aspose.Cells.msi من الصفحة التالية:
[تنزيل Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. انقر نقرًا مزدوجًا فوق Aspose Cells msi واتبع التعليمات لتثبيته:

**! [تثبيت Aspose Cells على windows] (install-on-windows.png)**

[مزيد من الخطوات للحصول على التفاصيل](/cells/ar/net/installing-aspose-cells-on-windows/)

### **قم بتثبيت Aspose.Cells على لينكس**

في هذا المثال ، أستخدم Ubuntu لإظهار كيفية بدء استخدام Aspose.Cells على نظام Linux.

1. قم بإنشاء تطبيق netcore ، باسم "AsposeCellsTest".
2. افتح الملف "AsposeCellsTest.csproj" ، أضف الأسطر التالية فيه للحصول على مراجع الحزمة Aspose.Cells:
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="22.12" />
  </ItemGroup>
{{< /highlight >}}
3. افتح المشروع باستخدام VSCode على Ubuntu:
**! [تثبيت Aspose Cells على لينكس] (install-on-linux.png)**
4. قم بإجراء الاختبار باستخدام الكود التالي:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

ملاحظة: Aspose.Cells بالنسبة إلى .NetStandard يمكنه دعم متطلباتك على نظام التشغيل Linux.

ينطبق على: NetStandard2.0 و NetCore2.1 و NetCore3.1 و Net5.0 و Net6.0 والإصدار المتقدم.

### **قم بتثبيت Aspose.Cells على MAC OS**

في هذا المثال ، أستخدم macOS High Sierra لإظهار كيفية بدء استخدام Aspose.Cells على نظام تشغيل MAC.

1. قم بإنشاء تطبيق netcore ، باسم "AsposeCellsTest".
2. افتح التطبيق باستخدام Visual Studio for Mac ، ثم قم بتثبيت Aspose Cells حتى NuGet:
**! [تثبيت Aspose Cells على macOS] (install-on-mac-os.png)**
3. قم بإجراء الاختبار باستخدام الكود التالي:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. إذا كنت بحاجة إلى استخدام الميزات المتعلقة بالرسم ، فالرجاء تثبيت libgdiplus في macOS ، راجع:
[كيفية تثبيت libgdiplus في macOS](/cells/ar/net/how-to-install-libgdiplus-in-macos/)

ملاحظة: Aspose.Cells بالنسبة لـ .NetStandard يمكنه دعم متطلباتك على نظام تشغيل MAC.

ينطبق على: NetStandard2.0 و NetCore2.1 و NetCore3.1 و Net5.0 و Net6.0 والإصدار المتقدم.

### **[تشغيل Aspose Cells في Docker] (/ cells / net / how-to-run-aspose-cells-in-docker /)**

### **كيفية استخدام مكتبة الرسومات على الأنظمة الأساسية التي لا تعمل بنظام Windows مع Net6**

 يستخدم Aspose.Cells لـ Net6 الآن SkiaSharp كمكتبة رسومات ، على النحو الموصى به في[بيان رسمي من Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) . لمزيد من التفاصيل حول استخدام Aspose.Cells مع NET6 ، يرجى مراجعة[كيفية تشغيل Aspose.Cells لـ NET6](/cells/ar/net/how-to-run-aspose-cells-for-net6/).

## **إنشاء تطبيق Hello World**

تؤدي الخطوات أدناه إلى إنشاء تطبيق Hello World باستخدام Aspose.Cells API:

1.  إذا كان لديك ترخيص ، إذن[قم بتطبيقه](/cells/ar/net/licensing/).
 إذا كنت تستخدم الإصدار التقييمي ، فتخط سطور التعليمات البرمجية المتعلقة بالترخيص.
1.  قم بإنشاء مثيل لـ[دفتر العمل](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة لإنشاء ملف Excel جديد ، أو فتح ملف Excel موجود.
1. قم بالوصول إلى أي خلية مرغوبة من ورقة العمل في ملف Excel.
1.  أدخل الكلمات**Hello World!** في خلية تم الوصول إليها.
1. قم بإنشاء ملف Excel Microsoft المعدل.

يتم توضيح تنفيذ الخطوات المذكورة أعلاه في الأمثلة أدناه.

### **نموذج التعليمات البرمجية: إنشاء مصنف جديد**

يقوم المثال التالي بإنشاء مصنف جديد من البداية ، ويدرج "Hello World!" في الخلية A1 في ورقة العمل الأولى وحفظها كملف Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **نموذج التعليمات البرمجية: فتح ملف موجود**

يفتح المثال التالي ملف قالب Excel Microsoft موجود "Sample.xlsx" ، ويدرج "Hello World!" في الخلية A1 في ورقة العمل الأولى وحفظها كملف Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
