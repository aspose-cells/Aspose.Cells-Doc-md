---
title: Omvandling mellan cellnamn och rad/kolumnindex
linktitle: Cellnamn och Index Omvandling
type: docs
weight: 10
url: /sv/net/names-and-indices/
description: Lär dig hur man får omvandling mellan cellnamn och rad/kolumnsindex genom Aspose.Cells for .NET API.
keywords: Hämta cellnamn från rad och kolumnindex, Hämta rad och kolumnindex från cellnamn, Skapa säkra arbetsbladnamn, Lägg till säkra arbetsbladnamn
---

## **Hämta cellnamn från rad- och kolumnindex**
Det är möjligt att hitta ett cells namn med rad- och kolumnindex. Den här artikeln förklarar hur.
Aspose.Cells tillhandahåller CellsHelper.CellIndexToName-metoden som tillåter utvecklare att få ett cells namn om de tillhandahåller rad- och kolumnindex.

{{% alert color="primary" %}} 

Microsoft Excel börjar räkna rad- och kolumnindex från 1. Till skillnad från Microsoft Excel börjar Aspose.Cells räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempelkod illustrerar hur man använder CellsHelper.CellIndexToName för att komma åt cells namn utifrån ett känt rad- och kolumnindex. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Hämta rad- och kolumnindex från cellens namn**
Det är möjligt att hitta en rad- och kolumnindex för cellen från dess namn. Denna artikel förklarar hur.
Aspose.Cells tillhandahåller CellsHelper.CellNameToIndex-metoden som tillåter utvecklare att få rad- och kolumnindex från cells namn.

{{% alert color="primary" %}} 

Microsoft Excel börjar räkna rad- och kolumnindex från 1. Till skillnad från Microsoft Excel börjar Aspose.Cells räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempelkod illustrerar hur man använder CellsHelper.CellNameToIndex för att få rad- och kolumnindex från cells namn. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Skapa säkra kalkylbladsnamn**
Ibland finns det ett behov av att tilldela bladnamnet vid körning. I detta scenario kan det finnas bladnamn som kan innehålla vissa ytterligare tecken som <>+(?”. Det är nödvändigt att ersätta sådana tecken, som inte tillåts som bladnamn, med något förinställt tecken som tillhandahålls av användaren. På samma sätt kan längden öka till mer än 31 tecken vilket behöver kapas. Apache POI tillhandahåller vissa funktioner för att skapa säkra namn, därför tillhandahålls liknande funktion av Aspose.Cells för att hantera alla dessa problem. Följande exempelkod demonstrerar denna funktion:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Utdata:

Det här är det första namnet som skapas

` `< > + (adj.Private _ " Private"
{{< app/cells/assistant language="csharp" >}}
