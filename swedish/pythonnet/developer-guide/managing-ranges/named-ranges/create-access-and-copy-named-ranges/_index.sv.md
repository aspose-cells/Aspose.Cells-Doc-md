---
title: Skapa åtkomst och kopiera namngivna intervall
type: docs
weight: 200
url: /sv/python-net/create-access-and-copy-named-ranges/
description: Den här artikeln visar hur man skapar åtkomst och kopierar namngivna intervall med hjälp av Aspose.Cells för Python via .NET API.
keywords: Python Exceldatabibliotek, Skapa åtkomst och kopiera namngivna intervall i Python, Skapa namngivna intervall i Python, Kopiera namngivna intervall i Python, Få åtkomst till alla namngivna intervall i en kalkyl.
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

## **Arbeta med namngivet område med Aspose.Cells for Python Excel Library**

Här använder vi Aspose.Cells for Python via .NET API för att utföra uppgiften.
Aspose.Cells for Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samling.

### **Skapa namngivet område**

Det är möjligt att skapa ett namngivet område genom att anropa den överlagrade metoden [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) i samlingen [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). En vanlig version av [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str)-metoden tar följande parametrar:

- Namn på övre vänstra cell, namnet på den översta vänstra cellen i området.
- Namnet på den nedre högra cellen, namnet på den längst ner till höger i området.

När metoden [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) kallas returneras det nysskapade området som en instans av klassen [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). Använd detta [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-objekt för att konfigurera det namngivna området. Till exempel, ställ in namnet på området med hjälp av egenskapen [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/range/name). Följande exempel visar hur man skapar ett namngivet område av celler som sträcker sig över B4:G14.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CreateNamedRangeofCells-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-InputDataInCellsInRange-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IdentifyCellsinNamedRange-1.py" >}}

### **Åtkomst till namngivna områden**

#### **Åtkomst till ett specifikt namngivet område**

Anropa [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-kollektionens [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str)-metod för att få ett område med det angivna namnet. En typisk [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str)-metod tar namnet på det namngivna området och returnerar det angivna namngivna området som en instans av klassen [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). Följande exempel visar hur man åtkommer ett angivet område med dess namn.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessSpecificNamedRange-1.py" >}}

#### **Åtkomst till alla namngivna områden i ett kalkylblad**

Anropa [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-kollektionens [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#)-metod för att få alla namngivna områden i ett kalkylblad. [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#)-metoden returnerar en array av alla namngivna områden i [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)-kollektionen.

Följande exempel visar hur man åtkommer alla namngivna områden i en arbetsbok.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessAllNamedRanges-1.py" >}}

### **Kopiera namngivna områden**

Aspose.Cells för Python via .NET tillhandahåller [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range)-metoden för att kopiera en räcka med celler med formatering till ett annat område.

Följande exempel visar hur man kopierar en källräcka med celler till ett annat namngivet område.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CopyNamedRanges-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
