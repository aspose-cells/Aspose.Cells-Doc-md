---
title: PHP de Izgaraları Göster veya Gizle
type: docs
weight: 10
url: /tr/java/display-or-hide-gridlines-in-php/
---

## **Aspose.Cells - ızgaraları Göster veya Gizle**
### **Izgaraları Gizleme**
Aspose.Cells Java for PHP kullanarak çalışma sayfasını gizlemek için **displayhidegridlines** modülünü çağırın.

PHP Kodu

{{< highlight php >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

//Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the grid lines of the first worksheet of the Excel file

$worksheet->setGridlinesVisible(false);

//Saving the modified Excel file in default (that is Excel 2000) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Çalışan Kodu İndir**
**Aspose.Cells** ile **Izgaraları Göster veya Gizle**'yı aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
