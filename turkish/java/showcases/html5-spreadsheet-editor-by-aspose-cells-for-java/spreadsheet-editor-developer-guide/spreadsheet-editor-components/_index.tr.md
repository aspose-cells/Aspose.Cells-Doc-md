---
title: Hesap Tablosu Düzenleyicisi - Bileşenler
type: docs
weight: 50
url: /tr/java/spreadsheet-editor-components/
---
**İçindekiler**

- [index.html](#SpreadsheetEditor-Components-Index.html)
- [Çalışma Sayfası Görünümü](#SpreadsheetEditor-Components-WorksheetView)
- [Çalışma Kitabı Hizmeti](#SpreadsheetEditor-Components-WorkbookService)
- [Yükleyici Hizmeti](#SpreadsheetEditor-Components-LoaderService)
- [Hücre Hizmeti](#SpreadsheetEditor-Components-CellsService)

HTML5 Elektronik Tablo Düzenleyici, eksiksiz bir sistem oluşturmak için bir araya gelen birkaç bileşenden oluşturulmuştur. Burada her birinin amacını ve rolünü açıklıyoruz.
### **index.html**
Editörün kullanıcı arayüzünü ve uygulamamızın ana uç noktasını açıklayan bir JSF sayfasıdır. Web tarayıcısı ile sunucu arasında gerçekleştirilen tüm etkileşim bu uç nokta üzerinden gerçekleştirilir.

Kullanıcı arabirimini tanımlamanın yanı sıra, tüm arka uç hizmetleri buraya JSF teknolojileri kullanılarak eklenir. Kullanıcı kullanıcı arabirimi olayları ile etkileşime geçtiğinde ve veriler, örneğin elektronik tabloları dışa aktarma gibi görevlerimizi tamamlamak için hizmetler ve kullanıcı arasında ileri geri iletilir.

İki ana ilgi alanı vardır.

**Kurdele**

Üstteki sekmeli araç çubuğu alanına teknik olarak şerit denir. Elektronik tablo üzerinde birçok işlemi gerçekleştirmek için kullanılan düğmeler, açılır menüler, radyo menüleri, metin kutuları ve bazı gizli alanlar içerir. Bu düğmeler tıklandığında sunucuya komutlar gönderir ve sayfayı buna göre günceller.

**Çarşaf**

Sayfa, satırlar ve sütunlardır. Hücreler tıklandığında, şeridin ihtiyaç duyduğu tüm veriler her hücreye eklendiğinden, şerit sunucuya istek göndermeden buna göre güncellenir. Şerit, kullanıcı sayfada gezinirken seçilen hücre, satır ve sütunu da takip eder.

Her hücrenin, bir hücre düzenleme modundayken görünür hale gelen kendi satır içi düzenleyicisi vardır.
### **Çalışma Sayfası Görünümü**
Index.html'de açıklanan kullanıcı arabiriminin dinamik içeriğini yönetmekten sorumlu, görüntüleme kapsamlı bir JSF arka uç çekirdeğidir. Kullanıcı UI ile etkileşime girdikçe tetiklenen Ajax istekleri için olay işleyicileri vardır.
### **Çalışma Kitabı Hizmeti**
WorkbookService, görünüm kapsamlı bir JSF arka uç çekirdeğidir. Bir hizmet bileşeni olarak çalışır ve elektronik tablonun diğer hizmetlerin yardımıyla yüklenmesini ve kaldırılmasını sağlar. Aşağıdaki uç noktalara sahiptir:

**içinde**

 bu**içinde** dır-dir**Yapı Sonrası** Java Uygulama Sunucusu tarafından nesne oluşturma tamamlandıktan hemen sonra yürütülen yöntem. Bu kontrol**url** istek parametrelerindeki parametre eşlenir ve mümkünse ilgili elektronik tabloyu verilen konumdan yükler.

**tahrip etmek**

Edinilen tüm kaynakların artık gerekli olmadığında temizlenmesinden sorumludur.
### **Yükleyici Hizmeti**
Elektronik tablo örnekleri oluşturur ve ihtiyaç duyulduğu sürece bunları bellekte tutar.
### **Hücre Hizmeti**
 bu**Hücre Hizmeti** satırların, sütunların, hücrelerin önbelleğini, biçimlendirmeyi ve çalışma sayfalarının yapısını yönetir.
