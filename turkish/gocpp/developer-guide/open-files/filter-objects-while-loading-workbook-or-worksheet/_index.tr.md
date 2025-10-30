---
title: Golang ve C++ kullanarak Çalışma Kitabı veya Çalışma Sayfası yüklerken Nesneleri Filtreleme
linktitle: Çalışma Kitabı veya Çalışsayfa Yüklenirken Nesneleri Filtrele
type: docs
weight: 330
url: /tr/go-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Aspose.Cells for C++ kullanarak çalışma kitapları veya çalışma sayfaları yüklenirken grafikler, şekiller ve koşullu biçimlendirme gibi nesneleri nasıl filtreleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**
Lütfen verileri filtreden geçirmek için [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) özelliğini kullanın. Ancak, verileri bireysel çalışma sayfalarından filitrelemek istiyorsanız, [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/) yöntemini geçersiz kılmalısınız. Lütfen uygun değeri [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) dizininden sağlayın.

 [LoadDataFilterOptions](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) dizininde aşağıdaki olası değerler bulunmaktadır.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet.go" >}}
## **Çalışma Sayfasını Yüklerken Filtreleme Nesneleri**
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115255.xlsx) yükler ve çalışma sayfalarından aşağıdaki verileri özel bir filtreden geçirir.

- Tablo adı NoCharts olan çalışma sayfasından Grafikleri filtreler.
- Tablo adı NoShapes olan çalışma sayfasından Şekilleri filtreler.
- Tablo adı NoConditionalFormatting olan çalışma sayfasından Koşullu Biçimlendirmeyi filtreler.

Özel bir filtreden sonra [kaynak excel dosyasını](5115255.xlsx) yüklediğinde, tüm çalışma sayfalarının resimlerini sırayla alır. Referansınız için çıktı resimleri aşağıdadır. Görebileceğiniz gibi, ilk resimde grafik yok, ikinci resimde şekiller yok ve üçüncü resimde koşullu biçimlendirme yok.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-1.go" >}}
Bu, özel filtrenin çalışma sayfası adlarına göre nasıl kullanılacağının örneğidir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-2.go" >}}
