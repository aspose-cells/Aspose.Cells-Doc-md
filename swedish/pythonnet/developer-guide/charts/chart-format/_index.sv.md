---
title: Inställning diagramutseende
description: Lär dig hur du konfigurerar utseendet på diagram i Aspose.Cells för Python via .NET. Vår guide visar hur du ändrar diagramlayouter, färger, teckensnitt och effekter för att uppnå önskad visuellt stil och förbättra dina arbetsblad.
keywords: Aspose.Cells för Python via .NET, diagramatik, diagramutseende, layouter, färger, teckensnitt, effekter, arbetsblad.
linktitle: Diagramformat
type: docs
weight: 20
url: /sv/python-net/setting-chart-appearance/
---

## **Ställa in diagramens utseende**
I Hur man Skapar ett Diagram gav vi en kort introduktion till de typer av diagram och diagramobjekt som erbjuds av Aspose.Cells för Python via .NET, och beskrev hur man skapar ett. Denna artikel diskuterar hur man anpassar diagrammens utseende genom att ställa in deras egenskaper:

- Inställning av diagramområdet.
- Inställning av diagramlinjer.
- Tillämpa teman.
- Ställa in titlar på diagram och axlar.
- Arbeta med rutnät.
### **Inställning av diagramområde**
Det finns olika typer av områden i ett diagram och Aspose.Cells för Python via .NET ger flexibilitet att modifiera utseendet för varje område. Utvecklare kan tillämpa olika formateringsinställningar på ett område genom att ändra dess förgrundsfärg, bakgrundsfärg och fyllningsformat etc.

I det givna exemplet har vi tillämpat olika formateringsinställningar på olika typer av områden i ett diagram. Dessa områden inkluderar:

- Plotområde
- Diagramområde
- Serieområdesamling
- Område för en enskild punkt i en serieområdesamling

Följande kodsnuttdemonstrerar hur man ställer in diagramområdet.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartArea-1.py" >}}

### **Inställning av diagramlinjer**
Utvecklare kan också tillämpa olika typer av stilar på linjer eller datapunkter i [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection). Följande kodsnutt visar hur man ställer in diagramlinjer med Aspose.Cells för Python via .NET API.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartLines-1.py" >}}

### **Tillämpning av Microsoft Excel 2007/2010 teman på diagram**
Utvecklare kan tillämpa olika Microsoft Excel-teman/färger på [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) eller andra diagramobjekt som visas nedan i exemplet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ApplyingThemes-1.py" >}}

### **Inställning av diagram- eller axeltitlar**
Du kan använda Microsoft Excel för att sätta titlar på ett diagram och dess axlar i en WYSIWYG-miljö. Aspose.Cells för Python via .NET tillåter också utvecklare att sätta titlar på ett diagram och dess axlar under körning. Alla diagram och deras axlar innehåller en [Chart.title](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/title) egenskap som kan användas för att sätta deras titlar som visas nedan i ett exempel.

Följande kodsnutt demonstrerar hur man ställer in titlar på diagram och axlar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingTitlesAxes-1.py" >}}

### **Arbeta med stora rutnätlinjer**
Det är möjligt att anpassa utseendet på stora rutnätlinjer. Dölj eller visa rutnätlinjer, eller definiera deras färg och andra inställningar. Nedan visar vi hur man döljer rutnätlinjer och hur man ändrar deras färg.

#### **Dölja stora rutnät**
Utvecklare kan kontrollera synligheten av huvudrutnätlinjer genom att ställa in egenskapen [is_visible](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line/is_visible) på [Line](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line) objekt till **true** eller **false**.

Följande kodsnutt demonstrerar hur man döljer stora rutnätlinjer. Efter att ha dolt de stora rutnätlinjerna kommer ett kolumn- diagram att läggas till i arbetsbladet utan rutnätlinjer.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-MajorGridlines-1.py" >}}

#### **Ändra inställningar för stora rutnät**
Utvecklare kan inte bara kontrollera synligheten för stora rutnät utan också andra egenskaper inklusive dess färg osv.

Följande kodsnutt demonstrerar hur man ändrar färgen på stora rutnätlinjer. Efter att ha ställt in färgen på stora rutnätlinjer kommer ett kolumn- diagram att läggas till i arbetsbladet med modifierade rutnätlinjer.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ChangingMajorGridlines-1.py" >}}

## **Fortsatta ämnen**
- [Ställ in värdenas formatkod för diagramserier](/cells/sv/python-net/set-the-values-format-code-of-chart-series/)
- [Ange bild som bakgrundsfyllning i diagrammet.](/cells/sv/python-net/set-picture-as-background-fill-in-the-chart/)
