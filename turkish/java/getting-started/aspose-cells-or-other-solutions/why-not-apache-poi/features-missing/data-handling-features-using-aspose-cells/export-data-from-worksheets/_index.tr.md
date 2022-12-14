---
title: Çalışma Sayfalarından Verileri Dışa Aktarma
type: docs
weight: 40
url: /tr/java/export-data-from-worksheets/
---
## **Aspose.Cells - Çalışma Sayfalarından Verileri Dışa Aktar**
Aspose.Cells, kullanıcılarının yalnızca harici veri kaynaklarından çalışma sayfalarına veri aktarmalarına izin vermekle kalmaz, aynı zamanda çalışma sayfası verilerini bir diziye vermelerine de izin verir.

**Java**

{{< highlight "java" >}}

 //Açılacak Excel dosyasını içeren dosya akışı oluşturuluyor

FileInputStream fstream = yeni FileInputStream(dataDir + "workbook.xls");

//Çalışma Kitabı nesnesinin somutlaştırılması

Çalışma kitabı çalışma kitabı = yeni Çalışma Kitabı(fstream);

//Excel dosyasındaki ilk çalışma sayfasına erişim

Çalışma sayfası çalışma sayfası = workbook.getWorksheets().get(0);

//1. hücreden başlayarak 7 satır ve 2 sütun içeriğini Array'e aktarıyoruz.

Nesne dataTable [][]= worksheet.getCells().exportArray(4,0,7,8);

 için (int ben = 0 ; ben< dataTable.length ; i++)

{

	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));

}

//Closing the file stream to free all resources

fstream.close();

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/ExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Çalışma Sayfalarından Verileri Dışa Aktarma](/java/exporting-data-from-worksheets).

{{% /alert %}}
