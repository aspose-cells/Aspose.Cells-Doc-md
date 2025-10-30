---
title: Excel dosyasını yüklerken Pivot Önbellek Kayıtlarını Ayrıştırın
type: docs
weight: 70
url: /tr/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Python için Aspose.Cells ile Excel dosyasını yüklerken Pivot Önbellek Kayıtlarının Ayrıştırılması via .NET.
keywords: Python için Aspose.Cells Excel, Excel Python kütüphanesi, Aspose.Cells ile Excel dosyasını yüklerken Pivot Önbellek Kayıtlarını Ayrıştırma.
---

## **Olası Kullanım Senaryoları**

Bir Pivot Tablosu oluşturduğunuzda, Microsoft Excel kaynak verinin bir kopyasını alır ve Pivot Önbelleğine saklar. Pivot Önbelleği, Microsoft Excel'in belleğinin içinde bulunur. Onu göremezsiniz, ancak bu, Pivot Tablonuzu oluştururken veya bir Dilim Seçimi değiştirdiğinizde veya satırlar/sütunlar etrafında hareket ettiğinizde Pivot Tablosunun başvurduğu veridir. Bu, Microsoft Excel'in Pivot Tablosundaki değişikliklere çok duyarlı olmasını sağlar, ancak dosya boyutunun potansiyel olarak iki kat artmasına neden olabilir.

Excel dosyanızı Workbook nesnesi içine yüklerken, Pivot Önbellek kayıtlarını da yüklemek isteyip istemediğinize karar verebilirsiniz. Bunun için [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/) özelliğini kullanabilirsiniz. Bu özelliğin varsayılan değeri **false**'dur. Pivot Önbellek oldukça büyükse, performansı artırabilir. Ancak eğer Pivot Önbellek kayıtlarını da yüklemek istiyorsanız, bu özelliği **true** olarak ayarlamalısınız.

## **Excel dosyasını yüklerken Pivot Önbellek Kayıtlarını Ayrıştırma**

Aşağıdaki örnek kod, [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/) özelliğinin kullanımını açıklar. Pivot önbellek kayıtları ayrıştırılırken [örnek Excel dosyasını](61767773.xlsx) yükler. Ardından pivot tablosunu yeniler ve [çıktı Excel dosyası olarak](61767774.xlsx) kaydeder.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
{{< app/cells/assistant language="python-net" >}}
