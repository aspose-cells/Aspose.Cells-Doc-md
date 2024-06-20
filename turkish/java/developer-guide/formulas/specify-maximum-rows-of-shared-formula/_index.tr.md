---
title: Paylaşılan Formülün Maksimum Satırlarını Belirtme
type: docs
weight: 40
url: /tr/java/specify-maximum-rows-of-shared-formula/
---

## **Olası Kullanım Senaryoları**

Paylaşılan formülün varsayılan maksimum satır sayısı 64'tür. 1000 gibi herhangi bir sayı olabilir. Paylaşılan formül, farklı satır sayılarıyla farklı performans sağlar. Bu nedenle, Aspose.Cells, paylaşılan formülün maksimum satırlarını belirtmek için kullanılabilecek [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) özelliğini sağlar. Paylaşılan formül, toplam satırları bu sayıdan büyükse, aşağıdaki ekran görüntüsünde gösterildiği gibi paylaşılan formlüle ayrılır.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Paylaşılan Formülün Maksimum Satırlarını Belirtme**

Aşağıdaki örnek kod, [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) özelliğinin kullanımını açıklar. Paylaşılan formülün maksimum satır sayısını 5 olarak ayarlar ve 100 satır için D1 hücresine paylaşılan formül ekler ve [çıktı Excel dosyasına](61767869.xlsx) kaydeder. Çıktı Excel dosyasının içeriğini çıkartıp *sheet1.xml* dosyasını kontrol ederseniz, yukarıdaki ekran görüntüsünde vurgulandığı gibi paylaşılan formülün her 5 satırda bir bölündüğünü göreceksiniz.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
