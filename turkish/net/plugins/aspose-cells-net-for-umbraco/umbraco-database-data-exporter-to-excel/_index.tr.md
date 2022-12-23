---
title: Umbraco Veritabanı Verilerini Excel'e Aktarıcı
type: docs
weight: 20
url: /tr/net/umbraco-database-data-exporter-to-excel/
---
## **Giriş**
Aspose .NET Umbraco Modülü için Veritabanı Verilerini Excel'e Aktarıcı, kullanıcıların verileri doğrudan yerel veya uzak veritabanı tablolarından, görünümlerinden ve özel sorgu yoluyla Microsoft Excel veya OpenOffice Elektronik Tablosuna aktarmalarına olanak tanır. Bu modül, Aspose.Cells tarafından sağlanan güçlü elektronik tablo oluşturma özelliğini göstermektedir. Modülün bu ilk sürümü, Dışa Aktarma işlemini basit ve kullanımı kolay hale getirmek için aşağıdaki harika özelliklerle zenginleştirilmiştir.
### **Modül Özellikleri**
Eklentinin bu ilk sürümü aşağıdaki özelliklere sahiptir:

- Yerel MS SQL Server Veritabanına bağlanmaya izin ver
- Uzak MS SQL Server Veritabanına bağlanmaya izin ver
- Bağlı veritabanından tüm Tabloları doldurun
- Tüm Görünümleri bağlı veritabanından doldur
- Özel Sorgu yazmaya izin ver
- Sütunları içeriğin uzunluğuna Otomatik Sığdır.
- Excel hücrelerinde 32k'den fazla dize atlamaya izin ver (LoadOptions)
- Başlık Sütunu biçimlendirmesini Kalın Metin olarak uygula
- Veri Kaynağı olarak kullanılmasına izin ver (Tablo, Görünümler, Özel Sorgu)
- Verileri Microsoft Excel Belgelerine Aktar (.xls, .xlsx ve .xlsb)
- Verileri Sekmeyle ayrılmış metin belgesine (*.txt) Aktar
- Verileri CSV'e (Virgülle ayrılmış) (*.csv) Aktar
- Verileri OpenDocument Elektronik Tablosuna Aktarın (*.ods)
- Dışa aktarmadan önce istenen çıktı formatını seçme seçeneği.
- Dışa aktarılan belge, indirilmek üzere otomatik olarak tarayıcıya gönderilir.

.

![yapılacaklar:resim_alternatif_metin](umbraco-database-data-exporter-to-excel_1)
## **Sistem Gereksinimleri ve Desteklenen Platformlar**
### **sistem gereksinimleri**
Aspose .NET Database Data Exporter to Excel for Umbraco modülünü kurmak için aşağıdaki gereksinimleri karşılamanız gerekir:

- Umbraco 6.2.5 ve Umbraco 6 sürümleri
- MS SQL Server ile Umbraco
- Microsoft .Net Çerçeve 4.0

**Not:** Umbraco 7 ve üstü bu sürümde desteklenmemektedir. Geri bildirimlerinizi duymak ve bir sonraki sürümde Umbraco 7 için destek eklemek için sabırsızlanıyoruz.
### **Desteklenen Platformlar**
Modül, tüm sürümlerinde desteklenir

- ASP.NET 4.0 üzerinde çalışan Umbraco 6.0
## **indiriliyor**
Umbraco modülü için Aspose .NET Cells Database Data Exporter to Excel'i aşağıdaki lokasyonlardan birinden indirebilirsiniz.

- [ Umbraco Projeleri](https://goo.gl/BPrWm2)
- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsUmbracoDatatoExcel)
## **yükleme**
İndirdikten sonra, bu paketi Umbraco web sitenize yüklemek için lütfen şu adımları izleyin:

1.  Umbraco'da oturum açın**Geliştirici** bölüm, örneğin `http://www.myblog.com/umbraco`
1.  ağaçtan genişletin**Paketler** Klasör.
1.  Buradan bir paketi kurmanın iki yolu vardır: seçin**Yerel paketi kurun** veya göz atın**Umbraco Paket Deposu.**
1. eğer kurarsan**yerel paket**, paketi açmayın ama zip'i Umbraco'ya yükleyin.
1. Ekrandaki yönergeleri takip edin.

**Not:** Yükleme sırasında 'Maksimum istek uzunluğu aşıldı' hatası alabilirsiniz. Umbraco web.config dosyanızdaki 'maxRequestLength' değerini güncelleyerek bu sorunu kolayca çözebilirsiniz.
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
## **kullanma**
Aspose .NET Database Data Exporter to Excel for Umbraco modülünü yükledikten sonra web sitenizde kullanmaya başlamak gerçekten çok basit. Başlamak için lütfen bu basit adımları izleyin

1.  Umbraco'da oturum açtığınızdan emin olun**Geliştirici** bölüm, örneğin `http://www.myblog.com/umbraco/`
1.  Tıklamak**Ayarlar** ekranın sol alt kısmındaki bölümler listesinde.
1.  Genişletin**Şablonlar** düğümüne gidin ve eklemek istediğiniz şablonu seçin, örneğin Metin Sayfası.
1. Seçilen şablonda dışa aktarma düğmesinin eklenmesini istediğiniz konumu seçin. Genellikle sayfanın sağ üstüne veya sayfanın altına eklemek isteyebilirsiniz.
1.  Tıklamak**Makro Ekle** üst şeritte.
1.  İtibaren**Bir makro seçin** (Aspose .NET Database Data Exporter to Excel for Umbraco), en son yüklenen Aspose .NET Database Data Exporter to Excel for Umbraco makrosunu seçin ve tıklayın**Tamam**.

 Ayrıntılar için lütfen aşağıdaki ekran görüntüsünü kontrol edin.

![yapılacaklar:resim_alternatif_metin](umbraco-database-data-exporter-to-excel_2)

Aspose .NET Database Data Exporter to Excel modülünü sayfanıza başarıyla eklediniz.

![yapılacaklar:resim_alternatif_metin](umbraco-database-data-exporter-to-excel_1)

1. Önceden doldurulmuş MS SQL Server Bağlantı Dizesi Girin veya Kullanın
1. Seletec Veri Kaynağı Türü (Tablo, Görünüm, Özel Sorgu)
1. Veri Kaynağını Seçin veya Girin (Tablo, Görünüm, Özel Sorgu)
1. Dışa Aktarma Türünü Seçin
1. Verileri Dışa Aktar'a tıklayın
1. İstenen dosya otomatik olarak indirilecektir.
## **Video Demosu**
 lütfen kontrol edin[video](https://www.youtube.com/watch?v=MkfKyeLTauE) modülü çalışırken görmek için aşağıdaki
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

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.DatabaseDataExportertoExcel)
#### **Kaynak kodu nasıl yapılandırılır**
Kaynak kodunu açıp genişletmek için aşağıdakilerin kurulu olması gerekir.

- Visual Studio 2010 veya üzeri

Başlamak için lütfen bu basit adımları izleyin

1. Kaynak kodunu indirin/Klonlayın.
1.  Visual Studio 2010'u açın ve Seçin**Dosya** > **Açık Proje**
1.  İndirdiğiniz ve açtığınız en son kaynak koduna göz atın**örneğin Aspose.DatabaseDataExportertoExcel.sln**
