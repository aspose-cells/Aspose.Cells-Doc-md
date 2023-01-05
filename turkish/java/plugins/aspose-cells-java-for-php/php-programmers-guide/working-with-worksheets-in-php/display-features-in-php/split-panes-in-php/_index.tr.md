---
title: Php'de Bölme Bölmeleri
type: docs
weight: 70
url: /tr/java/split-panes-in-php/
---
## **Aspose.Cells - Bölmeli Bölmeler**
 Kullanarak Bölmeleri Bölmek için**Aspose.Cells Java for PHP** , sadece çağırmak**Bölünmüş Paneller** modül.

**PHP Kodu**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

//Instantiate a new workbook

//Open a template file

$book = new Workbook($dataDir . "book.xls");

//Set the active cell

$book->getWorksheets()->get(0)->setActiveCell("A20");

//Split the worksheet window

$book->getWorksheets()->get(0)->split();

//Save the excel file

$book->save($dataDir . "book.out.xls", $saveFormat->EXCEL_97_TO_2003);

{{< /highlight >}}
## **Çalışan Kodu İndir**
İndirmek**Bölünmüş Bölmeler (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
