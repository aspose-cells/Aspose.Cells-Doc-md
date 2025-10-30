---
title: Paylaşılan Formülün Maksimum Satırlarını Belirtme
type: docs
weight: 40
url: /tr/python-net/specify-maximum-rows-of-shared-formula/
---

## **Olası Kullanım Senaryoları**

Paylaşılan formülün varsayılan maksimum satır sayısı 64'tür. Bu herhangi bir sayı olabilir, örneğin 1000. Paylaşılan formülün performansı satır sayısına göre değişir. Bu nedenle, Aspose.Cells for Python via .NET, paylaşılan formülün maksimum satır sayısını belirlemek için [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula) özelliği sağlar. Toplam satır sayısı bu değeri aşarsa, paylaşılan formüller birkaç paylaşılan formüle bölünecektir, aşağıdaki ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Paylaşılan Formülün Maksimum Satırlarını Belirtme**

Aşağıdaki örnek kod, [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula) özelliğinin kullanımını açıklar. Paylaşılan formülün maksimum satırlarını 5'e ayarlar ve D1 hücresine paylaşılan formül ekler ve 100 satıra ulaştıktan sonra [çıktı Excel dosyasına](61767856.xlsx) kaydeder. Çıkış Excel dosyasının içeriğini çıkarıp *sheet1.xml* dosyasını kontrol ederseniz, yukarıdaki ekran görüntüsünde vurgulanan şekilde her 5 satırda bir paylaşılan formülün bölündüğünü göreceksiniz.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SpecifyMaximumRowsOfSharedFormula.py" >}}

{{< app/cells/assistant language="python-net" >}}
