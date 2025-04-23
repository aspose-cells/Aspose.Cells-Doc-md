---
title: Diagrammdarstellung einstellen
description: Erfahren Sie, wie Sie das Aussehen von Diagrammen in Aspose.Cells für Python via .NET konfigurieren. Unser Leitfaden zeigt, wie Sie Diagrammlayouts, Farben, Schriftarten und Effekte ändern, um den gewünschten visuellen Stil zu erreichen und Ihre Tabellenblätter zu verbessern.
keywords: Aspose.Cells für Python via .NET, Diagramme, Diagrammansichten, Layouts, Farben, Schriftarten, Effekte, Tabellenblätter.
linktitle: Diagrammformat
type: docs
weight: 20
url: /de/python-net/setting-chart-appearance/
---

## **Diagrammaussehen festlegen**
Beim Erstellen eines Diagramms geben wir eine kurze Einführung in die Arten der von Aspose.Cells für Python via .NET angebotenen Diagramme und Diagrammobjekte und beschreiben, wie man eines erstellt. Dieser Artikel behandelt, wie man das Erscheinungsbild von Diagrammen anpasst, indem man ihre Eigenschaften festlegt:

- Festlegen des Diagrammbereichs.
- Festlegen von Diagrammlinien.
- Anwenden von Designs.
- Titel für Diagramme und Achsen festlegen.
- Arbeiten mit Gitterlinien.
### **Diagrammbereich einstellen**
Es gibt verschiedene Bereiche in einem Diagramm, und Aspose.Cells für Python via .NET bietet die Flexibilität, das Erscheinungsbild jedes Bereichs anzupassen. Entwickler können verschiedene Formatierungseinstellungen auf einen Bereich anwenden, indem sie seine Vordergrundfarbe, Hintergrundfarbe und Füllformat ändern.

Im untenstehenden Beispiel haben wir verschiedene Formatierungseinstellungen auf verschiedene Arten von Bereichen eines Diagramms angewendet. Diese Bereiche umfassen:

- Plot-Bereich
- Diagrammbereich
- SeriesCollection Bereich
- Fläche eines einzelnen Punktes in einer SeriesCollection

Der folgende Codeschnipsel zeigt, wie der Diagrammbereich festgelegt wird.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartArea-1.py" >}}

### **Einstellen von Diagramm Linien**
Entwickler können auch verschiedene Stile auf Linien oder Datenmarkierungen der [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) anwenden. Das folgende Codebeispiel zeigt, wie man Diagrammlinien mit Aspose.Cells für Python via .NET festlegt.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartLines-1.py" >}}

### **Anwendung von Microsoft Excel 2007/2010-Themen auf Diagramme**
Entwickler können verschiedene Microsoft Excel-Themen/Farben auf [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) oder andere Diagrammobjekte anwenden, wie im Beispiel gezeigt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ApplyingThemes-1.py" >}}

### **Einstellen der Titel von Diagrammen oder Achsen**
Sie können Microsoft Excel verwenden, um die Titel eines Diagramms und seiner Achsen in einer WYSIWYG-Umgebung festzulegen. Aspose.Cells für Python via .NET erlaubt Entwicklern auch, die Titel eines Diagramms und seiner Achsen zur Laufzeit festzulegen. Alle Diagramme und ihre Achsen enthalten eine [Chart.title](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/title)-Eigenschaft, mit der ihre Titel eingestellt werden können, wie im Beispiel gezeigt.

Der folgende Codeausschnitt zeigt, wie Titel für Diagramme und Achsen festgelegt werden können.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingTitlesAxes-1.py" >}}

### **Arbeiten mit Haupt-Gitterlinien**
Es ist möglich, das Aussehen der Haupt-Gitterlinien anzupassen. Gitterlinien ausblenden oder anzeigen, oder ihre Farbe und andere Einstellungen definieren. Nachfolgend zeigen wir, wie die Gitterlinien ausgeblendet und wie ihre Farbe geändert wird.

#### **Ausblenden von Haupt-Gitterlinien**
Entwickler können die Sichtbarkeit der Haupt-Gitterlinien steuern, indem sie die Eigenschaft [is_visible](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line/is_visible) des [Line](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line)-Objekts auf **true** oder **false** setzen.

Der folgende Codeschnipsel zeigt, wie Haupt-Gitterlinien verborgen werden. Nach dem Ausblenden der Haupt-Gitterlinien wird dem Arbeitsblatt ein Säulendiagramm hinzugefügt, das keine Gitterlinien hat.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-MajorGridlines-1.py" >}}

#### **Ändern der Einstellungen für Haupt-Gitterlinien**
Entwickler können nicht nur die Sichtbarkeit der Haupt-Gitterlinien, sondern auch andere Eigenschaften wie deren Farbe usw. steuern.

Der folgende Codeschnipsel zeigt, wie die Farbe der Haupt-Gitterlinien geändert wird. Nachdem die Farbe der Haupt-Gitterlinien festgelegt wurde, wird dem Arbeitsblatt ein Säulendiagramm mit geänderten Gitterlinien hinzugefügt.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ChangingMajorGridlines-1.py" >}}

## **Erweiterte Themen**
- [Setzen des Werteformatcodes der Diagrammserie](/cells/de/python-net/set-the-values-format-code-of-chart-series/)
- [Bild als Hintergrundfüllung im Diagramm festlegen](/cells/de/python-net/set-picture-as-background-fill-in-the-chart/)
