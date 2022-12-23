---
title: Çalışma Sayfası CSS'sini Çıktı HTML'de Ayrı Olarak Dışa Aktar
type: docs
weight: 80
url: /tr/java/export-worksheet-css-separately-in-output-html/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, Excel dosyanızı HTML'e dönüştürdüğünüzde çalışma sayfası CSS'sini ayrı olarak dışa aktarma özelliği sağlar. Lütfen bu amaçla HtmlSaveOptions.ExportWorksheetCSSSeparately özelliğini kullanın ve Excel dosyasını HTML biçiminde kaydederken bunu doğru olarak ayarlayın.

## **Çalışma Sayfası CSS'sini Çıktı HTML'de Ayrı Olarak Dışa Aktar**

Aşağıdaki örnek kod bir Excel dosyası oluşturur, B5 hücresine Kırmızı renkte bir miktar metin ekler ve ardından HtmlSaveOptions.ExportWorksheetCSSSeparately özelliğini kullanarak HTML biçiminde kaydeder. Lütfen bkz[çıkış HTML](60489780.zip)referans için kod tarafından oluşturulur. İçinde örnek kodun bir sonucu olarak stylesheet.css dosyasını bulacaksınız.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Tek sayfalık çalışma kitabını HTML'e aktar**

Birden çok sayfası olan bir çalışma kitabı Aspose.Cells kullanılarak HTML'e dönüştürüldüğünde, CSS ve birden çok HTML dosyası içeren bir klasörle birlikte bir HTML dosyası oluşturur. Bu HTML dosyası tarayıcıda açıldığında sekmeler görünür. Tek çalışma sayfalı bir çalışma kitabı HTML'e dönüştürüldüğünde aynı davranış gerekir. Daha önce tek sayfalık çalışma kitapları için ayrı bir klasör oluşturulmuyordu ve yalnızca HTML dosyası oluşturuluyordu. Böyle bir HTML dosyası, tarayıcıda açıldığında sekme göstermez. Excel, tek sayfalar için de uygun klasör ve HTML oluşturur ve dolayısıyla aynı davranış Aspose.Cells kullanılarak uygulanır. Aşağıdaki örnek kodda kullanmak için örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
