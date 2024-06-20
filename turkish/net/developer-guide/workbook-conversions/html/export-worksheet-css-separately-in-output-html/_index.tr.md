---
title: Çıktı HTML sindeki Sayfa CSS sini Ayrı Ayrı Dışa Aktarma
type: docs
weight: 80
url: /tr/net/export-worksheet-css-separately-in-output/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, Excel dosyanızı HTML'ye dönüştürdüğünüzde çalışsayı CSS'sini ayrı ayrı dışa aktarmayı sağlar. Bu amaçla [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) özelliğini kullanın ve Excel dosyasını HTML formatında kaydederken **true** olarak ayarlayın.

## **Çıktı HTML'sindeki Sayfa CSS'sini Ayrı Ayrı Dışa Aktarma**

Aşağıdaki örnek kod, bir Excel dosyası oluşturur, **B5** hücresine **kırmızı** renkte bir metin ekler ve ardından [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) özelliğini kullanarak HTML formatında kaydeder. Referans için kod tarafından oluşturulan [çıktı HTML'si](60489766.zip)'nı inceleyin. Örnek kodun bir çıktısı olarak içinde **stylesheet.css** bulacaksınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Tek Çalışsayı İş Kitabını HTML'ye Dışa Aktarma**

Aspose.Cells tarafından birden fazla sayfaya sahip bir çalışsayının HTML'ye dönüştürülmesi durumunda, HTML dosyası ve CSS ile birlikte birden çok HTML dosyası içeren bir klasör oluşturur. Bu HTML dosyası tarayıcıda açıldığında sekmeler görünür. Bu sekmeler, tek çalışsayılı bir iş kitabı HTML'ye dönüştürüldüğünde gereklidir. Daha önce tek sayfalı çalışma kitapları için ayrı klasör oluşturulmamış ve sadece HTML dosyası oluşturulmuştu. Bu tür HTML dosyaları, tarayıcıda açıldığında sekme göstermez. MS Excel ayrıca tek sayfalı için uygun klasör ve HTML oluşturur ve bu nedenle Aspose.Cells API'leri kullanılarak aynı davranış uygulanır. Örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz: 

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
