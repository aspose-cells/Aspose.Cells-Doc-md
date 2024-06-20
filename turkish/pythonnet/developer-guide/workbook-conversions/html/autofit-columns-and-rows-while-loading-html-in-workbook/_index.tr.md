---
title: Çalışma Kitabında HTML yüklenirken Sütunları ve Satırlar Otomatik Uydurma
type: docs
weight: 120
url: /tr/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Bu konu, Aspose.Cells için Python via NET kullanarak çalışma Kitabı içine HTML yüklenirken Sütunları ve Satırları Otomatik Boyutlandırma nasıl yapılacağını gösterir.
keywords: HTML yüklenirken Sütunları ve Satırları Otomatik Boyutlandırma, HTML yüklerken Sütunları ve Satırları Otomatik Boyutlandırma.
---

## **Olası Kullanım Senaryoları**

HTML dosyanızı Çalışma Kitabının içine yüklerken sütun ve satırları otomatik olarak uyarlatabilirsiniz. Bu amaçla lütfen [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) özelliğini **true** olarak ayarlayın.

## **HTML yüklenirken Sütunları ve Satırları Otomatik Uydurma**

Aşağıdaki örnek kod, önce örnek HTML'yi herhangi bir yükleme seçeneği olmadan Çalışma Kitabına yükler ve XLSX formatında kaydeder. Daha sonra örnek HTML'yi tekrar Çalışma Kitabına yükler, bu sefer [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) özelliğini **true** olarak ayarladıktan sonra XLSX formatında kaydeder. Lütfen hem otomatik uyarlama sütunları ve satırları olmadan [OtomatikUyarlanmamışSütunveSatırÇıktıExcelDosyası](outputWithout_AutoFitColsAndRows.xlsx) hem de otomatik uyarlama sütunları ve satırları olan [OtomatikUyarlanmışSütunveSatırÇıktıExcelDosyası](outputWith_AutoFitColsAndRows.xlsx) dosyalarını indirin. Aşağıdaki ekran görüntüsü, [**HtmlLoadOptions.auto_fit_cols_and_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/) özelliğinin her iki çıktı Excel dosyasındaki etkisini gösterir.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

