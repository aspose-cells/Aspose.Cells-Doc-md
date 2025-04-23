---
title: Verwenden von Sparklines und Einstellungen 3D Format
type: docs
weight: 40
url: /de/python-net/using-sparklines-and-settings-3d-format/
---

## **Verwendung von Sparklines**
Microsoft Excel 2010 kann Informationen auf vielfältige Weise analysieren. Es ermöglicht Benutzern, wichtige Datentrends mit neuen Datenanalyse- und Visualisierungstools nachzuverfolgen und hervorzuheben. Sparklines sind Mini-Diagramme, die Sie innerhalb von Zellen platzieren können, um Daten und Diagramme in derselben Tabelle anzuzeigen. Wenn Sparklines richtig verwendet werden, ist die Datenanalyse schneller und präziser. Sie bieten auch einen einfachen Überblick über Informationen, vermeiden überfüllte Arbeitsblätter mit vielen belebten Diagrammen.

Aspose.Cells für Python via .NET bietet eine API zur Manipulation von Sparklines in Tabellenblättern.
### **Sparklines in Microsoft Excel**
Um Sparklines in Microsoft Excel 2010 einzufügen:

1. Wählen Sie die Zellen aus, in denen die Sparklines erscheinen sollen. Um sie leicht zu sehen, wählen Sie Zellen neben den Daten aus.
1. Klicken Sie auf **Einfügen** im Menüband und wählen Sie dann **Spalte** in der Gruppe **Sparklines** aus.
1. Wählen Sie den Bereich der Zellen im Arbeitsblatt aus oder geben Sie ihn ein, der die Quelldaten enthält. Die Diagramme werden angezeigt.

Sparklines helfen Ihnen, Trends zu erkennen, beispielsweise die Gewinn- oder Verlustbilanz für eine Softball-Liga. Sparklines können sogar die gesamte Saison jedes Teams in der Liga zusammenfassen.
### **Sparklines mit Aspose.Cells für Python via .NET**
Entwickler können Sparklines (im Vorlage-File) mit der API von Aspose.Cells für Python via .NET erstellen, löschen oder lesen. Die Klassen, die Sparklines verwalten, sind im Namespace [aspose.cells.charts](https://reference.aspose.com/cells/python-net/aspose.cells.charts) enthalten, daher müssen Sie diesen Namespace importieren, bevor Sie diese Funktionen verwenden.

Durch das ​​Hinzufügen benutzerdefinierter Grafiken für einen bestimmten Datenbereich haben Entwickler die Freiheit, verschiedene Arten von Mini-Diagrammen in ausgewählten Zellbereichen hinzuzufügen.

Das folgende Beispiel zeigt die Sparklines-Funktion. Das Beispiel zeigt, wie man:

1. Eine einfache Vorlagendatei öffnen.
1. Sparklines-Informationen für ein Arbeitsblatt lesen.
1. Neue Sparklines für einen bestimmten Datenbereich zu einem Zellbereich hinzufügen.
1. Speichern Sie die Excel-Datei auf der Festplatte.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-UsingSparklines-1.py" >}}
## **Einstellung des 3D-Formats**
Vielleicht benötigen Sie 3D-Diagramm-Stile, um nur die Ergebnisse für Ihr Szenario zu erhalten. Aspose.Cells für Python via .NET bietet die entsprechende API, um das Microsoft Excel 2007 3D-Format anzuwenden.

Ein vollständiges Beispiel finden Sie unten, um zu demonstrieren, wie man ein Diagramm erstellt und Microsoft Excel 2007 3D-Formatierung anwendet. Nach Ausführung des Beispielcodes wird ein Spaltendiagramm (mit 3D-Effekten) zum Arbeitsblatt hinzugefügt.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-Applying3DFormat-1.py" >}}

