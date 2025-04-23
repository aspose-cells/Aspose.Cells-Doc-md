---
title: Ta reda på om kalkylbladet är Dialog sheet
type: docs
weight: 90
url: /sv/python-net/find-if-the-worksheet-is-dialog-sheet/
description: Dialogblad är ett gammalt format av blad. Denna artikel ger instruktioner och kodexempel för att automatiskt avgöra om ett Excel ark är ett Dialogblad med Aspose.Cells för Python via .NET bibliotek.
keywords: Python Excel bibliotek, Python sökdialog för Excel arkstyp, dialog för ark i Python.
---

## **Möjliga användningsscenario**

Dialog Sheet är ett gammalt format av ark som innehåller en dialogruta. Ett sådant ark kunde sättas in av en äldre version av Microsoft Excel t.ex. 2003 som visas på denna skärmbild. Det kan också sättas in med VBA i nyare versioner t.ex. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Du kan avgöra om arket är ett dialogark eller någon annan typ av ark med [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/)-egenskapen som tillhandahålls av Aspose.Cells för Python via .NET. Om det returnerar värdet för [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) betyder det att du arbetar med ett dialogark.

## **Ta reda på om kalkylbladet är Dialog sheet**

Följande kodexempel laddar [provmallen i Excel](64716820.xlsx) som innehåller dialogarket. Det kontrollerar egenskapen [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) jämför det med [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) och skriver sedan ut meddelandet. Se konsolutmatningen av det kodexempel som ges nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **Konsoloutput**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
