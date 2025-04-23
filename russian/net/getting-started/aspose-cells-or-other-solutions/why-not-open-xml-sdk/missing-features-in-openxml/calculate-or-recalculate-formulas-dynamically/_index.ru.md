---
title: Динамически вычислить или пересчитать формулы
type: docs
weight: 10
url: /ru/net/calculate-or-recalculate-formulas-dynamically/
---

**Формула вычисления** встроена в **Aspose.Cells**. Она может не только пересчитать формулу, импортированную из файла дизайнера, но и поддерживает вычисление результатов формул, добавленных во время выполнения.
## **Добавление формул и вычисление результатов**
Aspose.Cells поддерживает большинство формул или функций, которые являются частью Microsoft Excel. Разработчики могут использовать эти формулы с помощью API или дизайнерских электронных таблиц. Aspose.Excel поддерживает огромный набор математических, строковых, булевых, даты/времени, статистических, баз данных, поиска и ссылочных формул.

Используйте свойство Formula класса Cell, чтобы добавить формулу в ячейку. При применении формулы к ячейке всегда начинайте строку с знака равенства (=), как это делаете при создании формулы в Microsoft Excel. Используйте запятую (,) для разделения параметров функции.

Для вычисления результатов формул вызовите метод CalculateFormula класса Excel, который обрабатывает все формулы, встроенные в файл Excel. Читайте [url: список функций, поддерживаемых методом CalculateFormula](/cells/ru/net/supported-formula-functions/).

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a value to "A1" cell

worksheet.Cells["A1"].PutValue(1);

//Adding a value to "A2" cell

worksheet.Cells["A2"].PutValue(2);

//Adding a value to "A3" cell

worksheet.Cells["A3"].PutValue(3);

//Adding a SUM formula to "A4" cell

worksheet.Cells["A4"].Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

workbook.CalculateFormula();

//Get the calculated value of the cell

string value = worksheet.Cells["A4"].Value.ToString();

//Saving the Excel file

workbook.Save("Adding Formula.xls");

{{< /highlight >}}
## **Вычисление формул один раз**
Когда пользователь вызывает Workbook.CalculateFormula(), чтобы вычислить значения формул внутри шаблона книги Excel, Aspose.Cells создает цепочку расчетов. Это повышает производительность при расчете формул во второй или третий раз и т.д.
Однако, если пользовательский шаблон содержит много разнообразных формул, то при первом вычислении формул может потребляться много времени процессора и памяти.

Aspose.Cells позволяет отключить создание цепочки расчетов, что полезно в ситуациях, когда вы хотите вычислить формулы файла только один раз.

Если вы хотите повысить производительность расчета формул с помощью Aspose.Cells и не хотите создавать цепочку расчетов, установите **FormulaSettings.EnableCalculationChain** в **false**. По умолчанию оно установлено как **true**.

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Adding Formula.xlsx";

//Load the template workbook

Workbook workbook = new Workbook(FileName);

//Print the time before formula calculation

Console.WriteLine(DateTime.Now);

//Set the CreateCalcChain as false

workbook.Settings.FormulaSettings.EnableCalculationChain = false;

//Calculate the workbook formulas

workbook.CalculateFormula();

//Print the time after formula calculation

Console.WriteLine(DateTime.Now);

workbook.Save(FileName);

{{< /highlight >}}
## **Прямое вычисление формулы**
Движок вычисления формул встроен в Aspose.Cells. Кроме того, помимо повторного вычисления формул, импортированных из файла дизайнера, Aspose.Cells также поддерживает вычисление результатов формул непосредственно.
Иногда вам нужно вычислить результаты формул непосредственно, не добавляя их фактически в рабочий лист. Значения ячеек, использованных в формуле, уже существуют в рабочем листе, и все, что вам нужно, это найти результат этих значений на основе какой-то формулы Ms-Excel без добавления формулы в рабочий лист.

Вы можете использовать API движка вычисления формул Aspose.Cells, т. е. **worksheet.Calculate(string formula)**, чтобы вычислить результаты таких формул, не добавляя их фактически в рабочий лист.

{{< highlight csharp >}}

 //Create a workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put 20 in cell A1

Cell cellA1 = worksheet.Cells["A1"];

cellA1.PutValue(20);

//Put 30 in cell A2

Cell cellA2 = worksheet.Cells["A2"];

cellA2.PutValue(30);

//Calculate the Sum of A1 and A2

var results = worksheet.CalculateFormula("=Sum(A1:A2)");

Cell cellA3 = worksheet.Cells["A3"];

cellA3.PutValue(results);

//Print the output

Debug.WriteLine("Value of A1: " + cellA1.StringValue);

Debug.WriteLine("Value of A2: " + cellA2.StringValue);

Debug.WriteLine("Result of Sum(A1:A2): " + results.ToString());

workbook.Save("Calulate Any Formulae.xls");

{{< /highlight >}}
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
