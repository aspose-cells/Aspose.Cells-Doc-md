---
title: Вычислять или пересчитывать формулы динамически
type: docs
weight: 10
url: /ru/net/calculate-or-recalculate-formulas-dynamically/
---
**Формула расчета** двигатель встроен в**Aspose.Cells**. Он может не только повторно вычислить формулу, импортированную из файла конструктора, но также поддерживает вычисление результатов формул, добавленных во время выполнения.
## **Добавление формул и расчет результатов**
Aspose.Cells поддерживает большинство формул и функций, входящих в состав Microsoft Excel. Разработчики могут использовать эти формулы с помощью API или электронных таблиц конструктора. Aspose.Excel поддерживает огромный набор формул Mathematical, String, Boolean, Date/Time, Statistical, Database, Lookup и Reference.

Используйте свойство Formula класса Cell, чтобы добавить формулу в ячейку. При применении формулы к ячейке всегда начинайте строку со знака равенства (=), как при создании формулы в Microsoft Excel. Используйте запятую (,) для разделения параметров функции.

 Чтобы вычислить результаты формул, вызовите метод CalculateFormula класса Excel, который обрабатывает все формулы, встроенные в файл Excel. Читать[url:список функций, поддерживаемых методом CalculateFormula](/cells/ru/net/supported-formula-functions/).

{{< highlight "csharp" >}}

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
## **Расчет формул только один раз**
Когда пользователь вызывает Workbook.CalculateFormula() для вычисления значений формул внутри шаблона книги, Aspose.Cells создает цепочку вычислений. Это увеличивает производительность, когда формулы вычисляются во второй или третий раз и т. д.
Однако, если пользовательский шаблон содержит множество разнообразных формул, то первое вычисление формулы может потреблять много процессорного времени и памяти.

Aspose.Cells позволяет отключить создание цепочки вычислений, что полезно в сценариях, когда вы хотите вычислить формулы вашего файла только один раз.

 Если вы хотите повысить производительность вычислений по формуле по номеру Aspose.Cells и не хотите создавать цепочку вычислений по формуле, установите**FormulaSettings.EnableCalculationChain** как**ЛОЖЬ** . По умолчанию установлено как**истинный**.

{{< highlight "csharp" >}}

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
## **Прямой расчет формулы**
Механизм вычисления формулы встроен в Aspose.Cells. Кроме того, пересчитывая формулу, импортированную из файла конструктора, Aspose.Cells также поддерживает прямой расчет результатов формул.
Иногда вам нужно вычислить результаты формул напрямую, не добавляя их на лист. Значения ячеек, используемых в формуле, уже существуют на листе, и все, что вам нужно, это найти результат этих значений на основе некоторой формулы Ms-Excel без добавления формулы на лист.

 Вы можете использовать Aspose.Cells Механизм вычисления формул API, т.е.**рабочий лист.Рассчитать(строковая формула)**для вычисления результатов таких формул, фактически не добавляя их на лист.

{{< highlight "csharp" >}}

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
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
