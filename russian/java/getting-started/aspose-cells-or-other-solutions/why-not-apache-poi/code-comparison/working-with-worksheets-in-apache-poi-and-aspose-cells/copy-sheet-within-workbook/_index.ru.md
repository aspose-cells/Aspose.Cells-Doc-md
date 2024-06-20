---
title: Копирование листа в рабочей книге
type: docs
weight: 40
url: /ru/java/copy-sheet-within-workbook/
---

## **Microsoft Excel - Перемещение или копирование листов в рабочей книге**
Вот какие шаги включены в копирование и перемещение листов внутри или между рабочими книгами.

1. Для перемещения или копирования листов внутри или между рабочими книгами откройте книгу, которая получит листы.
1. Переключитесь на рабочую книгу, которая содержит листы, которые вы хотите переместить или скопировать, а затем выберите листы.
1. На меню **Правка** щелкните **Переместить или скопировать лист**.
1. В поле **В книгу** щелкните рабочую книгу, которая получит листы.
1. Чтобы переместить или скопировать выбранные листы в новую рабочую книгу, щелкните **новая книга**.
1. В поле **Перед листом** щелкните лист, перед которым вы хотите вставить перемещенные или скопированные листы.
1. Чтобы скопировать листы вместо их перемещения, выберите флажок **Создать копию**.
## **Aspose.Cells - Копировать лист в рабочей книге**
{{% alert color="primary" %}} 

Aspose.Cells предоставляет перегруженный метод, WorksheetCollection.addCopy(), который используется для добавления листа в коллекцию и копирования данных с существующего листа. Одна из версий метода принимает индекс исходного листа в качестве параметра. Другая версия принимает имя исходного листа.

В следующем примере показано, как скопировать существующий лист в рамках рабочей книги.

{{% /alert %}} 

Копирование листов с помощью Aspose.Cells

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Копирование листа в рамках книги**
{{% alert color="primary" %}} 

Workbook.cloneSheet() используется для копирования листов в рамках книги.

{{% /alert %}} 

Копирование листов с помощью Apache POI SS

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

Для получения более подробной информации посетите [Копирование и перемещение листов](/cells/ru/java/copying-and-moving-worksheets).

{{% /alert %}}
