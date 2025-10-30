---
title: Çıkış HTML sinde Sayfa Sekmesine Ayrık CSS Dışa Aktarımı ile
linktitle: Çıktı HTML sindeki Sayfa CSS sini Ayrı Ayrı Dışa Aktarma
type: docs
weight: 80
url: /tr/go-cpp/export-worksheet-css-separately-in-output/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını HTML ye dönüştürürken çalışma sayfası CSS lerini ayrı olarak ihraç etmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, Excel dosyanızı HTML'ye dönüştürürken çalışma sayfası CSS'sini ayrı olarak dışa aktarma özelliği sağlar. Lütfen bu amaçla [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/) özelliğini kullanın ve Excel dosyasını HTML formatına kaydederken **true** olarak ayarlayın.

## **Çıktı HTML'sindeki Sayfa CSS'sini Ayrı Ayrı Dışa Aktarma**

Aşağıdaki örnek kod, bir Excel dosyası oluşturur, **B5** hücresine **kırmızı** renkte bir metin ekler ve ardından [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/) özelliğini kullanarak HTML formatında kaydeder. Referans için kod tarafından oluşturulan [çıktı HTML'si](60489766.zip)'nı inceleyin. Örnek kodun bir çıktısı olarak içinde **stylesheet.css** bulacaksınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml.go" >}}
## **Tek Sayfa Çalışma Kitabını HTML'ye Dışa Aktar**

Birden fazla çalışma sayfası içeren bir çalışma kitabı Aspose.Cells kullanılarak HTML'ye dönüştürüldüğünde, CSS ve çoklu HTML dosyalarını içeren bir klasörle birlikte bir HTML dosyası oluşturur. Bu HTML dosyası tarayıcıda açıldığında sekmeler görülür. Aynı davranış, tek sayfalık çalışma kitabı HTML'ye dönüştürülürken de istenir. Önceden, tek sayfalık çalışma kitapları için ayrı bir klasör oluşturulmazdı ve yalnızca bir HTML dosyası oluşturulurdu. Böyle bir HTML dosyası tarayıcıda açıldığında sekme göstermez. MS Excel, tek sayfalık çalışma kitabı için de uygun bir klasör ve HTML oluşturur ve bu nedenle aynı davranış Aspose.Cells API'leri kullanılarak uygulanmıştır. Aşağıdaki bağlantıdan örnek dosya indirilebilir ve aşağıdaki örnek kodda kullanılabilir:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml-1.go" >}}
