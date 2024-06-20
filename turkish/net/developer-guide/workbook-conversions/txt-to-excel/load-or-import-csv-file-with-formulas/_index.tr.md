---
title: Formülleri içeren CSV dosyasını yükle veya içe aktar
type: docs
weight: 350
url: /tr/net/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSV dosyaları çoğunlukla metinsel veriler içerir ve formül içermezler. Ancak bazen CSV dosyalarının da formüller içerdiği olur. Bu tür CSV dosyaları, [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) özelliğini **true** olarak ayarlayarak yüklenmelidir. Bu özellik **true** olarak ayarlandığında, Aspose.Cells formülü basit metin olarak değil, formül olarak işleyecektir ve Aspose.Cells formül hesaplama motoru onları normal olarak işleyecektir.

{{% /alert %}} 

Aşağıdaki kod, formülleri içeren CSV dosyasını nasıl yükleyebileceğinizi ve içe aktarabileceğinizi gösterir. Herhangi bir CSV dosyasını kullanabilirsiniz. İllüstrasyon amacıyla, bu veriyi içeren [basit csv dosyasını](5115034.csv) kullanıyoruz.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



Kod önce CSV dosyasını yükler, ardından D4 hücresine yeniden içe aktarır. Son olarak, workbook nesnesini XSLX formatında kaydeder. [Çıktı XLSX dosyası](5115052.xlsx) şöyle görünüyor. C3 ve F4 hücrelerinin formülü ve sonucu 800 olduğunu görebilirsiniz.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

