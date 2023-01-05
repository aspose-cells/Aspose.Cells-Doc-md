---
title: Открытие файлов в PHP
type: docs
weight: 10
url: /ru/java/opening-files-in-php/
---
## **Aspose.Cells - Простые способы открытия файлов Excel**
### **Открытие через Путь**
Просто откройте файл Excel Microsoft, указав путь к файлу.

**PHP-код**

{{< highlight "ruby" >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Открытие через поток**
Иногда файл Excel, который вы хотите открыть, хранится в виде потока. В этом случае используйте перегруженную версию метода Open, который принимает объект Stream, содержащий файл Excel, для открытия файла.

**PHP-код**

{{< highlight "ruby" >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Открытие файлов (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
