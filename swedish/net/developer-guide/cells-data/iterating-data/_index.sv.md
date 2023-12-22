---
title: Hur och var man använder enumerators
linktitle: Iterera data
type: docs
weight: 55
url: /sv/net/how-and-where-to-use-enumerators/
description: Lär dig hur och var du använder enumerators via Aspose.Cells for .NET API.
keywords: How to use Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---
{{% alert color="primary" %}}

En uppräkning är ett objekt som ger möjlighet att passera en behållare eller en samling. Enumeratorer kan användas för att läsa data i samlingen, men de kan inte användas för att modifiera den underliggande samlingen, medan IEnumerable är ett gränssnitt som definierar en metod GetEnumerator som returnerar ett IEnumerator-gränssnitt, vilket i sin tur tillåter skrivskyddad tillgång till en samling.

Aspose.Cells API:er tillhandahåller ett gäng uppräknare, men den här artikeln diskuterar huvudsakligen de tre typerna som listas nedan.

1. Cells Enumerator
1. Raduppräkning
1. Kolumnuppräkning

{{% /alert %}}

##  **Hur man använder Enumerators**

###  **Cells Enumerator**

Det finns olika sätt att komma åt Cells Enumerator, och man kan använda vilken som helst av dessa metoder baserat på applikationskraven. Här är metoderna som returnerar celluppräkningen.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Alla de ovan nämnda metoderna returnerar enumeratorn som gör det möjligt att gå igenom samlingen av celler som har initierats.

{{% alert color="primary" %}}

När du korsar cellerna bör samlingen inte modifieras (operationer som gör att en ny Cell instansieras eller befintlig Cell tas bort). Annars kan det hända att enumeratorn inte kan gå igenom alla celler korrekt (vissa element kan korsas upprepade gånger eller hoppa över).

{{% /alert %}}

Följande kodexempel visar implementeringen av IEnumerator-gränssnittet för en Cells-samling.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

###  **Raduppräkning**

 Rows Enumerator kan nås när du använder[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) metod. Följande kodexempel visar implementeringen av IEnumerator-gränssnittet för[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

###  **Kolumnuppräkning**

 Kolumnuppräkningen kan nås när du använder[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) metod. Följande kodexempel visar implementeringen av IEnumerator-gränssnittet för[**Kolumnsamling**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

##  **Var kan man använda Enumerators**

För att diskutera fördelarna med att använda uppräknare, låt oss ta ett exempel i realtid.

**Scenario**

 Ett applikationskrav är att korsa alla celler i en given[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)att läsa deras värderingar. Det kan finnas flera sätt att genomföra detta mål. Några få visas nedan.

###  **Använda visningsintervall**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

###  **Använda MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Som du kan observera att båda de ovan nämnda tillvägagångssätten använder mer eller mindre liknande logik, det vill säga; loop över alla celler i samlingen för att läsa cellvärdena. Detta kan vara problematiskt av ett antal skäl som diskuteras nedan.

1.  API:er som t.ex[**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)kräver extra tid för att samla in motsvarande statistik. Om datamatrisen (rader x kolumner) är stor, kan användningen av dessa API:er innebära en prestationsstraff.
1. de flesta fall instansieras inte alla celler i ett givet intervall. I sådana situationer är det inte så effektivt att kontrollera varje cell i matrisen jämfört med att kontrollera endast de initialiserade cellerna.
1. Åtkomst till en cell i en loop som Cells rad, kolumn gör att alla cellobjekt i ett intervall instansieras, vilket så småningom kan orsaka OutOfMemoryException.

##  **Slutsats**

Baserat på ovan nämnda fakta är följande möjliga scenarier där uppräknare bör användas.

1. Skrivskyddad åtkomst till cellsamlingen krävs, det vill säga; kravet är att endast inspektera cellerna.
1. Ett stort antal celler ska passeras.
1. Endast initierade celler/rader/kolumner som ska passeras.
