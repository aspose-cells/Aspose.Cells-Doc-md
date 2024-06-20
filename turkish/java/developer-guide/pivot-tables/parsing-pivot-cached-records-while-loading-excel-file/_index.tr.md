---
title: Excel dosyasını yüklerken Pivot Önbellek Kayıtlarını Ayrıştırın
type: docs
weight: 100
url: /tr/java/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Olası Kullanım Senaryoları**

Bir Pivot Tablosu oluşturduğunuzda, Microsoft Excel kaynak verinin bir kopyasını alır ve Pivot Önbelleğine saklar. Pivot Önbelleği, Microsoft Excel'in belleğinin içinde bulunur. Onu göremezsiniz, ancak bu, Pivot Tablonuzu oluştururken veya bir Dilim Seçimi değiştirdiğinizde veya satırlar/sütunlar etrafında hareket ettiğinizde Pivot Tablosunun başvurduğu veridir. Bu, Microsoft Excel'in Pivot Tablosundaki değişikliklere çok duyarlı olmasını sağlar, ancak dosya boyutunun potansiyel olarak iki kat artmasına neden olabilir.

Excel dosyanızı Workbook nesnesi içinde yüklerken, Pivot Önbellek kayıtlarını da yüklemek isteyip istemediğinize karar verebilirsiniz. Bu özelliğin varsayılan değeri **false**. Pivot Önbelleği oldukça büyükse, performansı artırabilir. Ancak Pivot Önbellek kayıtlarını da yüklemek istiyorsanız, bu özelliği **true** olarak ayarlamalısınız.

## **Excel dosyasını yüklerken Pivot Önbellek Kayıtlarını Ayrıştırın**

Aşağıdaki örnek kod, [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords) özelliğinin kullanımını açıklar. Pivot Önbellek kayıtlarını ayrıştırarak [örnek Excel dosyasını](61767786.xlsx) yükler, sonra pivot tabloyu yeniler ve [çıktı Excel dosyası](61767785.xlsx) olarak kaydeder.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
