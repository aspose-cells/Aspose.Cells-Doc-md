---
title: Çalışma kitabında HTML yüklerken Otomatik Sığdır Columns ve Satırlar Golang ve C++ ile
linktitle: Çalışma Kitabında HTML yüklenirken Sütunları ve Satırlar Otomatik Uydurma
type: docs
weight: 120
url: /tr/go-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Aspose.Cells for C++ kullanarak, HTML yükleme sırasında sütun ve satırların otomatik uyumunu nasıl sağlayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

HTML dosyanızı Çalışma Kitabının içine yüklerken sütun ve satırları otomatik olarak uyarlatabilirsiniz. Bu amaçla lütfen [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) özelliğini **true** olarak ayarlayın.

## **HTML yüklenirken Sütunları ve Satırları Otomatik Uydurma**

Aşağıdaki örnek kod, önce örnek HTML'yi herhangi bir yükleme seçeneği olmadan Çalışma Kitabına yükler ve XLSX formatında kaydeder. Daha sonra örnek HTML'yi tekrar Çalışma Kitabına yükler, bu sefer [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) özelliğini **true** olarak ayarladıktan sonra XLSX formatında kaydeder. Lütfen hem otomatik uyarlama sütunları ve satırları olmadan [OtomatikUyarlanmamışSütunveSatırÇıktıExcelDosyası](outputWithout_AutoFitColsAndRows.xlsx) hem de otomatik uyarlama sütunları ve satırları olan [OtomatikUyarlanmışSütunveSatırÇıktıExcelDosyası](outputWith_AutoFitColsAndRows.xlsx) dosyalarını indirin. Aşağıdaki ekran görüntüsü, [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getautofitcolsandrows/) özelliğinin her iki çıktı Excel dosyasındaki etkisini gösterir.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitColumnsAndRowsWhileLoadingHtmlInWorkbook.go" >}}
