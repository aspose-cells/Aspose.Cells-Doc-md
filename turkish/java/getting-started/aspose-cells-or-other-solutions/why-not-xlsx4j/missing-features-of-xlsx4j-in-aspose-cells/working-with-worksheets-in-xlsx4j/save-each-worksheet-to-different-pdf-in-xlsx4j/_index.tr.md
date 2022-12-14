---
title: Her Çalışma Sayfasını xlsx4j'de Farklı PDF'ye Kaydet
type: docs
weight: 50
url: /tr/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---
## **Aspose.Cells - Her Çalışma Sayfasını Farklı PDF'ye Kaydet**
Aspose.Cells, XLS dosyalarının (resimler, çizelgeler vb. içeren) PDF belgelerine dönüştürülmesini destekler. Aspose.Cells for Java bir elektronik tabloyu pdf belgesine dönüştürmek için bağımsız olarak çalışabilir ve artık dönüştürme için Aspose.Pdf for Java kullanmanıza gerek yoktur. Tüm işlem bellekte yapılabildiğinden, dönüştürme herhangi bir geçici dosya (lar) oluşturmayı / kullanmayı gerektirmez.

**Java**

{{< highlight "java" >}}

//Excel dosya yolunu al

String filePath = dataDir + "workbook.xlsx";

//Yeni bir çalışma kitabı oluşturun ve Excel'i açın

// Bulunduğu yerden dosya

Çalışma kitabı çalışma kitabı = yeni Çalışma Kitabı(filePath);

//Çalışma kitabındaki çalışma sayfalarının sayısını al

int SheetCount = workbook.getWorksheets().getCount();

//İlk çalışma sayfası dışında tüm sayfaları görünmez yap

 için (int ben = 1; ben< workbook.getWorksheets().getCount(); i++)

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
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Her Çalışma Sayfasını Farklı Bir PDF Dosyasına Kaydet](/cells/tr/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
