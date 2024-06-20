---
title: Omvandling mellan cellnamn och rad/kolumnindex
linktitle: Cellnamn och Index Omvandling
type: docs
weight: 10
url: /sv/python-net/names-and-indices/
description: Lär dig hur man får konvertering mellan cellnamn och rad/kolumnindex genom Aspose.Cells för Python via .NET API.
keywords: Python Excel Library, Python Hämta cellnamn från rad och kolumnindex, Python Hämta rad och kolumnindex från cellnamn, Python Skapa säkra kalkylbladnamn, Python Lägg till säkra kalkylbladnamn
---

## **Hämta cellnamn från rad- och kolumnindex**
Det är möjligt att hitta ett cells namn med rad- och kolumnindex. Den här artikeln förklarar hur.
Aspose.Cells for Python via .NET tillhandahåller metoden [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) som gör att utvecklare kan få namnet på en cell om de anger rad och kolumnindex.

{{% alert color="primary" %}} 

Till skillnad från Microsoft Excel, där rad- och kolumnindex börjar från 1, börjar Aspose.Cells for Python via .NET att räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempelkod illustrerar hur man använder [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) för att få åtkomst till cellnamnet med en känd rad och kolumnindex. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **Hämta rad- och kolumnindex från cellens namn**
Det är möjligt att hitta en rad- och kolumnindex för cellen från dess namn. Denna artikel förklarar hur.
Aspose.Cells for Python via .NET tillhandahåller metoden [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) som gör att utvecklare kan få rad- och kolumnindex från cellens namn.

{{% alert color="primary" %}} 

Till skillnad från Microsoft Excel, där rad- och kolumnindex börjar från 1, börjar Aspose.Cells for Python via .NET att räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempelkod illustrerar hur man använder [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) för att få rad- och kolumnindex från cellens namn. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **Skapa säkra kalkylbladsnamn**
Ibland finns det ett behov av att tilldela kalkylbladsnamnet vid körning. I detta scenario kan det finnas kalkylbladsnamn som kan innehålla vissa ytterligare tecken som <>+(?”. Det finns ett behov av att ersätta något sådant tecken, som inte är tillåtet som kalkylbladsnamn, med några förinställda tecken som tillhandahålls av användaren. På samma sätt kan längden öka till mer än 31 tecken vilket måste förkortas. Apache POI tillhandahåller vissa funktioner för att skapa säkra namn, därför tillhandahålls liknande funktion av Aspose.Cells för Python via .NET för att hantera alla dessa problem. Följande exempelkod demonstrerar denna funktion:



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

Utdata:

Det här är det första namnet som skapas

` `< > + (adj.Private _ " Private"
