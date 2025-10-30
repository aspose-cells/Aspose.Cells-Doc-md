---
title: Diagrammgestaltung mit Golang via C++ festlegen
linktitle: Diagrammformat
description: Lernen Sie, wie man das Erscheinungsbild von Diagrammen in Aspose.Cells for C++ konfiguriert. Unser Leitfaden zeigt, wie man Diagrammlayouts, Farben, Schriftarten und Effekte anpasst, um den gewünschten visuellen Stil zu erzielen und Ihre Arbeitsblätter zu verbessern.
keywords: Aspose.Cells for C++, Diagramm, Diagrammgestaltung, Layouts, Farben, Schriftarten, Effekte, Arbeitsblätter.
type: docs
weight: 20
url: /de/go-cpp/setting-chart-appearance/
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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat.go" >}}
### **Einstellen von Diagramm Linien**
Entwickler können auch verschiedene Arten von Stilen auf die Linien oder Datenmarkierungen der [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/) anwenden. Das folgende Codebeispiel zeigt, wie man Diagrammlinien mit der Aspose.Cells API festlegt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-1.go" >}}
### **Anwendung von Microsoft Excel 2007/2010-Themen auf Diagramme**
Entwickler können unterschiedliche Microsoft Excel-Themen/Farben auf [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/) oder andere Diagrammobjekte anwenden, wie im Beispiel unten gezeigt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-2.go" >}}
### **Einstellen der Titel von Diagrammen oder Achsen**
Sie können Microsoft Excel verwenden, um die Titel eines Diagramms und seiner Achsen in einer WYSIWYG-Umgebung festzulegen. Aspose.Cells ermöglicht es Entwicklern auch, die Titel eines Diagramms und seiner Achsen zur Laufzeit festzulegen. Alle Diagramme und deren Achsen enthalten eine [Title](https://reference.aspose.com/cells/go-cpp/title/) Eigenschaft, mit der ihre Titel festgelegt werden können, wie in einem Beispiel unten gezeigt.

Der folgende Codeausschnitt zeigt, wie Titel für Diagramme und Achsen festgelegt werden können.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-3.go" >}}
### **Arbeiten mit Haupt-Gitterlinien**
Es ist möglich, das Aussehen der Haupt-Gitterlinien anzupassen. Gitterlinien ausblenden oder anzeigen, oder ihre Farbe und andere Einstellungen definieren. Nachfolgend zeigen wir, wie die Gitterlinien ausgeblendet und wie ihre Farbe geändert wird.

#### **Ausblenden von Haupt-Gitterlinien**
Entwickler können die Sichtbarkeit der Hauptgitterlinien steuern, indem sie die [IsVisible](https://reference.aspose.com/cells/go-cpp/line/isvisible/) Eigenschaft des [Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) Objekts auf **true** oder **false** setzen.

Der folgende Codeschnipsel zeigt, wie Haupt-Gitterlinien verborgen werden. Nach dem Ausblenden der Haupt-Gitterlinien wird dem Arbeitsblatt ein Säulendiagramm hinzugefügt, das keine Gitterlinien hat.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-4.go" >}}
#### **Ändern der Einstellungen für Haupt-Gitterlinien**
Entwickler können nicht nur die Sichtbarkeit der Haupt-Gitterlinien, sondern auch andere Eigenschaften wie deren Farbe usw. steuern.

Der folgende Codeschnipsel zeigt, wie die Farbe der Haupt-Gitterlinien geändert wird. Nachdem die Farbe der Haupt-Gitterlinien festgelegt wurde, wird dem Arbeitsblatt ein Säulendiagramm mit geänderten Gitterlinien hinzugefügt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-5.go" >}}
## **Erweiterte Themen**
- [Setzen des Werteformatcodes der Diagrammserie](/cells/de/cpp/set-the-values-format-code-of-chart-series/)
- [Bild als Hintergrundfüllung im Diagramm festlegen](/cells/de/cpp/set-picture-as-background-fill-in-the-chart/)
