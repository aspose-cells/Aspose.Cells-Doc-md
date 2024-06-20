---
title: Öppna filer i PHP
type: docs
weight: 10
url: /sv/java/opening-files-in-php/
---

## **Aspose.Cells - Enkla sätt att öppna Excel-filer**
### **Öppning genom sökväg**
Öppna en Microsoft Excel-fil genom att referera till filens sökväg

**PHP-kod**

{{< highlight ruby >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Öppning genom Ström**
Ibland är Excel-filen som du vill öppna lagrad som en ström. I så fall använd en överlagrad version av **Open** metoden som tar **Stream** objektet som innehåller Excel-filen för att öppna filen.

**PHP-kod**

{{< highlight ruby >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Öppnar filer (Aspose.Cells)** från någon av de nedan nämnda sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
