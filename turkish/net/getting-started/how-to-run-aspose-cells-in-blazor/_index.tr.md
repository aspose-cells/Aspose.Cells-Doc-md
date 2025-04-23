---
title: Blazor da Aspose.Cells ı Nasıl Çalıştırılır
type: docs
weight: 138
url: /tr/net/how-to-run-aspose-cells-in-blazor/
description: Aspose.Cells i Blazor WebAssembly Uygulaması ve Blazor Sunucu Uygulamasında Nasıl Çalıştırılır Öğrenin.
keywords: C# ile Aspose.Cells i Blazor WebAssembly de çalıştırın, Aspose.Cells i Blazor WebAssembly de kullanın, Blazor WebAssembly Uygulaması ile Aspose.Cells
---

## Genel Bakış

Blazor, Microsoft tarafından geliştirilen ve JavaScript yerine C# ve .NET kullanarak etkileşimli, istemci tarafı web uygulamaları geliştirmeye olanak tanıyan bir web çerçevesidir. Blazor'un iki ana barındırma modeli vardır: **Blazor WebAssembly** ve **Blazor Server**. Her iki modelde de **Aspose.Cells for .NET** kullanılabilir.

## Aspose.Cells ile Blazor WebAssembly Uygulaması

Blazor WebAssembly, tarayıcıda WebAssembly kullanılarak istemci tarafında çalışır. Bu, geliştiricilerin .NET uygulamalarını doğrudan tarayıcıda çalıştırmasına ve sunucuya gerek olmadan görüntüleme yapmasına olanak tanır. **Aspose.Cells for .NET 25.1**'den itibaren, Aspose.Cells doğrudan Blazor WebAssembly Uygulamasında kullanılabilir. Bu örnekte, Aspose.Cells ile basit bir Blazor WebAssembly oluşturacak, metin ve şekiller içeren bir Excel dosyasını png resmi olarak render edecek ve ardından resmi bir sayfada göstereceksiniz.

### Blazor WebAssembly Uygulaması Oluşturma

Hadi, ilk Blazor WebAssembly Uygulaması ile Aspose.Cells'i VS2022 aracını kullanarak oluşturalım, aşağıdaki adımları takip edin:

1. **Blazor WebAssembly Standalone App** şablonuyla yeni bir proje oluşturun.

   ![webassembly_proje_tam_template.jpg](webassembly_proje_tam_template.jpg)

.NET 8.0 veya üzeri önerilen hedef çerçeveyi seçin.

   ![webassembly_framework_net9.jpg](webassembly_framework_net9.jpg)

3. Proje oluşturulduktan sonra, Aspose.Cells paketini projeye ekleyin. Aspose.Cells, SkiaSharp'e referans verir; WebAssembly'de SkiaSharp'in çalışması için "SkiaSharp.Views.Blazor" paketine ihtiyaç vardır.

   ```
   <PackageReference Include="Aspose.Cells" Version="25.1.1" />
   <PackageReference Include="SkiaSharp.Views.Blazor" Version="3.116.1" />
   ```

   *Lütfen, eklenen "SkiaSharp.Views.Blazor" paketinin sürümünün, Aspose.Cells for .NET tarafından referans verilen "SkiaSharp" sürümüyle karşılık geldiğinden emin olun. Aspose.Cells for .NET ve karşılık gelen "SKiaSharp" sürümlerinin sürümleri aşağıda açıklanmıştır:*

   | Aspose.Cells for .NET |                SkiaSharp                |
   | :-------------------: | :-------------------------------------: |
   |       = 25.1.1        |                 3.116.1                 |
   |       >=25.1.2        | 2.88.9(net6.0, net8.0), 3.116.1(net9.0) |

4. Projede "Pages" klasöründeki "Home.razor" dosyasına gidin, bazı veri ve şekiller eklemek için kod yazın ve görüntü olarak göstermek için render edin.

   ![webassembly_code.jpg](webassembly_code.jpg)

5. Projeye sağ tıklayın ve "Publish..." seçeneğini seçin, ardından projeyi AOT seçeneğiyle veya seçmeden dizine yayınlayın.

   ![webassembly_publish.jpg](webassembly_publish.jpg)

6. Yayınlandıktan sonra, çıktı dosyaları `publish/wwwroot` klasöründe bulunur. Bu dosyalar statik dosyalardır (HTML, JS, CSS, vb.), ve şu yollarla barındırılabilir:

   - **Yerel Web Sunucusu** (örn., `dotnet serve`, `nginx`, veya `Apache`).
   - **Bulut barındırma** (örn., Azure, AWS, Netlify, GitHub Pages).

   Örnek olarak `dotnet serve`'yi alalım:

   - `dotnet-serve` aracını yükleyin (eğer yüklü değilse):

     ```bash
     dotnet tool install -g dotnet-serve
     ```

   - Yayınlanan `wwwroot` dizinine gidin.

   - Sunucuyu başlatın:

     ```bash
     dotnet serve
     ```

7. Tarayıcınızı açın ve görüntülenen adrese gidin (örn., `http://localhost:1970`), çıktı resmi sayfada gösterilecektir.

   ![webassembly_output.jgp](webassembly_output.jpg)

### Blazor WebAssembly Uygulamasında Örnek Kod

Aşağıdaki örnek kod, Home.razor dosyasına dahildir:

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

### Sorun Çözüm

Currently(Jan 2025) there is a known issue of `dotnet` in the case that publishing a Blazor WebAssembly project which targets to net8.0 with .NET 9.0 SDK(.NET 9.0 SDK is installed and .NET 8.0 SDK is uninstalled if you upgraded Visual Studio to the version v17.12.x). For more info, check the link: <https://github.com/dotnet/runtime/issues/109951>.

```
System.PlatformNotSupportedException: PlatformNotSupported_HybridGlobalization, HashCode
   at System.Globalization.CompareInfo.GetHashCodeOfStringCore(ReadOnlySpan`1 , CompareOptions )
   at System.Globalization.CompareInfo.GetHashCode(ReadOnlySpan`1 , CompareOptions )
   at System.Globalization.CompareInfo.GetHashCode(String , CompareOptions )
   at System.CultureAwareComparer.GetHashCode(String )
   at System.StringComparer.GetHashCode(Object )
```

Durumunuz buysa, üç seçenek vardır:

1. .NET 8.0 SDK'yı yeniden yükleyin (kaldırıldıysa) ve çözüm düzeyinde bir "global.json" dosyası kullanarak kullanılan SDK'yı belirtin. İşte "global.json" dosyasına bir örnek:

   ```
   {
     "sdk": {
       "version": "8.0.300",
       "rollForward": "latestFeature"
     }
   }
   ```



2. Proje dosyasını güncelleyerek net9.0 hedefleyin.

3. Update Visual Studio to the version v17.12.4.(The issue <https://github.com/dotnet/runtime/issues/109951> is fixed.(updated on Jan 15, 2025))

## Aspose.Cells ile Blazor Sunucu Uygulaması

Bu örnekte, veriler ve grafikler ekleyen, bunları görüntüleyen basit bir Blazor Sunucu Uygulaması oluşturacaksınız. Proje oluşturma sırasında, ihtiyaçlarınıza göre ayarları yapılandırabilirsiniz. Örneğin, "Enable Docker" seçeneğini işaretlerseniz, Blazor uygulaması Docker'da derlenip çalıştırılabilir.

### Blazor Sunucu Uygulaması Oluşturma

Örnek olarak VS2022 aracını kullanarak, Aspose.Cells ile ilk Blazor Sunucu Uygulaması'nı oluşturmak için aşağıdaki adımları takip edin:
1. Dosya -> Yeni -> Proje'yi seçin ve blazer anahtar kelimesini kullanarak ilgili proje şablonunu seçin.
<br>
<img src="1.png" width=70% />
1. Proje adını "BlazorTest" olarak ayarlayın ve yolunu seçin.
<br>
<img src="2.png" width=70% />
1. Proje kullanılan kütüphaneleri ve diğer seçenekleri yapılandırın. Son olarak,"Oluştur" düğmesini tıklayarak ilk blazer projenizi oluşturun.
<br>
<img src="3.png" width=70% />
1. Projeye girdikten sonra, projenin altındaki "Bağımlılıklar"a tıklayın ve "NuGet Paketlerini Yönet..."'i seçerek Aspose.Cells kütüphanesini ekleyin.
<br>
<img src="4.png" width=70% />
1. Filtreleme için anahtar kelimeleri girin ve en son Aspose.Cells kütüphanesini yükleyin. Aynı anda SkiaSharp gibi bağımlı kütüphaneler de birlikte yüklenecektir.
<br>
<img src="5.png" width=70% />
1. Gerekli kütüphaneyi içe aktarmak için "Index.razor" dosyasını çift tıklatın ve düzenleyin. Bir miktar veri ve grafik ekleyin ve bunları görüntülemek için grafiklere dönüştürün.
<br>
<img src="6.png" width=70% />
1. Projeyi derleyip çalıştırın ve aşağıdaki sonuçları elde edeceksiniz.
<br>
<img src="7.png" width=70% />

### Blazor Sunucu Uygulamasında Örnek Kod

Aşağıdaki örnek kod, Index.razor dosyasına dahil edilmiştir:
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
