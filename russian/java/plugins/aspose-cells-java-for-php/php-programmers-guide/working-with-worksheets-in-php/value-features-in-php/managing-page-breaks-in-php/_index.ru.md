---
title: Управление разрывами страниц в Php
type: docs
weight: 20
url: /ru/java/managing-page-breaks-in-php/
---
## **Aspose.Cells - Управление разрывами страниц**
### **Добавление разрывов страниц**
 Чтобы добавить разрывы страниц с помощью**Aspose.Cells Java для PHP** , вызов**add_page_breaks** метод**разрывы страниц** модуль. Ниже вы можете увидеть пример кода.

**PHP-код**

{{< highlight "php" >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **Удаление всех разрывов страниц**
 Чтобы очистить все разрывы страниц с помощью**Aspose.Cells Java для PHP** , вызов**clear_all_page_breaks** метод**разрывы страниц** модуль. Ниже вы можете увидеть пример кода.

**PHP-код**

{{< highlight "php" >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Удаление определенного разрыва страницы**
 Чтобы удалить определенный разрыв страницы, используя**Aspose.Cells Java для PHP** , вызов**remove_page_break** метод**разрывы страниц** модуль. Ниже вы можете увидеть пример кода.

**PHP-код**

{{< highlight "php" >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Управление разрывами страниц (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
