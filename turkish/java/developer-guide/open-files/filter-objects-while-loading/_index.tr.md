---
title: Çalışma Kitabı veya Çalışsayfa Yüklenirken Nesneleri Filtrele
type: docs
weight: 1060
url: /tr/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **Olası Kullanım Senaryoları**
[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) özelliğini kullanarak çalışma kitabından veri filtrelerken. Ancak, tek tek çalışsayfalardan veri filtrelemek istiyorsanız, [LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\)) yöntemini geçersiz kılmanız gerekecek. [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) numaralandırmasından uygun değeri sağlarken [LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter) ile oluştururken veya çalışırken, lütfen uygun bir değer sağlayın.

[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) numaralandırmasının aşağıdaki değerleri bulunmaktadır.

- [YOK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [TÜMÜ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [HÜCRE_BOŞ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [HÜCRE_METİN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [HÜCRE_SAYISAL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [HÜCRE_HATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [HÜCRE_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [HÜCRE_DEĞER](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [FORMÜL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [HÜCRE_VERİ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [GRAFİK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [ŞEKİL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [BİRLEŞTİRİLMİŞ_ALAN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [KOŞULLU_FORMAT](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [VERİ_DOĞRULAMA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [ÖZET_TABLO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [TABLO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [HYPERLINKLER](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [SAYFA_AYARLARI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [SAYFA_VERİ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [KİTAP_AYARLARI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [AYARLAR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_HARİTASI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [YAPI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [BELGE ÖZELLİKLERİ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [TANIMLI_AD](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [STİL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Çalışma Kitabı Yüklenirken Nesneleri Filtrele**
Aşağıdaki örnek kod, çalışma kitabından grafikleri filtrelemeyi göstermektedir. Lütfen bu kodda kullanılan [örnek excel dosyasını](5472489.xlsx) ve bunun tarafından üretilen [çıktı PDF'yi](5472488.pdf) kontrol edin. Çıktı PDF'de, tüm grafiklerin çalışma kitabından filtre edildiğini görebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Çalışma Sayfası Yüklenirken Nesneleri Filtrele**
Aşağıdaki örnek kod, [kaynak excel dosyasını](5472492.xlsx) yükler ve çalışma sayfalarındaki belirli verileri özel bir filtre kullanarak filtreler.

- Tablo adı NoCharts olan çalışma sayfasından Grafikleri filtreler.
- Tablo adı NoShapes olan çalışma sayfasından Şekilleri filtreler.
- Tablo adı NoConditionalFormatting olan çalışma sayfasından Koşullu Biçimlendirmeyi filtreler.

Özelleştirilmiş bir filtre kullanarak [kaynak excel dosyasını](5472492.xlsx) yükledikten sonra, tüm çalışma sayfalarının resimlerini tek tek alır. İşte referansınız için çıktı resimleri. Görebileceğiniz gibi, ilk resimde grafikler yok, ikinci resimde şekiller yok ve üçüncü resimde koşullu biçimlendirme yok.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
