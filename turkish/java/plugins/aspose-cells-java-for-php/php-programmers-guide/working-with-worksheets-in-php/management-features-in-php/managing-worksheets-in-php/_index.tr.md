---
title: Php de Çalışma Sayfalarını Yönetme
type: docs
weight: 10
url: /tr/java/managing-worksheets-in-php/
---

## **Aspose.Cells - Çalışma Sayfalarını Yönetme**
### **Yeni bir Excel Dosyasına Çalışsayfalar Ekleme**
Yeni bir Excel dosyasına **Aspose.Cells Java for PHP** kullanarak Çalışsayfa eklemek için, **ManagingWorksheets** modülünün **add_worksheet** yöntemini çağırın.

PHP Kodu

{{< highlight php >}}

 //Instantiating a Workbook object

$workbook = new Workbook();

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$sheetIndex = $worksheets->add();

$worksheet = $worksheets->get($sheetIndex);

//Setting the name of the newly added worksheet

$worksheet->setName("My Worksheet");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
### **Sayfa Adını Kullanarak Çalışsayfaları Kaldırma**
**Aspose.Cells Java for PHP** kullanarak sayfa adını kullanarak çalışma sayfasını kaldırmak için **MangingWorksheets** modülünün **remove_worksheet_by_name** yöntemini çağırın.

PHP Kodu

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream = new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet name

$workbook->getWorksheets()->removeAt("Sheet1");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
### **Sayfa Dizinini Kullanarak Çalışma Sayfalarını Kaldırma**
**Aspose.Cells Java for PHP** kullanarak sayfa indeksini kullanarak çalışma sayfasını kaldırmak için **MangingWorksheets** modülünün **remove_worksheet_by_index** yöntemini çağırın.

PHP Kodu

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream=new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet index

$workbook->getWorksheets()->removeAt(0);

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Yönetim Çalışma Sayfalarını (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
