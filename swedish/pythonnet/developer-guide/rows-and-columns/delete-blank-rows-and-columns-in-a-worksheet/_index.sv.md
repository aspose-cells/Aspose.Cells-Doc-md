---
title: Radera tomma rader och kolumner i ett kalkylblad
type: docs
weight: 300
url: /sv/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: Den här artikeln beskriver hur man tar bort tomma rader och kolumner i ett kalkylblad med Aspose.Cells för Python via .NET biblioteket.
keywords: Python Excel bibliotek, Python ta bort tomma rader, Python ta bort tomma kolumner, Python ta bort eller ta bort tomma rader och kolumner.
---

{{% alert color="primary" %}}

Det är möjligt att ta bort alla tomma rader och kolumner från ett kalkylblad. Detta är användbart när man till exempel genererar en PDF-fil från en Microsoft Excel-fil och vill konvertera endast rader och kolumner som innehåller data eller relaterade objekt.

Använd följande Aspose.Cells-metoder för att ta bort tomma rader och kolumner:

1. För att ta bort tomma rader, använd metoden [**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows). Observera, för tomma rader som kommer att tas bort, krävs det inte bara att [**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/) ska vara sant, utan det får inte heller finnas någon synlig kommentar definierad för någon cell i dessa rader, och ingen pivottabell vars omfång korsar dem.
1. För att ta bort tomma kolumner, använd metoden [**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns).

{{% /alert %}}

## C# kod för att ta bort tomma rader

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## C# kod för att ta bort tomma kolumner

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
