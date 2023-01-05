---
title: Configuración del modo de cálculo de fórmula del libro de trabajo en Aspose.Cells
type: docs
weight: 100
url: /es/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel le permite configurar el modo de cálculo de fórmulas, es decir, la forma en que se calculan las fórmulas. Hay tres valores posibles:

- Automático: vuelve a calcular cada vez que se cambia algo y cada vez que se abre un libro.
- Automático excepto para las tablas de datos: vuelve a calcular cada vez que se cambia algo, pero omite las tablas de datos.
- Manual: vuelva a calcular solo cuando el usuario lo solicite explícitamente presionando F9 o CTRL+ALT+F9, o cuando se guarde el libro.

{{% /alert %}} 

Para configurar el modo de cálculo de fórmula en Microsoft Excel:

1.  Seleccione**Fórmulas** y luego**Opciones de cálculo**.
1. Seleccione una de las opciones.

 Aspose.Cells también le permite configurar el**Modo de cálculo de fórmula** usando la propiedad de modo FormulaSettings.CalculationMode. Puede asignarle la enumeración CalcModeType que tiene uno de los siguientes valores:

- CalcModeType.Automático
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

El siguiente código de ejemplo primero crea un libro de trabajo, luego establece el modo de cálculo de fórmulas en**Manual** y guarda el libro de trabajo como archivo de salida de Excel en el disco.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Descargar ejemplo de ejecución**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
