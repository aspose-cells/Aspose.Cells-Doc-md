---
title: PHP de Çalışsayıları Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/java/copying-and-moving-worksheets-in-php/
---

## **Aspose.Cells - Çalışma Sayfalarını Kopyalama ve Taşıma**
### **Çalışma Kitabı İçinde Çalışma Sayfalarını Kopyalama**
**PHP** için **Aspose.Cells for Java** kullanarak çalışsayıyı kopyalamak için **copyworksheets** modülünün **copy_worksheet** yöntemini çağırın. Aşağıda kod örneğini görebilirsiniz.

PHP Kodu

{{< highlight php >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **Çalışma Kitabı İçinde Çalışma Sayfalarını Taşıma**
**PHP** için **Aspose.Cells for Java** kullanarak çalışsayıyı taşımak için **copyworksheets** modülünün **move_worksheet** yöntemini çağırın. Aşağıda kod örneğini görebilirsiniz.

PHP Kodu

{{< highlight php >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıdaki sosyal kodlama sitelerinden herhangi birinden **Kopyalama ve Taşıma Çalışma Sayfalarını (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
