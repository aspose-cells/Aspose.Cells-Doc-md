---
title: Akıllıca Veri İçe Aktarma ve Yerleştirme ile Akıllı İşaretçiler
linktitle: Akıllı İşaretçiler ile
type: docs
weight: 190
url: /tr/net/using-smart-markers/
description: Aspose.Cells kitaplığı ile şablon Excel dosyalarına göre veri akıllıca aktarılması ve yerleştirilmesi
---

## **Akıllı İşaretçilerle Veriyi Excel'e İçe Aktarmanın Nedenleri**
Smart Markers kullanarak veriyi Excel'e içe aktarmak, şablon tabanlı tasarım ile dinamik veri bağlamayı birleştirerek veri entegrasyonunu kolaylaştırır. Bu yaklaşım, Aspose.Cells gibi araçlarda, işaretçilerin şablonlardaki yer tutucu olarak hareket ettiği ve çeşitli kaynaklardan verileri otomatik doldurduğu durumlarda özellikle değerlidir. İşte bu yöntemi benimsemek için temel nedenler:

1. Tekrarlayan Raporlamada Verimlilik: Şablonun Yeniden Kullanımı, gömülü işaretçili (örn. &=$DeğişkenAdı, &=VeriKaynağı.Sütun) önceden tasarlanmış Excel şablonları birçok veri kümesi arasında yeniden kullanılabilir, manuel yeniden biçimlendirmeye gerek kalmaz. Örneğin, finansal raporlar veya envanter tabloları yalnızca veri kaynağını günceller, düzenleri yeniden oluşturmaz. Otomatik Veri Bağlama, Smart Markers doğrudan veri kaynaklarına (örn. veritabanları, JavaBeans, diziler) bağlanır. Kaynak verilerdeki değişiklikler, işlendiğinde otomatik olarak çıktı Excel dosyasına yansır, böylece kopyala-yapıştır hataları azalır.

2. Karmaşık Veri Yapılarını Destekleme: Çok Kaynaklı Entegrasyon, tek bir şablon farklı kaynaklardan (örn. değişkenler, diziler, SonuçSetleri) veri birleştirebilir. Hiyerarşik Veri İşleme, iç içe veriler (örn. gruplanmış kayıtlar) &=subtotal9:Person.id gibi işaretçiler kullanılarak işlenebilir ve toplamlar (toplamlar, ortalamalar) doğrudan Excel'de gruplayabilir.

3. Excel İşlevselliğinin Korunması: Smart Markers, Excel'in formüller, koşullu biçimlendirme ve grafik gibi özellikleriyle birlikte çalışabilir. Örneğin: &==C{r}*D{r} kullanılarak dinamik hesaplamalar, veri enjeksiyonu sırasında satıra özgü formüller uygular. Şablonlar, önceden tanımlanmış stiller (başlıklar, hücre renkleri) korur ve böylece sonra düzenleme yapmaya gerek kalmadan tutarlılık sağlanır.

4. Gelişmiş Otomasyon Yetkinlikleri: Özel Veri Kaynağı Entegrasyonu, Geliştiriciler ICellsDataTable gibi arayüzleri (.NET'te) kullanarak özel veri yapılarıyla işaretçileri eşleyebilir. Bu esneklik, API'ler veya sensörlerden gelen gerçek zamanlı verileri destekler. Toplu İşlem, Aspose.Cells’in WorkbookDesigner aracıyla büyük ölçekli işlemler (örn. 1.000’den fazla fatura oluşturma) gerçekleştirilerek, döngüler aracılığıyla veri kümeleri üzerinde işlem yapılabilir.

5. Geliştirme ve Bakım Çabalarını Azaltma: Mantık ve Tasarımın Ayrılması, Tasarımcılar JavaScript veya VBA kullanmadan şablonları Excel’de yönetirken, geliştiriciler veri mantığını ele alır. Bu bölünme, yineleme hızını artırır. Hata Azaltma, Otomatik veri eşleştirmesi manuel giriş riskini azaltır. Örneğin, VC++’ta analiz edilen sensör verileri, nesne arayüzleri aracılığıyla Excel şablonlarına otomatik doldurularak transkripsiyon hatalarını önler.

## **Smart Markers ile Veri Tablosu İçe Aktarma için Örnek Kod**
Aşağıdaki örnek kodda, 6 kayıttan oluşan bir veri kaynağı vardır. Sadece 3 kaydı bir çalışma sayfasında göstermek istiyoruz, kalan kayıtlar otomatik olarak ikinci sayfaya geçecektir. Lütfen ikinci sayfanın da aynı smart marker etiketiyle işaretlenmiş olduğundan emin olun ve [WorkbookDesigner.Process(sayfaİndeksi, sakla)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) metodunu her iki sayfa için çağırmalısınız. Oluşturulan referans için [döndürülmüş Excel dosyasını](SmartMarkerDataTableToExcel.xlsx) gözden geçirin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportDataTableToExcel.cs" >}}

## **Akıllı İşaretçilerle JSON Verisi İçe Aktarma Örnek Kodu**
Aspose.Cells for .NET, akıllı işaretçilerde json verisini destekler. Örnek kod, bir tablo şablonunu yükler, verileri akıllı bir şekilde içe aktarır ve ardından tablo verilerini hesaplar. Lütfen [şablon dosyasını](table.xlsx), [json dosyasını](table.json) ve aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin.

|**table.xlsx dosyasının ilk çalışma sayfasında akıllı işaretçilerin gösterimi.**|
| :- |
|![todo:image_alt_text](tabletemplate.png)|

|**Çıktı excel dosyasının ekran görüntüsü.**|
| :- |
|![todo:image_alt_text](tableresult.png)|

Json verileri şu şekildedir:
```json data
{
	"Items" : [
		{
			"ItemName" : "A123",
			"Description" : "Peonies",
			"Qty" : "55",
			"UnitPrice" : "3.05"			
		},
		{
			"ItemName" : "B456",
			"Description" : "Tulips",
			"Qty" : "45",
			"UnitPrice" : "2.66",
		},
		{
			"ItemName" : "K789",
			"Description" : "Buttercup",
			"Qty" : "68",
			"UnitPrice" : "8.35",
		}
	]
}
```
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportJsonToTable.cs" >}}

## **İç İçe Nesneleri Akıllı İşaretçilerle İçeri Aktarma Örnek Kodu**
Aspose.Cells, iç içe geçmiş nesneleri akıllı işaretlerde destekler, iç içe geçen nesneler basit olmalıdır. Basit bir şablon dosyası kullanıyoruz. Birkaç iç içe akıllı işaret içeren tasarımcı elektronik tabloyu gösteren SM_NestedObjects.xlsx dosyasının ilk çalışma sayfasını görüntüleyin.

|** SM_NestedObjects.xlsx dosyasının ilk çalışma sayfasında iç içe akıllı işaretleri gösteren ilk çalışma sayfasının **|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Gelişmiş Konular**
- [Akıllı İşaretçi Parametreleri](/cells/tr/net/smart-marker-parameters/)
- [Akıllı İşaretlere Anonim veya Özel Nesne Ekleme](/cells/tr/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Veri Çok Büyükse Diğer Çalışsayfalara Akıllı İşaret Verileri Otomatik Doldur](/cells/tr/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Biçimlendirme Akıllı İşaretler](/cells/tr/net/formatting-smart-markers/)
- [Akıllı İşaretçilerle Veri Birleştirirken Bildirim Almak](/cells/tr/net/getting-notifications-while-merging-data-with-smart-markers/)
- [WorkbookDesigner için özel Veri Kaynağı Ayarlama](/cells/tr/net/set-custom-datasource-for-workbookdesigner/)
- [Hücrelerde Öncü Apostrof Göster](/cells/tr/net/show-leading-apostrophe-in-cells/)
- [Akıllı İşaretçi Alanında Formula Parametresi Kullanımı](/cells/tr/net/using-formula-parameter-in-smart-marker-field/)
- [Akıllı İşaretçilerle Diziyi Belirli Bir İndeksle Akıllıca İçeri Aktarma](/cells/tr/net/how-to-import-array-element-by-index-with-smart-markers/)
- [Akıllı İşaretçilerle Diziyi Slicer Kullanarak Akıllıca İçeri Aktarma](/cells/tr/net/how-to-import-array-element-by-slicer-with-smart-markers/)
- [Akıllı İşaretçilerle JSON'u Excel'e Akıllıca İçe Aktarma](/cells/tr/net/how-to-import-json-into-excel-with-smart-markers/)
- [Akıllı İşaretçilerle İç İçe Nesneleri Excel'e Akıllıca İçe Aktarma](/cells/tr/net/how-to-import-nested-objects-with-smart-markers/)
- [Değişken Dizileri Akıllı İşaretçilerle Excel'e Akıllıca İçe Aktarma](/cells/tr/net/how-to-import-variable-arrays-with-smart-markers/)
- [Akıllı İşaretçilerde Görüntü İşaretçileri Nasıl Kullanılır](/cells/tr/net/how-to-use-image-markers-in-smart-markers/)
- [Akıllı İşaretçilerde Verileri Nasıl Gruplandırırsınız](/cells/tr/net/how-to-group-data-in-smart-markers/)

{{< app/cells/assistant language="csharp" >}}
