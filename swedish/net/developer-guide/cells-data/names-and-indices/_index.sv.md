---
title: Konvertering mellan cellnamn och rad-/kolumnindex
linktitle: Cell Namn och indexkonvertering
type: docs
weight: 10
url: /sv/net/names-and-indices/
---
## **Hämta Cell Namn från rad- och kolumnindex**
Det är möjligt att hitta en cells namn med tanke på rad- och kolumnindex. Den här artikeln förklarar hur.
Aspose.Cells tillhandahåller metoden CellsHelper.CellIndexToName som tillåter utvecklare att få en cells namn om de tillhandahåller rad- och kolumnindex.

{{% alert color="primary" %}} 

Till skillnad från Microsoft Excel, där rad- och kolumnindex börjar från 1, börjar Aspose.Cells räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempelkod illustrerar hur du använder CellsHelper.CellIndexToName för att komma åt cellens namn givet ett känt rad- och kolumnindex. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Hämta rad- och kolumnindex från Cell Namn**
Det är möjligt att hitta ett rad- och kolumnindex för cellen från dess namn. Den här artikeln förklarar hur.
Aspose.Cells tillhandahåller metoden CellsHelper.CellNameToIndex som tillåter utvecklare att hämta ett rad- och kolumnindex från cellens namn.

{{% alert color="primary" %}} 

Till skillnad från Microsoft Excel, där rad- och kolumnindex börjar från 1, börjar Aspose.Cells räkna rad- och kolumnindex från 0.

{{% /alert %}} 

Följande exempelkod illustrerar hur du använder CellsHelper.CellNameToIndex för att hämta rad- och kolumnindex från cellens namn. Koden genererar följande utdata.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Skapa säkra bladnamn**
 Ibland finns det ett behov av att tilldela arknamnet vid körning. I det här scenariot kan det finnas arknamn som kan innehålla några ytterligare tecken som<>+(?”. Det finns ett behov av att ersätta alla sådana tecken, som inte är tillåtna som ett arknamn med något förinställt tecken som tillhandahålls av användaren. På samma sätt kan längden öka till mer än 31 tecken som måste trunkeras. Apache POI tillhandahåller vissa funktioner för att skapa säkra namn, därför tillhandahålls liknande funktion av Aspose.Cells för att hantera alla dessa problem. Följande exempelkod visar denna funktion:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Produktion:

detta är förnamn som är cre

` `<> + (adj.Privat _ "Privat"
