---
title: xlsx4j deki Her Bir Çalışma Sayfasını Farklı Bir PDF olarak Kaydet
type: docs
weight: 50
url: /tr/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---

## **Aspose.Cells - Her Bir Çalışma Sayfasını Farklı PDF'ye Kaydetme**
Aspose.Cells, görüntü, grafik vb. içeren XLS dosyalarını PDF belgelerine dönüştürmeyi destekler. Aspose.Cells for Java, bir elektronik tabloyu Pdf belgesine dönüştürmek için bağımsız olarak çalışabilir ve artık dönüştürme için Aspose.Pdf for Java'yı kullanmanıza gerek yok. Ayrıca dönüşümün herhangi bir geçici dosya oluşturmaya / kullanmaya gerek duymadığını da unutmayın, çünkü tüm işlem bellekte yapılabilir.

**Java**

{{< highlight java >}}

 //Get the Excel file path

String filePath = dataDir + "workbook.xlsx";

//Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook(filePath);

//Get the count of the worksheets in the workbook

int sheetCount = workbook.getWorksheets().getCount();

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.getWorksheets().getCount(); i++)

{

     workbook.getWorksheets().get(i).setVisible(false);

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.getWorksheets().getCount(); j++)

{

    Worksheet ws = workbook.getWorksheets().get(j);

    workbook.save(dataPath + ws.getName() + ".pdf");

    if (j < workbook.getWorksheets().getCount() - 1)

    {

       workbook.getWorksheets().get(j + 1).setVisible(true);

       workbook.getWorksheets().get(j).setVisible(false);

    }

}

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Her Bir Çalışma Sayfasını Farklı Bir PDF Dosyasına Kaydet](/cells/tr/java/save-each-worksheet-to-a-different-pdf-file)'i ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
