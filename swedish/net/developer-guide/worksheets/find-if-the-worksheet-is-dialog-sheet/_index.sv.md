---
title: Ta reda på om arbetsbladet är dialogblad
type: docs
weight: 90
url: /sv/net/find-if-the-worksheet-is-dialog-sheet/
description: Dialog Sheet är ett gammalt arkformat. Den här artikeln innehåller instruktioner och exempelkod för att avgöra om ett Excel-kalkylblad är ett dialogblad med hjälp av C# API eller .NET bibliotek.
keywords: find excel worksheet dialog type c#, worksheet dialog c#
---
##  **Möjliga användningsscenarier**

Dialogark är ett gammalt arkformat som innehåller en dialogruta. Ett sådant ark kan infogas med en äldre version av Microsoft Excel, t.ex. 2003, som visas i denna skärmdump. Den kan även infogas med VBA i nyare versioner t.ex. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Du kan se om arket är ett dialogblad eller någon annan typ av ark med[**Arbetsblad.Typ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)egendom tillhandahållen av Aspose.Cells. Om den returnerar uppräkningsvärde[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), då betyder det att du har att göra med dialogblad.

##  **Ta reda på om arbetsbladet är dialogblad**

 Följande exempelkod laddar[exempel på Excel-fil](64716820.xlsx) som innehåller ett dialogblad. Den kontrollerar[**Arbetsblad.Typ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)fastighet jämför det med[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) och skriver sedan ut meddelandet. Se konsolutgången för exempelkoden nedan för mer hjälp.

##  **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

##  **Konsolutgång**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
