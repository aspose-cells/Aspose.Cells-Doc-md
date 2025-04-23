---
title: Web Tarayıcıları tarafından Desteklenmeyen Kenar Stili Benzeri Kenar Stilini Dışa Aktar
type: docs
weight: 70
url: /tr/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, Web Tarayıcıları tarafından desteklenmeyen kesikli kenarlar türünü destekler. Aspose.Cells kullanarak böyle bir Excel dosyasını HTML'e dönüştürdüğünüzde, bu tür kenarlar kaldırılır. Bununla birlikte, Aspose.Cells, ayrıca benzer kenarları da [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) özelliğini kullanarak göstermeyi destekleyebilir. Lütfen değerini **true** olarak ayarlayın ve desteklenmeyen kenarlar ayrıca HTML dosyasına da dışa aktarılacaktır.

## **CrossHideRight ile Üzerine Binme Content'ini HTML'şe kaydederken Gizle**

Aşağıdaki örnek kod, aşağıdaki ekran görüntüsünde gösterilen desteklenmeyen kenarları içeren [örnek Excel dosyasını](64716832.xlsx) yükler. Ekran görüntüsü, kodun [çıktı HTML'sinde](64716831.zip) [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) özelliğinin etkisini daha da açıklamaktadır.

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
{{< app/cells/assistant language="java" >}}
