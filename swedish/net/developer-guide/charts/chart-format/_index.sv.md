---
title: Inställning diagramutseende
description: Lär dig hur du konfigurerar utseendet på diagram i Aspose.Cells for .NET. Vår guide kommer att visa dig hur du modifierar diagramlayout, färger, teckensnitt och effekter för att uppnå önskad visuell stil och förbättra dina arbetsblad.
keywords: Aspose.Cells for .NET, diagramskapande, diagramutseende, layout, färger, teckensnitt, effekter, arbetsblad.
linktitle: Diagramformat
type: docs
weight: 20
url: /sv/net/setting-chart-appearance/
---

## **Ställa in diagramens utseende**
I Hur man skapar ett diagram gav vi en kort introduktion till typerna av diagram och diagramobjekt som erbjuds av Aspose.Cells, och beskrev hur man skapar ett. Den här artikeln diskuterar hur man anpassar diagrammens utseende genom att ställa in deras egenskaper:

- Inställning av diagramområdet.
- Inställning av diagramlinjer.
- Tillämpa teman.
- Ställa in titlar på diagram och axlar.
- Arbeta med rutnät.
### **Inställning av diagramområde**
Det finns olika typer av områden i ett diagram och Aspose.Cells ger flexibilitet att modifiera utseendet på varje område. Utvecklare kan tillämpa olika formateringsinställningar på ett område genom att ändra dess förgrundsfärg, bakgrundsfärg och fyllning osv.

I det givna exemplet har vi tillämpat olika formateringsinställningar på olika typer av områden i ett diagram. Dessa områden inkluderar:

- Plotområde
- Diagramområde
- Serieområdesamling
- Område för en enskild punkt i en serieområdesamling

Följande kodsnuttdemonstrerar hur man ställer in diagramområdet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **Inställning av diagramlinjer**
Utvecklare kan också tillämpa olika typer av stilar på linjer eller datamarkörer för [Serieområdesamling](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). Följande kodsnutt visar hur man ställer in diagramlinjer med Aspose.Cells API.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Tillämpning av Microsoft Excel 2007/2010 teman på diagram**
Utvecklare kan tillämpa olika Microsoft Excel-teman/färger på [Serieområdesamling](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) eller andra diagramobjekt enligt exemplet nedan.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **Inställning av diagram- eller axeltitlar**
Du kan använda Microsoft Excel för att ställa in diagrammets titlar och dess axlar i en WYSIWYG-miljö. Aspose.Cells tillåter också utvecklare att ställa in diagrammets titlar och dess axlar vid körning. Alla diagram och deras axlar innehåller en [Title](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)-egenskap som kan användas för att ställa in deras titlar enligt exempel nedan.

Följande kodsnutt demonstrerar hur man ställer in titlar på diagram och axlar.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **Arbeta med stora rutnätlinjer**
Det är möjligt att anpassa utseendet på stora rutnätlinjer. Dölj eller visa rutnätlinjer, eller definiera deras färg och andra inställningar. Nedan visar vi hur man döljer rutnätlinjer och hur man ändrar deras färg.
#### **Dölja stora rutnät**
Utvecklare kan kontrollera synligheten av stora rutnätlinjer genom att ställa in [Är synligt](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible)-egenskapen för [Linje](https://reference.aspose.com/cells/net/aspose.cells.drawing/line)-objektet till **true** eller **false**.

Följande kodsnutt demonstrerar hur man döljer stora rutnätlinjer. Efter att ha dolt de stora rutnätlinjerna kommer ett kolumn- diagram att läggas till i arbetsbladet utan rutnätlinjer.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **Ändra inställningar för stora rutnät**
Utvecklare kan inte bara kontrollera synligheten för stora rutnät utan också andra egenskaper inklusive dess färg osv.

Följande kodsnutt demonstrerar hur man ändrar färgen på stora rutnätlinjer. Efter att ha ställt in färgen på stora rutnätlinjer kommer ett kolumn- diagram att läggas till i arbetsbladet med modifierade rutnätlinjer.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **Fortsatta ämnen**
- [Ställ in värdenas formatkod för diagramserier](/cells/sv/net/set-the-values-format-code-of-chart-series/)
- [Ange bild som bakgrundsfyllning i diagrammet.](/cells/sv/net/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="csharp" >}}
