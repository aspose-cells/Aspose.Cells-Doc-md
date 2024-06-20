---
title: Skapa åtkomst och kopiera namngivna intervall
type: docs
weight: 200
url: /sv/net/create-access-and-copy-named-ranges/
---

## **Introduktion**

Vanligtvis används kolumn- och radetiketter för att hänvisa till enskilda celler. Det är möjligt att skapa beskrivande namn för att representera celler, cellområden, formler eller konstanta värden. Ordet **namn** kan hänvisa till en sträng av tecken som representerar en cell, cellområde, formel eller konstant värde. Att tilldela ett namn till ett intervall innebär att det intervallet av celler kan hänvisas till med sitt namn. Använd lättförståeliga namn, såsom Produkter, för att hänvisa till svårförståeliga intervall, som Försäljning!C20:C30. Etiketter kan användas i formler som hänvisar till data på samma arbetsblad; om du vill representera ett intervall på ett annat arbetsblad kan du använda ett namn. *Namngivna intervall är bland de mest kraftfulla funktionerna i Microsoft Excel, särskilt när de används som källintervall för listkontroller, pivot-tabeller, diagram och så vidare.

## **Arbeta med namngivet intervall med Microsoft Excel**

### **Skapa namngivna intervall**

Följande steg beskriver hur man namnger en cell eller ett cellområde med **MS Excel**. Denna metod gäller för **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** och **2002**.

1. Välj cellen, cellområdet som du vill namnge.
1. Klicka på **Namnboxen** i vänstra änden av formelfältet.
1. Skriv namnet för cellerna.
1. Tryck på ENTER.

{{% alert color="primary" %}}

Du kan inte namnge en cell medan du ändrar innehållet i cellen.

{{% /alert %}}

## **Arbeta med namngivna områden med hjälp av Aspose.Cells**

Här använder vi Aspose.Cells API för att utföra uppgiften.
Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samling.

### **Skapa namngivet område**

Det är möjligt att skapa ett namngivet område genom att anropa den överlagrade metoden [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) i samlingen [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). En vanlig version av [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3)-metoden tar följande parametrar:

- Namn på övre vänstra cell, namnet på den översta vänstra cellen i området.
- Namnet på den nedre högra cellen, namnet på den längst ner till höger i området.

När metoden [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) kallas returneras det nysskapade området som en instans av klassen [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Använd detta [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)-objekt för att konfigurera det namngivna området. Till exempel, ställ in namnet på området med hjälp av egenskapen [**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name). Följande exempel visar hur man skapar ett namngivet område av celler som sträcker sig över B4:G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Ange data i cellerna i det namngivna området**

Du kan sätta in data i de individuella cellerna i ett område enligt mönstret

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Säg att du har ett namngivet område av celler som sträcker sig över A1:C4. Matrisen skapar 4 * 3 = 12 celler. De individuella områdets celler är arrangerade sekventiellt: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

Använd följande egenskaper för att identifiera cellerna i området:

- FirstRow returnerar indexet för den första raden i det namngivna området.
- FirstColumn returnerar indexet för den första kolumnen i det namngivna området.
- RowCount returnerar det totala antalet rader i det namngivna området.
- ColumnCount returnerar det totala antalet kolumner i det namngivna området.

Följande exempel visar hur man anger några värden i cellerna i ett specificerat område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **Identifiera celler i det namngivna området**

Du kan sätta in data i de individuella cellerna i ett område enligt mönstret:

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Om du har ett namngivet område som sträcker sig över A1:C4. Matrisen skapar 4 * 3 = 12 celler. De individuella områdets celler är arrangerade sekventiellt: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

Använd följande egenskaper för att identifiera cellerna i området:

- FirstRow returnerar indexet för den första raden i det namngivna området.
- FirstColumn returnerar indexet för den första kolumnen i det namngivna området.
- RowCount returnerar det totala antalet rader i det namngivna området.
- ColumnCount returnerar det totala antalet kolumner i det namngivna området.

Följande exempel visar hur man anger några värden i cellerna i ett specificerat område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Åtkomst till namngivna områden**

#### **Åtkomst till ett specifikt namngivet område**

Anropa [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)-kollektionens [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname)-metod för att få ett område med det angivna namnet. En typisk [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname)-metod tar namnet på det namngivna området och returnerar det angivna namngivna området som en instans av klassen [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Följande exempel visar hur man åtkommer ett angivet område med dess namn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Åtkomst till alla namngivna områden i ett kalkylblad**

Anropa [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)-kollektionens [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges)-metod för att få alla namngivna områden i ett kalkylblad. [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges)-metoden returnerar en array av alla namngivna områden i [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)-kollektionen.

Följande exempel visar hur man åtkommer alla namngivna områden i en arbetsbok.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Kopiera namngivna områden**

Aspose.Cells tillhandahåller [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index)-metoden för att kopiera ett cellområde med formatering till ett annat område.

Följande exempel visar hur man kopierar en källräcka med celler till ett annat namngivet område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
