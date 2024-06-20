---
title: PHP de Dosya Kaydetme
type: docs
weight: 20
url: /tr/java/saving-files-in-php/
---

## **Aspose.Cells - Dosyaları Kaydetme**
### **Dosyayı belirli bir konuma kaydetme**
Geliştiricilerin **Aspose.Cells Java for PHP** kullanarak dosyalarını belirli bir depolama konumuna kaydetmeleri gerekiyorsa, **workbook** nesnesinin **save** yöntemini çağırırken dosya adını (tam depolama yolunu kullanarak) ve istenen dosya biçimini (**FileFormatType** numaralandırmasını kullanarak) belirtebilirler.

PHP Kodu

{{< highlight php >}}

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
Herhangi bir aşağıda belirtilen sosyal kodlama sitesinden **Dosyaları Kaydetme (Aspose.Cells)**'ı indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
