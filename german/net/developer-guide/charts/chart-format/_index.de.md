---
title: Festlegen der Darstellung des Diagramms
description: Erfahren Sie, wie Sie das Erscheinungsbild von Diagrammen unter Aspose.Cells for .NET konfigurieren. Unser Leitfaden zeigt Ihnen, wie Sie Diagrammlayouts, Farben, Schriftarten und Effekte ändern, um den gewünschten visuellen Stil zu erreichen und Ihre Arbeitsblätter aufzuwerten.
keywords: Aspose.Cells for .NET, charting, chart appearance, layouts, colors, fonts, effects, worksheets.
linktitle: Diagrammformat
type: docs
weight: 20
url: /de/net/setting-chart-appearance/
---
##  **Festlegen der Darstellung des Diagramms**
In „So erstellen Sie ein Diagramm“ haben wir eine kurze Einführung in die von Aspose.Cells angebotenen Diagrammtypen und Diagrammobjekte gegeben und beschrieben, wie man ein Diagramm erstellt. In diesem Artikel wird erläutert, wie Sie das Erscheinungsbild von Diagrammen anpassen, indem Sie deren Eigenschaften festlegen:

- Festlegen des Diagrammbereichs.
- Diagrammlinien festlegen.
- Anwenden von Themen.
- Titel für Diagramme und Achsen festlegen.
- Arbeiten mit Gitterlinien.
###  **Diagrammbereich festlegen**
Es gibt verschiedene Arten von Bereichen in einem Diagramm und Aspose.Cells bietet die Flexibilität, das Erscheinungsbild jedes Bereichs zu ändern. Entwickler können verschiedene Formatierungseinstellungen auf einen Bereich anwenden, indem sie dessen Vordergrundfarbe, Hintergrundfarbe, Füllformat usw. ändern.

Im folgenden Beispiel haben wir unterschiedliche Formatierungseinstellungen auf verschiedene Arten von Bereichen eines Diagramms angewendet. Zu diesen Bereichen gehören:

- Grundstücksfläche
- Diagrammbereich
- SeriesCollection-Bereich
- Fläche eines einzelnen Punkts in einer SeriesCollection

Der folgende Codeausschnitt zeigt, wie der Diagrammbereich festgelegt wird.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
###  **Diagrammlinien festlegen**
 Entwickler können auch verschiedene Arten von Stilen auf die Linien oder Datenmarkierungen anwenden[SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). Der folgende Codeausschnitt zeigt, wie Diagrammlinien mit Aspose.Cells API festgelegt werden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
###  **Anwenden von Microsoft Excel 2007/2010-Designs auf Diagramme**
 Entwickler können verschiedene Microsoft Excel-Designs/-Farben anwenden[SeriesCollection](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)oder andere Diagrammobjekte, wie unten im Beispiel gezeigt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
###  **Festlegen der Titel von Diagrammen oder Achsen**
 Mit Microsoft Excel können Sie die Titel eines Diagramms und seiner Achsen in einer WYSIWYG-Umgebung festlegen. Mit Aspose.Cells können Entwickler außerdem die Titel eines Diagramms und seiner Achsen zur Laufzeit festlegen. Alle Diagramme und ihre Achsen enthalten a[Titel](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)Eigenschaft, mit der ihre Titel festgelegt werden können, wie unten in einem Beispiel gezeigt.

Der folgende Codeausschnitt zeigt, wie Titel für Diagramme und Achsen festgelegt werden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
###  **Arbeiten mit wichtigen Gitternetzlinien**
Es ist möglich, das Aussehen der wichtigsten Gitterlinien anzupassen. Blenden Sie Gitterlinien ein oder aus oder legen Sie deren Farbe und andere Einstellungen fest. Im Folgenden zeigen wir, wie man Gitterlinien ausblendet und ihre Farbe ändert.
####  **Ausblenden wichtiger Gitterlinien**
 Entwickler können die Sichtbarkeit wichtiger Gitternetzlinien steuern, indem sie festlegen[Ist sichtbar](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) Eigentum der[Linie](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) widersprechen**WAHR** oder falsch**.

Der folgende Codeausschnitt zeigt, wie wichtige Gitternetzlinien ausgeblendet werden. Nachdem die wichtigsten Gitterlinien ausgeblendet wurden, wird dem Arbeitsblatt ein Säulendiagramm hinzugefügt, das keine Gitterlinien enthält.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
####  **Ändern der wichtigsten Gitterlinieneinstellungen**
Entwickler können nicht nur die Sichtbarkeit der wichtigsten Gitterlinien steuern, sondern auch andere Eigenschaften, einschließlich ihrer Farbe usw.

Der folgende Codeausschnitt zeigt, wie man die Farbe der Hauptgitterlinien ändert. Nachdem Sie die Farbe der Hauptgitterlinien festgelegt haben, wird dem Arbeitsblatt ein Säulendiagramm mit geänderten Gitterlinien hinzugefügt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

##  **Vorabthemen**
- [Legen Sie den Werteformatcode der Diagrammreihe fest](/cells/de/net/set-the-values-format-code-of-chart-series/)
- [Bild als Hintergrund festlegen. Füllen Sie das Diagramm aus](/cells/de/net/set-picture-as-background-fill-in-the-chart/)
