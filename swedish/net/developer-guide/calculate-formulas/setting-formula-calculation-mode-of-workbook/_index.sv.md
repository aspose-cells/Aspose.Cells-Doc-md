---
title: Ställa in formelberäkningsläget för arbetsboken
description: Denna artikel introducerar hur du ställer in formelberäkningsläget för en arbetsbok i Microsoft Excel med Aspose.Cells biblioteket. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda metoden som tillhandahålls av Aspose.Cells för att ställa in formelberäkningsläget och få resultatet. Till slut sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, arbetsbok, formelberäkningsläge, inställningar
type: docs
weight: 110
url: /sv/net/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells tillåter också att du ställer in **Formelberäkningsläget** med hjälp av [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode)-lägesegenskapen. Du kan tilldela den [**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)-uppräkningen som har ett av följande värden:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
