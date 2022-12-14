---
title: Çalışma Kitabı veya Çalışma Sayfası yüklenirken Nesneleri Filtrele
type: docs
weight: 330
url: /tr/net/filter-objects-while-loading-workbook-or-worksheet/
---
## **Olası Kullanım Senaryoları**
Lütfen kullan[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)çalışma kitabından verileri filtrelerken özelliği. Ancak verileri tek tek çalışma sayfalarından filtrelemek istiyorsanız, o zaman geçersiz kılmak zorunda kalacaksınız.[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)yöntem. Lütfen uygun değeri girin[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)oluştururken veya birlikte çalışırken numaralandırma[Yük Filtresi](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

 bu[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)numaralandırma aşağıdaki olası değerlere sahiptir.

- Herşey
- Kitap Ayarları
- HücreBlank
- HücreBool
- Hücre Verileri
- hücre hatası
- HücreSayısal
- hücre dizisi
- Hücre Değeri
- Çizelge
- Koşullu biçimlendirme
- Veri doğrulama
- tanımlı adlar
- Döküman özellikleri
- formül
- köprüler
- BirleştirilmişAlan
- Pivot tablo
- Ayarlar
- Şekil
- SheetData
- Sayfa Ayarları
- Yapı
- stil
- Masa
- VBA
- XmlMap
## **Çalışma Kitabını yüklerken Nesneleri Filtrele**
 Aşağıdaki örnek kod, çalışma kitabından grafiklerin nasıl filtreleneceğini gösterir. lütfen kontrol ediniz[örnek excel dosyası](5115258.xlsx) Bu kodda kullanılan ve[çıktı PDF](5115257.pdf)onun tarafından oluşturulur. Çıktı PDF'sinde görebileceğiniz gibi, tüm grafikler çalışma kitabından filtrelendi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Çalışma Sayfası yüklenirken Nesneleri Filtrele**
 Aşağıdaki örnek kod,[kaynak excel dosyası](5115255.xlsx) ve özel bir filtre kullanarak aşağıdaki verileri çalışma sayfalarından filtreler.

- NoCharts adlı çalışma sayfasındaki Grafikleri filtreler.
- NoShapes adlı çalışma sayfasındaki Şekilleri filtreler.
- NoConditionalFormatting adlı çalışma sayfasından Koşullu Biçimlendirmeyi filtreler.

 Bir kez, yükler[kaynak excel dosyası](5115255.xlsx) özel bir filtre ile tüm çalışma sayfalarının resimlerini tek tek alır. İşte referansınız için çıktı görüntüleri. Gördüğünüz gibi, ilk resimde grafikler yok, ikinci resimde şekiller yok ve üçüncü resimde koşullu biçimlendirme yok.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


Bu, CustomLoadFilter sınıfını çalışma sayfası adlarına göre nasıl kullanacağınızdır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
