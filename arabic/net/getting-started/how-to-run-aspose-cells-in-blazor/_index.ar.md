---
title: كيفية تشغيل Aspose.Cells في Blazor
type: docs
weight: 138
url: /ar/net/how-to-run-aspose-cells-in-blazor/
description: تعلم كيفية تشغيل Aspose.Cells في تطبيق Blazor WebAssembly و Blazor Server.
keywords: C# تشغيل Aspose.Cells في Blazor WebAssembly، استخدام Aspose.Cells في Blazor WebAssembly، تطبيق Blazor WebAssembly مع Aspose.Cells
---

## نظرة عامة

Blazor إطار ويب طورته شركة Microsoft يتيح للمطورين بناء تطبيقات ويب تفاعلية من جانب العميل باستخدام C# و .NET بدلاً من JavaScript. يأتي Blazor بنموذجين رئيسيين للاستضافة: **Blazor WebAssembly** و **Blazor Server**. يمكنك استخدام **Aspose.Cells for .NET** مباشرة في كلا النموذجين.

## تطبيق Blazor WebAssembly مع Aspose.Cells

يعمل Blazor WebAssembly على جانب العميل في المتصفح باستخدام WebAssembly. يتيح للمطورين تشغيل تطبيقات .NET مباشرة في المتصفح دون الاعتماد على خادم للعرض. من إصدار **Aspose.Cells for .NET 25.1**، يمكن استخدام Aspose.Cells مباشرة في تطبيق Blazor WebAssembly. في هذا المثال، ستنشئ تطبيق Blazor WebAssembly بسيط مع Aspose.Cells، يعرض ملف إكسل يحتوي على نص وأشكال كصورة PNG، ثم يعرض الصورة على صفحة.

### إنشاء تطبيق Blazor WebAssembly

لنستخدم أداة VS2022 كمثال لإنشاء أول تطبيق Blazor WebAssembly مع Aspose.Cells، اتبع الخطوات التالية:

1. أنشئ مشروعًا جديدًا باستخدام قالب **Blazor WebAssembly Standalone App**.

   ![webassembly_project_template.jpg](webassembly_project_template.jpg)

2. اختر إطار العمل الهدف، ينصح بـ .NET 8.0 أو أعلى.

   ![webassembly_framework_net9.jpg](webassembly_framework_net9.jpg)

3. بعد إنشاء المشروع، أضف حزمة Aspose.Cells إلى المشروع. نظرًا لأن Aspose.Cells يربط بـ SkiaSharp، لجعل SkiaSharp يعمل في WebAssembly، يلزم حزمة "SkiaSharp.Views.Blazor".

   ```
   <PackageReference Include="Aspose.Cells" Version="25.1.1" />
   <PackageReference Include="SkiaSharp.Views.Blazor" Version="3.116.1" />
   ```

   *يرجى ملاحظة أن إصدار الحزمة المضافة "SkiaSharp.Views.Blazor" يجب أن يتوافق مع إصدار "SkiaSharp" المشار إليه في Aspose.Cells for .NET. توصف إصدارات Aspose.Cells for .NET والإصدارات المقابلة من "SkiaSharp" كالتالي:*

   | Aspose.Cells for .NET |                SkiaSharp                |
   | :-------------------: | :-------------------------------------: |
   |       = 25.1.1        |                 3.116.1                 |
   |       >=25.1.2        | 2.88.9 (net6.0، net8.0)، 3.116.1 (net9.0) |

4. انتقل إلى ملف "Home.razor" في مجلد "Pages" في المشروع، اكتب رمزًا لإضافة بعض البيانات والأشكال، وعرضها كصورة للعرض.

   ![webassembly_code.jpg](webassembly_code.jpg)

5. انقر بزر الماوس الأيمن على المشروع واختر "نشر..."، ثم انشر المشروع في مجلد مع خيار AOT أو بدونه.

   ![webassembly_publish.jpg](webassembly_publish.jpg)

6. بعد النشر، ستكون ملفات الإخراج موجودة في مجلد `publish/wwwroot`. هذه الملفات هي ملفات ثابتة (HTML، JS، CSS، إلخ)، لذلك يمكن استضافتها باستخدام:

   - **خادم ويب محلي** (على سبيل المثال، `dotnet serve`، `nginx`، أو `Apache`).
   - **استضافة سحابية** (على سبيل المثال، Azure، AWS، Netlify، GitHub Pages).

   لنأخذ مثال `dotnet serve` على النحو التالي:

   - قم بتثبيت أداة `dotnet-serve` (إذا لم تكن مثبتة بالفعل):

     ```bash
     dotnet tool install -g dotnet-serve
     ```

   - انتقل إلى دليل `wwwroot` المنشور.

   - ابدأ الخادم:

     ```bash
     dotnet serve
     ```

7. افتح متصفحك وادخل إلى العنوان المعروض (على سبيل المثال، `http://localhost:1970`)، ستظهر الصورة الناتجة على الصفحة.

   ![webassembly_output.jgp](webassembly_output.jpg)

### نموذج الكود في تطبيق Blazor WebAssembly

الكود النموذجي التالي مضمن في ملف Home.razor:

```cs
@page "/"
@using Aspose.Cells
@using Aspose.Cells.Drawing
@using Aspose.Cells.Rendering

<PageTitle>Home</PageTitle>

<h1>Aspose.Cells works in Blazor WebAssembly App</h1>

@if (imageSrc is not null)
{
    <img src="@imageSrc" alt="Output Image" style="float: left; margin-right: 10px;" />
}
else
{
    <p>Loading image...</p>
}

@code
{
    private string? imageSrc;

    protected override void OnInitialized()
    {
        imageSrc = "data:image/png;base64, " + Convert.ToBase64String(CreateFile());
    }

    private byte[] CreateFile()
    {
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        sheet.Cells["A1"].Value = "Aspose.Cells works in Blazor WebAssembly App!";

        sheet.PageSetup.PrintGridlines = true;
        sheet.PageSetup.PrintArea = "A1:F20";

        ShapeCollection shapes = sheet.Shapes;

        //Add rectangle shape
        shapes.AddRectangle(1, 0, 1, 0, 100, 150);

        //Add line shape
        shapes.AddLine(8, 0, 1, 0, 100, 150);

        //Add oval shape
        shapes.AddOval(13, 0, 1, 0, 100, 150);

        using MemoryStream ms = new();

        SheetRender render = new SheetRender(sheet, new ImageOrPrintOptions());
        render.ToImage(0, ms);

        return ms.ToArray();
    }
}
```

### استكشاف المشاكل وإصلاحها

Currently(Jan 2025) there is a known issue of `dotnet` in the case that publishing a Blazor WebAssembly project which targets to net8.0 with .NET 9.0 SDK(.NET 9.0 SDK is installed and .NET 8.0 SDK is uninstalled if you upgraded Visual Studio to the version v17.12.x). For more info, check the link: <https://github.com/dotnet/runtime/issues/109951>.

```
System.PlatformNotSupportedException: PlatformNotSupported_HybridGlobalization, HashCode
   at System.Globalization.CompareInfo.GetHashCodeOfStringCore(ReadOnlySpan`1 , CompareOptions )
   at System.Globalization.CompareInfo.GetHashCode(ReadOnlySpan`1 , CompareOptions )
   at System.Globalization.CompareInfo.GetHashCode(String , CompareOptions )
   at System.CultureAwareComparer.GetHashCode(String )
   at System.StringComparer.GetHashCode(Object )
```

إذا كانت هذه حالتك، فهناك ثلاثة خيارات للاختيار من بينها:

1. أعِد تثبيت .NET 8.0 SDK (إذا تم إلغاء تثبيته) واستخدم ملف "global.json" على مستوى الحل (نفس المجلد الذي يحتوي على ملف .sln) لتحديد SDK المستخدم. إليك مثال على ملف "global.json":

   ```
   {
     "sdk": {
       "version": "8.0.300",
       "rollForward": "latestFeature"
     }
   }
   ```



2. قم بتحديث ملف المشروع ليهدف إلى net9.0.

3. Update Visual Studio to the version v17.12.4.(The issue <https://github.com/dotnet/runtime/issues/109951> is fixed.(updated on Jan 15, 2025))

## تطبيق Blazor Server مع Aspose.Cells

في هذا المثال، ستقوم بإنشاء تطبيق Blazor Server بسيط يضيف بعض البيانات والرسومات، وي renderها كصور للعرض على صفحة الويب. أثناء عملية إنشاء المشروع، يمكنك تكوين الخيارات وفقًا لاحتياجاتك الشخصية. على سبيل المثال، عند تحديد خيار "تمكين Docker"، يمكن بعد ذلك بناء تطبيق Blazor وتشغيله داخل Docker..

### إنشاء تطبيق Blazor Server

لنستخدم أداة VS2022 كمثال لإنشاء أول تطبيق Blazor Server باستخدام Aspose.Cells، اتبع الخطوات أدناه:
1. حدد ملف -> جديد -> مشروع وقم بتصفية باستخدام كلمة blazer لتحديد قالب المشروع المقابل.
<br>
<img src="1.png" width=70% />
1. قم بتعيين اسم المشروع إلى "BlazorTest" وحدد المسار.
<br>
<img src="2.png" width=70% />
1. قم بتكوين المكتبات والخيارات الأخرى المستخدمة في المشروع. في النهاية، انقر على زر "إنشاء" لتوليد مشروع blazer الأول الخاص بك.
<br>
<img src="3.png" width=70% />
1. بعد دخول المشروع، انقر فوق "التبعيات" تحت المشروع واختر "إدارة حزم NuGet..." لإضافة مكتبة Aspose.Cells.
<br>
<img src="4.png" width=70% />
1. أدخل الكلمات الرئيسية للتصفية وقم بتثبيت مكتبة Aspose.Cells الأحدث. ستتم أيضًا تثبيت المكتبات التابعة مثل SkiaSharp معًا.
<br>
<img src="5.png" width=70% />
1. انقر نقرًا مزدوجًا فوق ملف "Index.razor" للتحرير واستيراد المكتبة المطلوبة. أضف بعض البيانات والرسومات، وقم بتقديمها في رسومات للعرض.
<br>
<img src="6.png" width=70% />
1. قم بتجميع وتشغيل المشروع، وستحصل على النتائج التالية.
<br>
<img src="7.png" width=70% />

### كود عيني في تطبيق خادم Blazor

تتضمن الكود العيني التالي في ملف Index.razor:
```
@page "/"
@using SkiaSharp;
@using Aspose.Cells;
@using Aspose.Cells.Drawing;
@using Aspose.Cells.Rendering;


<PageTitle>Index</PageTitle>

<h1>Hello, world!</h1>

Welcome to your new app.

<SurveyPrompt Title="How is Blazor working for you?" />

<img src="@imageSrc" />

@code
{
    private string imageSrc;

    public Index()
    {
        imageSrc = "data:image/png;base64, " + Convert.ToBase64String(CreateFile());
    }

    private byte[] CreateFile()
    {
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        sheet.Cells["A1"].Value = "test data for blazor";

        sheet.PageSetup.PrintGridlines = true;
        sheet.PageSetup.PrintArea = "A1:F20";

        ShapeCollection shapes = sheet.Shapes;

        //Add rectangle shape
        shapes.AddRectangle(1, 0, 1, 0, 100, 150);

        //Add line shape
        shapes.AddLine(8, 0, 1, 0, 100, 150);

        //Add oval shape
        shapes.AddOval(13, 0, 1, 0, 100, 150);

        using MemoryStream ms = new();

        SheetRender render = new SheetRender(sheet, new ImageOrPrintOptions());
        render.ToImage(0, ms);

        return ms.ToArray();
    }
}

```
{{< app/cells/assistant language="csharp" >}}
