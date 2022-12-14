---
title: Aspose Cells ila NuGet'i yükleyin
type: docs
weight: 30
url: /tr/net/installation/
---
## **Aspose.Cells for .NET ila NuGet'i yükleyin**
NuGet, Aspose API'lerini for .NET indirip kurmanın en kolay yoludur. Microsoft Visual Studio'yu ve NuGet paket yöneticisini açın. İstediğiniz Aspose API'i bulmak için "aspose" araması yapın. "Yükle"ye tıklayın, seçilen API indirilecek ve projenizde referans gösterilecektir.

Not: Daha fazla bilgi için aspose.cells için nuget web sayfasını ziyaret edebilirsiniz:
[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/)

### **Paket Yöneticisi GUI'sini kullanarak Aspose.Cells'i kurun**
Paket yöneticisi GUI'sini kullanarak Aspose.Cells bileşenine başvurmak için şu adımları izleyin:

- Çözümünüzü/projenizi Visual Studio'da açın.
- Tıklamak**Aletler** -> **Kitaplık Paket Yöneticisi** -> **NuGet Paketlerini Yönet**Solution'dan. Aynı seçeneğe Çözüm Gezgini aracılığıyla da kolayca erişebilirsiniz. Çözüme veya projeye sağ tıklayın ve seçin**NuGet Paketlerini Yönet**bağlam menüsünden.
- Seçme**Çevrimiçi**Aspose.Cells .NET paketini bulmak için soldaki menüden arama metin kutusuna "Aspose.Cells" yazın.
- Tıkla**Düzenlemek**projenize en son sürümü yüklemek için Aspose.Cells for .NET girişinin yanındaki düğme.
### **Paket Yöneticisi Konsolunu kullanarak Aspose.Cells'i kurun**
Paket yöneticisi konsolunu kullanarak Aspose.Cells bileşenine başvurmak için aşağıdaki adımları takip edebilirsiniz:

- Çözümünüzü/projenizi Visual Studio'da açın.
- Seçme**Aletler** -> **Kitaplık Paket Yöneticisi** -> **Paket Yöneticisi Konsolu**menüden paket yöneticisi konsolunu açmak için.
 Uygulamanıza en son tam sürümü yüklemek için “Install-Package Aspose.Cells” komutunu yazın ve enter tuşuna basın. Alternatif olarak, düzeltmeleri içeren en son sürümün de kurulacağını belirtmek için komuta "-prerelease" sonekini ekleyebilirsiniz.
- Pencerenin sol alt kısmında indirme işleminin devam ettiğini gösteren "İndiriliyor Aspose.Cells..." ipucunun göründüğünü göreceksiniz.
- İndirdikten sonra aşağıdaki onay mesajlarını göreceksiniz. Aspose EULA'ya aşina değilseniz, URL'de atıfta bulunulan lisansı okumak iyi bir fikirdir.
- Artık Aspose.Cells'in sizin için başvurunuza başarıyla eklendiğini ve başvuruda bulunduğunu görmelisiniz.
## **Bir .NET Projesinden Aspose.Cells'e atıfta bulunulması**
Aspose.Cells'i bir uygulamada kullanmak için ona bir referans ekleyin. Visual Studio'yu kullanarak bir referans eklemek için:

1.  İçinde**Çözüm Gezgini**, referans eklemek istediğiniz proje düğümünü genişletin.
1.  sağ tıklayın**Referanslar** proje için düğüm ve seçin**Referans ekle** menüden.
1.  İçinde**Referans ekle** iletişim kutusunda .NET sekmesini seçin (varsayılan olarak seçilidir). MSI yükleyicisini kullanarak yüklediyseniz, üst bölmede Aspose.Cells görünecektir.
1.  Onu seçin ve tıklayın**Seçme**.

Yalnızca DLL dosyasını indirdiyseniz veya paketini açtıysanız:

1.  Aspose.Cells.dll dosyasını kullanarak bulun**Araştır** buton. Aspose.Cells görünmelidir**Seçilen Bileşenler** iletişim kutusunun bölmesi.
1.  Tıklamak**TAMAM** . Aspose.Cells referansı,**Referanslar** projenin düğümü.
### **Bileşene bir VS.NET 2010 İstemci Profili projesinden başvuru**
Projenizin Hedef çerçevesi .NET Framework 3.5/4 İstemci Profili ise, kurulum dizininizin net_ClientProfile klasöründe bulunan Aspose.Cells.dll bileşen dosyasını kullanın. Örneğin:

-  İçinde**Çözüm Gezgini** projeniz için VS.NET 2010, sağ tıklayın**Referanslar** ve seç**Referans ekle**.
-  seçin**Araştır** iletişim kutusunda sekmesine gidin ve Şunu ara açılır menüsüne tıklayın.
- Kurulum dizininizde Aspose.Cells.dll bileşen dosyasını bulun ve seçin, örneğin: .../Program Files/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(Ürünü MSI yükleyicisini kullanarak makinenize kurduğunuzdan emin olun. .)**
-  Tıklamak**TAMAM** iletişim kutusunu kapatmak için

{{% alert color="primary" %}} 

VS.NET 2010 projenizin hedef çerçevesi ".NET Çerçeve 4" veya başka ise, net4.0/net2.0 klasöründe bulunan Aspose.Cells.dll bileşen dosyasını kullanmanız yeterlidir.

{{% /alert %}} 
## **Bir .NET projesinden Aspose.Cells Grid Controls referansı**
Uygulamanızda bir kılavuz denetimi kullanmak için buna bir başvuru ekleyin. Visual Studio'da bir ızgara denetimine başvurmak için aşağıdakileri yapın:

-  İçinde**Çözüm Gezgini**, referans eklemek istediğiniz proje düğümünü genişletin.
-  sağ tıklayın**Referanslar** proje için düğüm ve seçin**Referans ekle** menüden.
-  İçinde**Referans ekle** iletişim kutusunda,**.NET sekmesi** (varsayılan olarak seçilidir). Aspose.Cells for .NET'i yüklemek için MSI yükleyicisini kullandıysanız, üst bölmede Aspose.Cells.GridDesktop ve Aspose.Cells.GridWeb görünür.
-  Onları seçin ve tıklayın**Seçme**.
- Aspose.Cells.GridDesktop ve Aspose.Cells.GridWeb referansları, projenin Referanslar düğümü altında görünür.

Yalnızca DLL dosyasını indirip paketinden çıkardıysanız:

-  Gözat düğmesini kullanarak Aspose.Cells.GridDesktop.dll ve Aspose.Cells.GridWeb.dll dosyalarını bulun. Aspose.Cells Grid Suite'e başvurulmuştur ve şu adreste görünmelidir:**Seçilen Bileşenler** iletişim kutusunun bölmesi.
-  Tıklamak**TAMAM.**
## **Kaldırma Aspose.Cells for .NET**
Aspose.Cells for .NET'i dağıtmak için MSI yükleyicisini kullandıysanız, bileşeni ve kontrolleri, ilgili demoları ve belgeleri tamamen kaldırmak için şu adımları izleyin:

-  itibaren**Başlama** menü, seç**Ayarlar** , bunu takiben**Kontrol Paneli**.
-  Tıklamak**Program Ekle/Kaldır**.
- Aspose.Cells for .NET'i (sürüm) seçin.
-  Tıklamak**Değiştir/Kaldır** Aspose.Cells'i kaldırmak için.
