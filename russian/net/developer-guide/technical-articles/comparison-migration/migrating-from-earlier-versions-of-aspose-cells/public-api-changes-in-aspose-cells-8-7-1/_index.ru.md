---
title: Изменения в общедоступном API в Aspose.Cells 8.7.1
type: docs
weight: 240
url: /ru/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.7.0 до 8.7.1, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство LookInType.OriginalValues**
API Aspose.Cells уже поддерживают [поиск данных](/cells/ru/net/find-or-search-data/) в электронных таблицах для поиска определенного содержимого в значении ячейки и формуле. Однако этой функции не хватало аспекта форматирования, примененного к ячейке, которое может изменить внешний вид и значение содержимого и, следовательно, сделать текст непоисковым с использованием исходного значения. В этом выпуске API Aspose.Cells для общественности была предоставлена еще одна константа под названием LookInType.OriginalValues, которая позволяет преодолеть обсуждаемую ситуацию.

{{% alert color="primary" %}} 

Для получения дополнительной информации о этой функции, пожалуйста, ознакомьтесь с подробной статьей по [поиску данных с использованием исходных значений](/cells/ru/net/search-data-using-original-values/)

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 in cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formatted as ---

cell.Formula = "=Sum(A1:A2)";

//Calculate the workbook

workbook.CalculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.LookInType = LookInType.OriginalValues;

options.LookAtType = LookAtType.EntireContent;

Cell foundCell = null;

object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.Cells.Find(obj, foundCell, options);

//Print the found cell

Console.WriteLine(foundCell);

{{< /highlight >}}


### **Добавлено событие OnBeforeColumnFilter для GridWeb**
Aspose.Cells.GridWeb для .NET 8.7.1 представил событие OnBeforeColumnFilter, которое служит обратным вызовом для механизма фильтрации, выполняемой через пользовательский интерфейс GridWeb. Как следует из названия, событие срабатывает перед применением фильтрации столбца и может использоваться для получения информации о фильтрации, такой как индекс столбца и значение, на котором должен быть применен фильтр.

Простой сценарий использования выглядит следующим образом.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
