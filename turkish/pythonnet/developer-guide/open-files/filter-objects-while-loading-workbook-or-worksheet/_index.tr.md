---
title: Çalışma Kitabı veya Çalışsayfa Yüklenirken Nesneleri Filtrele
type: docs
weight: 330
url: /tr/python-net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Olası Kullanım Senaryoları**
Lütfen, çalışma kitabından veri filtrelerken [LoadOptions.load_filter](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) özelliğini kullanın. Ancak, bireysel çalışma sayfelerinden veri filtrelemeniz gerekirse, o zaman [LoadFilter.start_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter/start_sheet) metodunu geçersiz kılmanız gerekir. Lütfen uygun değeri [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) kümesinden sağlayın ve [LoadFilter](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) ile çalışırken kullanın.

[LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) kümesinin aşağıdaki geçerli değerleri vardır.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilteringObjectsAtLoadTime-FilteringObjects.py" >}}

{{< app/cells/assistant language="python-net" >}}
