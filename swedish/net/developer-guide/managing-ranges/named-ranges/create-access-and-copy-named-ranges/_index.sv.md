---
title: Skapa åtkomst och kopiera namngivna intervall
type: docs
weight: 200
url: /sv/net/create-access-and-copy-named-ranges/
---
## **Introduktion**

 Normalt används kolumn- och radetiketter som refererar till enskilda celler. Det är möjligt att skapa beskrivande namn för att representera celler, cellintervall, formler eller konstanta värden. Ordet**namn**kan hänvisa till en teckensträng som representerar en cell, cellintervall, formel eller konstant värde. Att tilldela ett namn till ett område innebär att det cellområdet kan refereras till med dess namn. Använd lättförståeliga namn, som Produkter, för att referera till svårförståeliga intervall, som Sales!C20:C30. Etiketter kan användas i formler som refererar till data på samma kalkylblad; om du vill representera ett intervall på ett annat kalkylblad kan du använda ett namn. *Namngivna intervall är bland de mest kraftfulla funktionerna i Microsoft Excel, särskilt när de används som källintervall för listkontroller, pivottabeller, diagram och så vidare.

## **Arbeta med namngivna intervall med Microsoft Excel**

### **Skapa namngivna intervall**

 Följande steg beskriver hur man namnger en cell eller ett cellområde med hjälp av**MS Excel** . Denna metod gäller för**Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** och**2002**.

1. Markera cellen, cellintervallet som du vill namnge.
1.  Klicka på**Namnruta** till vänster i formelfältet.
1. Skriv namnet på cellerna.
1. Tryck enter.

{{% alert color="primary" %}}

Du kan inte namnge en cell medan du ändrar innehållet i cellen.

{{% /alert %}}

## **Arbeta med namngett område med Aspose.Cells**

Här använder vi Aspose.Cells API för att göra uppgiften.
 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling.

### **Skapa namngivna intervall**

 Det är möjligt att skapa ett namngivet intervall genom att anropa den överbelastade[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) metod för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling. En typisk version av[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) metoden tar följande parametrar:

- Namn på den övre vänstra cellen, namnet på den övre vänstra cellen i intervallet.
- Namnet på den nedre högra cellen, namnet på den nedre högra cellen i intervallet.

 När[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) metoden anropas, returnerar den det nyskapade intervallet som en instans av[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range) klass. Använd detta[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range) objekt för att konfigurera det namngivna området. Ange till exempel namnet på intervallet med hjälp av[**namn**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name) fast egendom. Följande exempel visar hur man skapar ett namngivet cellområde som sträcker sig över B4:G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Mata in data i Cells i det namngivna intervallet**

Du kan infoga data i de enskilda cellerna i ett intervall som följer mönstret

- **C#**: Område[rad,kolumn]
- **VB**: Range(rad, kolumn)

Säg att du har ett namngivet cellområde som sträcker sig över A1:C4. Matrisen gör 4 * 3 = 12 celler. De individuella intervallcellerna är ordnade sekventiellt: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

Använd följande egenskaper för att identifiera cellerna i intervallet:

- FirstRow returnerar indexet för den första raden i det namngivna intervallet.
- FirstColumn returnerar indexet för den första kolumnen i det namngivna intervallet.
- RowCount returnerar det totala antalet rader i det namngivna intervallet.
- ColumnCount returnerar det totala antalet kolumner i det namngivna intervallet.

Följande exempel visar hur man matar in vissa värden i cellerna i ett specificerat område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **Identifiera Cells i det namngivna intervallet**

Du kan infoga data i de individuella cellerna i ett intervall enligt mönstret:

- **C#**: Område[rad,kolumn]
- **VB**: Range(rad, kolumn)

Om du har ett namngivet område som sträcker sig över A1:C4. Matrisen gör 4 * 3 = 12 celler. De individuella intervallcellerna är ordnade sekventiellt: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

Använd följande egenskaper för att identifiera cellerna i intervallet:

- FirstRow returnerar indexet för den första raden i det namngivna intervallet.
- FirstColumn returnerar indexet för den första kolumnen i det namngivna intervallet.
- RowCount returnerar det totala antalet rader i det namngivna intervallet.
- ColumnCount returnerar det totala antalet kolumner i det namngivna intervallet.

Följande exempel visar hur man matar in vissa värden i cellerna i ett specificerat område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Få tillgång till namngivna intervall**

#### **Få tillgång till ett specifikt namngivet intervall**

 Ring[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) samlingens[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) metod för att få ett intervall med det angivna namnet. En typisk[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) metoden tar namnet på det namngivna området och returnerar det angivna namngivna området som en instans av[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range) klass. Följande exempel visar hur man kommer åt ett angivet intervall med dess namn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Få tillgång till alla namngivna intervall i ett kalkylblad**

 Ring[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) samlingens[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) metod för att få alla namngivna intervall i ett kalkylblad. De[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) metod returnerar en array med alla namnintervall i[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) samling.

Följande exempel visar hur du kommer åt alla namngivna intervall i en arbetsbok.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Kopiera namngivna intervall**

 Aspose.Cells tillhandahåller[**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) metod för att kopiera ett cellområde med formatering till ett annat område.

Följande exempel visar hur man kopierar ett källintervall med celler till ett annat namngivet intervall.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
