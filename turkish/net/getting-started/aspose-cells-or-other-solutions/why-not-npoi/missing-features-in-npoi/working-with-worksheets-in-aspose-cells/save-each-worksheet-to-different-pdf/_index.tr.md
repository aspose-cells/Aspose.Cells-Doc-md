---
title: Her Bir Çalışma Sayfasını Farklı PDF ye Kaydetme
type: docs
weight: 10
url: /tr/net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - Her Bir Çalışma Sayfasını Farklı PDF'ye Kaydetme**
Aspose.Cells, resimler, grafikler vb. içeren XLS dosyalarını PDF belgelerine dönüştürmeyi destekler. Aspose.Cells for .NET, bir elektronik tabloyu PDF belgesine dönüştürmek için bağımsız olarak çalışabilir ve dönüşüm için artık Aspose.Pdf for .NET'i kullanmanıza gerek yoktur. Dönüşüm, tüm işlem belleğinde yapılabileceği için herhangi bir geçici dosya oluşturma / kullanma gerektirmez.

**C#**

{{< highlight cs >}}

 //Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the count of the worksheets in the workbook

int sheetCount = workbook.Worksheets.Count;

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.Worksheets.Count; i++)

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
Her çalışma sayfasını farklı bir PDF olarak kaydetmeyi indirin herhangi aşağıda belirtilen sosyal kodlama sitelerinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Her Çalışma Sayfasını Farklı Bir PDF Dosyasına Kaydetme](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/) adresini ziyaret edin.

{{% /alert %}}
