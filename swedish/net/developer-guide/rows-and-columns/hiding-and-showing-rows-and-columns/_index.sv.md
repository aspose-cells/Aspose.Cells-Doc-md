---
title: Dölja och visa rader och kolumner
type: docs
weight: 60
url: /sv/net/hiding-and-showing-rows-and-columns/
---
{{% alert color="primary" %}}

Ibland är det vettigt att dölja vissa rader eller kolumner i ett kalkylblad och visa dem senare. Microsoft Excel tillhandahåller den här funktionen och det gör Aspose.Cells också.

{{% /alert %}}

## **Kontrollera synligheten för rader och kolumner**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) som låter utvecklare komma åt varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling som representerar alla celler i kalkylbladet. De[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

### **Döljer rader och kolumner**

 Utvecklare kan dölja en rad eller kolumn genom att anropa[**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) och[**Dölj kolumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) metoder för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)insamling respektive. Båda metoderna tar rad- och kolumnindex som en parameter för att dölja den specifika raden eller kolumnen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}}

### **Visar rader och kolumner**

 Utvecklare kan visa alla dolda rader eller kolumner genom att anropa[**Visa rad**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) och[**Ta fram kolumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) metoder för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)insamling respektive. Båda metoderna tar två parametrar:

- **Rad- eller kolumnindex** - indexet för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden som tilldelats raden eller kolumnen efter att ha visat sig.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

När du gör en dold kolumn synlig, om du behöver återställa den till tidigare tilldelad bredd eller till dess ursprungliga bredd, vänligen visa kolumnen med en negativ bredd. Till exempel: kalkylblad.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Dölja flera rader och kolumner**

 Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa[**Göm rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) och[**Dölj kolumner**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) metoder för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)insamling respektive. Båda metoderna tar startraden eller kolumnindexet och antalet rader eller kolumner som ska döljas som parametrar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

 Det är också möjligt att använda[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) klass'[**Visa rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) och[**Visa kolumner**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)metoder för att göra flera rader och kolumner synliga.

{{% /alert %}}
