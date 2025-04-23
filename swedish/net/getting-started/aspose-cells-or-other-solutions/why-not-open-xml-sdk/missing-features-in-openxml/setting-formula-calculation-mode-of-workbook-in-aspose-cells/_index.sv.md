---
title: Ange arbetsbokens formelberäkningsläge i Aspose.Cells
type: docs
weight: 100
url: /sv/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter dig att ställa in formelberäkningsläget, det vill säga hur formler beräknas. Det finns tre möjliga värden:

- Automatisk - beräknas om varje gång något ändras och varje gång en arbetsbok öppnas.
- Automatisk, utom för datatabeller - beräknas om varje gång något ändras, men exkluderar datatabeller.
- Manuell - beräknas endast när användaren uttryckligen begär det genom att trycka på F9 eller CTRL+ALT+F9 eller när arbetsboken sparas.

{{% /alert %}} 

För att ställa in formelberäkningsläge i Microsoft Excel:

1. Välj **Formler** och sedan **Beräkningsalternativ**.
1. Välj ett av alternativen.

Aspose.Cells låter dig också ställa in **Formelberäkningsläget** med hjälp av FormulaSettings.CalculationMode-egenskapen. Du kan tilldela den CalcModeType-uppräkningen som har ett av följande värden:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

Följande exempelkod skapar först en arbetsbok, sedan ställer den in formelberäkningsläget till **Manuell** och sparar arbetsboken som utdata Excel-fil på disk.

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
## **Ladda ned provkoden**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Ladda ner exempel på körning**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
