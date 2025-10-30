---
title: Lägg till celler till Microsoft Excel formelvaktfönster med Python.NET
linktitle: Lägg till celler till formelvaktfönster
type: docs
weight: 60
url: /sv/python-net/add-cells-to-microsoft-excel-formula-watch-window/
description: Lär dig hur du övervakar celler i Excels formelvaktfönster med Aspose.Cells för Python via .NET. Inkluderar kodexempel och API referenser.
keywords: python excel, formel vaktfönster, cellövervakning, aspose.cells, python.net
---

## **Möjliga användningsscenario**

Microsoft Excel Watch Window är ett användbart verktyg för att övervaka cellvärden och formler bekvämt i ett dedikerat fönster. Du kan öppna *Watch Window* i Microsoft Excel genom att navigera till *Formulas > Watch Window*. Knappen *Add Watch* tillåter att lägga till celler för inspektion. På samma sätt kan du använda metoden [**Worksheet.cell_watches.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/cellwatchcollection/add/) för att programmatiskt lägga till celler till Watch Window med Aspose.Cells API.

## **Lägg till celler i Microsoft Excel Formelövervakningsfönstret**

Följande kodexempel sätter formler för cellerna C1 och E1 och lägger till båda i Watch Window. Det sparar arbetsboken som [utmatad Excel-fil](67338481.xlsx). När du öppnar utmatningsfilen i Excel kommer båda cellerna att visas i Watch Window som visas:

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Exempelkod**

```python
from aspose.cells import Workbook, SaveFormat

# Create empty workbook.
wb = Workbook()

# Access first worksheet.
ws = wb.worksheets[0]

# Put some integer values in cell A1 and A2.
ws.cells.get("A1").put_value(10)
ws.cells.get("A2").put_value(30)

# Access cell C1 and set its formula.
c1 = ws.cells.get("C1")
c1.formula = "=Sum(A1,A2)"

# Add cell C1 into cell watches by name.
ws.cell_watches.add(c1.name)

# Access cell E1 and set its formula.
e1 = ws.cells.get("E1")
e1.formula = "=A2*A1"

# Add cell E1 into cell watches by its row and column indices.
ws.cell_watches.add(e1.row, e1.column)

# Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat.XLSX)
```
{{< app/cells/assistant language="python-net" >}}
