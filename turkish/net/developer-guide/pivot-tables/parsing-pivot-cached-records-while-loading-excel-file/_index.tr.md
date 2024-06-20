---
title: Excel dosyasını yüklerken Pivot Önbellek Kayıtlarını Ayrıştırın
type: docs
weight: 70
url: /tr/net/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Olası Kullanım Senaryoları**

Bir Pivot Tablosu oluşturduğunuzda, Microsoft Excel kaynak verinin bir kopyasını alır ve Pivot Önbelleğine saklar. Pivot Önbelleği, Microsoft Excel'in belleğinin içinde bulunur. Onu göremezsiniz, ancak bu, Pivot Tablonuzu oluştururken veya bir Dilim Seçimi değiştirdiğinizde veya satırlar/sütunlar etrafında hareket ettiğinizde Pivot Tablosunun başvurduğu veridir. Bu, Microsoft Excel'in Pivot Tablosundaki değişikliklere çok duyarlı olmasını sağlar, ancak dosya boyutunun potansiyel olarak iki kat artmasına neden olabilir.

Excel dosyanızı Workbook nesnesi içine yüklerken, Pivot Önbellek kayıtlarını da yüklemek isteyip istemediğinize karar verebilirsiniz. Bunun için [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) özelliğini kullanabilirsiniz. Bu özelliğin varsayılan değeri **false**'dur. Pivot Önbellek oldukça büyükse, performansı artırabilir. Ancak eğer Pivot Önbellek kayıtlarını da yüklemek istiyorsanız, bu özelliği **true** olarak ayarlamalısınız.

## **Excel dosyasını yüklerken Pivot Önbellek Kayıtlarını Ayrıştırın**

Aşağıdaki örnek kod, [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) özelliğinin kullanımını açıklar. Pivot önbellek kayıtları ayrıştırılırken [örnek Excel dosyasını](61767773.xlsx) yükler. Ardından pivot tablosunu yeniler ve [çıktı Excel dosyası olarak](61767774.xlsx) kaydeder.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.cs" >}}
