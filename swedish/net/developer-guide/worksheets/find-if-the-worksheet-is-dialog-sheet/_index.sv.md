---
title: Ta reda på om kalkylbladet är Dialog sheet
type: docs
weight: 90
url: /sv/net/find-if-the-worksheet-is-dialog-sheet/
description: Dialog Sheet är ett gammalt format av ark. Den här artikeln ger instruktioner och exempelkod för att bestämma programmatiskt om ett Excel kalkylblad är ett Dialog Sheet som använder C# API eller .NET Library.
keywords: hitta excel kalkylblad dialogtyp c#, kalkylblad dialog c#
---

## **Möjliga användningsscenario**

Dialog Sheet är ett gammalt format av ark som innehåller en dialogruta. Ett sådant ark kunde sättas in av en äldre version av Microsoft Excel t.ex. 2003 som visas på denna skärmbild. Det kan också sättas in med VBA i nyare versioner t.ex. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Du kan ta reda på om arket är ett dialogark eller någon annan typ av ark med [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) egenskapen som tillhandahålls av Aspose.Cells. Om det returnerar uppräkningsvärdet [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), betyder det att du hanterar dialogbladet.

## **Ta reda på om kalkylbladet är Dialog sheet**

Följande kodexempel laddar [provmallen i Excel](64716820.xlsx) som innehåller dialogarket. Det kontrollerar egenskapen [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) jämför det med [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) och skriver sedan ut meddelandet. Se konsolutmatningen av det kodexempel som ges nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
