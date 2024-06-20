---
title: Открытие файлов в PHP
type: docs
weight: 10
url: /ru/java/opening-files-in-php/
---

## **Aspose.Cells - Простые Способы Открытия Файлов Excel**
### **Открытие через путь**
Просто откройте файл Microsoft Excel, указав путь к файлу

**PHP-код**

{{< highlight ruby >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Открытие через Поток**
Иногда файл Excel, который вы хотите открыть, хранится как поток. В этом случае используйте перегруженную версию метода Открыть, который принимает объект Поток, содержащий файл Excel, чтобы открыть файл.

**PHP-код**

{{< highlight ruby >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Скачать работающий код**
Загрузите ** Открытие файлов (Aspose.Cells) ** из любого из перечисленных ниже сайтов социального кодинга:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
