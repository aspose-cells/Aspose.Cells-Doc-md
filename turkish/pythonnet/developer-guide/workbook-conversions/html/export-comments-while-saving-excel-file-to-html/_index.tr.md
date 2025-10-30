---
title: Excel Dosyasını HTML ye Kaydederken Yorumları Dışa Aktar
type: docs
weight: 40
url: /tr/python-net/export-comments-while-saving-excel-file-to/
---

## **Olası Kullanım Senaryoları**

 Excel dosyanızı HTML'ye kaydederken, yorumlar dışa aktarılmaz. Ancak, Aspose.Cells for Python via .NET, bu özelliği [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments) özelliği kullanarak sağlar. Eğer **true** olarak ayarlarsanız, HTML ayrıca Excel dosyanızdaki yorumları da gösterecektir.

## **Excel Dosyasını HTML'ye Kaydederken Yorumları Dışa Aktar**

Aşağıdaki örnek kod, [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments) özelliğinin kullanımını açıklar. Ekran görüntüsü, bu kodun **true** olarak ayarlandığında HTML üzerindeki etkisini göstermektedir. Referans için lütfen [örnek Excel dosyasını](50528260.xlsx) ve [oluşturulan HTML'i](5052826.txt) indirin.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
