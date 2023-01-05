---
title: Установите заголовки печати в xlsx4j
type: docs
weight: 40
url: /ru/java/set-print-titles-in-xlsx4j/
---
## **Aspose.Cells - Установить заголовки для печати**
Aspose.Cells позволяет указать, что заголовки строк и столбцов будут повторяться на всех страницах печатного листа. Для этого используйте[Настройка страницы](/java/PageSetup)свойства class'setPrintTitleColumns и setPrintTitleRows.

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строк или столбцов. Например, строки определяются как $1:$2, а столбцы — как $A:$B.

**Java**

{{< highlight "java" >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Настройка параметров печати](/cells/ru/java/page-setup-features/#setting-print-options).

{{% /alert %}}
