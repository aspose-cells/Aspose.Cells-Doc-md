---
title: Establecer el modo de cálculo de fórmulas del libro en Aspose.Cells
type: docs
weight: 100
url: /es/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel te permite establecer el modo de cálculo de fórmulas, es decir, la forma en que se calculan las fórmulas. Hay tres valores posibles:

- Automático: recalcula cada vez que algo cambia, y cada vez que se abre un libro.
- Automático excepto para tablas de datos: recalcula cada vez que algo cambia, pero deja fuera las tablas de datos.
- Manual: recalcula solo cuando el usuario lo solicita explícitamente presionando F9 o CTRL+ALT+F9, o cuando se guarda el libro.

{{% /alert %}} 

Para establecer el modo de cálculo de fórmulas en Microsoft Excel:

1. Selecciona **Fórmulas** y luego **Opciones de cálculo**.
1. Selecciona una de las opciones.

Aspose.Cells también te permite establecer el **Modo de cálculo de fórmula** utilizando la propiedad de modo FormulaSettings.CalculationMode. Puedes asignarle la enumeración CalcModeType que tiene uno de los siguientes valores:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

El siguiente código de muestra primero crea un libro, luego establece el modo de cálculo de fórmulas a **Manual** y guarda el libro como archivo de Excel de salida en el disco.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Descargar Ejemplo en Ejecución**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
