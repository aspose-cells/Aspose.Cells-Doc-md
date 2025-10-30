---
title: Akıllıca Ana ve Detay Verilerini Excel e Master ve Detaylar ile Getirme
type: docs
weight: 30
url: /tr/net/how-to-use-master-and-details-with-smart-markers/
---

## **Olası Kullanım Senaryoları**
Bazen, dinamik Excel raporları üretmek istersiniz, bunlar kapsamlı bir ana gösterge paneli ve birkaç ince detaylı çalışma sayfasını içerir. Bunlar arasında, tek bir ana tablo genel bir bakış sunar ve çeşitli ürün varyantlarını gösterebilir, her bir detay sayfası ise tek bir varyanta ait belirli ve derin verileri sağlar. Aspose.Cells, master ve detailler ile smart markerlar aracılığıyla ihtiyaçlarınızı mükemmel şekilde karşılar.


## **Master ve detaylar için Smart Marker Parametreleri**
Excel'e ana ve detay verisi almak için aşağıdaki smart marker parametrelerini kullanmanız gerekir:

| Parametre | Açıklama | Kabul Edilebilir Değerler (Sözdizimi) | Kısıtlamalar | İsteğe Bağlılık | Varsayılan Davranış | Excel Kısıtlamaları |
| --- | --- | --- | --- | --- | --- | --- |
| `DetailSheet` | Şablon dosyasında saklanan detay çalışma sayfasının adını belirtir. | String değer | Değer null veya çalışma sayfası ismi olmalı. Null ise, bu bir detay sayfasıdır. Basit bir string değeri olmalı. Değişken desteklenmiyor. | Atlanırsa, ana veya detay sayfası değildir. | Normal çalışma sayfası, ana veya detay sayfası değil. | |
| `DetailTable` | Şablon dosyasındaki detay çalışma sayfasının tablo adını belirtir. | String değer | | Atlanırsa, detay sayfasındaki akıllı gösterge ana sayfaya benzer olmalı, aksi takdirde veri kaynağını bulamayız. | Atlanırsa, detay sayfasındaki akıllı gösterge ana sayfaya benzer olmalı, aksi takdirde veri kaynağını bulamayız. | |
| `DetailSheetNewName` | Yeni oluşturulacak detay çalışma sayfasının ismini belirtir. | Excel formülü gibi ifade | Sadece değer yerine değişken ({a.bc}) kullanırsak, geçerli bir Excel formülü olmalı. | Atlanırsa, yeni sayfalar Sheet1, Sheet2... olur | Atlanırsa, yeni sayfalar Sheet1, Sheet2... olur | İsim geçerli bir sayfa adı olmalı. |
| `DetailLink` | Dışa aktarılan verilerin konumuna köprüler eklenip eklenmeyeceğini belirtir. | | | Atlanırsa, dışa aktarılan verilerin konumuna köprü eklenmez. | Atlanırsa, dışa aktarılan verilerin konumuna köprü eklenmez. | |

## **Ana ve Detaylar Nasıl Kullanılır: Aynı Çalışma Sayfasında Ana ve Detaylar**
Bazen, SmartMarkers'da ana ve detay verilerini içe aktarmanız gerekir. Aspose.Cells, SmartMarkers'ta master ve detay parametrelerini kullanmayı mümkün kılar. Lütfen [şablon dosyasını](MasterDetailInOneSheet.xlsx), [json dosyasını](MasterDetailData.json) ve aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin.

|**Şablon.xlsx dosyasının ilk sayfası.**|
| :- |
|![todo:image_alt_text](1.png)|

|**Üretim excel dosyasının ilk sayfası.**|
| :- |
|![todo:image_alt_text](2.png)|

|**Üretim excel dosyasının ikinci sayfası.**|
| :- |
|![todo:image_alt_text](3.png)|

Json verileri şu şekildedir:
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InOneSheet.cs" >}}

## **Farklı Çalışma Sayfalarında Master ve Detaylar Nasıl Kullanılır**
Bazen, SmartMarkers'da ana ve detay verilerini içe aktarmanız gerekir. Aspose.Cells, SmartMarkers'ta master ve detay parametrelerini kullanmayı mümkün kılar. Lütfen [şablon dosyasını](MasterDetailInTwoSheets.xlsx), [json dosyasını](MasterDetailData.json) ve aşağıdaki kodla oluşturulan çıktı excel dosyasının ekran görüntüsünü kontrol edin.

|**template.xlsx dosyasının ilk ana çalışma sayfası.**|
| :- |
|![todo:image_alt_text](4.png)|

|**template.xlsx dosyasının ikinci ana çalışma sayfası.**|
| :- |
|![todo:image_alt_text](5.png)|

|**Şablon.xlsx'nin detay çalışma sayfası.**|
| :- |
|![todo:image_alt_text](6.png)|

|**Çıkış excel dosyasının ilk ana çalışma sayfası.**|
| :- |
|![todo:image_alt_text](7.png)|

|**Çıkış excel dosyasının ikinci ana çalışma sayfası.**|
| :- |
|![todo:image_alt_text](8.png)|

|**Çıkış excel dosyasındaki ilk ana çalışma sayfasının detay çalışma sayfası.**|
| :- |
|![todo:image_alt_text](9.png)|

|**Çıkış excel dosyasındaki ikinci ana çalışma sayfasının ilk detay çalışma sayfası.**|
| :- |
|![todo:image_alt_text](10.png)|

|**Çıkış excel dosyasındaki ikinci ana çalışma sayfasının ikinci detay çalışma sayfası.**|
| :- |
|![todo:image_alt_text](11.png)|

Json verileri şu şekildedir:
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
Aşağıdaki örnek, bu işlemin nasıl çalıştığını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InDifferentSheets.cs" >}}
