---
title: Få cellerindex
type: docs
weight: 600
url: /sv/python-net/get-cells-index/
description: Lär dig hur man får rad eller kolumn genom radens namn genom Aspose.Cells för Python via .NET API, kolumn eller celler. Konvertera cellens namn till rad och kolumnindex med nollbaserad indexering genom Aspose.Cells för Python via .NET API.
keywords: Python Excel, Hämta radindex och kolumnindex genom cellens namn med hjälp av Python, Hämta kolumnindex genom kolumnens namn med hjälp av Python, Hämta radindex genom radens namn med hjälp av Python, Få index genom cellens namn med hjälp av Python. 
---

{{% alert color="primary" %}}
Standardvyn i Excel är A1-stilreferens, där varje kolumn är definierad som A, B, C ... och cellerna namnges som A1, B2, C3 ... och så vidare.
Du kan vilja veta vilken rad och kolumn är denna cell i.

{{% /alert %}}


## **Möjliga användningsscenario**
När du bara behöver manipulera en specifik data på arbetsbladet genom rad- och kolumnindex behöver du veta kolumn- och kolumnindex för den specifika cellen. 
Aspose.Cells för Python via .NET erbjuder denna funktion för att få rad- och kolumnindex genom namnet på raden, kolumnen och cellen. 
Aspose.Cells för Python via .NET tillhandahåller följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

Observera: Indexeringen är nollbaserad i Aspose.Cells för Python via .NET, men radens ID är baserad på ett i MS Excel.

## **Få cellindex med hjälp av Aspose.Cells för Python Excel-bibliotek**
Detta exempel visar hur man:

1. Skapa en arbetsbok och lägg till lite data.
1. Hitta den specifika cellen i det första arbetsbladet.
1. Få radindex och kolumnindex efter namnet på cellen.
1. Få kolumnindex efter namnet på kolumnen.
1. Få radindex efter namnet på raden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
{{< app/cells/assistant language="python-net" >}}
