---
title: Php de Bölünmüş Paneller
type: docs
weight: 70
url: /tr/java/split-panes-in-php/
---

## **Aspose.Cells - Bölünmüş Panolar**
**Aspose.Cells Java for PHP** kullanarak Bölünmüş Panelleri ayarlamak için **SplitPanes** modülünü çağırın.

PHP Kodu

{{< highlight php >}}

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
İndirin **Bölünmüş Panolar (Aspose.Cells)** any of the aşağıda bahsedilen sosyal kodlama sitelerinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
