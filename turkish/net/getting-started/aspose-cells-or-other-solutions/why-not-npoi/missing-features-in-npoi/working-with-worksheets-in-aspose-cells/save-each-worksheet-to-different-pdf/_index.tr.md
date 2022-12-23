---
title: Her Çalışma Sayfasını Farklı PDF'e Kaydet
type: docs
weight: 10
url: /tr/net/save-each-worksheet-to-different-pdf/
---
## **Aspose.Cells - Her Çalışma Sayfasını Farklı PDF'e Kaydet**
Aspose.Cells, XLS dosyasının (resim, çizelge vb. içeren) PDF belgesine dönüştürülmesini destekler. Aspose.Cells for .NET bir elektronik tabloyu pdf belgesine dönüştürmek için bağımsız olarak çalışabilir ve artık dönüştürme için Aspose.Pdf for .NET kullanmanıza gerek yoktur. Tüm işlem bellekte yapılabildiğinden, dönüştürme herhangi bir geçici dosya (lar) oluşturmayı / kullanmayı gerektirmez.

**C#**

{{< highlight "cs" >}}

 //Yeni bir çalışma kitabı oluşturun ve Excel'i açın

// Bulunduğu yerden dosya

Çalışma kitabı çalışma kitabı = new Workbook("../../data/test.xlsx");

//Çalışma kitabındaki çalışma sayfalarının sayısını al

int SheetCount = workbook.Worksheets.Count;

//İlk çalışma sayfası dışında tüm sayfaları görünmez yap

 için (int ben = 1; ben< workbook.Worksheets.Count; i++)

{

    workbook.Worksheets[i].IsVisible = false;

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.Worksheets.Count; j++)

{

    Worksheet ws = workbook.Worksheets[j];

    workbook.Save(ws.Name + ".pdf");

    if (j < workbook.Worksheets.Count - 1)

    {

        workbook.Worksheets[j + 1].IsVisible = true;

        workbook.Worksheets[j].IsVisible =false;

    }

}

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Her Çalışma Sayfasını Farklı PDF'e Kaydet** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Her Çalışma Sayfasını Farklı Bir PDF Dosyasına Kaydet](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
