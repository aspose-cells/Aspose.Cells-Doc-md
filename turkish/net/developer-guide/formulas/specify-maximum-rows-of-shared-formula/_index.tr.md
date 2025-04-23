---
title: Paylaşılan Formülün Maksimum Satırlarını Belirtme
type: docs
weight: 40
url: /tr/net/specify-maximum-rows-of-shared-formula/
---

## **Olası Kullanım Senaryoları**

Paylaşılan formülün varsayılan maksimum satır sayısı 64'tür. 1000 gibi herhangi bir sayı olabilir. Paylaşılan formülün performansı, farklı satır sayıları ile değişir. Bu nedenle, Aspose.Cells, maksimum paylaşılan formül satırlarını belirlemek için kullanılabilecek [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) özelliğini sağlar. Eğer paylaşılan formülün toplam satır sayısı bunun üstündeyse, paylaşılan formül gösterildiği gibi birden çok paylaşılmış formüle bölünecektir.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Paylaşılan Formülün Maksimum Satırlarını Belirtme**

Aşağıdaki örnek kod, [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) özelliğinin kullanımını açıklar. Paylaşılan formülün maksimum satırlarını 5'e ayarlar ve D1 hücresine paylaşılan formül ekler ve 100 satıra ulaştıktan sonra [çıktı Excel dosyasına](61767856.xlsx) kaydeder. Çıkış Excel dosyasının içeriğini çıkarıp *sheet1.xml* dosyasını kontrol ederseniz, yukarıdaki ekran görüntüsünde vurgulanan şekilde her 5 satırda bir paylaşılan formülün bölündüğünü göreceksiniz.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
