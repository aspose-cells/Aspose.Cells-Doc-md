---
title: Visa och Dölja Kalkylblad och Flikar
type: docs
weight: 10
url: /sv/net/show-and-hide-worksheets-and-tabs/
description: Den här artikeln ger kodexempel för att använda C# API eller .NET Biblioteket för att programmatiskt visa och dölja ett Excel kalkylblad. Dessutom, hur man visar och döljer Excel kalkylbladets flikar.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter användaren att visa och dölja element i en arbetsbok inklusive kalkylblad och flikar.

{{% /alert %}}

## **Visa och dölj ett arbetsblad**

En Excel-fil kan ha ett eller flera arbetsblad. När vi skapar en Excel-fil lägger vi till arbetsblad i Excel-filen där vi arbetar. Varje arbetsblad i en Excel-fil är oberoende från det andra arbetsbladet genom att ha sina egna data och formateringsinställningar osv. Ibland kan utvecklare behöva dölja några arbetsblad och göra andra synliga i Excel-filen för deras eget intresse. Så, **Aspose.Cells** låter utvecklare kontrollera synligheten av arbetsbladen i deras Excel-filer.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som tillåter åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att kontrollera ett kalkylblads synlighet, använd klassen [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) egenskap. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) är en boolesk egenskap, vilket innebär att den bara kan lagra **true** eller **false** värden.

### **Göra ett arbetsblad synligt**

Gör ett kalkylblad synligt genom att ställa in klassens [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) egenskap [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) till **true**

### **Dölja ett arbetsblad**

Dölj ett kalkylblad genom att ställa in klassens [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) egenskap [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) till **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Visa och dölj flikar**

Om du tittar noga längst ner i en Microsoft Excel-fil, kommer du att se ett antal kontroller. Dessa inkluderar:

- Arkflikar.
- Flikbläddringsknappar.

Arkflikar representerar arbetsbladen i Excel-filen. Klicka på vilken flik som helst för att växla till det arbetsbladet. Ju fler arbetsblad i arbetsboken, desto fler arkflikar finns det. Om Excel-filen har ett bra antal arbetsblad behöver du knappar för att navigera genom dem. Så tillhandahåller Microsoft Excel flikbläddringsknappar för att bläddra igenom arkflikarna.

Genom att använda Aspose.Cells kan utvecklare kontrollera synligheten av arkflikar och flikbläddringsknappar i Excel-filer.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen ger ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten av flikar i en Excel-fil kan utvecklare använda [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassens [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)-egenskap. [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) är en boolesk egenskap, vilket innebär att den endast kan lagra ett **true** eller **false** värde.

### **Göra flikar synliga**

Gör flikar synliga med [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassens [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)-egenskap till **true**.

### **Gömma flikar**

Dölj flikar i en Excel-fil genom att ställa in [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassens [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)-egenskap till false.

Här är ett komplett exempel som öppnar en Excel-fil (book1.xls), döljer dess flikar och sparar den modifierade filen som output.xls. Efter att kodexekveringen har utförts kommer du att se att arbetsbokens flikar är dolda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Styra fliken Bredd**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
