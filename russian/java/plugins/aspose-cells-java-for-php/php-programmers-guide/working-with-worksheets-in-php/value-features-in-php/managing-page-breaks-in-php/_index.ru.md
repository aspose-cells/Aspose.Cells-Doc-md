---
title: Управление разрывами страниц в Php
type: docs
weight: 20
url: /ru/java/managing-page-breaks-in-php/
---

## **Aspose.Cells - Управление разрывами страниц**
### **Добавление разрывов страниц**
Чтобы добавить разрывы страниц с использованием **Aspose.Cells Java для PHP**, вызовите метод **add_page_breaks** модуля **pagebreaks**. Ниже приведен пример кода.

**PHP-код**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **Очистка всех разрывов страниц**
Чтобы очистить все разрывы страниц с использованием **Aspose.Cells Java для PHP**, вызовите метод **clear_all_page_breaks** модуля **pagebreaks**. Ниже приведен пример кода.

**PHP-код**

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Удаление конкретного разрыва страницы**
Чтобы удалить конкретный разрыв страницы с использованием **Aspose.Cells Java для PHP**, вызовите метод **remove_page_break** модуля **pagebreaks**. Ниже приведен пример кода.

**PHP-код**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **Скачать работающий код**
Загрузите **Управление разрывами страниц (Aspose.Cells)** с любого из указанных ниже сайтов социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
