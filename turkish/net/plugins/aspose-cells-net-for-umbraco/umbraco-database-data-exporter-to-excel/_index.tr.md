---
title: Umbraco Veritabanı Verilerini Excel e Aktar
type: docs
weight: 20
url: /tr/net/umbraco-database-data-exporter-to-excel/
---

## **Giriş**
Aspose .NET Database Data Exporter for Umbraco Modülü, kullanıcıların yerel veya uzak veritabanı tablolarından, görünümlerden ve özel sorgudan doğrudan Microsoft Excel veya OpenOffice Elektronik Tabloya veri aktarmasına olanak tanır. Bu modül, Aspose.Cells'in sağladığı güçlü elektronik tablo oluşturma özelliğini sergilemektedir. Bu ilk sürüm, İhracat işlemini basit ve kullanımı kolay hale getirmek için aşağıdaki harika özelliklerle zenginleştirilmiştir
### **Modül Özellikleri**
Bu eklentinin ilk sürümü aşağıdaki özelliklere sahiptir:

- Yerel MS SQL Server Veritabanına Bağlanma İzni
- Uzak MS SQL Server Veritabanına Bağlanma İzni
- Bağlanılan veritabanından Tüm Tabloları Doldurma
- Bağlanılan veritabanından Tüm Görünümleri Doldurma
- Özel Sorgu Yazma İzni
- İçeriği otomatik olarak kolon uzunluğuna sığacak biçimde uyarlama
- Excel hücrelerindeki 32k'dan uzun dizeyi atlamak için izin verme (LoadOptions)
- Kalın Metin olarak Başlık Sütunu biçimlendirme uygulama
- Veri Kaynağı olarak kullanma izni (Tablo, Görünümler, Özel Sorgu)
- Verileri Microsoft Excel Belgesine Aktarma (.xls, .xlsx ve .xlsb)
- Verileri Sekme sınırlı metin belgesine aktarma (*.txt)
- Verileri CSV'ye Aktar (Virgülle Sınırlı) (*.csv)
- Verileri OpenDöküman Elektronik Tabloya Aktar (*.ods)
- İhracat öncesinde istenen çıkış biçimini seçme seçeneği.
- İhrac edilen belge, otomatik olarak indirilmek üzere tarayıcıya gönderilir. 

.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)
## **Sistem Gereksinimleri ve Desteklenen Platformlar**
### **Sistem Gereksinimleri**
Aspose .NET Veritabanı Veri Dışa Aktarıcısı için Excel için Umbraco modülünü kurmak için aşağıdaki gereksinimlerin karşılanmış olması gerekmektedir:

- Umbraco 6.2.5 & Umbraco 6 sürümleri
- MS SQL Sunucusu ile Umbraco
- Microsoft .Net Framework 4.0

**Not:** Bu sürümde Umbraco 7 ve üstü desteklenmemektedir. Geri bildiriminizi bekliyoruz ve Umbraco 7 için destek eklemeyi dört gözle bekliyoruz.
### **Desteklenen Platformlar**
Modül tüm sürümlerde desteklenir

- ASP.NET 4.0'ta çalışan Umbraco 6.0
## **İndirme**
Aspose .NET Cells Database Data Exporter to Excel for Umbraco modülünü aşağıdaki konumlardan birinden indirebilirsiniz

- [Umbraco Projeleri](https://goo.gl/BPrWm2)
- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsUmbracoDatatoExcel)
## **Yüklemek**
İndirdikten sonra lütfen bu paketi Umbraco web sitenize yüklemek için aşağıdaki adımları izleyin:

1. Örneğin `http://www.myblog.com/umbraco` üzerindeki Umbraco **Geliştirici** bölümüne giriş yapın
1. Ağaçtan **Paketler** klasörünü genişletin
1. Buradan paket kurmanın iki yolu vardır: **Yerel paket yükle**'yi seçin veya **Umbraco Paket Deposu'nu** göz atın.
1. **Yerel paket** kurarsanız, paketi açmayın, sadece zip'i Umbraco'ya yükleyin
1. Ekrandaki talimatları izleyin

**Not:** Kurulum sırasında ‘Maximum request length exceeded’ hatası alabilirsiniz. Bu sorunu Umbraco web.config dosyanızdaki ‘maxRequestLength’ değerini güncelleyerek kolayca çözebilirsiniz.
<httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
## **Kullanarak**
Aspose .NET Database Data Exporter to Excel for Umbraco modülünü kurduktan sonra web sitenizde kullanmaya başlamak gerçekten çok basittir. Lütfen başlamak için bu basit adımları izleyin

1. Örneğin `http://www.myblog.com/umbraco/` üzerindeki Umbraco **Geliştirici** bölümüne giriş yaptığınızdan emin olun
1. Ekranın sol alt kısmındaki bölümler listesinde **Ayarlar**'ı tıklayın.
1. **Şablonlar** düğümünü genişletin ve örneğin Metin Sayfası'yı seçin.
1. Seçilen şablon içinde veri dışa aktarma düğmesini eklemek istediğiniz konumu seçin. Genellikle sayfanın sağ üst kısmına veya sayfanın alt kısmına eklemek istersiniz.
1. Üst menü şeridinde **Makro Ekle**'yi tıklayın.
1. **Makro Seçin** (Aspose .NET Database Data Exporter to Excel for Umbraco) üzerinden, nedavce kurduğunuz Aspose .NET Database Data Exporter to Excel for Umbraco makrosunu seçin ve **Tamam**'ı tıklayın.

Ayrıntılar için lütfen aşağıdaki ekran görüntüsünü kontrol edin. 

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_2)

Sayfanıza Aspose .NET Database Data Exporter to Excel modülünü başarıyla eklediniz.

![todo:image_alt_text](umbraco-database-data-exporter-to-excel_1)

1. MSSQL Server Bağlantı Dizesi Girin veya Ön Yüklü Olanı Kullanın
1. Veri Kaynağı Türünü Seçin (Tablo, Görünüm, Özel Sorgu)
1. Veri Kaynağını Seçin veya Girin (Tablo, Görünüm, Özel Sorgu)
1. Dışa Aktarma Türünü Seçin
1. Veri Dışa Aktarımını Tıklayın
1. İstenen dosya otomatik olarak indirilecektir.
## **Video Demo**
Modülün çalışmasını görmek için lütfen aşağıdaki [videoya](https://www.youtube.com/watch?v=MkfKyeLTauE) göz atın.
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

- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.DatabaseDataExportertoExcel)
#### **Kaynak kodunu yapılandırmak için**
Aşağıdakileri açıp kaynak kodunu genişletmek için aşağıdakilere sahip olmanız gerekir

- Visual Studio 2010 veya daha yükseği

Başlamak için lütfen bu basit adımları izleyin

1. Kaynak kodunu indirin/kopyalayın.
1. Visual Studio 2010'u açın ve **Dosya** > **Proje Aç**'ı seçin
1. İndirdiğiniz en yeni kaynak kodunu bulup **örneğin Aspose.DatabaseDataExportertoExcel.sln**'i açın
