---
title: Ställa in formelberäkningsläge för arbetsbok i Aspose.Cells
type: docs
weight: 100
url: /sv/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel låter dig ställa in formelberäkningsläget, det vill säga hur formler beräknas. Det finns tre möjliga värden:

- Automatiskt - räkna om när något ändras och varje gång en arbetsbok öppnas.
- Automatisk utom för datatabeller - räkna om när något ändras, men utelämna datatabeller.
- Manuell - räkna om endast när användaren uttryckligen begär det genom att trycka på F9 eller CTRL+ALT+F9, eller när arbetsboken sparas.

{{% /alert %}} 

Så här ställer du in formelberäkningsläget i Microsoft Excel:

1.  Välj**Formler** och då**Beräkningsalternativ**.
1. Välj ett av alternativen.

 Aspose.Cells låter dig också ställa in**Formelberäkningsläge** med hjälp av egenskapen FormulaSettings.CalculationMode. Du kan tilldela den CalcModeType-uppräkningen som har ett av följande värden:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

Följande exempelkod skapar först en arbetsbok och ställer sedan in formelberäkningsläget till**Manuell** och sparar arbetsboken som utdata Excel-fil på disk.

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
## **Ladda ner provkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Ladda ner körningsexempel**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
