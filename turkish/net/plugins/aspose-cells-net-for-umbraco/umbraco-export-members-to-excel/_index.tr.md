---
title: Umbraco Üyeleri Excel'e Aktar
type: docs
weight: 10
url: /tr/net/umbraco-export-members-to-excel/
---
## **Giriş**

 Üyeleri Excel'e Aktar, üyeleri Umbraco CMS'nizden bir Excel'e ve OpenDocument Elektronik Tablosuna aktarmanıza izin veren bir Umbraco Eklentisidir.[Aspose.Cells](https://products.aspose.com/cells/net/) . adlı yeni bir düğüm**Üyeleri Excel'e Aktar**kurulumdan sonra Umbraco arka ucundaki Üyeler ağacının altında belirir ve burada dışa aktarılacak üyeleri kolayca seçebilir ve üyeleri seçilen çıktı belgesi biçiminde almak için çıktı biçimini alabilirsiniz.

### **Modül Özellikleri**

Eklentinin bu ilk sürümü aşağıdaki özelliklere sahiptir:

- Üyeleri Microsoft Excel Belgelerine (.xls, .xlsx ve .xlsb) dışa aktarın
- Üyeleri Sekmeyle ayrılmış metin belgesine (.txt) dışa aktar
- Üyeleri CSV (Virgülle ayrılmış) (*.csv) olarak dışa aktar
- Üyeleri OpenDocument Elektronik Tablosuna (*.ods) aktarın
- Dışa aktarmadan önce istenen çıktı formatını seçme seçeneği
- Tüm veya seçili üyeleri seçili çıktı belgesi biçimine aktarma seçeneği.
- .NET 2.0'dan itibaren tüm .NET sürümleriyle çalışır.
- Dışa aktarılan belge, indirilmek üzere otomatik olarak tarayıcıya gönderilir
- Seçilirse, dışa aktarılan belgenin bir kopyası daha sonra kullanılmak üzere sunucudaki App_Data/AsposeMemberExport klasörüne kaydedilir.
-  Çok çeşitli Umbraco sürümleriyle uyumlu**4.5**+ **Sürüm 6 ve 7 dahil.**

## **Sistem Gereksinimleri ve Desteklenen Platformlar**

### **sistem gereksinimleri**

Bu modülü kurmak için aşağıdaki gereksinimleri karşılamanız gerekir:

- Umbraco 6.0 +

Bu modülü Umbraco'nun diğer sürümlerine kurmak isterseniz lütfen bizimle iletişime geçmekten çekinmeyin.

### **Desteklenen Platformlar**

Modül, tüm sürümlerinde desteklenir

- ASP.NET 4.0 üzerinde çalışan Umbraco

## **indiriliyor**

Üyeleri Excel'e Aktar Eklentisini aşağıdaki konumlardan birinden indirebilirsiniz.

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **yükleme**

İndirdikten sonra, bu paketi Umbraco web sitenize yüklemek için lütfen şu adımları izleyin:

1.  Umbraco'da oturum açın**Geliştirici** bölüm, örneğin `http://www.myblog.com/umbraco/`
1.  ağaçtan genişletin**Paketler** Klasör.
1.  Buradan bir paketi kurmanın iki yolu vardır: seçin**Yerel paketi kurun** veya göz atın**Umbraco Paket Deposu.**
1. eğer kurarsan**yerel paket**, paketi açmayın ama zip'i Umbraco'ya yükleyin.
1. Ekrandaki yönergeleri takip edin.

**Not:** Yükleme sırasında 'Maksimum istek uzunluğu aşıldı' hatası alabilirsiniz. Umbraco web.config dosyanızdaki 'maxRequestLength' değerini güncelleyerek bu sorunu kolayca çözebilirsiniz.

{{< highlight "java" >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **kullanma**

Makroyu yükledikten sonra web sitenizde kullanmaya başlamak gerçekten çok basit:

1. Umbraco'da oturum açtığınızdan emin olun**Geliştirici** bölüm, örneğin `http://www.myblog.com/umbraco/`
1.  Tıklamak**Üyeler** ekranın sol alt kısmındaki bölümler listesinde.
1.  Ağacın sonunda başlıklı bir düğüm göreceksiniz.**Üyeleri Excel'e Aktar** Excel'e Aktar eklentisini başlatmak için üzerine tıklayın.
1. İstediğiniz çıktı belgesi biçimini seçin ve dışa aktarılacak Üyeler'i seçin. Dilerseniz tüm üyeleri dışa aktarın, üye seçiminden çıkın veya başlık satırındaki onay kutusunu tıklayın.
1.  Tıklamak**İhracat** düğmesine basın ve dışa aktarılan dosyayı indirmeniz istenecektir.

## **Video Demosu**

 lütfen kontrol edin[video](https://www.youtube.com/watch?v=6PxZFvjWr2Y) modülü çalışırken görmek için aşağıdaki

## **Destekleyin, Genişletin ve Katkıda Bulunun**

### **Destek olmak**

Aspose'in ilk günlerinden itibaren müşterilerimize sadece iyi ürünler vermenin yeterli olmayacağını biliyorduk. Ayrıca iyi hizmet vermemiz gerekiyordu. Biz de geliştiriciyiz ve teknik bir sorun veya yazılımdaki bir tuhaflık, yapmanız gerekeni yapmanızı engellediğinde bunun ne kadar sinir bozucu olduğunu anlıyoruz. Sorunları çözmek için buradayız, onları yaratmak için değil.

Bu nedenle ücretsiz destek sunuyoruz. İster satın almış olsun ister bir değerlendirme yapıyor olsun, ürünümüzü kullanan herkes, tüm dikkatimizi ve saygımızı hak ediyor.

Umbraco Modülleri için Aspose.Words .NET ile ilgili sorun ve önerilerinizi aşağıdaki platformlardan herhangi birini kullanarak kaydedebilirsiniz.

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Genişletin ve Katkıda Bulunun**

Üyeleri Excel'e Aktar, açık kaynaklı bir Eklentidir ve kaynak kodu, aşağıda listelenen başlıca sosyal kodlama web sitelerinde mevcuttur. Geliştiricilerin kaynak kodunu indirmeleri ve işlevselliği kendi gereksinimlerine göre genişletmeleri önerilir.

#### **Kaynak kodu**

En son kaynak kodunu aşağıdaki konumlardan birinden alabilirsiniz.

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **Kaynak kodu nasıl yapılandırılır**

Kaynak kodunu açıp genişletmek için aşağıdakilerin kurulu olması gerekir.

- Visual Studio 2010 veya üzeri

Başlamak için lütfen bu basit adımları izleyin

1. Kaynak kodunu indirin/Klonlayın.
1.  Visual Studio 2010'u açın ve Seçin**Dosya** > **Açık Proje**
1.  İndirdiğiniz ve açtığınız en son kaynak koduna göz atın**örneğin Aspose.UmbracoMemberExportToExcel.sln**
