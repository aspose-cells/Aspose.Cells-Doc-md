---
title: Yeni satırlara veri girilirken Tablo veya List Objesinde Formülü otomatik olarak çoğaltın
type: docs
weight: 980
url: /tr/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Olası Kullanım Senaryoları**
Bazen, yeni veriler girilirken Tablo veya Liste Nesnesindeki bir formülün otomatik olarak yeni satırlara yayılmasını istersiniz. Bu, Microsoft Excel'in varsayılan davranışıdır. Aynı şeyi Aspose.Cells ile başarmak için lütfen [ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula) özelliğini kullanın.
## **Yeni satırlara veri girilirken Tablo veya List Objesinde Formülü otomatik olarak çoğaltın**
Aşağıdaki örnek kod, Tablo veya Liste Nesnesini öyle bir şekilde oluşturur ki sütun B'deki formül, yeni veriler girildiğinde otomatik olarak yeni satırlara yayılır. Bu kodla oluşturulan [çıktı excel dosyasını](5472519.xlsx) kontrol edin. A3 hücresine herhangi bir sayı girerseniz, B2 hücresindeki formülün otomatik olarak B3 hücresine yayıldığını göreceksiniz.
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
{{< app/cells/assistant language="java" >}}
