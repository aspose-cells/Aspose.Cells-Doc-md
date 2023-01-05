---
title: Ta reda på om arbetsbladet är dialogblad
type: docs
weight: 70
url: /sv/python-java/find-if-the-worksheet-is-dialog-sheet/
---
## **Möjliga användningsscenarier**
Dialogark är ett gammalt format av arket som innehåller en dialogruta. Ett sådant blad skulle kunna infogas av en äldre version av Microsoft Excel, t.ex. 2003 som visas i denna skärmdump. Den kan även infogas med VBA i nyare versioner t.ex. Microsoft Excel 2016.

![todo:image_alt_text](DialogSheet.png)
## **Ta reda på om arbetsbladet är dialogblad**
Aspose.Cells for Python via Java ger dig möjlighet att kontrollera om kalkylbladet är ett dialogblad. För detta ger den[Arbetsblad.Typ](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)fast egendom. Om[Arbetsblad.Typ](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)returnerar uppräkningsvärde[SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG), då betyder det att du har att göra med ett dialogblad.

Följande kodavsnitt visar hur du söker efter ett dialogblad. Konsolutdata som genereras av koden ges nedan som referens.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Konsolutgång**
Arbetsblad är ett dialogblad.
