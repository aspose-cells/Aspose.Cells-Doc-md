---
title: Başlarken
type: docs
weight: 10
url: /tr/net/getting-started/
---

{{% alert color="primary" %}} 

Bu sayfa, Aspose Cells'i nasıl kuracağınızı gösterecek ve bir Merhaba Dünya uygulaması oluşturmanıza yardımcı olacaktır.

{{% /alert %}}

## **Kurulum**

### **Aspose.Cells'i NuGet üzerinden yükleyin**

NuGet, Aspose.Cells for .NET indirmenin ve yüklemenin en kolay yoludur. 

1. Microsoft Visual Studio'yu açın ve NuGet paket yöneticisini açın. 
1. Arama yapın "aspose.cells" istenen Aspose.Cells for .NET bulmak için. 
1. "Yükle" üzerine tıklayın, Aspose.Cells for .NET projenizde indirilip referans olarak eklenir.
**![NuGet ile Aspose Cells'yi Yükle](install-through-nuget.png)**

Aspose.Cells için nuget web sayfasından da indirebilirsiniz: 
[Aspose.Cells for .NET NuGet Paketi](https://www.nuget.org/packages/Aspose.Cells/)

[Daha fazla adım detayı için](/cells/tr/net/installation/)

### **Windows üzerinde Aspose.Cells'i Yükle**

1. Aşağıdaki sayfadan Aspose.Cells.msi'yi indirin:
[Aspose.Cells.msi'yi İndirin](https://downloads.aspose.com/cells/net/)
1. Aspose Cells msi dosyasına çift tıklayın ve kurulum talimatlarını takip edin:

**![Aspose Cells'i Windows'ta Yükle](install-on-windows.png)**

[Daha fazla adım detayı için](/cells/tr/net/installing-aspose-cells-on-windows/)

### **Linux'ta Aspose.Cells'i Yükle**

Bu örnekte, Ubuntu kullanarak Linux'ta Aspose.Cells nasıl kullanılacağını gösteriyorum.

1. "AsposeCellsTest" adında bir .netcore uygulaması oluşturun.
2. "AsposeCellsTest.csproj" dosyasını açın, Aspose.Cells paket referansları için aşağıdaki satırları ekleyin:
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="25.10" />
  </ItemGroup>
{{< /highlight >}}
3. Ubuntu'da projeyi VSCode ile açın:
**![Aspose Cells'i Linux'ta Yükle](install-on-linux.png)**
4. Aşağıdaki kodla testi çalıştırın:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Not: Aspose.Cells For .NetStandard, linux'ta ihtiyacınızı destekleyebilir.

Uygulanabilir: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 ve gelişmiş sürüm.

### **MAC OS'ta Aspose.Cells'i Yükle**

Bu örnekte, Aspose.Cells'i MAC OS üzerinde nasıl kullanmaya başlayacağımı göstermek için macOS High Sierra'yı kullanıyorum.

1. "AsposeCellsTest" adında bir .netcore uygulaması oluşturun.
2. Visual Studio for Mac ile uygulamayı açın, daha sonra Aspose Cells'i NuGet ile yükleyin:
**![Aspose Cells'i macOS Üzerinde Yükle](install-on-mac-os.png)**
3. Aşağıdaki kodla testi çalıştırın:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Çizimle ilgili özellikleri kullanmanız gerekiyorsa, lütfen macOS'ta libgdiplus'ı yükleyin, bkz:
[macOS'ta libgdiplus Nasıl Yüklenir](/cells/tr/net/macos'ta-libgdiplus-nasil-yuklenir/)

Not: Aspose.Cells For .NetStandard MAC OS'ta gereksiniminizi destekleyebilir.

Uygulanabilir: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 ve gelişmiş sürüm.

### [**Run Aspose Cells in Docker**](/cells/tr/net/how-to-run-aspose-cells-in-docker/)

### **Net6 ile grafik kütüphanesinin kullanımı**

Aspose.Cells for Net6 artık grafiğin kütüphanesi olarak [Microsoft'ın resmi açıklamasında](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) önerildiği gibi SkiaSharp kullanıyor. NET6 ile Aspose.Cells kullanımı hakkında daha fazla bilgi için [Aspose.Cells for .Net6 Çalıştırma Nasıl Yapılır](/cells/tr/net/asp/asp-net-support-mac/) sayfasına bakınız.

## **Merhaba Dünya Uygulamasını Oluşturma**

Aşağıdaki adımlar, Aspose.Cells API'sini kullanarak Merhaba Dünya uygulamasını oluşturur:

1. Bir lisansınız varsa, [uygulayın](/cells/tr/net/licensing).
   Eğer değerlendirme sürümünü kullanıyorsanız, lisansla ilgili kod satırlarını atlayın.
1. Yeni bir Excel dosyası oluşturmak veya mevcut bir Excel dosyasını açmak için [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfından bir örnek oluşturun.
1. Excel dosyasındaki istenen hücreye erişin.
1. Erişilen bir hücreye **Merhaba Dünya!** kelimesini ekleyin.
1. Değiştirilmiş Microsoft Excel dosyasını oluşturun.

Yukarıdaki adımların uygulanışı aşağıdaki örneklerde gösterilmektedir.

### **Kod Örneği: Yeni Bir Workbook Oluşturma**

Aşağıdaki örnek, sıfırdan yeni bir çalışma kitabı oluşturur, ilk çalışma sayfasındaki A1 hücresine "Merhaba Dünya!" ekler ve Excel dosyası olarak kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Kod Örneği: Mevcut Bir Dosyayı Açma**

Aşağıdaki örnek, mevcut bir Microsoft Excel şablon dosyasını açar, ilk çalışma sayfasındaki A1 hücresine "Merhaba Dünya!" ekler ve Excel dosyası olarak kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
