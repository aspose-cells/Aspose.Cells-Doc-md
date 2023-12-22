---
title: Excel dosyasını yüklerken Pivot Önbelleğe Alınmış Kayıtları Ayrıştırma
type: docs
weight: 70
url: /tr/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Aspose.Cells for Python via .NET ile Excel dosyası yüklenirken Pivot Önbelleğe Alınmış Kayıtlar nasıl ayrıştırılır.
keywords: Parse Pivot Cached Records while loading Excel file.
---
##  **Olası Kullanım Senaryoları**

Bir Pivot Tablo oluşturduğunuzda, Microsoft Excel, kaynak verilerin bir kopyasını alır ve bunu Pivot Önbelleğinde saklar. Pivot Cache, Microsoft Excel'in belleğinde tutulur. Bunu göremezsiniz ancak Pivot Tablonuzu oluşturduğunuzda veya bir Dilimleyici seçimini değiştirdiğinizde veya satırları/sütunları hareket ettirdiğinizde Pivot Tablonun referans verdiği veriler budur. Bu, Microsoft Excel'in Pivot Tablodaki değişikliklere çok duyarlı olmasını sağlar, ancak dosyanızın boyutunu da iki katına çıkarabilir. Sonuçta Pivot Önbellek, kaynak verilerinizin yalnızca bir kopyasıdır, dolayısıyla dosya boyutunuzun potansiyel olarak iki katı olması mantıklıdır.

Excel dosyanızı Çalışma Kitabı nesnesine yüklediğinizde Pivot Cache kayıtlarını da yüklemek isteyip istemediğinize karar verebilirsiniz.[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)mülk. Bu özelliğin varsayılan değeri *yanlış**'tır. Pivot Cache oldukça büyükse performansı arttırabilir. Ancak Pivot Cache'in kayıtlarını da yüklemek istiyorsanız bu özelliği *true** olarak ayarlamalısınız.

##  **Excel dosyasını yüklerken Pivot Önbelleğe Alınmış Kayıtları Ayrıştırma**

Aşağıdaki örnek kod, kullanımını açıklamaktadır.[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)mülk. Şunu yükler:[örnek Excel dosyası](61767773.xlsx) Pivot önbelleğe alınmış kayıtları ayrıştırırken. Daha sonra pivot tabloyu yeniler ve onu şu şekilde kaydeder:[Excel dosyasının çıktısı](61767774.xlsx).

##  **Basit kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
