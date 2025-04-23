---
title: Web Tarayıcıları tarafından Desteklenmeyen Kenar Stili Benzeri Kenar Stilini Dışa Aktar
type: docs
weight: 70
url: /tr/python-net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, Web Tarayıcıları tarafından desteklenmeyen bazı kesik kenar sınırlarını destekler. Bu tür sınırlar Aspose.Cells for Python via .NET kullanılarak HTML’ye dönüştürüldüğünde, bu sınırlar kaldırılır. Ancak, Aspose.Cells for Python via .NET, [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) özelliğini kullanarak bu sınırların gösterilmesine de destek sağlar. Lütfen değeri **true** olarak ayarlayın ve desteklenmeyen sınırlar da HTML'ye aktarılır.

## **CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle**

Aşağıdaki örneğin kodu, aşağıdaki ekran görüntüsünde gösterildiği gibi desteklenmeyen bazı kenarlıkları içeren [örnek Excel dosyasını](64716806.xlsx) yükler. Ekran görüntüsü, [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) özelliğinin [çıkış HTML'sinin](64716804.zip) içindeki etkisini daha ayrıntılı olarak açıklar.

![todo:image_alt_text](1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportSimilarBorderStyle.py" >}}
