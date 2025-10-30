---
title: Konvertera Text till Kolumner med Aspose.Cells
type: docs
weight: 30
url: /sv/python-net/convert-text-to-columns-using-aspose-cells/
description: Denna artikel visar hur man konverterar text till kolumner med hjälp av Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Konvertera text till kolumner, Konvertera text till kolumner i Python.
---

## **Möjliga användningsscenario**

Du kan konvertera din text till kolumner med hjälp av Microsoft Excel. Denna funktion är tillgänglig från *Dataverktyg* under fliken *Data*. För att dela upp innehållet i en kolumn i flera kolumner, ska datan innehålla en specifik avgränsare som en komma (eller något annat tecken) baserat på vilket Microsoft Excel delar upp innehållet i en cell i flera celler. Aspose.Cells for Python via .NET tillhandahåller också den här funktionen via [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) metoden.

## **Konvertera text till kolumner med hjälp av Aspose.Cells for Python Excel Library**

Följande exemplarkod förklarar användningen av [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) metod. Koden lägger först till några personers namn i kolumn A av den första kalkylbladet. Förnamnet och efternamnet är separerade av ett blanktecken. Sedan tillämpar det [**Worksheet.Cells.text_to_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/text_to_columns/) metoden på kolumn A och sparar det som en utfil. Om du öppnar [utfilen](25395213.xlsx) ser du att förnamnen är i kolumn A medan efternamnen är i kolumn B som visas i denna skärmbild.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-ConvertTextToColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
