---
title: Darstellung des Diagramms einstellen
linktitle: Diagrammformat
type: docs
weight: 20
url: /de/net/setting-chart-appearance/
---
## **Darstellung des Diagramms einstellen**
In So erstellen Sie ein Diagramm haben wir eine kurze Einführung in die Arten von Diagrammen und Diagrammobjekten gegeben, die von Aspose.Cells angeboten werden, und beschrieben, wie Sie eines erstellen. In diesem Artikel wird erläutert, wie Sie das Erscheinungsbild von Diagrammen anpassen, indem Sie ihre Eigenschaften festlegen:

- Einstellen des Diagrammbereichs.
- Diagrammlinien setzen.
- Themen anwenden.
- Titel für Diagramme und Achsen festlegen.
- Arbeiten mit Gitterlinien.
### **Diagrammbereich einstellen**
Es gibt verschiedene Arten von Bereichen in einem Diagramm und Aspose.Cells bietet die Flexibilität, das Erscheinungsbild jedes Bereichs zu ändern. Entwickler können verschiedene Formatierungseinstellungen auf einen Bereich anwenden, indem sie dessen Vordergrundfarbe, Hintergrundfarbe und Füllformat usw. ändern.

In dem unten angegebenen Beispiel haben wir verschiedene Formatierungseinstellungen auf verschiedene Arten von Bereichen eines Diagramms angewendet. Zu diesen Bereichen gehören:

- Grundstücksfläche
- Diagrammbereich
- SeriesCollection-Bereich
- Bereich eines einzelnen Punkts in einer SeriesCollection

Das folgende Code-Snippet zeigt, wie Sie den Diagrammbereich festlegen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **Diagrammlinien festlegen**
 Entwickler können auch verschiedene Arten von Stilen auf die Linien oder Datenmarkierungen des anwenden[SerieSammlung](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). Das folgende Code-Snippet zeigt, wie Sie Diagrammlinien mit Aspose.Cells API festlegen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Anwenden von Microsoft Excel 2007/2010-Designs auf Diagramme**
 Entwickler können verschiedene Microsoft Excel-Designs/-Farben anwenden[SerieSammlung](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)oder andere Diagrammobjekte, wie unten im Beispiel gezeigt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **Festlegen der Titel von Diagrammen oder Achsen**
Sie können Microsoft Excel verwenden, um die Titel eines Diagramms und seine Achsen in einer WYSIWYG-Umgebung festzulegen. Aspose.Cells ermöglicht es Entwicklern auch, die Titel eines Diagramms und seiner Achsen zur Laufzeit festzulegen. Alle Diagramme und ihre Achsen enthalten a[Titel](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)Eigenschaft, die verwendet werden kann, um ihre Titel festzulegen, wie unten in einem Beispiel gezeigt.

Das folgende Code-Snippet zeigt, wie Titel für Diagramme und Achsen festgelegt werden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **Arbeiten mit großen Gitternetzlinien**
Es ist möglich, das Aussehen der Hauptrasterlinien anzupassen. Blenden Sie Rasterlinien ein oder aus oder definieren Sie deren Farbe und andere Einstellungen. Im Folgenden zeigen wir, wie Gitternetzlinien ausgeblendet und ihre Farbe geändert werden.
#### **Ausblenden wichtiger Gitternetzlinien**
Entwickler können die Sichtbarkeit wichtiger Gitternetzlinien steuern, indem sie die[Ist sichtbar](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) Eigentum der[Linie](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) widersprechen**wahr** oder**FALSCH**.

Das folgende Code-Snippet zeigt, wie wichtige Gitternetzlinien ausgeblendet werden. Nach dem Ausblenden der Hauptgitterlinien wird dem Arbeitsblatt ein Säulendiagramm hinzugefügt, das keine Gitterlinien enthält.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **Ändern der Einstellungen für Hauptgitterlinien**
Entwickler können nicht nur die Sichtbarkeit wichtiger Gitterlinien steuern, sondern auch andere Eigenschaften, einschließlich ihrer Farbe usw.

Das folgende Code-Snippet zeigt, wie die Farbe der Hauptrasterlinien geändert wird. Nachdem Sie die Farbe der Hauptgitterlinien festgelegt haben, wird dem Arbeitsblatt ein Säulendiagramm mit geänderten Gitterlinien hinzugefügt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **Themen vorantreiben**
- [Legen Sie den Werteformatcode der Diagrammreihe fest](/cells/de/net/set-the-values-format-code-of-chart-series/)
- [Bild als Hintergrund festlegen Füllen Sie das Diagramm aus](/cells/de/net/set-picture-as-background-fill-in-the-chart/)
