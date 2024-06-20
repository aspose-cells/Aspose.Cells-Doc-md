---
title: Tablo Düzenleyici  Bileşenler
type: docs
weight: 50
url: /tr/java/spreadsheet-editor-components/
---

**İçindekiler**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [WorksheetView](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

HTML5 Tablo Düzenleyici, tam sistem oluşturmak için bir araya gelen birkaç bileşenden oluşmaktadır. Burada her bir bileşenin amacını ve rolünü açıklıyoruz.
### **Index.html**
Bu, editörün UI'sını ve uygulamamızın ana uç noktasını tanımlayan bir JSF sayfasıdır. Web tarayıcısı ile sunucu arasında gerçekleştirilen tüm etkileşimler bu uç nokta aracılığıyla gerçekleştirilir.

UI'nin tanımlanmasının yanı sıra, tüm backend servisleri JSF teknolojileri kullanılarak buraya bağlanır. Kullanıcı UI ile etkileşime geçtiğinde, etkinlikler ve veriler görevlerimizi tamamlamak için servisler arasında kullanıcı arasında sürekli olarak iletilir.

İki ana ilgi alanı vardır.

**Kurdele**

Üst kısımdaki sekme aralığı aslında kurdele olarak adlandırılır. Butonlar, açılır menüler, radyo düğmeleri, metin kutuları ve sayfa üzerinde birçok işlemi gerçekleştirmek için kullanılan bazı gizli alanları içerir. Bu düğmeler tıklandığında komutları sunucuya gönderir ve sayfayı buna göre günceller.

**Sayfa**

Sayfa, satırlar ve sütunlardır. Hücrelere tıklandığında, verilen istekler sunucuya gönderilmeden kurdele buna göre güncellenir çünkü kurdeledeki gereken tüm veri her bir hücreye eklenmiştir. Kurdele ayrıca kullanıcı sayfa üzerinde gezindiğinde seçili hücreyi, satırı ve sütunu takip eder.

Her hücre kendi içinde düzenleyiciye sahiptir ve bir hücre düzenleme modunda olduğunda görünür hale gelir.
### **WorksheetView**
Bu, index.html'de tanımlanan arayüzün dinamik içeriğini yönetmekten sorumlu olan bir görünüm kapsamlı JSF backend beandir. Kullanıcı arayüzü ile etkileşimde bulunduğunda tetiklenen Ajax istekleri için olay işleyicilere sahiptir.
### **WorkbookService**
WorkbookService, görünüm kapsamlı JSF backend bean'dir. Hizmet bileşeni olarak çalışır ve diğer hizmetlerin yardımıyla elektronik tabloyu yükler ve boşaltır. Aşağıdaki uç noktalara sahiptir:

**init**

**init** Java Application Server tarafından nesne oluşturulma işleminden hemen sonra gerçekleştirilen **PostConstruct** yöntemidir. İstek parametreleri haritasında **url** parametresi kontrol edilir ve mümkünse belirtilen konumdan karşılık gelen elektronik tablo yüklenir.

**destroy**

Gereksinim duyulmadığında tüm edinilen kaynakları temizlemekten sorumludur.
### **LoaderService**
Elektronik tablonun örneklerini oluşturur ve onları gerektiği sürece bellekte tutar.
### **CellsService**
**CellsService**, satırların, sütunların, hücrelerin, biçimlendirmenin ve çalışma sayfasının yapısının önbelleğini yönetir.
