---
title: Formüllerle CSV dosyasını yükleyin veya içe aktarın
type: docs
weight: 350
url: /tr/net/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 CSV dosyası çoğunlukla metinsel veriler içerir ve herhangi bir formül içermez. Ancak bazen CSV dosyalarının da formüller içerdiği görülür. Bu tür CSV dosyaları ayarlanarak yüklenmelidir.[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) olarak**doğru** . Bu özellik ayarlandıktan sonra**doğru**, Aspose.Cells, formülü basit metin olarak ele almaz. Bunlar formül olarak ele alınacak ve Aspose.Cells formül hesaplama motoru bunları her zamanki gibi işleyecektir.

{{% /alert %}} 

 Aşağıdaki kod, formüller içeren bir CSV dosyasını nasıl yükleyebileceğinizi ve içe aktarabileceğinizi gösterir. Herhangi bir CSV dosyasını kullanabilirsiniz. Örnekleme amacıyla,[basit csv dosyası](5115034.csv) bu verileri içeren. Gördüğünüz gibi bir formül içeriyor.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



 Kod önce CSV dosyasını yükler, ardından D4 hücresinde yeniden içe aktarır. Son olarak, çalışma kitabı nesnesini XSLX biçiminde kaydeder. bu[çıktı XLSX dosyası](5115052.xlsx) buna benzer. Gördüğünüz gibi C3 ve F4 hücresi formül ve sonucu 800 içerir.

|![yapılacaklar:resim_alternatif_Metin](load-or-import-csv-file-with-formulas_1.png)|
|:- |

