---
title: Calcular o Recalcular fórmulas dinámicamente
type: docs
weight: 10
url: /es/net/calculate-or-recalculate-formulas-dynamically/
---

El motor de cálculo de fórmulas está integrado en **Aspose.Cells**. No solo puede volver a calcular la fórmula importada del archivo de diseño, sino que también admite calcular los resultados de las fórmulas agregadas en tiempo de ejecución.
## **Agregar fórmulas y calcular resultados**
Aspose.Cells admite la mayoría de las fórmulas o funciones que son parte de Microsoft Excel. Los desarrolladores pueden utilizar estas fórmulas con la API o en las hojas de cálculo de diseño. Aspose.Excel admite un amplio conjunto de fórmulas matemáticas, de texto, booleanas, de fecha/hora, estadísticas, de base de datos, de búsqueda y de referencia.

Utilice la propiedad Formula de la clase Cell para agregar una fórmula a una celda. Al aplicar una fórmula a una celda, siempre comience la cadena con un signo igual (=) como lo hace al crear una fórmula en Microsoft Excel. Utilice una coma (,) para delimitar los parámetros de la función.

Para calcular los resultados de las fórmulas, llame al método CalculateFormula de la clase Excel que procesa todas las fórmulas incrustadas en un archivo de Excel. Lea la [url:lista de funciones admitidas por el método CalculateFormula](/cells/es/net/supported-formula-functions/).

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
## **Calcular fórmulas solo una vez**
Cuando el usuario llama a Workbook.CalculateFormula() para calcular los valores de las fórmulas dentro de la plantilla del libro de trabajo, Aspose.Cells crea una cadena de cálculo. Mejora el rendimiento cuando las fórmulas se calculan por segunda o tercera vez, etc.
Sin embargo, si la plantilla del usuario contiene muchas fórmulas diversas, la primera vez que se calcula la fórmula puede consumir mucho tiempo de procesamiento de CPU y memoria.

Aspose.Cells le permite desactivar la creación de una cadena de cálculo que es útil en escenarios en los que desea calcular las fórmulas de su archivo solo una vez.

Si busca mejorar el rendimiento de los cálculos de fórmulas con Aspose.Cells y no desea crear una cadena de cálculo de fórmulas, entonces configure **FormulaSettings.EnableCalculationChain** como **false**. De forma predeterminada, está configurado como **true**.

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
## **Cálculo directo de fórmulas**
El motor de cálculo de fórmulas está integrado en Aspose.Cells. Además de recalcular la fórmula importada del archivo de diseño, Aspose.Cells también admite calcular los resultados de las fórmulas directamente.
A veces, necesita calcular los resultados de las fórmulas directamente sin agregarlas realmente en una hoja de cálculo. Los valores de las celdas utilizados en la fórmula ya existen en una hoja de cálculo y todo lo que necesita es encontrar el resultado de esos valores basados en alguna fórmula de Ms-Excel sin agregar la fórmula en una hoja de cálculo.

Puede utilizar la API del motor de cálculo de fórmulas de Aspose.Cells, es decir, **worksheet.Calculate(string formula)**, para calcular los resultados de tales fórmulas sin agregarlas realmente en la hoja de cálculo.

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
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
