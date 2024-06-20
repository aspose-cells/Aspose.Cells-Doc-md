---
title: Ta reda på om kalkylbladet är Dialog sheet
type: docs
weight: 70
url: /sv/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **Möjliga användningsscenario**
Dialogblad är ett gammalt format av bladet som innehåller en dialogruta. Ett sådant blad kan sättas in av en äldre version av Microsoft Excel t.ex. 2003 som visas på denna skärmbild. Det kan också sättas in med VBA i nyare versioner t.ex. Microsoft Excel 2016.

![todo:image_alt_text](DialogSheet.png)
## **Ta reda på om kalkylbladet är Dialog sheet**
Aspose.Cells för Python via Java ger dig möjlighet att kontrollera om kalkylbladet är ett dialogblad. För detta tillhandahåller det [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) egenskapen. Om [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) returnerar uppräkningens värde [SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG), då innebär det att du hanterar ett dialogblad.

Följande kodsnutt visar hur man kontrollerar om det finns ett dialogblad. Konsoloutputen som genereras av koden ges nedan för referens.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Konsoloutput**
{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
