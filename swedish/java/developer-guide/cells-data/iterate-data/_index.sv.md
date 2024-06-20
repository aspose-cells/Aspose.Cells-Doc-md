---
title: Hur och var man ska använda iteratorer
linktitle: Iterera data
type: docs
weight: 640
url: /sv/java/how-and-where-to-use-iterators/
---

{{% alert color="primary" %}} 

Ett objekt av en iteratorgränssnitt kan användas för att traversera genom alla element i en samling. Iteratorer kan användas för att inspektera datan i en samling, men de kan inte användas för att modifiera den underliggande samlingen. Generellt sett måste följande steg tas för att använda en iterator för att cykla genom innehållet i en samling:

1. Få en iterator till början av samlingen genom att ringa samlingens iterator-metod.
1. Sätt upp en loop som gör ett anrop till hasNext-metoden. Låt loopen iterera så länge hasNext-metoden returnerar true.
1. Inom loopen, hämta varje element genom att ringa nästa metod.

Aspose.Cells API:er tillhandahåller en mängd iteratorer, men den här artikeln diskuterar främst de tre typerna som listas nedan.

1. Cells Iterator
1. Rows Iterator
1. Columns Iterator

{{% /alert %}} 
## **Hur man använder Iteratorer**
### **Cells Iterator**
Det finns olika sätt att komma åt cellernas iterator, och man kan använda någon av dessa metoder baserat på applikationskraven. Här är metoderna som returnerar cellernas iterator.

1. Cells.iterator
1. Row.iterator
1. Range.iterator

Alla ovan nämnda metoder returnerar en iterator som tillåter att traversera samlingen av celler som har initierats.

{{% alert color="primary" %}} 

Under traverseringen av cellerna bör samlingen inte modifieras (operationer som kommer att orsaka en ny cell att instansieras eller befintlig cell att raderas). Annars kan iteratorn inte traversera alla celler korrekt (vissa element kan traverseras upprepade gånger eller hoppas över).

{{% /alert %}} 

Följande kodexempel demonstrerar implementeringen av Iterator-klassen för en cellers samling.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Rows Iterator**
Rows Iterator kan kommas åt när man använder RowCollection.iterator-metoden. Följande kodexempel demonstrerar implementeringen av Iteratorklassen för RowCollection-klassen.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Columns Iterator**
Columns Iterator kan kommas åt när man använder ColumnCollection.iterator-metoden. Följande kodexempel demonstrerar implementeringen av Iteratorklassen för ColumnCollection-klassen.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Var man ska använda Iteratorer**
För att diskutera fördelarna med att använda iteratorer, låt oss ta ett verkligt exempel.
##### **Scenario**
Ett applikationskrav är att traversera alla celler i en given arbetsbok för att läsa deras värden. Det kan finnas flera sätt att implementera detta mål. Några demonstreras nedan.
###### **Användning av Display Range**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Användning av MaxDataRow & MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Som du kan se, använder båda ovan nämnda tillvägagångssätt mer eller mindre liknande logik, det vill säga; loopa över alla celler i samlingen för att läsa cellvärdena. Detta kan vara problematiskt av flera skäl som diskuteras nedan.

1. API:er som MaxRow, MaxDataRow, MaxColumn, MaxDataColumn & MaxDisplayRange kräver extra tid för att samla in motsvarande statistik. Om datamatrisen (rader x kolumner) är stor kan användningen av dessa API:er innebära prestandastraff.
1. I de flesta fall är inte alla celler i en given omfattning instansierade. I sådana situationer är det inte så effektivt att kontrollera varje cell i matrisen jämfört med att bara kontrollera de initierade cellerna.
1. Åtkomst av en cell i en loop som Cells.get(rowIndex, columnIndex) kommer att orsaka att alla cellobjekt i en omfattning instansieras, vilket eventuellt kan orsaka OutOfMemoryError.
##### **Slutsats**
Baserat på ovan nämnda fakta, följande är de möjliga scenarier där iteratorer bör användas.

1. Endast läsåtkomst av cellkollektionen krävs, det vill säga; kravet är att bara inspektera cellerna.
1. Ett stort antal celler ska traverseras.
1. Endast initialiserade celler/rader/kolumner ska traverseras.
