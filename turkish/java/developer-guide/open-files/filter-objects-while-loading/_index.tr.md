---
title: Çalışma Kitabı veya Çalışma Sayfası yüklenirken Nesneleri Filtrele
type: docs
weight: 1060
url: /tr/java/filter-objects-while-loading-workbook-or-worksheet/
---
## **Olası Kullanım Senaryoları**
 Lütfen kullan[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) çalışma kitabından verileri filtrelerken özelliği. Ancak verileri tek tek çalışma sayfalarından filtrelemek istiyorsanız, geçersiz kılmanız gerekir.[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\) ) yöntem. Lütfen uygun değeri girin[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) oluştururken veya birlikte çalışırken numaralandırma[Yük Filtresi](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

 bu[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)numaralandırma aşağıdaki değerlere sahiptir.

- [YOK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [TÜM](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [HÜCRE_BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [HÜCRE_HATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [HÜCRE_DEĞERİ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [FORMÜL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [HÜCRE_VERİLERİ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [ÇİZELGE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [ŞEKİL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [MERGED_AREA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [KOŞULLU BİÇİMLENDİRME](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [VERİ DOĞRULAMA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [PİVOT TABLO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [MASA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [KÖPRÜLER](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [SHEET_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [SHEET_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [KİTAP_AYARLARI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [AYARLAR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [YAPI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [DÖKÜMAN ÖZELLİKLERİ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [DEFINED_NAMES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [STİL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Çalışma Kitabını Yüklerken Nesneleri Filtrele**
 Aşağıdaki örnek kod, çalışma kitabından grafiklerin nasıl filtreleneceğini gösterir. lütfen kontrol ediniz[örnek excel dosyası](5472489.xlsx) Bu kodda kullanılan ve[çıktı PDF](5472488.pdf)onun tarafından oluşturulur. Çıktı PDF'sinde görebileceğiniz gibi, tüm grafikler çalışma kitabından filtrelendi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Çalışma Sayfasını Yüklerken Nesneleri Filtrele**
 Aşağıdaki örnek kod,[kaynak excel dosyası](5472492.xlsx) ve özel bir filtre kullanarak aşağıdaki verileri çalışma sayfalarından filtreler.

- NoCharts adlı çalışma sayfasındaki Grafikleri filtreler.
- NoShapes adlı çalışma sayfasındaki Şekilleri filtreler.
- NoConditionalFormatting adlı çalışma sayfasından Koşullu Biçimlendirmeyi filtreler.

 Bir kez, yükler[kaynak excel dosyası](5472492.xlsx) özel bir filtre ile tüm çalışma sayfalarının resimlerini tek tek alır. İşte referansınız için çıktı görüntüleri. Gördüğünüz gibi, ilk resimde grafikler yok, ikinci resimde şekiller yok ve üçüncü resimde koşullu biçimlendirme yok.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
