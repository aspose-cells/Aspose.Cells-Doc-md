---
title: Çalışma Kitabı veya Çalışsayfa Yüklenirken Nesneleri Filtrele
type: docs
weight: 330
url: /tr/net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Olası Kullanım Senaryoları**
Lütfen, çalışma kitabından veri filtrelerken [LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) özelliğini kullanın. Ancak tek tek çalışsayfalarından veri filtrelemek istiyorsanız, [LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet) yöntemini geçersiz kılmanız gerekecektir. [LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) oluştururken veya çalışırken uygun değeri [LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) numaralandırmasından belirtmelisiniz.

[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) numaralandırmasında aşağıdaki olası değerler bulunmaktadır.

- Tümü
- KitapAyarları
- HücreBoş
- HücreBool
- CellData
- CellError
- CellNumeric
- CellString
- CellValue
- Chart
- ConditionalFormatting
- DataValidation
- DefinedNames
- DocumentProperties
- Formula
- Hyperlinkler
- MergedArea
- PivotTable
- Settings
- Shape
- SheetData
- SheetSettings
- Structure
- Style
- Table
- VBA
- XmlMap
## **Çalışma Kitabını Yüklerken Filtreleme Nesneleri**
Aşağıdaki örnek kodlar, çalışma kitabından grafikleri filtrelemenin nasıl yapıldığını göstermektedir. Lütfen bu kodda kullanılan [örnek excel dosyasını](5115258.xlsx) ve bunun tarafından oluşturulan [çıktı PDF'yi](5115257.pdf) kontrol edin. Çıktı PDF'de, tüm grafiklerin çalışma kitabından filtrelenmiş olduğunu görebilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Çalışma Sayfasını Yüklerken Filtreleme Nesneleri**
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115255.xlsx) yükler ve çalışma sayfalarından aşağıdaki verileri özel bir filtreden geçirir.

- Tablo adı NoCharts olan çalışma sayfasından Grafikleri filtreler.
- Tablo adı NoShapes olan çalışma sayfasından Şekilleri filtreler.
- Tablo adı NoConditionalFormatting olan çalışma sayfasından Koşullu Biçimlendirmeyi filtreler.

Özel bir filtreden sonra [kaynak excel dosyasını](5115255.xlsx) yüklediğinde, tüm çalışma sayfalarının resimlerini sırayla alır. Referansınız için çıktı resimleri aşağıdadır. Görebileceğiniz gibi, ilk resimde grafik yok, ikinci resimde şekiller yok ve üçüncü resimde koşullu biçimlendirme yok.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


Bu, özel filtrenin çalışma sayfası adlarına göre nasıl kullanılacağının örneğidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
