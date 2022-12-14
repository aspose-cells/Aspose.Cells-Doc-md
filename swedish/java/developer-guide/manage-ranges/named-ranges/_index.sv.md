---
title: Namngivna Ranges
type: docs
weight: 40
url: /sv/java/named-ranges/
---
{{% alert color="primary" %}} 

Normalt används kolumn- och radetiketter för att referera till enskilda celler. Det är möjligt att skapa beskrivande namn för att representera celler, cellintervall, formler eller konstanta värden. Ordet**namn** kan hänvisa till en teckensträng som representerar en cell, cellintervall, formel eller ett konstant värde. Att tilldela ett namn till ett område innebär att det cellområdet kan refereras till med dess namn. Använd lättförståeliga namn, som Produkter, för att referera till svårförståeliga intervall, som Sales!C20:C30. Etiketter kan användas i formler som refererar till data på samma kalkylblad; om du vill representera ett intervall på ett annat kalkylblad kan du använda ett namn. *Namngivna intervall är bland de mest kraftfulla funktionerna i Microsoft Excel, särskilt när de används som källintervall för listkontroller, pivottabeller, diagram och så vidare.

{{% /alert %}} 
## **Skapa ett namngivet intervall**
### **Använder Microsoft Excel**
Följande steg beskriver hur du namnger en cell eller ett cellområde med hjälp av Microsoft Excel. Denna metod gäller för Microsoft Office Excel 2003, Microsoft Excel 97, 2000 och 2002.

1. Markera cellen, cellintervallet som du vill namnge.
1. Klicka på namnrutan till vänster i formelfältet.
1. Skriv namnet på cellerna.
1. Tryck enter.

{{% alert color="primary" %}} 

Du kan inte namnge en cell medan du ändrar innehållet i cellen.

{{% /alert %}} 
### **Använder Aspose.Cells**
Här använder vi Aspose.Cells API för att göra uppgiften.

 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling.

 Det är möjligt att skapa ett namngivet intervall genom att anropa den överbelastade[skapa Range](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) metod för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. En typisk version av[skapa Range](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) metod tar följande parametrar:

- Namnet på den övre vänstra cellen, namnet på den övre vänstra cellen i intervallet.
- Namnet på den nedre högra cellen, namnet på den nedre högra cellen i intervallet.

 När[skapa Range](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) anropas, returnerar den det nyskapade namngivna intervallet som en instans av[Räckvidd](https://reference.aspose.com/cells/java/com.aspose.cells/range) klass.

Följande exempel visar hur man skapar ett namngivet cellområde som sträcker sig över B4:G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Få åtkomst till alla namngivna intervall i ett kalkylblad**
 Ring[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) metod för[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) för att få alla namngivna intervall i ett kalkylblad. De[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) )-metoden returnerar en array med alla namngivna intervall i[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

Följande exempel visar hur du kommer åt alla namngivna intervall i en arbetsbok.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Få tillgång till ett specifikt namngivet intervall**
 Ring[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) samlingens[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) metod för att få ett specificerat intervall efter namn. En typisk[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) )-metoden tar namnet på det namngivna området och returnerar det angivna namngivna området som en instans av[Räckvidd](https://reference.aspose.com/cells/java/com.aspose.cells/range)klass.

Följande exempel visar hur man kommer åt ett angivet intervall med dess namn.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Identifiera Cells i ett namngivet intervall**
Med Aspose.Cells kan du infoga data i de individuella cellerna i ett intervall. Anta att du har ett namngivet intervall av cells.ie, A1:C4. Så matrisen skulle göra 4 * 3 = 12 celler och de individuella intervallcellerna ordnas sekventiellt. Aspose.Cells ger dig några användbara egenskaper för klassen [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) för att komma åt de individuella cellerna i intervallet. Du kan använda följande metoder för att identifiera cellerna i intervallet:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) returnerar indexet för den första raden i det namngivna intervallet.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)returnerar indexet för den första kolumnen i det namngivna intervallet.

Följande exempel visar hur man matar in vissa värden i cellerna i ett specificerat område.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Mata in data i Cells i det namngivna intervallet**
Med Aspose.Cells kan du infoga data i de individuella cellerna i ett intervall. Antag att du har ett namngivet cellområde, dvs. H1:J4. Så matrisen skulle göra 4 * 3 = 12 celler och de individuella intervallcellerna ordnas sekventiellt. Aspose.Cells ger dig några användbara egenskaper för klassen [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) för att komma åt de individuella cellerna i intervallet. Du kan använda följande egenskaper för att identifiera cellerna i intervallet:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)returnerar indexet för den första raden i det namngivna intervallet.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)returnerar indexet för den första kolumnen i det namngivna intervallet.

Följande exempel visar hur man matar in vissa värden i cellerna i ett specificerat område.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Formatera intervall...Ställa in bakgrundsfärg och teckensnittsattribut till ett namngivet intervall**
 För att tillämpa formatering, definiera en[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) objekt för att ange stilinställningar och tillämpa det på[Räckvidd](https://reference.aspose.com/cells/java/com.aspose.cells/range)objekt.

Följande exempel visar hur man ställer in enfärgad fyllnadsfärg (skuggfärg) med teckensnittsinställningar till ett intervall.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Formatera intervall...Lägga till gränser till ett namngivet intervall**
 Det är möjligt att lägga till gränser till ett cellintervall istället för bara en enda cell. De[Räckvidd](https://reference.aspose.com/cells/java/com.aspose.cells/range) objekt ger en[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)metod som använder följande parametrar för att lägga till en kantlinje till cellområdet:

-  borderStyle: typen av kant, vald från[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)uppräkning.
-  borderColor: linjefärgen på kanten, vald från[Färg](https://reference.aspose.com/cells/java/com.aspose.cells/Color) uppräkning.

Följande exempel visar hur man ställer in en konturgräns för ett område.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


 Följande utdata skulle genereras efter exekvering av ovanstående kod:

![todo:image_alt_text](named-ranges_1.png)
#### **Använd stil på celler i ett intervall**
Ibland vill du skapa tillämpa en stil på cellerna i en[Räckvidd](https://reference.aspose.com/cells/java/com.aspose.cells/range) . För detta kan du iterera över cellerna i intervallet och använda[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) metod för att tillämpa stilen på cellen.

Följande exempel visar hur man tillämpar stilar på celler i ett intervall.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Ta bort ett namngivet intervall**
 Aspose.Cells tillhandahåller[NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\) ) metod för att radera namnet på området. För att rensa innehållet i intervallet, använd[Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) metod.
Följande exempel visar hur man tar bort ett namngivet område med dess innehåll.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors
