---
title: Çalışma Kitabında HTML yüklenirken Sütunları ve Satırlar Otomatik Uydurma
type: docs
weight: 70
url: /tr/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Olası Kullanım Senaryoları**

[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) nesnesine HTML dosyanızı yüklerken sütunları ve satırları otomatik ayarlayabilirsiniz. Bu amaçla [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) özelliğini **true** olarak ayarlayın lütfen.

## **HTML yüklenirken Sütunları ve Satırları Otomatik Uydurma**

Aşağıdaki örnek kod önce örnek HTML'i herhangi bir yükleme seçeneği olmadan Workbook'a yükler ve onu XLSX formatında kaydeder. Daha sonra örnek HTML'i tekrar Workbook'a yükler, ancak bu sefer [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) özelliğini **true** olarak ayarlayarak ve onu XLSX formatında kaydeder. Lütfen hem otomatik ayarlanmayan sütunlara ve satırlara sahip çıktı excel dosyasını ([Otomatik Olarak AyarlanmayanSutunlarVeSatirlar çıktısı](outputWithout_AutoFitColsAndRows.xlsx)) hem de otomatik ayarlanan sütunlara ve satırlara sahip çıktı excel dosyasını([Otomatik Olarak AyarlananSutunlarVeSatirlar çıktısı](outputWith_AutoFitColsAndRows.xlsx)) indirin. Aşağıdaki ekran görüntüsü [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) özelliğinin her iki çıktı excel dosyası üzerindeki etkisini göstermektedir.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
