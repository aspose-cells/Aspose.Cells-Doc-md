---
title: Excel dosyasını yüklerken Pivot Önbelleğe Alınmış Kayıtları Ayrıştırma
type: docs
weight: 70
url: /tr/net/parsing-pivot-cached-records-while-loading-excel-file/
---
## **Olası Kullanım Senaryoları**

Bir Pivot Tablo oluşturduğunuzda, Microsoft Excel, kaynak verilerin bir kopyasını alır ve bunu Pivot Önbellek'te depolar. Pivot Önbelleği, Microsoft Excel'in belleğinde tutulur. Bunu göremezsiniz, ancak Pivot Tablonuzu oluşturduğunuzda veya bir Dilimleyici seçimini değiştirdiğinizde veya satırları/sütunları hareket ettirdiğinizde Pivot Tablonun başvurduğu veriler budur. Bu, Microsoft Excel'in Pivot Tablodaki değişikliklere çok duyarlı olmasını sağlar, ancak dosyanızın boyutunu da ikiye katlayabilir. Ne de olsa Pivot Önbellek, kaynak verilerinizin yalnızca bir kopyasıdır, bu nedenle dosya boyutunuzun potansiyel olarak iki katına çıkması mantıklıdır.

Workbook nesnesinin içine Excel dosyanızı yüklediğinizde Pivot Cache kayıtlarını da yüklemek isteyip istemediğinize karar verebilirsiniz.[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) Emlak. Bu özelliğin varsayılan değeri**YANLIŞ** . Pivot Cache oldukça büyükse performansı artırabilir. Ancak Pivot Cache kayıtlarını da yüklemek istiyorsanız bu özelliği şu şekilde ayarlamalısınız:**doğru**.

## **Excel dosyasını yüklerken Pivot Önbelleğe Alınmış Kayıtları Ayrıştırma**

Aşağıdaki örnek kod, kullanımını açıklar[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) Emlak. o yükler[örnek excel dosyası](61767773.xlsx) pivot önbelleğe alınmış kayıtları ayrıştırırken. Ardından pivot tabloyu yeniler ve tablo olarak kaydeder.[çıktı excel dosyası](61767774.xlsx).

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.cs" >}}
