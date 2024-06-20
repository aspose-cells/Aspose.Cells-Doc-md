---
title: Çalışma Kitabında HTML yüklenirken Sütunları ve Satırlar Otomatik Uydurma
type: docs
weight: 120
url: /tr/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Olası Kullanım Senaryoları**

HTML dosyanızı Çalışma Kitabının içine yüklerken sütun ve satırları otomatik olarak uyarlatabilirsiniz. Bu amaçla lütfen [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) özelliğini **true** olarak ayarlayın.

## **HTML yüklenirken Sütunları ve Satırları Otomatik Uydurma**

Aşağıdaki örnek kod, önce örnek HTML'yi herhangi bir yükleme seçeneği olmadan Çalışma Kitabına yükler ve XLSX formatında kaydeder. Daha sonra örnek HTML'yi tekrar Çalışma Kitabına yükler, bu sefer [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) özelliğini **true** olarak ayarladıktan sonra XLSX formatında kaydeder. Lütfen hem otomatik uyarlama sütunları ve satırları olmadan [OtomatikUyarlanmamışSütunveSatırÇıktıExcelDosyası](outputWithout_AutoFitColsAndRows.xlsx) hem de otomatik uyarlama sütunları ve satırları olan [OtomatikUyarlanmışSütunveSatırÇıktıExcelDosyası](outputWith_AutoFitColsAndRows.xlsx) dosyalarını indirin. Aşağıdaki ekran görüntüsü, [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) özelliğinin her iki çıktı Excel dosyasındaki etkisini gösterir.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

