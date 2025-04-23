---
title: NuGet aracılığıyla Aspose Cells i yükleyin
type: docs
weight: 30
url: /tr/net/installation/
---


## **Aspose.Cells for .NET'yi NuGet aracılığıyla yükleyin**
.NET için Aspose API'lerini indirmek ve yüklemek için NuGet en kolay yöntemdir. Microsoft Visual Studio'yu açın ve NuGet paket yöneticisine erişin. Arama kutusuna "aspose" yazarak istediğiniz Aspose API'sini bulun. "Yükle" ye tıklayarak seçilen API indirilir ve projenize referans olarak eklenir.

Not: Daha fazla bilgi için aspose.cells için nuget web sayfasını ziyaret edebilirsiniz: 
[Aspose.Cells for .NET NuGet Paketi](https://www.nuget.org/packages/Aspose.Cells/)

### **Paket Yöneticisi GUI kullanarak Aspose.Cells'i yükleyin**
Paket yöneticisi GUI kullanarak Aspose.Cells bileşenine referans vermek için aşağıdaki adımları izleyin:

- Çözümünüzü/projenizi Visual Studio'da açın.
- **Tools** -> **Library Package Manager** -> **Çözüm'den NuGet Paketleri Yönetin**'i tıklayın. Ayrıca aynı seçeneğe Solution Explorer'dan kolayca erişebilirsiniz. Çözüm veya projeyi sağ tıklayarak bağlam menüsünden **NuGet Paketleri Yönetin**'i seçin.
- Sol taraftaki menüden **Çevrimiçi**'yi seçin ve Aspose.Cells .NET paketini bulmak için arama kutusuna “Aspose.Cells” yazın.
- Aspose.Cells for .NET girişinin yanındaki **Yükle** düğmesine tıklayarak en son sürümünü projenize yükleyin.
### **Paket Yöneticisi Konsolu kullanarak Aspose.Cells'i yükleyin**
Paket Yöneticisi Konsolunu kullanarak Aspose.Cells bileşenine başvuruda bulunmak için aşağıdaki adımları izleyebilirsiniz:

- Çözümünüzü/projenizi Visual Studio'da açın.
- Menüden **Tools** -> **Library Package Manager** -> **Paket Yöneticisi Konsolu**'nu seçerek paket yöneticisi konsolunu açın.
  - “Install-Package Aspose.Cells” komutunu yazın ve uygulamanıza en son tam sürümü yüklemek için enter tuşuna basın. Ayrıca en son sürümdeki hata düzeltmelerini içeren en son sürümün yükleneceğini belirtmek için komuta "-prerelease" ekleyebilirsiniz.
- İndirme işleminin olduğunu gösteren "Aspose.Cells indiriliyor..." ipucunu pencerenin sol alt köşesinde göreceksiniz.
- İndirme tamamlandığında aşağıdaki onay mesajlarını göreceksiniz. Aspose EULA hakkında bilgi sahibi değilseniz, URL'de belirtilen lisansı okumanız iyi bir fikirdir.
- Şimdi Aspose.Cells'in başarılı bir şekilde uygulamanıza eklendiğini ve referanslandığını göreceksiniz.
## **.NET Projesinden Aspose.Cells Başvurmak**
Bir uygulamada Aspose.Cells'i kullanmak için ona bir referans ekleyin. Visual Studio kullanarak bir referans eklemek için:

1. **Solution Explorer**'da referans eklemek istediğiniz proje düğümünü genişletin.
1. Projeye sağ tıklayarak **References** düğümünü seçin ve menüden **Add Reference**'ı seçin.
1. **Add Reference** iletişim kutusunda .NET sekmesini (varsayılan olarak seçilmiş) seçin. Eğer MSI yükleyicisini kullanarak yüklediyseniz, Aspose.Cells üst pencerede görünecektir.
1. Onu seçin ve **Select**'i tıklayın.

Eğer yalnızca DLL'yi indirdiyseniz veya açtıysanız:

1. **Gözat** düğmesini kullanarak Aspose.Cells.dll dosyasını bulun. Aspose.Cells, iletişim kutusunun **Seçilen Bileşenler** bölümünde görünmelidir.
1. **Tamam**'a tıklayın. Proje **Referanslar** düğümü altında Aspose.Cells referans gözükür.
### **VS.NET 2010 İstemci Profili projesinden bileşenin referans gösterilmesi**
Projenizin Hedef çerçevesi .NET Framework 3.5/4 İstemci Profili ise, kurulum dizininizdeki net_ClientProfile klasöründe bulunan Aspose.Cells.dll bileşen dosyasını kullanın. Örnek:

- VS.NET 2010 **Çözüm Gezgini**'nde projeniz için **Referanslar** üzerine sağ tıklayın ve **Referans Ekle**'yi seçin.
- İletişim kutusunda **Gözat** sekmesini seçin ve açılır menüden **Bul**'ü tıklayın.
- Kurulum dizininizde Aspose.Cells.dll bileşen dosyasını bulun ve seçin, örneğin: .../Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(Ürünü makinenize MSI yükleyicisi kullanarak kurduğunuzdan emin olun.)**
- İletişim kutusunu kapatmak için **Tamam**'ı tıklayın.

{{% alert color="primary" %}} 

VS.NET 2010 projesinin hedef çerçevesi ".NET Framework 4" veya başka ise, net4.0/net2.0 klasöründe bulunan Aspose.Cells.dll bileşen dosyasını kullanın.

{{% /alert %}} 
## **.NET projesinden Aspose.Cells Grid Kontrollerine referans verme**
Uygulamanızda bir grid kontrolü kullanmak için ona bir referans ekleyin. Visual Studio'da bir grid kontrolüne referans vermek için aşağıdaki adımları uygulayın:

- **Çözüm Gezgini**'nde, referans eklemek istediğiniz proje düğümünü genişletin.
- **Proje** için **Referanslar** düğümüne sağ tıklayın ve menüden **Referans Ekle**'yi seçin.
- **Referans Ekle** iletişim kutusunda **.NET sekmesi**'ni seçin (varsayılan olarak seçilidir). Aspose.Cells for .NET'yi yüklemek için MSI yükleyicisini kullandıysanız, Aspose.Cells.GridDesktop ve Aspose.Cells.GridWeb üst bölümde görünür.
- Onları seçin ve **Seç**'i tıklayın.
- Aspose.Cells.GridDesktop ve Aspose.Cells.GridWeb referansları proje **Referanslar** düğümü altında görünür.

DLL dosyasını indirip açtıysanız:

- Aspose.Cells.GridDesktop.dll ve Aspose.Cells.GridWeb.dll dosyalarını bulmak için **Gözat** düğmesini kullanın. Aspose.Cells Grid Suite referans gösterilmiş olmalı ve iletişim kutusunun **Seçilen Bileşenler** bölümünde görünmelidir.
- **Tamam**'ı tıklayın.
## **Aspose.Cells for .NET'nin Kaldırılması**
Aspose.Cells for .NET'yi tamamen kaldırmak ve denetimlerin, ilgili demoların ve belgelerin ortadan kaldırılması için MSI yükleyicisini kullandıysanız, aşağıdaki adımları izleyin:

- **Başlat** menüsünden, **Ayarlar**'ı, ardından **Denetim Masası**'nı seçin.
- **Ekle/Kaldır Programlar**'ı tıklayın.
- Aspose.Cells for .NET (sürüm)’ü seçin.
- Aspose.Cells'ı kaldırmak için **Düzenle/Kaldır**'ı tıklayın.
{{< app/cells/assistant language="csharp" >}}
