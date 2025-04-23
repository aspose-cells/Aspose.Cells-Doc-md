---
title: Изменения в общедоступном API в Aspose.Cells 8.7.1
type: docs
weight: 250
url: /ru/java/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.7.0 до 8.7.1, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство LookInType.ORIGINAL_VALUES**
API Aspose.Cells уже поддерживал функцию [Поиск данных](/cells/ru/java/find-or-search-data/) для электронных таблиц, позволяющую найти определенный элемент содержимого в значении ячейки и формуле. Однако эта функция не учитывала форматирование, примененное к ячейке, которое может изменить внешний вид и значение содержимого, что делает текст непоискимым с использованием исходного значения. В этом релизе API Aspose.Cells была добавлена еще одна константа под названием LookInType.ORIGINAL_VALUES, позволяющая преодолеть описанную ситуацию. 

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в подробной статье [Поиск данных с использованием исходных значений](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="java" >}}
