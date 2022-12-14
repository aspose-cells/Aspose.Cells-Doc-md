---
title: Öppna filer i PHP
type: docs
weight: 10
url: /sv/java/opening-files-in-php/
---
## **Aspose.Cells - Enkla sätt att öppna Excel-filer**
### **Öppning genom vägen**
Öppna helt enkelt en Microsoft Excel-fil genom att referera till filens sökväg

**PHP-kod**

{{< highlight "ruby" >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Öppnas genom Stream**
Ibland lagras Excel-filen som du vill öppna som en ström. Använd i så fall en överbelastad version av Open-metoden som tar Stream-objektet som innehåller Excel-filen för att öppna filen.

**PHP-kod**

{{< highlight "ruby" >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Öppna filer (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
