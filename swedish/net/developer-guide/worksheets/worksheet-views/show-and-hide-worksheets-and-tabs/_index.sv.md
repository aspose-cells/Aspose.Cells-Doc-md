---
title: Visa och dölj arbetsblad och flikar
type: docs
weight: 10
url: /sv/net/show-and-hide-worksheets-and-tabs/
description: Den här artikeln innehåller exempelkod för att använda biblioteket C# API eller .NET för att programmatiskt visa och dölja ett Excel-kalkylblad. Dessutom, hur du visar och döljer Excel-arbetsboksflikar.
---
{{% alert color="primary" %}}

Aspose.Cells låter användaren visa och dölja delar av en arbetsbok inklusive kalkylblad och flikar.

{{% /alert %}}

## **Visa och dölj ett arbetsblad**

 En Excel-fil kan ha ett eller flera kalkylblad. När vi skapar en Excel-fil lägger vi till kalkylblad till Excel-filen som vi arbetar i. Varje kalkylblad i en Excel-fil är oberoende av det andra kalkylbladet genom att ha sina egna data och formateringsinställningar etc. Ibland kan utvecklare behöva göra några kalkylblad dolda och andra synliga i Excel-filen för sitt eget intresse. Så,**Aspose.Cells** låter utvecklare kontrollera synligheten för kalkylbladen i sina Excel-filer.

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i Excel-filen.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att kontrollera ett kalkylblads synlighet, använd[**Är synlig**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) egendom av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass.[**Är synlig**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) är en boolesk egenskap, vilket betyder att den bara kan lagra en**Sann** eller**falsk** värde.

### **Göra ett arbetsblad synligt**

 Gör ett kalkylblad synligt genom att ställa in[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass'[**Är synlig**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) egendom till**Sann**

### **Dölja ett arbetsblad**

Dölj ett kalkylblad genom att ställa in[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass'[**Är synlig**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) egendom till**falsk**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Visa och dölj flikar**

Om du tittar noga på botten av en Microsoft Excel-fil kommer du att se ett antal kontroller. Dessa inkluderar:

- Bladflikar.
- Tabbrullningsknappar.

Bladflikar representerar kalkylbladen i Excel-filen. Klicka på valfri flik för att växla till det kalkylbladet. Ju fler kalkylblad i arbetsboken, desto fler flikar finns det. Om Excel-filen har ett stort antal kalkylblad behöver du knappar för att navigera genom dem. Så, Microsoft Excel tillhandahåller flikrullningsknappar för att rulla igenom arkflikarna.

Med hjälp av Aspose.Cells kan utvecklare styra synligheten för arkflikar och flikars rullningsknappar i Excel-filer.

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten för flikar i en Excel-fil kan utvecklare använda[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) fast egendom.[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) är en boolesk egenskap, vilket betyder att den bara kan lagra en**Sann** eller**falsk** värde.

### **Göra flikar synliga**

 Gör flikarna synliga med[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) egendom till**Sann**.

### **Döljer flikar**

 Dölj flikar i en Excel-fil genom att ställa in[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)egendom till falsk.

Nedan är ett komplett exempel som öppnar en Excel-fil (book1.xls), gömmer dess flikar och sparar den ändrade filen som output.xls. Efter kodexekveringen kommer du att se att flikarna i arbetsboken är dolda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Styra flikfältets bredd**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
