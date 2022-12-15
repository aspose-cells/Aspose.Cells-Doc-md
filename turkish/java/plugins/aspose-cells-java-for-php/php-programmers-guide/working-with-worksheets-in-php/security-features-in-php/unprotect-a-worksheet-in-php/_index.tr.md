---
title: Php'de bir Çalışma Sayfasının korumasını kaldırın
type: docs
weight: 20
url: /tr/java/unprotect-a-worksheet-in-php/
---
## **Aspose.Cells - Bir Çalışma Sayfasının korumasını kaldırın**
 Çalışma sayfasını kullanarak korumak için**Aspose.Cells Java for PHP** , aramak**unprotect_worksheet** yöntemi**koruma** modül.

**PHP Kodu**

{{< highlight "php" >}}

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
İndirmek**Bir Çalışma Sayfasının korumasını kaldırın (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
