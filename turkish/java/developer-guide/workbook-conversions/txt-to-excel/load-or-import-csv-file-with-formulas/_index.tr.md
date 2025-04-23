---
title: Formülleri içeren CSV dosyasını yükle veya içe aktar
type: docs
weight: 500
url: /tr/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSV dosyaları genellikle metin verileri içerir ve herhangi bir formül içermez. Ancak bazen CSV dosyalarının da formülleri içerdiği olur. Bu tür CSV dosyaları [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) değerini **true** ayarlayarak yüklenebilir. Bu özellik **true** olarak ayarlandığında, Aspose.Cells formülü basit metin olarak değil, formül olarak işleyecektir. Bunlar, Aspose.Cells formül hesaplama motoru tarafından normal olarak işlenecektir.

{{% /alert %}} 
## **Formülleri Yükle veya İçe Aktar CSV Dosyası**
Aşağıdaki kod, formüller içeren bir CSV dosyasını nasıl yükleyip içe aktarabileceğinizi göstermektedir. Herhangi bir CSV dosyası kullanabilirsiniz. İllüstrasyon amacıyla [basit csv dosyasını](5472505.csv) kullanıyoruz. İçerisinde formül bulunduğunu göreceksiniz.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

Kod ilk olarak CSV dosyasını yükler, ardından D4 hücresine yeniden içe aktarır. Son olarak, çalışma kitabı nesnesini XSLX formatında kaydeder. [Çıktı XLSX dosyası](5472503.xlsx) şöyle görünüyor. C3 ve F4 hücrelerinde formül ve sonucu 800 bulunmaktadır.

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
{{< app/cells/assistant language="java" >}}
