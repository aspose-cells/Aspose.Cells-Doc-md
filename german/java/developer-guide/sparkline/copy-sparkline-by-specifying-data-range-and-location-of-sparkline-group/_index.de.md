---
title: Sparkline kopieren durch Festlegen des Datenbereichs und des Speicherorts der Sparkline Gruppe
type: docs
weight: 120
url: /de/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

Sparkline kopieren, indem der Datenbereich und der Speicherort der Sparkline-Gruppe in MS Excel festgelegt werden

Microsoft Excel ermöglicht es Ihnen, eine Sparkline zu kopieren, indem Sie den Datenbereich und den Speicherort der Sparkline-Gruppe angeben. Befolgen Sie diese Schritte, um Ihre Sparkline in andere Zellen zu kopieren.

- Wählen Sie die Zelle mit Ihrer Sparkline aus.
- Wählen Sie **Daten bearbeiten** im **Sparkline**-Abschnitt im **Entwurf**-Tab aus
- Wählen Sie **Gruppenposition & Daten bearbeiten...** aus
- Geben Sie den Datenbereich und den Speicherort an und klicken Sie auf OK.

## Beispiel

Aspose.Cells bietet die Methode [**SparklineCollection.add(dataRange, row, column)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection), um den Datenbereich und den Speicherort der Sparkline-Gruppe anzugeben.

### Screenshots der Quell- und Ausgabedateien

Der folgende Screenshot zeigt die im Code verwendete Quelldatei. Der rot markierte Bereich zeigt die Option "**Gruppenposition & Daten bearbeiten...**" an, um den Datenbereich und den Speicherort der Sparkline-Gruppe anzugeben. Die Zelle P4 zeigt die Sparkline, die in die anderen vier Zellen kopiert wird, die mit gelber Farbe gefüllt sind, indem Aspose.Cells verwendet wird.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

Der folgende Screenshot zeigt die Ausgabedatei, die durch den Beispielcode generiert wurde. Wie Sie sehen können, wurde die Sparkline in der Zelle P4 in die nächsten vier Zellen in Spalte P kopiert, jeder mit einem anderen Datenbereich.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Java-Code zum Kopieren von Sparkline durch Festlegen des Datenbereichs und des Speicherorts der Sparkline-Gruppe

Der folgende Beispielcode lädt die im obigen Screenshot gezeigte Quelldatei, greift dann auf die erste Sparkline-Gruppe zu und fügt Datenbereiche und -speicherorte in die Sparkline-Gruppe ein. Schließlich schreibt er die Ausgabedatei auf die Festplatte, die auch im obigen Screenshot zu sehen ist.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
{{< app/cells/assistant language="java" >}}
