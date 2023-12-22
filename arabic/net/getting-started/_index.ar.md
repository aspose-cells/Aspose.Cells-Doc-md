---
title: ابدء
type: docs
weight: 10
url: /ar/net/getting-started/
---
{{% alert color="primary" %}} 

ستوضح لك هذه الصفحة كيفية تثبيت Aspose Cells وإنشاء تطبيق Hello World.

{{% /alert %}}

##  **تثبيت**

###  **قم بتثبيت Aspose.Cells حتى NuGet**

 NuGet أسهل طريقة للتحميل والتثبيت Aspose.Cells for .NET.

1.  افتح Microsoft Visual Studio ومدير الحزم NuGet.
1.  ابحث عن "aspose.cells" للعثور على Aspose.Cells for .NET المطلوب.
1. انقر على "تثبيت"، وسيتم تنزيل Aspose.Cells for .NET والإشارة إليها في مشروعك.
**![تثبيت Aspose Cells حتى NuGet](التثبيت من خلال nuget.png)**

 يمكنك أيضًا تنزيله من صفحة الويب nuget الخاصة بـ aspose.cells:
[Aspose.Cells for .NET NuGet الباقة](https://www.nuget.org/packages/Aspose.Cells/)

[المزيد من الخطوات للحصول على التفاصيل](/cells/ar/net/installation/)

###  **تثبيت Aspose.Cells على النوافذ**

1. قم بتنزيل Aspose.Cells.msi من الصفحة التالية:
[تحميل Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. انقر نقرًا مزدوجًا فوق Aspose Cells msi واتبع الإرشادات لتثبيته:

**![تثبيت Aspose Cells على النوافذ](install-on-windows.png)**

[المزيد من الخطوات للحصول على التفاصيل](/cells/ar/net/installing-aspose-cells-on-windows/)

###  **تثبيت Aspose.Cells على لينكس**

في هذا المثال، أستخدم Ubuntu لإظهار كيفية البدء في استخدام Aspose.Cells على نظام التشغيل Linux.

1. أنشئ تطبيق ‎.netcore باسم "AsposeCellsTest".
2. افتح الملف "AsposeCellsTest.csproj"، وأضف الأسطر التالية فيه لمراجع الحزمة Aspose.Cells:
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="23.12" />
  </ItemGroup>
{{< /highlight >}}
3. افتح المشروع باستخدام VSCode على Ubuntu:
**![تثبيت Aspose Cells على نظام التشغيل Linux](install-on-linux.png)**
4. قم بإجراء الاختبار باستخدام الكود التالي:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

ملاحظة: Aspose.Cells لـ .NetStandard يمكنه دعم متطلباتك على نظام التشغيل Linux.

ينطبق على: NetStandard2.0 وNetCore2.1 وNetCore3.1 وNet5.0 وNet6.0 والإصدار المتقدم.

###  **قم بتثبيت Aspose.Cells على نظام التشغيل MAC**

في هذا المثال، أستخدم macOS High Sierra لإظهار كيفية البدء في استخدام Aspose.Cells على نظام التشغيل MAC OS.

1. أنشئ تطبيق ‎.netcore باسم "AsposeCellsTest".
2. افتح التطبيق باستخدام Visual Studio for Mac، ثم قم بتثبيت Aspose Cells حتى NuGet:
**![تثبيت Aspose Cells على نظام التشغيل macOS](install-on-mac-os.png)**
3. قم بإجراء الاختبار باستخدام الكود التالي:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. إذا كنت بحاجة إلى استخدام الميزات المتعلقة بالرسم، فيرجى تثبيت libgdiplus في نظام التشغيل macOS، راجع:
[كيفية تثبيت libgdiplus في نظام التشغيل MacOS](/cells/ar/net/how-to-install-libgdiplus-in-macos/)

ملحوظة: Aspose.Cells لـ .NetStandard يمكنه دعم متطلباتك على نظام التشغيل MAC.

ينطبق على: NetStandard2.0 وNetCore2.1 وNetCore3.1 وNet5.0 وNet6.0 والإصدار المتقدم.

###  **[تشغيل Aspose Cells في Docker](/cells/net/how-to-run-aspose-cells-in-docker/)**

###  **كيفية استخدام مكتبة الرسومات على منصات غير Windows مع Net6**

 Aspose.Cells لـ Net6 يستخدم الآن SkiaSharp كمكتبة رسومات، على النحو الموصى به في[بيان رسمي Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) . لمزيد من التفاصيل حول استخدام Aspose.Cells مع NET6، يرجى الاطلاع على[كيفية تشغيل Aspose.Cells لـ .Net6](/cells/ar/net/how-to-run-aspose-cells-for-net6/).

##  **إنشاء تطبيق Hello World**

الخطوات أدناه تنشئ تطبيق Hello World باستخدام Aspose.Cells API:

1.  إذا كان لديك ترخيص، ثم[قم بتطبيقه](/cells/ar/net/licensing/).
 إذا كنت تستخدم الإصدار التقييمي، فتخطى سطور التعليمات البرمجية المتعلقة بالترخيص.
1.  إنشاء مثيل لـ[دفتر العمل](https://reference.aspose.com/cells/net/aspose.cells/workbook) لإنشاء ملف Excel جديد، أو فتح ملف Excel موجود.
1. الوصول إلى أي خلية مطلوبة من ورقة العمل في ملف Excel.
1.  أدخل الكلمات**Hello World!** في الخلية التي تم الوصول إليها.
1. قم بإنشاء ملف Excel Microsoft المعدل.

يتم توضيح تنفيذ الخطوات المذكورة أعلاه في الأمثلة أدناه.

###  **نموذج التعليمات البرمجية: إنشاء مصنف جديد**

يقوم المثال التالي بإنشاء مصنف جديد من البداية، وإدراج "Hello World!" في الخلية A1 في ورقة العمل الأولى وحفظها كملف Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **نموذج التعليمات البرمجية: فتح ملف موجود**

يفتح المثال التالي ملف قالب Excel Microsoft الموجود "Sample.xlsx"، ويدرج "Hello World!" في الخلية A1 في ورقة العمل الأولى وحفظها كملف Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
