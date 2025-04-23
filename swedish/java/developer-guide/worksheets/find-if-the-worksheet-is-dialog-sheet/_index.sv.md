---
title: Ta reda på om kalkylbladet är Dialog sheet
type: docs
weight: 100
url: /sv/java/find-if-the-worksheet-is-dialog-sheet/
---

## **Möjliga användningsscenario**

Dialogblad är ett gammalt format av bladet som innehåller en dialogruta. Ett sådant blad kan sättas in av en äldre version av Microsoft Excel t.ex. 2003 som visas på denna skärmbild. Det kan också sättas in med VBA i nyare versioner t.ex. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Du kan ta reda på om arket är ett dialogblad eller något annat typ av blad med [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) egenskapen som tillhandahålls av Aspose.Cells. Om den returnerar uppräkningvärdet [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), betyder det att du hanterar ett dialogblad.

## **Ta reda på om kalkylbladet är Dialog sheet**

Följande provkod laddar [prov-Excel-filen](64716841.xlsx) som innehåller ett dialogblad. Den kontrollerar [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) egenskapen jämför den med [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) och skriver sedan ut meddelandet. Se konsolresultatet för källkoden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Konsoloutput**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
