---
title: Her bir Çalışsayfayı Farklı Bir PDF Dosyasına Kaydet
type: docs
weight: 130
url: /tr/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

Aspose.Cells, resimler, grafikler vb. içeren XLS dosyalarını PDF belgelerine dönüştürmeyi destekler. Aspose.Cells for .NET, bir elektronik tabloyu PDF'ye dönüştürmek için Aspose.PDF for .NET'i kullanmanızı gerektirmez. Bu dönüşüm, tüm sürecin bellekte yapılabilmesi nedeniyle herhangi bir geçici dosya oluşturma veya kullanma gerektirmez.

{{% /alert %}} 
## **Her Çalışsayarı Farklı Bir PDF Dosyasına Kaydet**
Şablon Excel dosyanızdaki her bir çalışsayfayı farklı PDF dosyaları oluşturmak için bu işlemi kolayca gerçekleştirebilirsiniz. PDF'ye dönüştürme işlemi sırasında bir çalışsayfa indeksini [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) seçeneğine ayarlayarak bunu kolayca yapabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
