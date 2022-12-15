---
title: Ayar Sayfası Seçenekleri
type: docs
weight: 10
url: /tr/net/setting-page-options/
---
{{% alert color="primary" %}}

Bazen, çalışma sayfalarının yazdırmayı denetlemesi için sayfa yapısı ayarlarının yapılandırılması gerekir. Bu sayfa yapısı ayarları çeşitli seçenekler sunar.

{{% /alert %}}

## **Ayar Sayfası Seçenekleri**

Sayfa yapısı seçenekleri Aspose.Cells'de tam olarak desteklenir. Bu makale, Aspose.Cells ile sayfa seçeneklerinin nasıl ayarlanacağını açıklar ve ayar için kod örneklerini gösterir:

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf.

 bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) çalışma sayfasının sayfa düzeni seçeneklerini ayarlamak için kullanılan özellik. Aslında, bu[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) özellik bir nesnedir[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) yazdırılan bir çalışma sayfası için farklı sayfa düzeni seçeneklerini ayarlamak için kullanılan sınıf. bu[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)class, sayfa düzeni seçeneklerini ayarlamak için kullanılan çeşitli özellikler sağlar. Bu özelliklerden bazıları aşağıda tartışılmaktadır.

### **Sayfa yönlendirmesi**

 Sayfa yönlendirmesi kullanılarak dikey veya yatay olarak ayarlanabilir.[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıf'[**Oryantasyon**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) Emlak. bu[**Oryantasyon**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) özelliği, önceden tanımlanmış değerlerden birini kabul eder.[**Sayfa Yönlendirme Türü**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)numaralandırma, aşağıda listelenmiştir.

|**Sayfa Yönlendirme Türleri**|**Tanım**|
|:- |:- |
|Manzara|Yatay yönlendirme|
|Vesika|Dikey yönlendirme|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

### **Ölçekleme faktörü**

 Ölçeklendirme faktörünü ayarlayarak bir çalışma sayfasının boyutunu küçültmek veya büyütmek mümkündür.[**Sayfa Kurulumu.Yakınlaştır**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)Emlak.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

### **Sayfalara Sığdır Seçenekleri**

 Çalışma sayfasının içeriğini belirli sayıda sayfaya sığdırmak için[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıf'[**Sayfalara SığdırUzun**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) ve[**Sayfalara SığdırGeniş**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)özellikleri. Bu özellikler, çalışma sayfalarını ölçeklendirmek için de kullanılır.

{{% alert color="primary" %}}

 ya seçebilirsiniz[**Sayfalara SığdırUzun**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**Sayfalara SığdırGeniş**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide) ya da[**yakınlaştır**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom) özellik ama ikisi aynı anda değil.

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

### **Kağıt boyutu**

 kullanarak çalışma sayfalarının yazdırılacağı kağıt boyutunu ayarlayın.[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıf'[**Kağıt boyutu**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) Emlak. bu[**Kağıt boyutu**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) özelliği, önceden tanımlanmış değerlerden birini kabul eder.[**KağıtBoyutuTürü**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)numaralandırma, aşağıda listelenmiştir.

|**Kağıt Boyutu Türleri**|**Tanım**|
|:- |:- |
|KağıtMektup|Harf (8-1/2 inç x 11 inç)|
|KağıtMektupKüçük|Küçük Harf (8-1/2 inç x 11 inç)|
|Kağıt Tabloid|Tabloid (11 inç x 17 inç)|
|Kağıt Defteri|Defter (17 inç x 11 inç)|
|KağıtYasal|Yasal (8-1/2 inç x 14 inç)|
|Kağıt Bildirimi|Açıklama (5-1/2 inç x 8-1/2 inç)|
|Kağıt Yöneticisi|Yönetici (7-1/4 inç x 10-1/2 inç)|
|KağıtA3|A3 (297 mm x 420 mm)|
|KağıtA4|A4 (210 mm x 297 mm)|
|KağıtA4Küçük|A4 Küçük (210 mm x 297 mm)|
|KağıtA5|A5 (148 mm x 210 mm)|
|KağıtB4|JIS B4 (257 mm x 364 mm)|
|KağıtB5|JIS B5 (182 mm x 257 mm)|
|Kağıt Folyo|Folyo (8-1/2 inç x 13 inç)|
|Kağıt Çeyrek|Çeyrek (215 mm x 275 mm)|
|Kağıt10x14|10 inç x 14 inç|
|Kağıt11x17|11 inç x 17 inç|
|Kağıt Not|Not (8-1/2 inç x 11 inç)|
|KağıtZarf9|Zarf #9 (3-7/8 inç x 8-7/8 inç)|
|KağıtZarf10|Zarf #10 (4-1/8 inç x 9-1/2 inç)|
|KağıtZarf11|Zarf #11 (4-1/2 inç x 10-3/8 inç)|
|KağıtZarf12|Zarf #12 (4-1/2 inç x 11 inç)|
|KağıtZarf14|Zarf #14 (5 inç x 11-1/2 inç)|
|KağıtÇerçeve|C boyutlu levha|
|KağıtDSayfa|D boyutlu sayfa|
|KâğıtÇerçeve|E boyutu sayfası|
|Kağıt ZarfıDL|Zarf DL (110 mm x 220 mm)|
|KağıtZarfC5|Zarf C5 (162 mm x 229 mm)|
|KağıtZarfC3|Zarf C3 (324 mm x 458 mm)|
|KağıtZarfC4|Zarf C4 (229 mm x 324 mm)|
|KağıtZarfC6|Zarf C6 (114 mm x 162 mm)|
|KağıtZarfC65|Zarf C65 (114 mm x 229 mm)|
|KağıtZarfB4|Zarf B4 (250 mm x 353 mm|
|KağıtZarfB5|Zarf B5 (176 mm x 250 mm)|
|KağıtZarfB6|Zarf B6 (176 mm x 125 mm)|
|KağıtZarfİtalya|Zarf İtalya (110 mm x 230 mm)|
|KağıtZarfMonarch|Zarf Monarch (3-7/8 inç x 7-1/2 inç)|
|KağıtZarfKişisel|Zarf (3-5/8 inç x 6-1/2 inç)|
|PaperFanfoldABD|ABD Standardı Yelpaze Katlama (14-7/8 inç x 11 inç)|
|PaperFanfoldStd Almanca|Alman Standardı Yelpaze Katlama (8-1/2 inç x 12 inç)|
|PaperFanfoldLegal Almanca|Alman Yasal Yelpaze Katlama (8-1/2 inç x 13 inç)|
|KağıtISOB4|B4 (ISO) 250 x 353 mm|
|KağıtJaponKartpostal|Japon Kartpostalı (100mm x 148mm)|
|Kağıt9x11|9 inç x 11 inç|
|Kağıt10x11|10 inç x 11 inç|
|Kağıt15x11|15 inç x 11 inç|
|KağıtZarfDavet|Zarf Davetiyesi(220mm x 220mm)|
|Ekstra KağıtMektup|US Letter Ekstra 9 \275 x 12 inç|
|KağıtYasalEkstra|US Legal Extra 9 \275 x 15 inç|
|KağıtTabloidEkstra|ABD Tabloid Ekstra 11,69 x 18 inç|
|KağıtA4Ekstra|A4 Ekstra 9,27 x 12,69 inç|
|KağıtMektupEnine|Harf Enine 8 \275 x 11 inç|
|KağıtA4Enine|A4 Enine 210 x 297 mm|
|KağıtMektupEkstraEnine|Harf Ekstra Çapraz 9\275 x 12 inç|
|Kağıt SüperA|SüperA/SüperA/A4 227 x 356 mm|
|Kağıt SüperB|SuperB/SuperB/A3 305 x 487 mm|
|KağıtMektupPlus|US Letter Plus 8,5 x 12,69 inç|
|KağıtA4Plus|A4 Artı 210 x 330 mm|
|KağıtA5Enine|A5 Enine 148 x 210 mm|
|KağıtJISB5Enine|B5 (JIS) Enine 182 x 257 mm|
|KağıtA3Ekstra|A3 Ekstra 322 x 445 mm|
|KağıtA5Ekstra|A5 Ekstra 174 x 235 mm|
|KağıtISOB5Ekstra|B5 (ISO) Ekstra 201 x 276 mm|
|KağıtA2|A2 420x594mm|
|KağıtA3Enine|A3 Enine 297 x 420 mm|
|KağıtA3EkstraEnine|A3 Ekstra Çapraz 322 x 445 mm|
|KağıtJaponÇiftKartpostal|Japon Çiftli Kartpostal 200 x 148 mm|
|KağıtA6|A6 105x148mm|
|KağıtJaponZarfKaku2|Japon Zarfı Kaku #2|
|KağıtJaponZarfKaku3|Japon Zarfı Kaku #3|
|KağıtJaponZarfChou3|Japon Zarfı Chou # 3|
|KağıtJaponZarfChou4|Japon Zarfı Chou # 4|
|KağıtMektupDöndürülmüş|11 inç x 8,5 inç|
|KağıtA3Döndürülmüş|420mm x 297mm|
|KağıtA4Döndürülmüş|297mm x 210mm|
|KağıtA5Döndürülmüş|210mm x 148mm|
|PaperJISB4Döndürülmüş|B4 (JIS) Döndürülmüş 364 x 257 mm|
|PaperJISB5Döndürülmüş|B5 (JIS) Döndürülmüş 257 x 182 mm|
|KağıtJaponKartpostalDöndürülmüş|Japon Kartpostalı Döndürülmüş 148 x 100 mm|
|KağıtJaponDoubleKartpostalDöndürülmüş|Döndürülmüş Çift Japon Kartpostalı 148 x 200 mm|
|KağıtA6Döndürülmüş|A6 Döndürülmüş 148 x 105 mm|
|KağıtJaponZarfKaku2Döndürülmüş|Japon Zarfı Kaku #2 Döndürülmüş|
|KağıtJaponZarfKaku3Döndürülmüş|Japon Zarfı Kaku #3 Döndürülmüş|
|KağıtJaponZarfChou3Döndürülmüş|Japon Zarfı Chou #3 Döndürülmüş|
|KağıtJaponZarfChou4Döndürülmüş|Japon Zarfı Chou #4 Döndürülmüş|
|KağıtJISB6|B6 (JIS) 128 x 182 mm|
|PaperJISB6Döndürülmüş|B6 (JIS) Döndürülmüş 182 x 128 mm|
|Kağıt12x11|12x11 inç|
|KağıtJaponZarfYou4|Japon Zarfı Sen 4.|
|KağıtJaponZarfYou4Döndürülmüş|You #4 Döndürülmüş Japon Zarfı|
|KağıtPRC16K|ÇHC 16K 146 x 215 mm|
|KağıtPRC32K|ÇHC 32K 97 x 151 mm|
|KağıtPRCBig32K|ÇHC 32K(Büyük) 97 x 151 mm|
|KağıtPRCEzf1|ÇHC Zarf #1 102 x 165 mm|
|KağıtPRCEzf2|ÇHC Zarf #2 102 x 176 mm|
|KağıtPRCEzf3|ÇHC Zarf #3 125 x 176 mm|
|KağıtPRCEzf4|ÇHC Zarf #4 110 x 208 mm|
|KağıtPRCEzf5|ÇHC Zarf #5 110 x 220 mm|
|KağıtPRCEzf6|ÇHC Zarf #6 120 x 230 mm|
|KağıtPRCEzf7|ÇHC Zarf #7 160 x 230 mm|
|KağıtPRCEzf8|ÇHC Zarf #8 120 x 309 mm|
|KağıtPRCEzf9|ÇHC Zarf #9 229 x 324 mm|
|KağıtPRCEzf10|ÇHC Zarf #10 324 x 458 mm|
|KağıtPRC16KDöndürülmüş|ÇHC 16K Döndürülmüş|
|KağıtPRC32KDöndürülmüş|ÇHC 32K Döndürülmüş|
|KağıtPRCBig32KDöndürülmüş|ÇHC 32K(Büyük) Döndürülmüş|
|KağıtPRCEzf1Döndürülmüş|ÇHC Zarf #1 Döndürülmüş 165 x 102 mm|
|KağıtPRCEnvelope2Döndürülmüş|ÇHC Zarf #2 Döndürülmüş 176 x 102 mm|
|KağıtPRCEzf3Döndürülmüş|ÇHC Zarf #3 Döndürülmüş 176 x 125 mm|
|KağıtPRCEnvelope4Döndürülmüş|PRC Zarf #4 Döndürülmüş 208 x 110 mm|
|KağıtPRCEzf5Döndürülmüş|ÇHC Zarf #5 Döndürülmüş 220 x 110 mm|
|KağıtPRCEzf6Döndürülmüş|ÇHC Zarf #6 Döndürülmüş 230 x 120 mm|
|KağıtPRCEzf7Döndürülmüş|PRC Zarf #7 Döndürülmüş 230 x 160 mm|
|KağıtPRCEzf8Döndürülmüş|ÇHC Zarf #8 Döndürülmüş 309 x 120 mm|
|KağıtPRCEzf9Döndürülmüş|PRC Zarf #9 Döndürülmüş 324 x 229 mm|
|KağıtPRCEzf10Döndürülmüş|ÇHC Zarf #10 Döndürülmüş 458 x 324 mm|
|KağıtB3|normal B3(13,9 x 19,7 inç)|
|KağıtKartvizit|Kartvizit(90mm x 55 mm)|
|Kağıt Termal|Termal(3 x 11 inç)|
|Gelenek|Özel kağıt boyutunu temsil eder.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

### **Baskı kalitesi**

 ile yazdırılacak çalışma sayfalarının baskı kalitesini ayarlayın.[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıf'[**Baskı kalitesi**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)Emlak. Baskı kalitesi için ölçüm birimi İnç Başına Nokta'dır (DPI).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

### **İlk Sayfa Numarası**

 kullanarak çalışma sayfası sayfalarının numaralandırılmasını başlatın.[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıf'[**İlk SayfaNumarası**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber) Emlak. bu[**İlk SayfaNumarası**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)özelliği, ilk çalışma sayfası sayfasının sayfa numarasını ayarlar ve sonraki sayfalar artan sırada numaralandırılır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
