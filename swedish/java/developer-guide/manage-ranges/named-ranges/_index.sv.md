---
title: Namngivna intervall
type: docs
weight: 40
url: /sv/java/named-ranges/
---

{{% alert color="primary" %}} 

Vanligtvis används kolumn- och radetiketter för att hänvisa till enskilda celler. Det är möjligt att skapa beskrivande namn för att representera celler, cellintervall, formler eller konstanta värden. Ordet **namn** kan hänvisa till en sträng av tecken som representerar en cell, ett cellintervall, en formel eller ett konstant värde. Genom att tilldela ett namn till ett intervall betyder det att det intervallet kan hänvisas till med sitt namn. Använd lättförståeliga namn, såsom Produkter, för att hänvisa till svårförståeliga intervall, såsom Försäljning!C20:C30. Etiketter kan användas i formler som hänvisar till data på samma kalkylblad; om du vill representera ett intervall på ett annat kalkylblad kan du använda ett namn. *Namngivna intervall är bland de mest kraftfulla funktionerna i Microsoft Excel, särskilt när de används som källintervall för listkontroller, pivottabeller, diagram osv.*

{{% /alert %}} 
## **Skapa en namngiven omfattning**
### **Använda Microsoft Excel**
Följande steg beskriver hur man namnger en cell eller ett cellintervall med Microsoft Excel. Denna metod gäller för Microsoft Office Excel 2003, Microsoft Excel 97, 2000 och 2002.

1. Välj cellen, cellområdet som du vill namnge.
1. Klicka på Namn ruta längst till vänster om formelfältet.
1. Skriv namnet för cellerna.
1. Tryck på ENTER.

{{% alert color="primary" %}} 

Du kan inte namnge en cell medan du ändrar innehållet i cellen.

{{% /alert %}} 
### **Använda Aspose.Cells**
Här använder vi Aspose.Cells API för att utföra uppgiften.

Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samling.

Det är möjligt att skapa ett namngivet intervall genom att anropa den överbelastade [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\))-metoden i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen. En vanlig version av [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\))-metoden tar följande parametrar:

- Namn på övre vänstra cell, namnet på den översta vänstra cellen i intervallet.
- Namnet på den nedre högra cellen, namnet på den längst ner till höger i området.

När [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\))-metoden anropas returnerar den det nyligen skapade namngivna intervallet som en instans av [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)-klassen.

Följande exempel visar hur man skapar ett namngivet intervall av celler som sträcker sig över B4:G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Åtkomst till alla namngivna intervall i ett kalkylblad**
Anropa [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\))-metoden i [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) för att få alla namngivna intervall i ett kalkylblad. [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\))-metoden returnerar en matris med alla namngivna intervall i [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

Följande exempel visar hur man åtkommer alla namngivna områden i en arbetsbok.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Åtkomst till ett specifikt namngivet område**
Anropa [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)s- samlingens [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\))-metod för att få ett specifierat intervall efter namn. En vanlig [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\))-metod tar namnet på namngivet intervallet och returnerar det specifierade namngivna intervallet som en instans av [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)-klassen.

Följande exempel visar hur man får åtkomst till ett specifierat intervall efter dess namn.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Identifiera celler i ett namngivet intervall**
Med Aspose.Cells kan du infoga data i de enskilda cellerna i ett intervall. Anta att du har ett namngivet intervall av celler, d.v.s., A1:C4. Så skulle matrisen göra 4 * 3 = 12 celler och de enskilda intervallscellerna är ordnade sekventiellt. Aspose.Cells tillhandahåller dig några användbara egenskaper i [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)-klassen för att få åtkomst till de enskilda cellerna i intervallet. Du kan använda följande metoder för att identifiera cellerna i intervallet:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) returnerar index för den första raden i det namngivna intervallet.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) returnerar index för den första kolumnen i det namngivna intervallet.

Följande exempel visar hur man anger några värden i cellerna i ett specificerat område.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Ange data i cellerna i det namngivna området**
Med Aspose.Cells kan du infoga data i de enskilda cellerna i ett intervall. Anta att du har ett namngivet intervall av celler d.v.s., H1:J4. Så skulle matrisen göra 4 * 3 = 12 celler och de enskilda intervallscellerna är ordnade sekventiellt. Aspose.Cells tillhandahåller dig några användbara egenskaper i [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)-klassen för att få åtkomst till de enskilda cellerna i intervallet. Du kan använda följande egenskaper för att identifiera cellerna i intervallet:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) returnerar index för den första raden i det namngivna intervallet.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) returnerar index för den första kolumnen i det namngivna intervallet.

Följande exempel visar hur man anger några värden i cellerna i ett specificerat område.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Formatera intervall... Ställa in bakgrundsfärg och fontattribut för ett namngivet intervall**
För att applicera formatering, definiera en [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-objekt för att ange stilinställningar och applicera det på [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)-objektet.

Följande exempel visar hur du ställer in en fyllningsfärg (skuggfärg) med teckensnittsinställningar för ett intervall.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Formatintervall...Lägga till ramar till ett namngivet intervall**
Det är möjligt att lägga till ramar till en cellgrupp istället för bara en enskild cell.  [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) objektet tillhandahåller en [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) metod som tar följande parametrar för att lägga till en ram till cellgruppen:

- borderStyle: ramtypen, vald från [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)  uppräkning.
- borderColor: linjens färg för ramen, vald från [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) uppräkning.

Följande exempel visar hur du ställer in en konturram till ett område.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


Följande utmatning skulle genereras efter att ovanstående kod har körts: 

![todo:image_alt_text](named-ranges_1.png)
#### **Tillämpa stil på celler i ett intervall**
Ibland vill du skapa och tillämpa en stil på cellerna i ett [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range). För detta kan du iterera över cellerna i intervallet och använda [Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) metoden för att tillämpa stilen på cellen.

Följande exempel visar hur du tillämpar stilar på celler i ett intervall.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Ta bort ett namngivet område**
Aspose.Cells tillhandahåller [NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\)) metoden för att ta bort namnet på intervallen. För att rensa innehållet i intervallet, använd [Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) metoden.
Följande exempel visar hur du tar bort ett namngivet intervall med dess innehåll.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
