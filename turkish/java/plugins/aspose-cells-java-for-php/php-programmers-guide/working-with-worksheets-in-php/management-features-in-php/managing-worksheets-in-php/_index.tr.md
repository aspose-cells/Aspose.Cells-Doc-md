---
title: Php'de Çalışma Sayfalarını Yönetme
type: docs
weight: 10
url: /tr/java/managing-worksheets-in-php/
---
## **Aspose.Cells - Çalışma Sayfalarını Yönetme**
### **Çalışma Sayfalarını Yeni Bir Excel Dosyasına Ekleme**
Çalışma Sayfası'nı kullanarak yeni bir Excel dosyasına eklemek için**PHP için Aspose.Cells Java** , aramanız yeterli**add_worksheet** yöntemi**YönetimÇalışma Sayfaları** modül.

**PHP Kodu**

{{< highlight "php" >}}

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
### **Sayfa Adını Kullanarak Çalışma Sayfalarını Kaldırma**
 Çalışma sayfasını kullanarak sayfa adına göre kaldırmak için**PHP için Aspose.Cells Java** , aramanız yeterli**remove_worksheet_by_name** yöntemi**YönetimÇalışma Sayfaları** modül.

**PHP Kodu**

{{< highlight "php" >}}

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
### **Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma**
 Çalışma sayfasını kullanarak sayfa dizinine göre kaldırmak için**PHP için Aspose.Cells Java** , aramanız yeterli**remove_worksheet_by_index** yöntemi**YönetimÇalışma Sayfaları** modül.

**PHP Kodu**

{{< highlight "php" >}}

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
İndirmek**Çalışma Sayfalarını Yönetme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
