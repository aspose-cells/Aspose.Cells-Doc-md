---
title: Yeni satırlara veri girilirken Tablo veya List Objesinde Formülü otomatik olarak çoğaltın
linktitle: Tablo Formülünü Ayarlar
type: docs
weight: 260
url: /tr/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Olası Kullanım Senaryoları**
Bazen, Tablo veya Liste Nesnesine girerken, formül otomatik olarak yeni satırlara yayılmasını istersiniz. Bu, Microsoft Excel'in varsayılan davranışıdır. Aynı şeyi Aspose.Cells for Python via .NET kullanarak gerçekleştirmek için [**ListColumn.formula**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listcolumn/formula) özelliğini kullanın.

## **Yeni satırlara veri girilirken Tablo veya List Objesinde Formülü otomatik olarak çoğaltın**
Aşağıdaki örnek kod, yeni veri girdiğinizde sütun B'deki formülün otomatik olarak yeni satırlara yayılacak şekilde bir Tablo veya List Objesi oluşturur. Lütfen bu kodla oluşturulan [çıktı excel dosyasını](5115469.xlsx) kontrol edin. A3 hücresine herhangi bir sayı girerseniz, B2 hücresindeki formülün otomatik olarak B3 hücresine yayıldığını göreceksiniz.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-PropagateFormulaInTable-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
