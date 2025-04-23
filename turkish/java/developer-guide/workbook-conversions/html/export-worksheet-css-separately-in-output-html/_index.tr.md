---
title: Çıktı HTML sindeki Sayfa CSS sini Ayrı Ayrı Dışa Aktarma
type: docs
weight: 80
url: /tr/java/export-worksheet-css-separately-in-output-html/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, Excel dosyanızı HTML'e dönüştürürken çalışsayfa CSS'sini ayrıca dışa aktarma özelliği sağlar. Bu amaçla lütfen HtmlSaveOptions.ExportWorksheetCSSSeparately özelliğini kullanın ve Excel dosyasını HTML biçimine kaydederken bunu **true** olarak ayarlayın.

## **Çıktı HTML'sindeki Sayfa CSS'sini Ayrı Ayrı Dışa Aktarma**

Aşağıdaki örnek kod, bir Excel dosyası oluşturur, B5 hücresine Kırmızı renkte bazı metin ekler ve ardından HtmlSaveOptions.ExportWorksheetCSSSeparately özelliğini kullanarak HTML biçiminde kaydeder. Lütfen örnek kodun sonucu olarak [oluşturulan çıktı HTML](60489780.zip) dosyasında bunu referans için bulunabilir; içerisinde stylesheet.css bulacaksınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Tek Çalışsayı İş Kitabını HTML'ye Dışa Aktarma**

Birkaç sayfalı bir çalışma kitabı, Aspose.Cells kullanılarak HTML'ye dönüştürüldüğünde, bir HTML dosyası ve CSS ve birden çok HTML dosyası içeren bir klasör oluşturur. Bu HTML dosyası tarayıcıda açıldığında sekmeler görünür. Tek çalışma sayfası olan bir çalışma kitabı HTML'ye dönüştürüldüğünde de aynı davranış gereklidir. Daha önce tek sayfalı çalışma kitapları için ayrı bir klasör oluşturulmuyordu ve yalnızca HTML dosyası oluşturuluyordu. Bu tür HTML dosyası tarayıcıda açıldığında sekme görüntülemezdi. Excel ayrıca tek sayfalar için doğru klasör ve HTML oluşturur ve bu nedenle aynı davranış, Aspose.Cells kullanılarak uygulanır. Örnek dosyayı aşağıdaki bağlantıdan indirebilir ve aşağıdaki örnek kod kullanılarak kullanmak için kullanabilirsiniz:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
{{< app/cells/assistant language="java" >}}
