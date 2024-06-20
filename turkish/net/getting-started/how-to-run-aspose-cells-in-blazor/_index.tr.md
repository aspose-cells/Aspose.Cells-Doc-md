---
title: Blazor da Aspose.Cells ı Nasıl Çalıştırılır
type: docs
weight: 138
url: /tr/net/how-to-run-aspose-cells-in-blazor/
description: Blazor da Aspose.Cells ı Nasıl Çalıştırılır ı Öğrenin.
keywords: C# Blazor da Aspose.Cells ı Çalıştırma, Blazor da Aspose.Cells Kullanma, Aspose.Cells ile Blazor Sunucu Uygulaması
---

## Genel Bakış

Blazor'da Aspose.Cells'ı çalıştırmak için .NET6 (veya daha sonraki) platformlarına ihtiyacınız olacak, önceki platformlarla (.netcore31 veya önceki) karşılaştırıldığında önemli bir fark grafik kütüphanesi ile ilgilidir. Bu resmi [Microsoft Belgesinde](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only)'de .NET6 veya sonraki sürümler için grafik kütüphanesi "System.Drawing.Common"'ın yalnızca Windows'ta destekleneceği açıklanmakta ve grafik kütüphanesini değiştirmek için önerilerde bulunmaktadır.

Apose.Cells ürünü için değerlendirmeyi gerçekleştirdik ve grafik kütüphanesinin göçünü tamamladık. Microsoft'un resmi belgesinde önerildiği gibi, .Net6 için Windows dışı sistemlerde System.Drawing.Common yerine SkiaSharp kullanıyoruz. Lütfen bu kritik değişikliğin Aspose.Cells 22.10.1 veya sonrasında .Net6 için geçerli olacağını unutmayın.

## Aspose.Cells ile Blazor Sunucu Uygulaması

Bu örnekte, bir blazor sunucu uygulaması oluşturarak bazı veri ve grafikler ekler ve bunları web sayfasında görüntülemek için görüntülere dönüştürürsünüz. Proje oluşturma aşamasında, kendi ihtiyaçlarınıza göre seçenekleri yapılandırabilirsiniz. Örneğin,"Enable Docker" seçeneğini işaretlediğinizde, blazor uygulaması Docker'da oluşturulabilir ve çalıştırılabilir.

### Blazor Sunucu Uygulaması Oluşturma

İlk blazor uygulamasını Aspose.Cells ile oluşturmak için aşağıdaki adımları izleyin:
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
<img src="5.png" width=70% />
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
