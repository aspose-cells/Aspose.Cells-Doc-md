---
title: CSV dosyasını Formüllerle Yükleyin veya İçe Aktarın
type: docs
weight: 500
url: /tr/java/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 CSV dosyası çoğunlukla metinsel veriler içerir ve herhangi bir formül içermez. Ancak bazen CSV dosyaları da formüller içeriyor. Bu tür CSV dosyaları ayarlanarak yüklenmelidir.[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) ile**doğru** . Bu özellik ayarlandıktan sonra**doğru**, Aspose.Cells, formülü basit metin olarak ele almaz. Bunlar formül olarak ele alınacak ve Aspose.Cells formül hesaplama motoru bunları her zamanki gibi işleyecektir.

{{% /alert %}} 
## **CSV dosyasını Formüllerle Yükleyin veya İçe Aktarın**
 Aşağıdaki kod, bir CSV dosyasını formüllerle nasıl yükleyebileceğinizi ve içe aktarabileceğinizi gösterir. Herhangi bir CSV dosyasını kullanabilirsiniz. Örnekleme amacıyla,[basit csv dosyası](5472505.csv) bu verileri içeren. Gördüğünüz gibi bir formül içeriyor.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

Kod önce CSV dosyasını yükler, ardından D4 hücresinde yeniden içe aktarır. Son olarak, çalışma kitabı nesnesini XSLX biçiminde kaydeder. bu[çıktı XLSX dosyası](5472503.xlsx) buna benzer. Gördüğünüz gibi C3 ve F4 hücresi formül ve sonucu 800 içerir.

![yapılacaklar:resim_alternatif_metin](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
