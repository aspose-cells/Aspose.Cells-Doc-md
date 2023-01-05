---
title: Общедоступный API Изменения в Aspose.Cells 8.7.1
type: docs
weight: 240
url: /ru/net/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.7.0 до 8.7.1, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Добавлено свойство LookInType.OriginalValues**
 Aspose.Cells API уже поддерживают[Поиск или поиск данных](/cells/ru/net/find-or-search-data/)функция для электронных таблиц, чтобы найти определенную часть содержимого в значении ячейки и формуле. Однако в этой функции отсутствовал аспект форматирования, применяемого к ячейке, который может изменить внешний вид, а также значение содержимого, следовательно, сделать текст недоступным для поиска с использованием исходного значения. В этом выпуске API Aspose.Cells другая константа с именем LookInType.OriginalValues была открыта для общественности API, что позволяет преодолеть описанную выше ситуацию.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Поиск данных с использованием исходных значений](/cells/ru/net/search-data-using-original-values/)

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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


### **Добавлено событие OnBeforeColumnFilter для GridWeb.**
Aspose.Cells.GridWeb for .NET 8.7.1 предоставляет событие OnBeforeColumnFilter, которое служит обратным вызовом для механизма фильтрации, выполняемого через пользовательский интерфейс GridWeb. Как следует из названия, событие запускается до применения фильтрации столбцов и может использоваться для получения информации о фильтрации, такой как индекс столбца и значение, к которому должен применяться фильтр.

Простой сценарий использования выглядит следующим образом.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Не забудьте зарегистрировать событие в элементе управления GridWeb.<acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
