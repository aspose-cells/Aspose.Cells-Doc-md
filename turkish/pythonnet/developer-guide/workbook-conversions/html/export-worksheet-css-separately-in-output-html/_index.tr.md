---
title: Çıktı HTML sindeki Sayfa CSS sini Ayrı Ayrı Dışa Aktarma
type: docs
weight: 80
url: /tr/python-net/export-worksheet-css-separately-in-output/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for Python via .NET, Excel dosyanızı HTML'ye dönüştürürken çalışma sayfası CSS'sini ayrı olarak dışa aktarma özelliği sunar. Bu amaçla [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately) özelliğini kullanın ve kaydederken **true** olarak ayarlayın.

## **Çıktı HTML'sindeki Sayfa CSS'sini Ayrı Ayrı Dışa Aktarma**

Aşağıdaki örnek kod, bir Excel dosyası oluşturur, **B5** hücresine **kırmızı** renkte bir metin ekler ve ardından [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately) özelliğini kullanarak HTML formatında kaydeder. Referans için kod tarafından oluşturulan [çıktı HTML'si](60489766.zip)'nı inceleyin. Örnek kodun bir çıktısı olarak içinde **stylesheet.css** bulacaksınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.py" >}}

## **Tek Çalışsayı İş Kitabını HTML'ye Dışa Aktarma**

 Çok sayfalı çalışma kitabı Aspose.Cells for Python via .NET kullanılarak HTML'ye dönüştürüldüğünde, HTML dosyası ve beraberinde CSS içeren klasör ve çok sayfalı HTML dosyaları oluşturulur. Bu HTML dosyası tarayıcıda açıldığında sekmeler görünür. Aynı davranış, tek sayfalık çalışma kitapları için de geçerlidir. Daha önce, yalnızca HTML dosyası oluşturulur ve sekmeler gösterilmezdi. Bu tarz HTML dosyası tarayıcıda açıldığında sekmeleri göstermez. Microsoft Excel, tek sayfalık çalışma kitabı için de uygun klasör yapısı ve HTML oluşturur ve bu nedenle, Aspose.Cells for Python via .NET API'leri kullanılarak aynı davranış sağlanmıştır. Aşağıdaki bağlantıdan örnek dosyayı indirebilir ve aşağıdaki örnek kodda kullanabilirsiniz:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetSingleSheetTabNameInHtml-1.py" >}}
