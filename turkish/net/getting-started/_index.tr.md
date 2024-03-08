---
title: Başlarken
type: docs
weight: 10
url: /tr/net/getting-started/
---
{{% alert color="primary" %}} 

Bu sayfada Aspose Cells'in nasıl kurulacağı ve Hello World uygulamasının nasıl oluşturulacağı gösterilecektir.

{{% /alert %}}

##  **Kurulum**

###  **Aspose.Cells ila NuGet'i yükleyin**

 NuGet, Aspose.Cells for .NET'i indirip kurmanın en kolay yoludur.

1.  Microsoft Visual Studio ve NuGet paket yöneticisini açın.
1.  İstediğiniz Aspose.Cells for .NET'i bulmak için "aspose.cells" ifadesini arayın.
1. "Yükle"ye tıklayın, Aspose.Cells for .NET indirilecek ve projenizde referans alınacaktır.
**![Aspose Cells'den NuGet'e kadar kurulum yapın](nuget.png aracılığıyla kurulum)**

 Ayrıca aspose.cells'in nuget web sayfasından da indirebilirsiniz:
[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/)

[Ayrıntılar için daha fazla adım](/cells/tr/net/installation/)

###  **Windows'a Aspose.Cells'i yükleyin**

1. Aspose.Cells.msi dosyasını aşağıdaki sayfadan indirin:
[Aspose.Cells.msi dosyasını indirin](https://downloads.aspose.com/cells/net/)
1. Aspose Cells msi'ye çift tıklayın ve yüklemek için talimatları izleyin:

**![Windows'a Aspose Cells'i yükleyin](install-on-windows.png)**

[Ayrıntılar için daha fazla adım](/cells/tr/net/installing-aspose-cells-on-windows/)

###  **Linux'a Aspose.Cells'i yükleyin**

Bu örnekte, Linux'ta Aspose.Cells'i kullanmaya nasıl başlayacağımı göstermek için Ubuntu'yu kullanıyorum.

1. "AsposeCellsTest" adlı bir .netcore uygulaması oluşturun.
2. "AsposeCellsTest.csproj" dosyasını açın, Aspose.Cells paket referansları için aşağıdaki satırları dosyaya ekleyin:
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="24.3" />
  </ItemGroup>
{{< /highlight >}}
3. Projeyi Ubuntu'da VSCode ile açın:
**![Linux'a Aspose Cells'i yükleyin](install-on-linux.png)**
4. testi aşağıdaki kodla çalıştırın:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Not: Aspose.Cells .NetStandard için linux gereksinimlerinizi destekleyebilir.

Şunlar için geçerlidir: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 ve gelişmiş sürüm.

###  **MAC OS'a Aspose.Cells'i yükleyin**

Bu örnekte, MAC OS'ta Aspose.Cells'i kullanmaya nasıl başlayacağımı göstermek için macOS High Sierra kullanıyorum.

1. "AsposeCellsTest" adlı bir .netcore uygulaması oluşturun.
2. Uygulamayı Mac için Visual Studio ile açın ve ardından Aspose Cells ila NuGet arasındaki sayıları yükleyin:
**![Aspose Cells'i macOS'a yükleyin](install-on-mac-os.png)**
3. testi aşağıdaki kodla çalıştırın:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Çizimle ilgili özellikleri kullanmanız gerekiyorsa lütfen libgdiplus'ı macOS'a yükleyin, bkz.:
[MacOS'ta libgdiplus nasıl kurulur](/cells/tr/net/how-to-install-libgdiplus-in-macos/)

Not: Aspose.Cells .NetStandard için MAC OS gereksinimlerinizi destekleyebilir.

Şunlar için geçerlidir: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 ve gelişmiş sürüm.

###  **[Docker'da Aspose Cells'i çalıştırın](/cells/net/how-to-run-aspose-cells-in-docker/)**

###  **Net6 ile Windows dışı platformlarda grafik kitaplığı nasıl kullanılır?**

 Net6 için Aspose.Cells artık grafik kitaplığı olarak SkiaSharp'ı kullanıyor.[Microsoft resmi beyanı](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) . Aspose.Cells'i NET6 ile kullanma hakkında daha fazla ayrıntı için lütfen bkz.[.Net6 için Aspose.Cells Nasıl Çalıştırılır](/cells/tr/net/how-to-run-aspose-cells-for-net6/).

##  **Hello World Uygulamasının Oluşturulması**

Aşağıdaki adımlar, Aspose.Cells API'i kullanarak Hello World uygulamasını oluşturur:

1.  Ehliyetin varsa o zaman[Uygula](/cells/tr/net/licensing/).
 Değerlendirme sürümünü kullanıyorsanız lisansla ilgili kod satırlarını atlayın.
1.  Bir örneğini oluşturun[Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook) Yeni bir Excel dosyası oluşturmak veya mevcut bir Excel dosyasını açmak için sınıfı kullanın.
1. Excel dosyasındaki bir çalışma sayfasının istediğiniz herhangi bir hücresine erişin.
1.  Kelimeleri ekleyin**Hello World!** erişilen bir hücreye.
1. Değiştirilen Microsoft Excel dosyasını oluşturun.

Yukarıdaki adımların uygulanması aşağıdaki örneklerde gösterilmiştir.

###  **Kod Örneği: Yeni Bir Çalışma Kitabı Oluşturma**

Aşağıdaki örnekte sıfırdan yeni bir çalışma kitabı oluşturulur ve "Hello World!" eklenir. ilk çalışma sayfasında A1 hücresine girer ve Excel dosyası olarak kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Kod Örneği: Mevcut Bir Dosyayı Açma**

Aşağıdaki örnek, mevcut bir Microsoft Excel şablon dosyasını "Sample.xlsx" açar ve "Hello World!" ilk çalışma sayfasında A1 hücresine girer ve Excel dosyası olarak kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
