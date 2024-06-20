---
title: PHP de Bir Çalışsayıyı Korumayı Kaldırma
type: docs
weight: 20
url: /tr/java/unprotect-a-worksheet-in-php/
---

## **Aspose.Cells - Bir Çalışma Sayfasının Korumasını Kaldırma**
**Aspose.Cells Java for PHP** kullanarak çalışsayıyı korumak için **protection** modülünün **unprotect_worksheet** yöntemini çağırın.

PHP Kodu

{{< highlight php >}}

 $filesFormatType = new FileFormatType();

//Instantiating a Workbook object

$workbook = new Workbook($dataDir . "book1.xls");

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//Unprotecting the worksheet with a password

$worksheet->unprotect("aspose");

// Save the excel file.

$workbook->save($dataDir . "output.xls", $filesFormatType->EXCEL_97_TO_2003); 

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Bir Çalışma Sayfasını Korumasız Bırakma (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
