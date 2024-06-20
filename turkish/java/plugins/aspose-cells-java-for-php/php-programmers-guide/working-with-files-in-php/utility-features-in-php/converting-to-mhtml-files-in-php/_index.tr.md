---
title: PHP de MHTML Dosyalarına Dönüştürme
type: docs
weight: 40
url: /tr/java/converting-to-mhtml-files-in-php/
---

## **Aspose.Cells - MHTML Dosyalarına Dönüştürme**
Aspose.Cells for Java kullanarak PHP'de Çalışma Sayfasını MHTML dosyasına dönüştürmek için, sadece Converter modülünün worksheet_to_mhtml() yöntemini çağırın.

PHP Kodu

{{< highlight php >}}

 $sveFormat = new SaveFormat();

//Specify the file path

$filePath = $dataDir . "Book1.xlsx";

//Specify the HTML saving options

$sv = new HtmlSaveOptions($sveFormat->M_HTML);

//Instantiate a workbook and open the template XLSX file

$wb = new Workbook($filePath);

//Save the MHT file

$wb->save($filePath . ".out.mht", $sv);

{{< /highlight >}}
## **Çalışan Kodu İndir**
**Aspose.Cells ile MHTML Dosyalarına Dönüştürme**'yi aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
