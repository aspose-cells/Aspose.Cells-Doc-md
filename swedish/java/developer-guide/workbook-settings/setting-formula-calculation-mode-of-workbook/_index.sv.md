---
title: Ställa in formelberäkningsläge för arbetsbok
type: docs
weight: 130
url: /sv/java/setting-formula-calculation-mode-of-workbook/
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

 Aspose.Cells låter dig också ställa in**Formelberäkningsläge** använda[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) fast egendom. Du kan tilldela den[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType)uppräkning som har ett av följande värden:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

 Följande exempelkod skapar först en arbetsbok och ställer sedan in formelberäkningsläget till**Manuell** och sparar arbetsboken som utdata Excel-fil på disk.

**Utdatafilen. Notera formelberäkningsläget.**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
