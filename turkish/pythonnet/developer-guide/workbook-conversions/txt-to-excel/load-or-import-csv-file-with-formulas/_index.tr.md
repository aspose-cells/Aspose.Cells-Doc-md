---
title: CSV dosyasını formüllerle yükleyin veya içe aktarın
type: docs
weight: 350
url: /tr/python-net/load-or-import-csv-file-with-formulas/
description: Aspose.Cells for Python via .NET API'i kullanarak CSV dosyasını Formüllerle yükleyin veya içe aktarın.
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---
{{% alert color="primary" %}} 

 CSV dosyası çoğunlukla metinsel veriler içerir ve herhangi bir formül içermez. Ancak bazen CSV dosyalarının formüller de içerdiği görülür. Bu tür CSV dosyaları ayarlanarak yüklenmelidir.[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) *doğru** olarak. Bu özellik *true** olarak ayarlandığında, Aspose.Cells formülü basit metin olarak değerlendirmeyecektir. Bunlar formül olarak ele alınacak ve Aspose.Cells formül hesaplama motoru bunları her zamanki gibi işleyecektir.

{{% /alert %}} 

 Aşağıdaki kod, formüller içeren bir CSV dosyasını nasıl yükleyebileceğinizi ve içe aktarabileceğinizi gösterir. Herhangi bir CSV dosyasını kullanabilirsiniz. Örnekleme amacıyla şunu kullanıyoruz:[basit csv dosyası](5115034.csv)bu verileri içeren. Gördüğünüz gibi bir formül içeriyor.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



 Kod önce CSV dosyasını yükler, ardından dosyayı D4 hücresine tekrar aktarır. Son olarak çalışma kitabı nesnesini XSLX formatında kaydeder.[çıktı XLSX dosyası](5115052.xlsx) buna benzer. Gördüğünüz gibi C3 ve F4 hücreleri formülü ve sonucunu 800 içeriyor.

|![yapılacak şey:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

