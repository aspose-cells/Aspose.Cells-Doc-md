---
title: Çalışma Sayfası CSS'sini Çıktı HTML'sinde Ayrı Olarak Dışa Aktarın
type: docs
weight: 80
url: /tr/java/export-worksheet-css-separately-in-output-html/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, Excel dosyanızı HTML'ye dönüştürdüğünüzde çalışma sayfası CSS'sini ayrı olarak dışa aktarma özelliği sağlar. Lütfen bu amaçla HtmlSaveOptions.ExportWorksheetCSSSeparately özelliğini kullanın ve Excel dosyasını HTML formatına kaydederken bunu true olarak ayarlayın.

## **Çalışma Sayfası CSS'sini Çıktı HTML'sinde Ayrı Olarak Dışa Aktarın**

Aşağıdaki örnek kod bir Excel dosyası oluşturur, B5 hücresine Kırmızı renkte bir metin ekler ve ardından HtmlSaveOptions.ExportWorksheetCSSSeparately özelliğini kullanarak HTML biçiminde kaydeder. Lütfen bkz[çıktı HTML'si](60489780.zip)referans için kod tarafından oluşturulur. İçinde örnek kodun bir sonucu olarak stylesheet.css dosyasını bulacaksınız.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Tek sayfalık çalışma kitabını HTML'ye aktar**

Birden çok sayfaya sahip bir çalışma kitabı Aspose.Cells kullanılarak HTML'ye dönüştürüldüğünde, CSS ve birden çok HTML dosyası içeren bir klasörle birlikte bir HTML dosyası oluşturur. Bu HTML dosyası tarayıcıda açıldığında sekmeler görünür durumdadır. HTML'ye dönüştürüldüğünde, tek çalışma sayfalı bir çalışma kitabı için aynı davranış gereklidir. Daha önce tek sayfalık çalışma kitapları için ayrı bir klasör oluşturulmuyordu ve yalnızca HTML dosyası oluşturuluyordu. Böyle bir HTML dosyası, tarayıcıda açıldığında sekme göstermez. Excel, tek sayfalar için de uygun klasör ve HTML oluşturur ve dolayısıyla aynı davranış Aspose.Cells kullanılarak gerçekleştirilir. Aşağıdaki örnek kodda kullanmak için örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
