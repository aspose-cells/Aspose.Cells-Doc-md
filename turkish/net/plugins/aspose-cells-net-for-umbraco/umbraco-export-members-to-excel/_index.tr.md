---
title: Umbraco Üyeleri Excel e Aktar
type: docs
weight: 10
url: /tr/net/umbraco-export-members-to-excel/
---

## **Giriş**

Üyeleri Excel'e Aktar, [Aspose.Cells](https://products.aspose.com/cells/net/) kullanarak Umbraco CMS'deki üyeleri Excel ve OpenDocument Yaprağına aktarmanıza olanak tanıyan bir Umbraco için bir Eklentidir. Kurulumdan sonra Umbraco arka ofisinde Üyeler ağacı altında **Üyeleri Excel'e Aktar** başlıklı yeni bir düğme belirir; buradan dilediğiniz üyeleri seçip çıkış formatını seçerek istenen doküman formatında üyeleri alabilirsiniz.

### **Modül Özellikleri**

Bu eklentinin ilk sürümü aşağıdaki özelliklere sahiptir:

- Üyeleri Microsoft Excel Belgelerine dışa aktarma (.xls, .xlsx ve .xlsb)
- Üyeleri Sekme ile ayrılmış metin belgesine dışa aktarma (.txt)
- Üyeleri CSV (Virgülle Ayrılmış) (*.csv) biçimine dışa aktarma
- Üyeleri OpenDocument Elektronik Tablosuna dışa aktarma (*.ods)
- Dışa aktarmadan önce istenen çıkış biçimini seçme seçeneği
- Tüm veya seçilen üyeleri seçilen çıkış belge biçimine dışa aktarma seçeneği
- .NET 2.0'dan başlayarak tüm .NET sürümleriyle çalışır.
- Dışa aktarılan belge otomatik olarak tarayıcıya indirilir
- Dışa aktarılan belgenin bir kopyası, ileride kullanılmak üzere sunucuda App_Data/AsposeMemberExport klasörüne kaydedilir.
- **4.5**+ sürümü de dahil olmak üzere geniş bir Umbraco sürüm yelpazesiyle uyumludur.

## **Sistem Gereksinimleri ve Desteklenen Platformlar**

### **Sistem Gereksinimleri**

Bu modülü kurmak için aşağıdaki gereksinimlerin karşılanması gerekmektedir:

- Umbraco 6.0 +

Bu modülü Umbraco'nun diğer sürümlerine kurmak istiyorsanız lütfen bize başvurun.

### **Desteklenen Platformlar**

Modül tüm sürümlerde desteklenir

- ASP.NET 4.0 üzerinde çalışan Umbraco

## **İndirme**

Export Members to Excel eklentisini aşağıdaki yerlerden birinden indirebilirsiniz

- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Yüklemek**

İndirdikten sonra lütfen bu paketi Umbraco web sitenize yüklemek için aşağıdaki adımları izleyin:

1. Örneğin, `http://www.myblog.com/umbraco/` adresine giriş yapın
1. Ağaçtan **Paketler** klasörünü genişletin
1. Buradan bir paket yüklemek için iki yol vardır: **Yerel paketi yükle**'yi seçin veya **Umbraco Paket Deposu'nu** göz atın
1. **Yerel paket** kurarsanız, paketi açmayın, sadece zip'i Umbraco'ya yükleyin
1. Ekrandaki talimatları izleyin

**Not:** Kurulum sırasında ‘Maximum request length exceeded’ hatası alabilirsiniz. Bu sorunu Umbraco web.config dosyanızdaki ‘maxRequestLength’ değerini güncelleyerek kolayca çözebilirsiniz.

{{< highlight java >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **Kullanarak**

Makroyu kurduktan sonra web sitenizde kullanmaya başlamak gerçekten çok basittir:

1. Umbraco **Developer** bölümüne giriş yaptığınızdan emin olun, örneğin `http://www.myblog.com/umbraco/`
1. Ekranın sol altındaki bölümler listesinde **Üyeler**'e tıklayın.
1. Ağacın sonunda, **Üyeleri Excel'e Aktar** başlıklı bir düğüm göreceksiniz, ona tıklayarak Excel'e Aktar eklentisini başlatın.
1. İstenen çıktı belge biçimini seçin ve İhracat yapmak için Üyeleri seçin. Tüm üyeleri ihraç etmek istiyorsanız üye seçimini bırakın veya başlık satırındaki onay kutusuna tıklayın.
1. Alt kısımdaki **İhracat** düğmesine tıklayın ve ihraç edilen dosyayı indirmeniz istenecektir.

## **Video Demo**

Eylemdeki modülü görmek için lütfen [video](https://www.youtube.com/watch?v=6PxZFvjWr2Y)'yu kontrol edin.

## **Destek, Genişletme ve Katkıda Bulunma**

### **Destek**

Aspose'un ilk günlerinden itibaren, müşterilerimize sadece iyi ürünler sunmanın yeterli olmayacağını biliyorduk. Ayrıca iyi bir hizmet sunmamız gerekiyordu. Kendi geliştiricileri olduğumuz için, teknik bir sorun veya yazılımdaki bir tuhaflık sizi yapmanız gereken şeyden alıkoyduğunda ne kadar sinir bozucu olduğunu anlıyoruz. Sorunları çözmek için buradayız, onları yaratmak için değil.

Bu nedenle ücretsiz destek sunuyoruz. Ürünlerimizi kullanan herkes, bunları satın almış olsun veya değerlendirme yapılıyor olsun, tam dikket ve saygıyı hak ediyor.

Aspose.Words .NET için Umbraco Modülleri ile ilgili herhangi bir sorunu veya öneriyi aşağıdaki platformlardan herhangi biri kullanarak kaydedebilirsiniz

- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Genişletme ve Katkı Sağlama**

Üyeleri Excel'e Aktar, açık kaynaklı bir Eklentidir ve kaynak kodu aşağıda listelenen ana sosyal kodlama web sitelerinde mevcuttur. Geliştiricilerin kaynak kodunu indirip kendi gereksinimlerine göre işlevselliği genişletmeleri teşvik edilmektedir.

#### **Kaynak Kodu**

En son kaynak kodunu aşağıdaki konumlardan birinden edinebilirsiniz

- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **Kaynak kodunu yapılandırmak için**

Aşağıdakileri açıp kaynak kodunu genişletmek için aşağıdakilere sahip olmanız gerekir

- Visual Studio 2010 veya daha yükseği

Başlamak için lütfen bu basit adımları izleyin

1. Kaynak kodunu indirin/kopyalayın.
1. Visual Studio 2010'u açın ve **Dosya** > **Proje Aç**'ı seçin
1. İndirdiğiniz en son kaynak koduna göz atın ve **örneğin Aspose.UmbracoMemberExportToExcel.sln**'yi açın
