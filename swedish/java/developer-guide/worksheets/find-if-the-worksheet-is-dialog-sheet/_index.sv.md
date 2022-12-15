---
title: Ta reda på om arbetsbladet är dialogblad
type: docs
weight: 100
url: /sv/java/find-if-the-worksheet-is-dialog-sheet/
---
## **Möjliga användningsscenarier**

Dialogark är ett gammalt format av arket som innehåller en dialogruta. Ett sådant blad skulle kunna infogas av en äldre version av Microsoft Excel, t.ex. 2003 som visas i denna skärmdump. Den kan även infogas med VBA i nyare versioner t.ex. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Du kan se om arket är ett dialogblad eller någon annan typ av ark med[**Arbetsblad.Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)egendom tillhandahållen av Aspose.Cells. Om den returnerar uppräkningsvärde[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), då betyder det att du har att göra med ett dialogblad.

## **Ta reda på om arbetsbladet är dialogblad**

Följande exempelkod laddar[exempel på Excel-fil](64716841.xlsx)som innehåller ett dialogblad. Den kontrollerar[**Arbetsblad.Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)fastighet jämför det med[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)och skriver sedan ut meddelandet. Se konsolutgången för exempelkoden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
