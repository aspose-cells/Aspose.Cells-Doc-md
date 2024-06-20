---
title: GridDesktop ta çalışma kitabını yüklerken filtre nesnelerini filtreleme
type: docs
weight: 1060
url: /tr/net/aspose-cells-griddesktop/loading-filter
description: Bu makale, GridDesktop ta yükleme filtresinin nasıl kullanılacağını açıklar
keywords: GridDesktop,loading,loading filter,filter
---

## **Olası Kullanım Senaryoları**
Lütfen bir dosyadan veri filtrelerken [GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter) özelliğini kullanın

[GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions) numaralandırmasının aşağıdaki değerleri bulunmaktadır
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
## **Çalışma Kitabını Yükleme Sırasında Veriyi Filtreleme**
Aşağıdaki örnek kod, çalışma kitabından çizimi filtreleme şeklini gösterir. Lütfen [örnek excel dosyasını](5472489.xlsx) kontrol edin. Görebileceğiniz gibi, tüm grafikler/şekiller/resimler çalışma kitabından filtrelenmiştir.
![resimsiz çalışma kitabı](nodrawing.png)
### **Örnek Kod**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}

