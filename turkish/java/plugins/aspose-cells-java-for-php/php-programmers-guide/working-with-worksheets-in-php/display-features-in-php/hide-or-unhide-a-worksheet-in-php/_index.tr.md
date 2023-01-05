---
title: Php'de Bir Çalışma Sayfasını Gizle veya Göster
type: docs
weight: 50
url: /tr/java/hide-or-unhide-a-worksheet-in-php/
---
## **Aspose.Cells - Bir Çalışma Sayfasını Gizle veya Göster**
### **Bir Çalışma Sayfasını Gizleme**
 Aspose.Cells Java for PHP'i kullanarak çalışma sayfasını gizlemek için arayın**çalışma sayfasını gizle** modül.

**PHP Kodu**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the first worksheet of the Excel file

$worksheet->setVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Bir Çalışma Sayfasını Gizle veya Göster (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
