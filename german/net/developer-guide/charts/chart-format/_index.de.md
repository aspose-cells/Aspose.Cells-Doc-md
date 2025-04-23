---
title: Diagrammdarstellung einstellen
description: Erfahren Sie, wie Sie das Erscheinungsbild von Diagrammen in Aspose.Cells for .NET konfigurieren können. Unser Leitfaden zeigt Ihnen, wie Sie Diagrammlayouts, Farben, Schriftarten und Effekte ändern können, um den gewünschten visuellen Stil zu erreichen und Ihre Arbeitsblätter zu verbessern.
keywords: Aspose.Cells for .NET, Charting, Diagrammdarstellung, Layouts, Farben, Schriftarten, Effekte, Arbeitsblätter.
linktitle: Diagrammformat
type: docs
weight: 20
url: /de/net/setting-chart-appearance/
---

## **Diagrammaussehen festlegen**
In How to Create a Chart haben wir eine kurze Einführung in die Arten von Diagrammen und Diagrammobjekten gegeben, die von Aspose.Cells angeboten werden, und beschrieben, wie man eines erstellt. In diesem Artikel wird erläutert, wie das Erscheinungsbild von Diagrammen durch Festlegen ihrer Eigenschaften angepasst werden kann:

- Festlegen des Diagrammbereichs.
- Festlegen von Diagrammlinien.
- Anwenden von Designs.
- Titel für Diagramme und Achsen festlegen.
- Arbeiten mit Gitterlinien.
### **Diagrammbereich einstellen**
Es gibt verschiedene Arten von Bereichen in einem Diagramm und Aspose.Cells bietet die Flexibilität, das Erscheinungsbild jedes Bereichs zu ändern. Entwickler können verschiedene Formatierungseinstellungen auf einen Bereich anwenden, indem sie seine Vordergrundfarbe, Hintergrundfarbe und Füllformat usw. ändern.

Im untenstehenden Beispiel haben wir verschiedene Formatierungseinstellungen auf verschiedene Arten von Bereichen eines Diagramms angewendet. Diese Bereiche umfassen:

- Plot-Bereich
- Diagrammbereich
- SeriesCollection Bereich
- Fläche eines einzelnen Punktes in einer SeriesCollection

Der folgende Codeschnipsel zeigt, wie der Diagrammbereich festgelegt wird.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **Einstellen von Diagramm Linien**
Entwickler können auch verschiedene Arten von Stilen auf die Linien oder Datenmarkierungen der [SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) anwenden. Der folgende Codeschnipsel zeigt, wie Diagrammlinien mit der Aspose.Cells-API festgelegt werden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Anwendung von Microsoft Excel 2007/2010-Themen auf Diagramme**
Entwickler können verschiedene Microsoft Excel-Themen/Farben auf [SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) oder andere Diagrammobjekte anwenden, wie im folgenden Beispiel gezeigt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **Einstellen der Titel von Diagrammen oder Achsen**
Sie können Microsoft Excel verwenden, um die Titel eines Diagramms und seiner Achsen in einer WYSIWYG-Umgebung einzustellen. Aspose.Cells ermöglicht es Entwicklern auch, die Titel eines Diagramms und seiner Achsen zur Laufzeit festzulegen. Alle Diagramme und ihre Achsen enthalten eine [Titel](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title) Eigenschaft, die in einem Beispiel unten wie folgt verwendet werden kann.

Der folgende Codeausschnitt zeigt, wie Titel für Diagramme und Achsen festgelegt werden können.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **Arbeiten mit Haupt-Gitterlinien**
Es ist möglich, das Aussehen der Haupt-Gitterlinien anzupassen. Gitterlinien ausblenden oder anzeigen, oder ihre Farbe und andere Einstellungen definieren. Nachfolgend zeigen wir, wie die Gitterlinien ausgeblendet und wie ihre Farbe geändert wird.
#### **Ausblenden von Haupt-Gitterlinien**
Entwickler können die Sichtbarkeit der Haupt-Gitterlinien steuern, indem sie die [IsVisible](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible)-Eigenschaft des [Line](https://reference.aspose.com/cells/net/aspose.cells.drawing/line)-Objekts auf **true** oder **false** setzen.

Der folgende Codeschnipsel zeigt, wie Haupt-Gitterlinien verborgen werden. Nach dem Ausblenden der Haupt-Gitterlinien wird dem Arbeitsblatt ein Säulendiagramm hinzugefügt, das keine Gitterlinien hat.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **Ändern der Einstellungen für Haupt-Gitterlinien**
Entwickler können nicht nur die Sichtbarkeit der Haupt-Gitterlinien, sondern auch andere Eigenschaften wie deren Farbe usw. steuern.

Der folgende Codeschnipsel zeigt, wie die Farbe der Haupt-Gitterlinien geändert wird. Nachdem die Farbe der Haupt-Gitterlinien festgelegt wurde, wird dem Arbeitsblatt ein Säulendiagramm mit geänderten Gitterlinien hinzugefügt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **Erweiterte Themen**
- [Setzen des Werteformatcodes der Diagrammserie](/cells/de/net/set-the-values-format-code-of-chart-series/)
- [Bild als Hintergrundfüllung im Diagramm festlegen](/cells/de/net/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="csharp" >}}
