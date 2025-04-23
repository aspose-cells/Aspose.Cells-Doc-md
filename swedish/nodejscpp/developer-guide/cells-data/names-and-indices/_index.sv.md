---
title: Omvandling mellan cellnamn och rad/kolumnindex
linktitle: Cellnamn och Index Omvandling
type: docs
weight: 10
url: /sv/nodejs-cpp/names-and-indices/
description: Lär dig hur du får konvertering mellan cellnamn och rad/kolumnindex via Aspose.Cells for Node.js via C++ API.
keywords: Node.js via C++ Få cellnamn från rad och kolumnindex, Få rad och kolumnindex från cellnamn, Skapa säkra bladnamn, Lägg till säkra bladnamn
---

## **Hämta cellnamn från rad- och kolumnindex**
Det är möjligt att hitta ett cells namn med rad- och kolumnindex. Den här artikeln förklarar hur.
Aspose.Cells for Node.js via C++ erbjuder metoden CellsHelper.cellIndexToName som gör att utvecklare kan få namnet på en cell om de tillhandahåller rad- och kolumnindex.

{{% alert color="primary" %}} 

Microsoft Excel börjar räkna rad- och kolumnindex från 1. Till skillnad från Microsoft Excel, börjar Aspose.Cells for Node.js via C++ räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempel visar hur man använder CellsHelper.cellIndexToName för att få tillgång till cellens namn givet ett känt rad- och kolumnindex. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-IndexToName-1.js" >}}
## **Hämta rad- och kolumnindex från cellens namn**
Det är möjligt att hitta en rad- och kolumnindex för cellen från dess namn. Denna artikel förklarar hur.
Aspose.Cells for Node.js via C++ tillhandahåller metoden CellsHelper.cellNameToIndex som gör att utvecklare kan få ett rad- och kolumnindex från cellnamnet.

{{% alert color="primary" %}} 

Microsoft Excel börjar räkna rad- och kolumnindex från 1. Till skillnad från Microsoft Excel, börjar Aspose.Cells for Node.js via C++ räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempel visar hur man använder CellsHelper.cellNameToIndex för att få rad- och kolumnindex från cellnamnet. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-NameToIndex-1.js" >}}

## **Skapa säkra kalkylbladsnamn**
Ibland kan det vara nödvändigt att tilldela bladnamnet i realtid. I denna scenarior kan det finnas bladnamn som innehåller ytterligare tecken som <>+(?”. Det kan vara nödvändigt att ersätta dessa tecken som inte är tillåtna som bladnamn med ett förutbestämt tecken som ges av användaren. Likaså kan längden öka till mer än 31 tecken vilket måste kortas ned. Apache POI tillhandahåller vissa funktioner för att skapa säkra namn, och liknande funktioner finns även i Aspose.Cells for Node.js via C++ för att hantera dessa problem. Följande exempel demonstrerar denna funktion:



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-CreateSafeSheetNames.js" >}}

Utdata:

Det här är det första namnet som skapas

` `< > + (adj.Private _ " Private"
