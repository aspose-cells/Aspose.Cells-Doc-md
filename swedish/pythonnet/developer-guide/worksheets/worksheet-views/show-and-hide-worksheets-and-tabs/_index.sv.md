---
title: Visa och Dölja Kalkylblad och Flikar
type: docs
weight: 10
url: /sv/python-net/show-and-hide-worksheets-and-tabs/
description: Denna artikel ger exempel på kod för att använda Aspose.Cells för Python via .NET API för att programmatiskt visa och dölja en Excel arbetsbok. Dessutom hur man visar och döljer flikarna i Excel arbetsboken.
keywords: Python Excel biblioteket, Python Visa och Dölj ett arbetsblad, Python Visa och Dölj flikar, Python Kontrollera flikens bredd.
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET tillåter användaren att visa och dölja element i en arbetsbok inklusive arbetsblad och flikar.

{{% /alert %}}

## **Visa och dölj ett arbetsblad**

Ett Excel-f12 kan ha ett eller flera arbetsblad. När vi skapar en Excel-fil lägger vi till arbetsblad i filen som vi arbetar i. Varje arbetsblad i en Excel-fil är oberoende av de andra genom att ha sina egna data och formateringsinställningar etc. Ibland kan utvecklare behöva göra några arbetsblad dolda medan andra är synliga i Excel-filen för deras eget intresse. Så, **Aspose.Cells för Python via .NET** gör det möjligt för utvecklare att kontrollera synligheten av arbetsbladen i deras Excel-filer.

Aspose.Cells för Python via .NET ger en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-samling som gör det möjligt att få tillgång till varje arbetsblad i Excel-filen.

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

Med Aspose.Cells för Python via .NET kan utvecklare kontrollera synligheten av bladflikar och flikskrollknappar i Excel-filer.

Aspose.Cells för Python via .NET ger en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen ger ett brett spektrum av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten av flikar i en Excel-fil, använd [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassens [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)-egenskap. [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) är en Boolean-egenskap, vilket innebär att den endast kan lagra ett **true** eller **false** värde.

### **Göra flikar synliga**

Gör flikar synliga med [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassens [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)-egenskap till **true**.

### **Gömma flikar**

Dölj flikar i en Excel-fil genom att ställa in [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassens [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs)-egenskap till false.

Här är ett komplett exempel som öppnar en Excel-fil (book1.xls), döljer dess flikar och sparar den modifierade filen som output.xls. Efter att kodexekveringen har utförts kommer du att se att arbetsbokens flikar är dolda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Styra fliken Bredd**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
