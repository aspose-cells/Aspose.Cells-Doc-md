---
title: Wie man ein Tornado Diagramm erstellt
type: docs
weight: 73
url: /de/net/create-tornado-chart/
description: Erfahren Sie, wie man ein Tornado Diagramm mit der Aspose.Cells for .NET API erstellt.
keywords: C# erstellen Sie ein Tornado Diagramm, fügen Sie ein Tornado Diagramm hinzu, fügen Sie ein Tornado Diagramm ein
---

## **Einführung**
Ein Tornado-Diagramm, auch als Tornado-Diagramm oder Tornado-Grafik bekannt, ist eine Art der Datendarstellung, die oft für die Sensitivitätsanalyse in Excel verwendet wird. Es hilft Ihnen, den Einfluss von sich ändernden Variablen auf ein bestimmtes Ergebnis oder Resultat zu verstehen.

## **Wie man ein Tornado-Diagramm in Excel erstellt**
Sie können ein Tornado-Diagramm in Excel erstellen, indem Sie diesen Schritten folgen:
1. Wählen Sie die Daten aus und gehen Sie zu Einfügen --> Diagramme --> Säulen- oder Balkendiagramm einfügen --> Gestapeltes Balkendiagramm. Klicken Sie darauf.
<br>
<img src="1.png" width=70% />
2. Ändern Sie die Y-Achse: Klicken Sie mit der rechten Maustaste auf die y-Achse. Klicken Sie auf Achsenformat. Klicken Sie in Beschriftungen auf das Dropdown-Menü für die Position der Beschriftung und wählen Sie Niedrigstes Element aus.
<br>
<img src="2.png" width=70% />
3. Wählen Sie eine beliebige Leiste aus und gehen Sie zur Formatierung. Legen Sie einen geeigneten Abstand fest.
<br>
<img src="3.png" width=70% />
4. Entfernen wir das Minuszeichen (-) aus dem Tornado-Diagramm. Wählen Sie die x-Achse aus. Gehen Sie zur Formatierung. Klicken Sie in den Achsenoptionen auf die Nummer. Wählen Sie in der Kategorie Benutzerdefiniert aus. Im Formatcode schreiben Sie ###0,###0. Klicken Sie auf Hinzufügen.
<br>
<img src="4.png" width=70% />
5. Klicken Sie auf die y-Achse und gehen Sie zu den Achsenoptionen. Überprüfen Sie in den Achsenoptionen Kategorien in umgekehrter Reihenfolge.
<br>
<img src="5.png" width=70% />

## **Wie man ein Tornado-Diagramm in Aspose.Cells hinzufügt**
Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die [Beispieldatei Excel](sample.xlsx), die einige Beispieldaten enthält. Danach erstellt es das gestapelte Balkendiagramm basierend auf den Anfangsdaten und setzt relevante Eigenschaften. Schließlich speichert es die Arbeitsmappe im [Ausgabe-XLSX-Format](out.xlsx). Der folgende Screenshot zeigt das von Aspose.Cells erstellte Tornado-Diagramm in der Ausgabe-Excel-Datei.
<br>
<img src="6.png" width=70% />

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
