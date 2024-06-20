---
title: Aspose.Cells.GridWeb ı .NET Core ile nasıl kullanılır
type: docs
weight: 40
url: /tr/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: Bu makale, .net core web uygulamasında GridWeb ın nasıl kullanılacağını tanıtır
---

{{% alert color="primary" %}} 

Bu konu, Visual Studio.NET 2019'u kullanarak .NET Core uygulamalarında Aspose.Cells.GridWeb'ı nasıl kullanacağını açıklar. Bu konu, Aspose.Cells.GridWeb ile çalışan başlangıç düzeyi geliştiriciler için faydalıdır.

{{% /alert %}} 
## **.NET Core ile Aspose.Cells.GridWeb Kullanımı**
Bu konu, Visual Studio 2019'da örnek bir web sitesi oluşturarak Aspose.Cells.GridWeb'in nasıl kullanılacağını göstermektedir. İşlem adımlara ayrılmıştır.
### **Adım 1: Yeni Bir Proje Oluşturma**
1. Visual Studio 2019'u açın.
1. **Dosya** menüsünden **Yeni**'yi seçin, ardından **Proje**'yi seçin.
   Yeni proje iletişim kutusu açılır.
1. Visual Studio yüklü proje şablonlarından **ASP.NET Core Web Uygulaması**'nı seçin ve **İleri**'ye tıklayın.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. Projenin konumunu ve adını belirtin ve **Oluştur**'a tıklayın.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. **Web Uygulaması (Model-Görünüm-Kontrolcü)** şablonunu seçin ve **ASP .NET Core 2.1**'in seçili olduğundan emin olun. 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. **Oluştur**'a tıklayın.
### **Adım 2: Başlangıç görünümünü kontrol etme**
Yeni oluşturulan proje tarayıcıda varsayılan şablonu gösterir.



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Adım 3: Aspose.Cells.GridWeb Ekleme**
1. Aşağıdaki Nuget Paketlerini projeye ekleyin

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Aspose.Cells.GridWeb Paketi Ekle

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Görünümler klasöründeki **_ViewImports.cshtml** dosyasına aşağıdakileri ekleyin.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Değişikliklerden sonra dosya aşağıdaki gibi görünecektir

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. HomeController'ın Index metoduna aşağıdaki kodu ekleyin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

SessionStorePath ve ImportExcelFile yolunu güncellemeyi unutmayın.

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. **Index.cshtml** dosyasına aşağıdaki kodu ekleyin, Görünüm > Ana dizininde.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

Değişikliklerden sonra dosya aşağıdaki gibi görünecektir.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Session desteği ve GridScheduedService'ı Startup.cs dosyasına ekleyin
   1. ConfigureServices yöntemine aşağıdaki kod parçacığını ekleyin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Configure yöntemine aşağıdaki kod parçacığını ekleyin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. **wwwroot/js** dizinine en son acw_client'i yerleştirin {{% alert color="primary" %}}   {{% /alert %}}
1. Tüm genel düzen eylemleri için varsayılan işlemleri sağlayabilen acw rotası haritasıyla başa çıkmak için **AcwController**'i Denetleyicilere ekleyin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Adım 4: Uygulamayı Test Etme**
Uygulama çalıştırıldığında aşağıdaki resimde gösterildiği gibi çıktı alınır.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
