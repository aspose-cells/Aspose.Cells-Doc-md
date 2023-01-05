---
title: Paylaşılan Formülün Maksimum Satırını Belirtin
type: docs
weight: 40
url: /tr/net/specify-maximum-rows-of-shared-formula/
---
## **Olası Kullanım Senaryoları**

Paylaşılan formülün varsayılan maksimum satır sayısı 64'tür. Herhangi bir sayı olabilir, örneğin 1000 olabilir. Paylaşılan formülün performansı, farklı satır sayısıyla değişir. Bu nedenle, Aspose.Cells,[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula)paylaşılan formülün maksimum satırlarını belirtmek için kullanılabilen özellik. Aşağıdaki ekran görüntüsünde gösterildiği gibi, paylaşılan formülün toplam satırları bundan büyükse, paylaşılan formül birkaç paylaşılan formüle bölünecektir.

![yapılacaklar:resim_alternatif_metin](specify-maximum-rows-of-shared-formula_1.png)

## **Paylaşılan Formülün Maksimum Satırını Belirtin**

Aşağıdaki örnek kod,[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) Emlak. Paylaşılan formülün maksimum satır sayısını 5 olarak ayarlar ve paylaşılan formülü 100 satır için D1 hücresine ekler ve şuraya kaydeder:[çıktı excel dosyası](61767856.xlsx). Çıktı Excel dosyasının içeriğini çıkarırsanız ve kontrol ederseniz*sayfa1.xml*, yukarıdaki ekran görüntüsünde vurgulandığı gibi, paylaşılan formülün her 5 satırdan sonra bölündüğünü göreceksiniz.

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
