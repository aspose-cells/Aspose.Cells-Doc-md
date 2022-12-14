---
title: Php'de Kılavuz Çizgilerini Görüntüleme veya Gizleme
type: docs
weight: 10
url: /tr/java/display-or-hide-gridlines-in-php/
---
## **Aspose.Cells - Kılavuz Çizgilerini Görüntüle veya Gizle**
### **Kılavuz Çizgilerini Gizleme**
 kullanarak çalışma sayfasını gizlemek için**PHP için Aspose.Cells Java** , aramak**displayhidegridlines** modül.

**PHP Kodu**

{{< highlight "php" >}}

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
İndirmek**Kılavuz Çizgilerini Görüntüle veya Gizle (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
