---
title: Hur och var man använder enumeratörer
linktitle: Iterera data
type: docs
weight: 55
url: /sv/net/how-and-where-to-use-enumerators/
description: Lär dig hur man använder enumeratörer genom Aspose.Cells for .NET API.
keywords: Hur man använder Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---

{{% alert color="primary" %}}

En enumerator är ett objekt som ger möjlighet att traversera en behållare eller en samling. Enumerators kan användas för att läsa data i samlingen, men de kan inte användas för att ändra den underliggande samlingen, medan IEnumerable är en gränssnitt som definierar en metod GetEnumerator som returnerar ett IEnumerator-gränssnitt, vilket i sin tur tillåter endast läsåtkomst till en samling.

Aspose.Cells API:er tillhandahåller ett gäng enumeratörer, denna artikel diskuterar huvudsakligen de tre typerna som listas nedan.

1. Cells Enumerator
1. Rows Enumerator
1. Kolumnenummer

{{% /alert %}}

## **Hur man använder Enumerators**

### **Cellers Enumerator**

Det finns olika sätt att komma åt Celler Enumerator, och man kan använda någon av dessa metoder baserat på programkraven. Här är metoderna som returnerar cellerna Enumerator.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Alla ovan nämnda metoder returnerar enumeratorn som tillåter att traversera samlingen av celler som har initierats.

{{% alert color="primary" %}}

När man traverserar cellerna ska samlingen inte modifieras (operationer som kommer att orsaka en ny cell att instansieras eller befintlig cell att ta bort). Annars kanske inte Enumeratorn kan traversera alla celler korrekt (vissa element kan traverseras upprepade gånger eller hoppas över).

{{% /alert %}}

Följande kodexempel visar implementeringen av IEnumerator-gränssnittet för en Cells-samling.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Radenummerator**

Radenummeratorn kan kommas åt vid användning av [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) metoden. Följande kodexempel visar implementeringen av IEnumerator-gränssnittet för [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Kolumnenummerator**

Kolumnenummeratorn kan kommas åt vid användning av [**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) metoden. Följande kodexempel visar implementeringen av IEnumerator-gränssnittet för [**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Var man ska använda Enumerators**

För att diskutera fördelarna med att använda enumerators, låt oss ta ett exempel i realtid.

**Scenario**

En applikationskrav är att traversera alla celler i en given [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) för att läsa deras värden. Det kan finnas flera sätt att implementera detta mål. Några demonstreras nedan.

### **Användning av Display Range**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Användning av MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Som du kan observera använder båda ovan nämnda tillvägagångssätten mer eller mindre liknande logik, det vill säga; loopa över alla celler i samlingen för att läsa cellvärdena. Detta kan vara problematiskt av flera skäl som diskuteras nedan.

1. API:er som [**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) kräver extra tid för att samla in motsvarande statistik. Om datamatrisen (rader x kolumner) är stor, kan användning av dessa API:er innebära en prestandaböter.
1. I de flesta fall är inte alla celler i en given omfattning instansierade. I sådana situationer är det inte så effektivt att kontrollera varje cell i matrisen jämfört med att bara kontrollera de initierade cellerna.
1. Åtkomst av en cell i en loop som Celler rad, kolumn kommer att orsaka att alla cellobjekt i ett område instansieras, vilket så småningom kan orsaka OutOfMemoryException.

## **Slutsats**

Baserat på ovan nämnda fakta är följande möjliga scenarier där enumerators bör användas.

1. Endast läsåtkomst av cellsamlingen krävs, dvs. kravet är att endast inspektera cellerna.
1. Ett stort antal celler ska traverseras.
1. Endast initialiserade celler/rader/kolumner ska traverseras.
