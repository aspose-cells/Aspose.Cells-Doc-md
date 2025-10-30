---
title: Formülleri içeren CSV dosyasını yükle veya içe aktar
type: docs
weight: 350
url: /tr/python-net/load-or-import-csv-file-with-formulas/
description: Aspose.Cells for Python via .NET API sını kullanarak Formüllerle CSV dosyası yükleme veya içe aktarma.
keywords: Python da formüllerle CSV dosyası yükleme veya içe aktarma, Python da Formüllü CSV yi Excel e dönüştürme via NET, Python da formüllü CSV yi xlsx ye dönüştürme, Excel dosyasına formüllü CSV yükleme
---

{{% alert color="primary" %}} 

CSV dosyası genellikle metin verileri içerir ve herhangi bir formül içermez. Bununla birlikte, bazen CSV dosyalarının formüller de içerdiği olur. Bu tür CSV dosyaları [TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) özelliği **true** olarak ayarlanarak yüklenmelidir. Bu özellik **true** olarak ayarlandığında, Aspose.Cells formülü basit bir metin olarak değil formül olarak ele alacaktır. Onlar formül olarak ele alınır ve Aspose.Cells formül hesaplama motoru bunları normal şekilde işleyecektir.

{{% /alert %}} 

Aşağıdaki kod, formülleri içeren CSV dosyasını nasıl yükleyebileceğinizi ve içe aktarabileceğinizi gösterir. Herhangi bir CSV dosyasını kullanabilirsiniz. İllüstrasyon amacıyla, bu veriyi içeren [basit csv dosyasını](5115034.csv) kullanıyoruz.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



Kod önce CSV dosyasını yükler, ardından D4 hücresine yeniden içe aktarır. Son olarak, workbook nesnesini XSLX formatında kaydeder. [Çıktı XLSX dosyası](5115052.xlsx) şöyle görünüyor. C3 ve F4 hücrelerinin formülü ve sonucu 800 olduğunu görebilirsiniz.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="python-net" >}}
