---
title: PHP'de Dosyaları Kaydetme
type: docs
weight: 20
url: /tr/java/saving-files-in-php/
---
## **Aspose.Cells - Dosyaları Kaydetme**
### **Dosyayı bir konuma kaydetme**
 Geliştiricilerin dosyalarını kullanarak kaydetmeleri gerekiyorsa**PHP için Aspose.Cells Java** bir depolama konumuna daha sonra dosya adını (tam depolama yolu ile birlikte) ve istenen dosya formatını (kullanarak) belirtebilirler.**Dosya Biçimi Türü**numaralandırma) çağrılırken**kaydetmek**yöntemi**Çalışma kitabı**nesne.

**PHP Kodu**

{{< highlight "php" >}}

 $fileFormatType = new FileFormatType();

//Creating an Workbook object with an Excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Save in default (Excel2003) format

$workbook->save($dataDir . "book.default.out.xls");

//Save in Excel2003 format

$workbook->save($dataDir . "book.out.xls",$fileFormatType->EXCEL_97_TO_2003);

//Save in Excel2007 xlsx format

$workbook->save($dataDir . "book.out.xlsx", $fileFormatType->XLSX);

//Save in SpreadsheetML format

$workbook->save($dataDir . "book.out.xml", $fileFormatType->EXCEL_2003_XML);

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Dosyaları Kaydetme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
