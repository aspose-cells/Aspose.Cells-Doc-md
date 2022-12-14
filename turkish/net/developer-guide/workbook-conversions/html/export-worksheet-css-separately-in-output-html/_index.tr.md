---
title: Çalışma Sayfası CSS'sini Çıktı HTML'sinde Ayrı Olarak Dışa Aktarın
type: docs
weight: 80
url: /tr/net/export-worksheet-css-separately-in-output/
---
## **Olası Kullanım Senaryoları**

 Aspose.Cells, Excel dosyanızı HTML'ye dönüştürdüğünüzde çalışma sayfası CSS'sini ayrı olarak dışa aktarma özelliği sağlar. Lütfen kullan[**HtmlSaveOptions.ExportWorksheetCSSAyrı Olarak**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) bu amaç için mülk ve onu şu şekilde ayarlayın:**doğru** Excel dosyasını HTML biçiminde kaydederken.

## **Çalışma Sayfası CSS'sini Çıktı HTML'sinde Ayrı Olarak Dışa Aktarın**

Aşağıdaki örnek kod bir Excel dosyası oluşturur, hücreye biraz metin ekler**B5** içinde**Kırmızı** renk ve ardından kullanarak HTML biçiminde kaydeder[**HtmlSaveOptions.ExportWorksheetCSSAyrı Olarak**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)Emlak. Lütfen bkz[çıktı HTML'si](60489766.zip) referans için kod tarafından oluşturulur. Bulacaksın**stil sayfası.css**örnek kodun bir sonucu olarak içinde.

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Tek sayfalık çalışma kitabını HTML'ye aktar**

Birden çok sayfası olan bir çalışma kitabı Aspose.Cells kullanılarak HTML'ye dönüştürüldüğünde, CSS ve birden çok HTML dosyası içeren bir klasörle birlikte bir HTML dosyası oluşturur. Bu HTML dosyası tarayıcıda açıldığında sekmeler görünür durumdadır. HTML'ye dönüştürüldüğünde, tek çalışma sayfalı bir çalışma kitabı için aynı davranış gereklidir. Daha önce tek sayfalık çalışma kitapları için ayrı bir klasör oluşturulmuyordu ve yalnızca HTML dosyası oluşturuluyordu. Böyle bir HTML dosyası, tarayıcıda açıldığında sekme göstermez. MS Excel, tek bir sayfa için de uygun klasör ve HTML oluşturur ve dolayısıyla aynı davranış, Aspose.Cells API'leri kullanılarak uygulanır. Örnek dosya, aşağıdaki örnek kodda kullanmak için aşağıdaki bağlantıdan indirilebilir:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
