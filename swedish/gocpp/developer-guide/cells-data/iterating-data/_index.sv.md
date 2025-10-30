---
title: Hur och var man använder enumerationer med Golang via C++
linktitle: Iterera data
type: docs
weight: 55
url: /sv/go-cpp/how-and-where-to-use-enumerators/
description: Lär dig hur och var man använder enumeratorer via API et Aspose.Cells for C++.
keywords: Hur man använder Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---

{{% alert color="primary" %}}

 En enumerator är ett objekt som ger möjlighet att traversera en behållare eller kollektion. Enumerators kan användas för att läsa data i kollektionen, men de kan inte ändra den underliggande kollektionen, medan IEnumerable är ett gränssnitt som definierar en metod GetEnumerator som returnerar ett IEnumerator-objekt, vilket i sin tur tillåter endast läsaccess till en kollektion.

Aspose.Cells API:er tillhandahåller ett gäng enumeratörer, denna artikel diskuterar huvudsakligen de tre typerna som listas nedan.

1. Cells Enumerator
1. Rows Enumerator
1. Kolumnenummer

{{% /alert %}}

## **Hur man använder Enumerators**

### **Cellers Enumerator**

Det finns olika sätt att komma åt Celler Enumerator, och man kan använda någon av dessa metoder baserat på programkraven. Här är metoderna som returnerar cellerna Enumerator.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/range/getenumerator/)

Alla ovan nämnda metoder returnerar enumeratorn som tillåter att traversera samlingen av celler som har initierats.

{{% alert color="primary" %}}

När man traverserar cellerna ska samlingen inte modifieras (operationer som kommer att orsaka en ny cell att instansieras eller befintlig cell att ta bort). Annars kanske inte Enumeratorn kan traversera alla celler korrekt (vissa element kan traverseras upprepade gånger eller hoppas över).

{{% /alert %}}

Följande kodexempel visar implementeringen av IEnumerator-gränssnittet för en Cells-samling.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData.go" >}}
### **Radenummerator**

Enumsator för rader kan nås medan du använder [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/rowcollection/getenumerator/) metoden. Följande kodexempel visar implementeringen av IEnumerator-gränssnittet för [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-1.go" >}}
### **Kolumner Hämtning**

 Kolumner kan nås medan du använder [**ColumnCollection.Get**](https://reference.aspose.com/cells/go-cpp/columncollection/get/) metoden. Följande kodexempel visar implementeringen av Get-metoden för [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-2.go" >}}
## **Var man ska använda Enumerators**

För att diskutera fördelarna med att använda enumerators, låt oss ta ett exempel i realtid.

**Scenario**

 Ett applikationskrav är att traversera alla celler i en given [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) för att läsa deras värden. Det kan finnas flera sätt att implementera detta mål. Några demonstreras nedan.

### **Användning av Display Range**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-3.go" >}}
### **Användning av MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-4.go" >}}
Som du kan observera använder båda ovan nämnda tillvägagångssätten mer eller mindre liknande logik, det vill säga; loopa över alla celler i samlingen för att läsa cellvärdena. Detta kan vara problematiskt av flera skäl som diskuteras nedan.

1. API:er som [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) & [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) kräver extra tid för att samla in motsvarande statistik. Om datamatrisen (rader x kolumner) är stor kan användningen av dessa API:er försena prestandan.
1. I de flesta fall är inte alla celler i en given omfattning instansierade. I sådana situationer är det inte så effektivt att kontrollera varje cell i matrisen jämfört med att bara kontrollera de initierade cellerna.
1. Åtkomst av en cell i en loop som Celler rad, kolumn kommer att orsaka att alla cellobjekt i ett område instansieras, vilket så småningom kan orsaka OutOfMemoryException.

## **Slutsats**

Baserat på ovan nämnda fakta är följande möjliga scenarier där enumerators bör användas.

1. Endast läsåtkomst av cellsamlingen krävs, dvs. kravet är att endast inspektera cellerna.
1. Ett stort antal celler ska traverseras.
1. Endast initialiserade celler/rader/kolumner ska traverseras.
