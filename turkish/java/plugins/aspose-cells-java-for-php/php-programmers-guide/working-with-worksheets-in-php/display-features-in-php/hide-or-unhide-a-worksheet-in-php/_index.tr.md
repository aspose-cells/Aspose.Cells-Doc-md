---
title: Php de Çalışma Sayfasını Gizle veya Göster
type: docs
weight: 50
url: /tr/java/hide-or-unhide-a-worksheet-in-php/
---

## **Aspose.Cells - Bir Çalışsayı Gizle veya Göster**
### **Bir Çalışsayıyı Gizleme**
Aspose.Cells Java for PHP kullanarak çalışma sayfasını gizlemek için **hideunhideworksheet** modülünü çağırın.

PHP Kodu

{{< highlight php >}}

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
Herhangi bir sosyal kodlama sitesinden **Aspose.Cells** ile Bir Çalışsayıyı Gizle veya Göster'i indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
