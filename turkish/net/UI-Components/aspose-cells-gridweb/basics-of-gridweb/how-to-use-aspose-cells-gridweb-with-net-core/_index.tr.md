---
title: Aspose.Cells.GridWeb'i .NET Core ile kullanma
type: docs
weight: 40
url: /tr/net/how-to-use-aspose-cells-gridweb-with-net-core/
---
{{% alert color="primary" %}} 

Bu konuda, Visual Studio.NET 2019 kullanılarak Aspose.Cells.GridWeb'in .NET Core uygulamalarıyla nasıl kullanılacağı açıklanmaktadır. Bu konu, Aspose.Cells.GridWeb ile çalışan başlangıç düzeyindeki geliştiriciler için yararlıdır.

{{% /alert %}} 
## **Aspose.Cells.GridWeb'i .NET Core ile kullanın**
Bu konu, Visual Studio 2019'da örnek bir web sitesi yaparak Aspose.Cells.GridWeb'in nasıl kullanılacağını gösterir. İşlem, adımlara ayrılmıştır.
### **1. Adım: Yeni Bir Proje Oluşturma**
1. Visual Studio 2019'u açın.
1.  itibaren**Dosya** menü, seç**Yeni** , o zamanlar**Proje**.
 Yeni bir proje oluştur iletişim kutusu açılır.
1.  Seçme**ASP.NET Temel Web Uygulaması** Visual Studio yüklü proje şablonlarından ve tıklayın**Sonraki**.

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1.  Projenin yeri ve adının bulunduğu bir yer belirleyin ve tıklayın.**Yaratmak**.

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1.  seçin**Web Uygulaması (Model-View-Controller)** şablon ve emin olun**ASP .NET Çekirdek 2.1** seçildi.

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1.  Tıklamak**Yaratmak**.
### **2. Adım: İlk görünümün kontrol edilmesi**
Yeni oluşturulan projeyi çalıştırmak, aşağıdaki resimde gösterildiği gibi tarayıcıda varsayılan şablonu gösterir.



![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **3. Adım: Aspose.Cells.GridWeb ekleme**
1. Aşağıdaki Nuget Paketlerini projeye ekleyin

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Aspose.Cells.GridWeb Paketi ekleyin

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Görünümler klasöründeki **_ViewImports.cshtml** dosyasına aşağıdakileri ekleyin.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Değişikliklerden sonra dosya böyle görünecek

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Aşağıdaki kodu HomeController'ın Index yöntemine koyun.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

SessionStorePath ve ImportExcelFile yolunu güncellemeyi unutmayın.

{{% /alert %}} 

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1.  içine aşağıdaki kodu ekleyin**index.cshtml** Görünüm > Giriş dizinindeki dosya.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

Değişiklikten sonra dosya bu şekilde görünecektir.

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Startup.cs dosyasına Oturum desteği ve GridScheduedService ekleyin
 1. Aşağıdaki kod parçacığını ConfigureServices yöntemine ekleyin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Aşağıdaki kod parçacığını Configure yöntemine ekleyin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. En son acw_client'i şu dizine koyun: **wwwroot/js** {{% alert color="primary" %}} {{% /alert %}}
1.  Eklemek**Acw Denetleyici**Genel düzenleme eylemi için tüm varsayılan işlemleri sağlayabilen acw rota haritasıyla ilgilenmek için Denetleyicilerde.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **4. Adım: Uygulamayı Test Edin**
Uygulamayı çalıştırmak, aşağıdaki resimde gösterilene benzer bir çıktı verecektir.

![yapılacaklar:resim_alternatif_metin](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
