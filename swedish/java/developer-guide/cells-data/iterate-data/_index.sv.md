---
title: Hur och var man använder iteratorer
linktitle: Iterera data
type: docs
weight: 640
url: /sv/java/how-and-where-to-use-iterators/
---
{{% alert color="primary" %}} 

Ett objekt i ett iteratorgränssnitt kan användas för att gå igenom alla element i en samling. Iteratorer kan användas för att inspektera data i en samling men de kan inte användas för att ändra den underliggande samlingen. I allmänhet, för att använda en iterator för att bläddra igenom innehållet i en samling, måste följande steg vidtas:

1. Skaffa en iterator till början av samlingen genom att anropa samlingens iteratormetod.
1. Sätt upp en loop som gör ett anrop till hasNext-metoden. Låt loopen iterera så länge hasNext-metoden returnerar sant.
1. Inom slingan skaffar du varje element genom att anropa nästa metod.

Aspose.Cells API:er tillhandahåller ett gäng iteratorer, men den här artikeln diskuterar huvudsakligen de tre typerna som anges nedan.

1. Cells Iterator
1. Rader Iterator
1. Kolumner Iterator

{{% /alert %}} 
## **Hur man använder Iteratorer**
### **Cells Iterator**
Det finns olika sätt att komma åt cellernas iterator, och man kan använda vilken som helst av dessa metoder baserat på applikationskraven. Här är metoderna som returnerar cellernas iterator.

1. Cells.iterator
1. Rad.iterator
1. Range.iterator

Alla de ovan nämnda metoderna returnerar iteratorn som gör det möjligt att passera samlingen av celler som har initierats.

{{% alert color="primary" %}} 

När du korsar cellerna bör samlingen inte modifieras (operationer som gör att en ny Cell instansieras eller befintlig Cell tas bort). Annars kanske iteratorn inte kan gå igenom alla celler korrekt (vissa element kan korsas upprepade gånger eller hoppa över).

{{% /alert %}} 

Följande kodexempel visar implementeringen av Iterator-klassen för en cellsamling.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Rader Iterator**
Rows Iterator kan nås när du använder metoden RowCollection.iterator. Följande kodexempel visar implementeringen av klassen Iterator for RowCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Kolumner Iterator**
Columns Iterator kan nås när du använder metoden ColumnCollection.iterator. Följande kodexempel visar implementeringen av klassen Iterator för ColumnCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Var man använder Iteratorer**
För att diskutera fördelarna med att använda iteratorer, låt oss ta ett exempel i realtid.
##### **Scenario**
Ett applikationskrav är att gå igenom alla celler i ett givet kalkylblad för att läsa deras värden. Det kan finnas flera sätt att genomföra detta mål. Några få visas nedan.
###### **Använda visningsintervall**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Använda MaxDataRow & MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Som du kan observera att båda ovan nämnda tillvägagångssätt använder mer eller mindre liknande logik, det vill säga; loop över alla celler i samlingen för att läsa cellvärdena. Detta kan vara problematiskt av ett antal skäl som diskuteras nedan.

1. API:erna som MaxRow, MaxDataRow, MaxColumn, MaxDataColumn & MaxDisplayRange kräver extra tid för att samla in motsvarande statistik. Om datamatrisen (rader x kolumner) är stor, kan användning av dessa API:er innebära prestationsstraff.
1. I de flesta fall instansieras inte alla celler i ett givet intervall. I sådana situationer är det inte så effektivt att kontrollera varje cell i matrisen jämfört med att kontrollera endast de initialiserade cellerna.
1. Att komma åt en cell i en loop som Cells.get(rowIndex, columnIndex) kommer att göra att alla cellobjekt i ett intervall instansieras, vilket så småningom kan orsaka OutOfMemoryError.
##### **Slutsats**
Baserat på ovan nämnda fakta, följer följande möjliga scenarier där iteratorer bör användas.

1. Skrivskyddad åtkomst till cellsamlingen krävs, det vill säga; kravet är att endast inspektera cellerna.
1. Ett stort antal celler ska passeras.
1. Endast initierade celler/rader/kolumner ska korsas.
