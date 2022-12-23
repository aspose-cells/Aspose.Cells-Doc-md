---
title: Visa och dölj rader Kolumner och rullningslister
type: docs
weight: 20
url: /sv/net/show-and-hide-rows-columns-and-scroll-bars/
description: Den här artikeln visar hur du programmatiskt visar och döljer rader och kolumner i Excel-kalkylblad med språket C# och .NET API eller bibliotek. Synligheten för rullningslister kan justeras och flera rader och kolumner kan döljas.
---
{{% alert color="primary" %}}

Aspose.Cells tillhandahåller sätt att kontrollera synligheten för rader, kolumner och rullningslister i ett kalkylblad.

{{% /alert %}}

## **Visa och dölj rader och kolumner**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som låter utvecklare komma åt varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling som representerar alla celler i kalkylbladet. De[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

### **Visa rader och kolumner**

 Utvecklare kan visa alla dolda rader eller kolumner genom att anropa[**Visa rad**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) och[**Ta fram kolumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) metoder för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)insamling respektive. Båda metoderna tar två parametrar:

- **Rad- eller kolumnindex** - indexet för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden som tilldelats raden eller kolumnen efter att ha visat sig.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

När du gör en dold kolumn synlig, om du behöver återställa den till tidigare tilldelad bredd eller till dess ursprungliga bredd, vänligen visa kolumnen med en negativ bredd. Till exempel: kalkylblad.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Göm rader och kolumner**

 Utvecklare kan dölja en rad eller kolumn genom att anropa[**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) och[**Dölj kolumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) metoder för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)insamling respektive. Båda metoderna tar rad- och kolumnindex som en parameter för att dölja den specifika raden eller kolumnen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}}

### **Göm flera rader och kolumner**

 Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa[**Göm rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) och[**Dölj kolumner**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) metoder för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)insamling respektive. Båda metoderna tar startraden eller kolumnindexet och antalet rader eller kolumner som ska döljas som parametrar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Visa och dölj rullningslister**

Rullningslister används för att navigera i innehållet i alla filer. Normalt finns det två typer av rullningslister:

- Vertikala rullningslister
- Horisontella rullningslister

Microsoft Excel tillhandahåller även horisontella och vertikala rullningslister så att användare kan rulla igenom kalkylbladets innehåll. Med hjälp av Aspose.Cells kan utvecklare kontrollera synligheten för båda typerna av rullningslister i Excel-filer.

### **Kontrollera synligheten för rullningslister**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten för rullningslister använder du[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) och[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) egenskaper.[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) och[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) är booleska egenskaper, vilket innebär att dessa egenskaper endast kan lagras**Sann** eller**falsk** värden.

#### **Göra rullningslister synliga**

 Gör rullningslister synliga genom att ställa in[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) eller[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) egendom till**Sann**.

#### **Döljer rullningslister**

 Dölj rullningslister genom att ställa in[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) eller[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) egendom till**falsk**.

**Exempelkod**

Nedan finns en komplett kod som öppnar en Excel-fil, book1.xls, döljer båda rullningslisterna och sedan sparar den ändrade filen som output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
