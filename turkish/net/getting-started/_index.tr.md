---
title: Başlarken
type: docs
weight: 10
url: /tr/net/getting-started/
---
{{% alert color="primary" %}} 

Bu sayfa size Aspose Cells'i nasıl kuracağınızı ve Hello World uygulamasını nasıl oluşturacağınızı gösterecek.

{{% /alert %}}

##  **Kurulum**

###  **Aspose.Cells'den NuGet'e yükleyin**

 NuGet Aspose.Cells for .NET indirip kurmanın en kolay yolu.

1.  Microsoft Visual Studio ve NuGet paket yöneticisini açın.
1.  İstediğiniz Aspose.Cells for .NET'i bulmak için "aspose.cells" araması yapın.
1. "Yükle"ye tıklayın, Aspose.Cells for .NET indirilecek ve projenizde referans gösterilecektir.
**![Aspose Cells ila NuGet'i yükleyin](nuget.png aracılığıyla yükleme)**

 aspose.cells için nuget web sayfasından da indirebilirsiniz:
[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/)

[Ayrıntılar için daha fazla adım](/cells/tr/net/installation/)

###  **Aspose.Cells'i pencerelere yükleyin**

1. Aşağıdaki sayfadan Aspose.Cells.msi dosyasını indirin:
[Aspose.Cells.msi dosyasını indirin](https://downloads.aspose.com/cells/net/)
1. Aspose Cells msi dosyasına çift tıklayın ve yüklemek için talimatları izleyin:

**![Windows'ta Aspose Cells'i yükleyin](windows-on-windows.png)**

[Ayrıntılar için daha fazla adım](/cells/tr/net/installing-aspose-cells-on-windows/)

###  **Aspose.Cells'i Linux'a kurun**

Bu örnekte, Linux'ta Aspose.Cells'i kullanmaya nasıl başlayacağımı göstermek için Ubuntu kullanıyorum.

1. "AsposeCellsTest" adlı bir .netcore uygulaması oluşturun.
2. "AsposeCellsTest.csproj" dosyasını açın, Aspose.Cells paket referansları için içine aşağıdaki satırları ekleyin:
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="23.5" />
  </ItemGroup>
{{< /highlight >}}
3. Projeyi Ubuntu'da VSCode ile açın:
**![Linux'ta Aspose Cells'i kurun](linux-on-linux.png)**
4. testi aşağıdaki kodla çalıştırın:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Not: Aspose.Cells .NetStandard için linux gereksinimlerinizi destekleyebilir.

Şunlar için geçerlidir: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 ve gelişmiş sürüm.

###  **Aspose.Cells'i MAC OS'ye kurun**

Bu örnekte, MAC OS'de Aspose.Cells'i kullanmaya nasıl başlayacağımı göstermek için macOS High Sierra kullanıyorum.

1. "AsposeCellsTest" adlı bir .netcore uygulaması oluşturun.
2. Uygulamayı Mac için Visual Studio ile açın, ardından Aspose Cells'den NuGet'e yükleyin:
**![macOS'ta Aspose Cells'i yükleyin](install-on-mac-os.png)**
3. testi aşağıdaki kodla çalıştırın:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Çizimle ilgili özellikleri kullanmanız gerekiyorsa, lütfen macOS'ta libgdiplus'ı yükleyin, bkz.:
[macOS'ta libgdiplus nasıl kurulur](/cells/tr/net/how-to-install-libgdiplus-in-macos/)

Not: Aspose.Cells .NetStandard, MAC OS gereksinimlerinizi destekleyebilir.

Şunlar için geçerlidir: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 ve gelişmiş sürüm.

###  **[Aspose Cells'i Docker'da çalıştırın](/cells/net/how-to-run-aspose-cells-in-docker/)**

###  **Net6 ile Windows dışı platformlarda grafik kitaplığı nasıl kullanılır?**

 Net6 için Aspose.Cells, şu bölümde önerildiği gibi artık grafik kitaplığı olarak SkiaSharp'ı kullanıyor:[resmi açıklama Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) . Aspose.Cells'i NET6 ile kullanma hakkında daha fazla ayrıntı için lütfen bkz.[.Net6 için Aspose.Cells Nasıl Çalıştırılır](/cells/tr/net/how-to-run-aspose-cells-for-net6/).

##  **Hello World Uygulamasını Oluşturma**

Aşağıdaki adımlar, Aspose.Cells API'i kullanarak Hello World uygulamasını oluşturur:

1.  Ehliyetin varsa o zaman[uygula](/cells/tr/net/licensing/).
Değerlendirme sürümünü kullanıyorsanız, lisansla ilgili kod satırlarını atlayın.
1.  örneğini oluşturun[Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook) Yeni bir Excel dosyası oluşturmak veya mevcut bir Excel dosyasını açmak için sınıfı kullanın.
1. Excel dosyasındaki bir çalışma sayfasının istediğiniz herhangi bir hücresine erişin.
1.  kelimeleri ekle**Hello World!** erişilen bir hücreye
1. Değiştirilen Microsoft Excel dosyasını oluşturun.

Yukarıdaki adımların uygulanması aşağıdaki örneklerde gösterilmektedir.

###  **Kod Örneği: Yeni Bir Çalışma Kitabı Oluşturma**

Aşağıdaki örnek sıfırdan yeni bir çalışma kitabı oluşturur ve "Hello World!" ekler. ilk çalışma sayfasındaki A1 hücresine girer ve Excel dosyası olarak kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Kod Örneği: Mevcut Bir Dosyayı Açma**

Aşağıdaki örnek, mevcut bir Microsoft Excel şablon dosyası olan "Sample.xlsx"i açar, "Hello World!" ekler. ilk çalışma sayfasındaki A1 hücresine girer ve Excel dosyası olarak kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
