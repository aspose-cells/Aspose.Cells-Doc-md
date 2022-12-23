---
title: Kopieren Sie die Sparkline, indem Sie den Datenbereich und den Speicherort der Sparkline-Gruppe angeben
type: docs
weight: 120
url: /de/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
Kopieren Sie die Sparkline, indem Sie den Datenbereich und den Speicherort der Sparkline-Gruppe in MS Excel angeben

Microsoft Mit Excel können Sie eine Sparkline kopieren, indem Sie den Datenbereich und den Speicherort der Sparkline-Gruppe angeben. Befolgen Sie diese Schritte, um Ihre Sparkline in andere Zellen zu kopieren.

- Wählen Sie die Zelle aus, die Ihre Sparkline enthält.
-  Wählen**Daten bearbeiten** von dem**Sparkline** Abschnitt innerhalb der**Design** Tab
-  Wählen**Standort und Daten der Gruppe bearbeiten...**
- Geben Sie Datenbereich und Speicherort an und klicken Sie auf OK.

## Beispiel

 Aspose.Cells bietet die[**SparklineCollection.add (Datenbereich, Zeile, Spalte)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) -Methode, um den Datenbereich und den Speicherort der Sparkline-Gruppe anzugeben.

### Screenshots der Quell- und Ausgabedateien

Der folgende Screenshot zeigt die im Code verwendete Excel-Quelldatei. Der rot markierte Bereich zeigt "**Standort und Daten der Gruppe bearbeiten...**" Option, um den Datenbereich und die Position der Sparkline-Gruppe anzugeben. Die Zelle P4 zeigt die Sparkline, die mit Aspose.Cells in die anderen vier mit gelber Farbe gefüllten Zellen kopiert wird.

![todo: Bild_alt_Text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

Der folgende Screenshot zeigt die vom Beispielcode generierte Excel-Ausgabedatei. Wie Sie sehen können, wurde die Sparkline in Zelle P4 in die nächsten vier Zellen in Spalte P mit jeweils unterschiedlichem Datenbereich kopiert.

![todo: Bild_alt_Text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Java-Code zum Kopieren der Sparkline durch Angabe des Datenbereichs und der Position der Sparkline-Gruppe

Der folgende Beispielcode lädt die Excel-Quelldatei wie im obigen Screenshot gezeigt, greift dann auf die erste Sparkline-Gruppe zu und fügt Datenbereiche und Speicherorte innerhalb der Sparkline-Gruppe hinzu. Schließlich schreibt es die ausgegebene Excel-Datei auf die Festplatte, die auch im obigen Screenshot gezeigt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
