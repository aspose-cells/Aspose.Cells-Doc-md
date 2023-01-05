---
title: Копировать лист в рабочей книге
type: docs
weight: 40
url: /ru/java/copy-sheet-within-workbook/
---
## **Microsoft Excel — перемещение или копирование листов в книге**
Ниже приведены шаги, необходимые для копирования и перемещения рабочих листов внутри или между книгами.

1. Чтобы переместить или скопировать листы внутри или между книгами, откройте книгу, в которую будут помещены листы.
1. Переключитесь на книгу, содержащую листы, которые вы хотите переместить или скопировать, а затем выберите листы.
1.  На**Редактировать** меню, нажмите**Переместить или скопировать лист**.
1. В поле В книгу щелкните книгу, чтобы получить листы.
1.  Чтобы переместить или скопировать выбранные листы в новую книгу, щелкните**новая книга**.
1.  в**Перед листом** щелкните лист, перед которым вы хотите вставить перемещенные или скопированные листы.
1.  Чтобы копировать листы, а не перемещать их, выберите значок**Создать копию** флажок.
## **Aspose.Cells - Копировать лист в рабочей книге**
{{% alert color="primary" %}} 

Aspose.Cells предоставляет перегруженный метод WorksheetCollection.addCopy(), который используется для добавления листа в коллекцию и копирования данных из существующего листа. Одна версия метода принимает в качестве параметра индекс исходного листа. Другая версия берет имя исходного рабочего листа.

В следующем примере показано, как скопировать существующий рабочий лист в рабочую книгу.

{{% /alert %}} 

Скопируйте листы, используя Aspose.Cells

**Java**

{{< highlight "java" >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS — копирование листа в рабочей книге**
{{% alert color="primary" %}} 

Workbook.cloneSheet() используется для копирования листов с рабочей книгой.

{{% /alert %}} 

Скопируйте листы с помощью Apache POI SS

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Копирование и перемещение рабочих листов](/cells/ru/java/copying-and-moving-worksheets).

{{% /alert %}}
