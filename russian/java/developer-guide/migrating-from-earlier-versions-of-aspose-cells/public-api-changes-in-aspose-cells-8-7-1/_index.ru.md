---
title: Общедоступный API Изменения в Aspose.Cells 8.7.1
type: docs
weight: 250
url: /ru/java/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.7.0 до 8.7.1, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Добавлено свойство LookInType.ORIGINAL_VALUES.**
 Aspose.Cells API уже поддерживают[Поиск или поиск данных](/cells/ru/java/find-or-search-data/)функция для электронных таблиц, чтобы найти определенную часть содержимого в значении ячейки и формуле. Однако в этой функции отсутствовал аспект форматирования, применяемого к ячейке, который может изменить внешний вид, а также значение содержимого, следовательно, сделать текст недоступным для поиска с использованием исходного значения. В этом выпуске API Aspose.Cells другая константа с именем LookInType.ORIGINAL_VALUES стала общедоступной API, что позволяет преодолеть описанную выше ситуацию.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Поиск данных с использованием исходных значений](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add 10 in cell A1 and A2

worksheet.getCells().get("A1").putValue(10);

worksheet.getCells().get("A2").putValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.getCells().get("D4");

Style style = cell.getStyle();

style.setCustom("---");

cell.setStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formated as ---

cell.setFormula("=Sum(A1:A2)");

//Calculate the workbook

workbook.calculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.setLookInType(LookInType.ORIGINAL_VALUES);

options.setLookAtType(LookAtType.ENTIRE_CONTENT);

Cell foundCell = null;

Object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.getCells().find(obj, foundCell, options);

//Print the found cell

System.out.println(foundCell);

{{< /highlight >}}
