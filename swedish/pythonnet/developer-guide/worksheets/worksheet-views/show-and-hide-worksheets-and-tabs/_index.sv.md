---
title: Visa och Dölja Kalkylblad och Flikar
type: docs
weight: 10
url: /sv/python-net/show-and-hide-worksheets-and-tabs/
description: Denna artikel ger provkod för att använda Aspose.Cells för Python via .NET API att programmatiskt visa och dölja ett Excel ark. Dessutom, hur man visar och döljer Excel arbetsbokflikar.
keywords: Python Excel Library, Python Visa och Dölj ett arbetsblad, Python Visa och Dölj Flikar, Python Kontrollera flikfältets bredd.
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET tillåter användaren att visa och dölja element i en arbetsbok inklusive arbetsblad och flikar.

{{% /alert %}}

## **Visa och dölj ett arbetsblad**

En Excel-fil kan ha ett eller flera kalkylblad. När vi skapar en Excel-fil, lägger vi till kalkylblad i Excel-filen där vi arbetar. Varje kalkylblad i en Excel-fil är oberoende från det andra kalkylbladet genom att ha sina egna data och formateringsinställningar etc. Ibland kan utvecklare behöva göra några kalkylblad dolda och andra synliga i Excel-filen för deras egen räkning. Så tillåter **Aspose.Cells för Python via .NET** utvecklare att kontrollera synligheten av kalkylbladen i deras Excel-filer.

Aspose.Cells för Python via .NET ger en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som tillåter åtkomst till varje arbetsblad i Excel-filen.

Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att kontrollera ett kalkylblads synlighet, använd klassen [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) egenskap. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) är en boolesk egenskap, vilket innebär att den bara kan lagra **true** eller **false** värden.

### **Göra ett arbetsblad synligt**

Gör ett kalkylblad synligt genom att ställa in klassens [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) egenskap [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) till **true**

### **Dölja ett arbetsblad**

Dölj ett kalkylblad genom att ställa in klassens [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) egenskap [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) till **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **Visa och dölj flikar**

Om du tittar noga längst ner i en Microsoft Excel-fil, kommer du att se ett antal kontroller. Dessa inkluderar:

- Arkflikar.
- Flikbläddringsknappar.

Arkflikar representerar arbetsbladen i Excel-filen. Klicka på vilken flik som helst för att växla till det arbetsbladet. Ju fler arbetsblad i arbetsboken, desto fler arkflikar finns det. Om Excel-filen har ett bra antal arbetsblad behöver du knappar för att navigera genom dem. Så tillhandahåller Microsoft Excel flikbläddringsknappar för att bläddra igenom arkflikarna.

Med Aspose.Cells för Python via .NET kan utvecklare kontrollera synligheten av flikflikar och flikrullningsknappar i Excel-filer.

Aspose.Cells for Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen erbjuder ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten av flikar i en Excel-fil kan utvecklare använda [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)-egenskapen för [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen. [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) är en boolesk egenskap vilket innebär att den endast kan lagra ett **true** eller **false** värde.

### **Göra flikar synliga**

Gör flikar synliga med [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassens [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)-egenskap till **true**.

### **Gömma flikar**

Dölj flikar i en Excel-fil genom att ställa in [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassens [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)-egenskap till false.

Här är ett komplett exempel som öppnar en Excel-fil (book1.xls), döljer dess flikar och sparar den modifierade filen som output.xls. Efter att kodexekveringen har utförts kommer du att se att arbetsbokens flikar är dolda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Styra fliken Bredd**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
