---
title: Ställa in formelberäkningsläget för arbetsboken
type: docs
weight: 130
url: /sv/java/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells tillåter också att du ställer in **Formelberäkningsläget** med hjälp av egenskapen [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode). Du kan tilldela det [**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType) uppräkningen som har något av följande värden:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC-EXCEPT-TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

Följande exempelkod skapar först en arbetsbok, sedan ställer den in formelberäkningsläget till **Manuell** och sparar arbetsboken som utdata Excel-fil på disk.

**Utdatafilen. Observera formelberäkningsläget.**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
{{< app/cells/assistant language="java" >}}
