---
title: Arbeitsblattansichten
type: docs
weight: 10
url: /de/java/worksheet-views/
---
## **Seitenumbruchvorschau**
Alle Arbeitsblätter können in zwei Modi angezeigt werden:

- Normale Ansicht.
- Seitenumbruchvorschau.

Eine normale Ansicht ist die Standardansicht eines Arbeitsblatts. Die Seitenumbruchvorschau ist eine Bearbeitungsansicht, die ein Arbeitsblatt so anzeigt, wie es gedruckt wird. Die Seitenumbruchvorschau zeigt, welche Daten auf jeder Seite erscheinen, sodass Sie den Druckbereich und die Seitenumbrüche anpassen können. Mit Aspose.Cells können Entwickler die Vorschaumodi Normalansicht oder Seitenumbruch aktivieren.
### **Ansichtsmodi steuern**
 Aspose.Cells bietet eine[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse, die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um die Vorschaumodi Normal oder Seitenumbruch zu aktivieren, verwenden Sie die[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)Methode.
#### **Normalansicht aktivieren**
Versetzen Sie jedes Arbeitsblatt in die normale Ansicht, indem Sie die verwenden[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) Methode der[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse und Bestehen**FALSCH** als Parameter.
#### **Seitenumbruchvorschau aktivieren**
Stellen Sie ein beliebiges Arbeitsblatt auf Seitenumbruchvorschau mit ein[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)Methode der[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse und Bestehen**Stimmt**als Parameter.

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)-Methode, um den Seitenumbruch-Vorschaumodus für das erste Arbeitsblatt der Excel-Datei zu aktivieren.

Im Screenshot unten sehen Sie, dass sich die Datei Book1.xls in der Normalansicht befindet.

**Book1.xls: Arbeitsblatt vor der Änderung** 

![todo: Bild_alt_Text](worksheet-views_1.png)

 Book1.xls wird mit dem geöffnet[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Klasse und der Modus wird auf Seitenumbruchvorschau für das erste Arbeitsblatt umgeschaltet. Die geänderte Datei wird als output.xls gespeichert.

**Output.xls: Arbeitsblatt nach Modifikation** 

![todo: Bild_alt_Text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Zoomfaktor**
Microsoft Excel bietet eine Funktion, mit der Benutzer den Zoom- oder Skalierungsfaktor eines Arbeitsblatts festlegen können. Diese Funktion hilft Benutzern, den Arbeitsblattinhalt in kleineren oder größeren Ansichten anzuzeigen. Benutzer können den Zoomfaktor auf einen beliebigen Wert einstellen.

**Einstellen des Zoomfaktors mit Microsoft Excel** 

![todo: Bild_alt_Text](worksheet-views_3.png)

Aspose.Cells ermöglicht es Entwicklern auch, den Zoomfaktor des Arbeitsblatts festzulegen.
### **Steuerung des Zoomfaktors**
Aspose.Cells bietet eine[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse, die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um den Zoomfaktor eines Arbeitsblatts festzulegen, verwenden Sie die[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)Methode.

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)Methode zum Festlegen des Zoomfaktors des ersten Arbeitsblatts in einer Excel-Datei.

Im Screenshot unten sehen Sie die Datei Book1.xls in der Standardansicht.

**Book1.xls: Arbeitsblatt vor der Änderung** 

![todo: Bild_alt_Text](worksheet-views_4.png)

 Die Datei Book1.xls wird mit dem geöffnet[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Klasse und der Zoomfaktor des ersten Arbeitsblatts wird auf 75 gesetzt. Die geänderte Datei wird als output.xls gespeichert.

**Output.xls: Arbeitsblatt nach der Änderung** 

![todo: Bild_alt_Text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Fenster einfrieren**
Fenster einfrieren ist eine Funktion, die von Microsoft Excel bereitgestellt wird. Durch das Einfrieren von Fenstern können Sie Daten auswählen, die beim Scrollen in einem Arbeitsblatt sichtbar bleiben sollen.

**Verwenden von Fixierfenstern in Microsoft Excel** 

![todo: Bild_alt_Text](worksheet-views_6.png)

Aspose.Cells ermöglicht es Entwicklern auch, zur Laufzeit eingefrorene Fenster auf Arbeitsblätter anzuwenden.

Aspose.Cells bietet eine[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse, die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Rufen Sie zum Konfigurieren von Einfrierfenstern die[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\) ) Methode. Das[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))-Methode nimmt die folgenden Parameter an:

- **Die Zeile**, der Zeilenindex der Zelle, bei der das Einfrieren beginnt.
- **Spalte**, der Spaltenindex der Zelle, ab der das Einfrieren beginnt.
- **Gefrorene Reihen**, die Anzahl der sichtbaren Zeilen im oberen Bereich.
- **Gefrorene Säulen**, die Anzahl der sichtbaren Spalten im linken Bereich

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von zeigt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))-Methode zum Einfrieren von Zeilen und Spalten (beginnend bei C4, dargestellt durch die 4. Zeile und die 3. Spalte, wobei die Zeilen und Spalten bei 0-Indizes beginnen) des ersten Arbeitsblatts der Excel-Datei.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


Im folgenden Screenshot sehen Sie die Datei Book1.xls ohne Fenster zum Einfrieren.

**Book1.xls: Arbeitsblattansicht vor jeder Änderung** 

![todo: Bild_alt_Text](worksheet-views_7.png)

 Die Datei Book1.xls wird mit dem geöffnet[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Klasse und dann werden einige Zeilen und Spalten auf dem ersten Arbeitsblatt eingefroren. Die geänderte Datei wird als output.xls gespeichert.

**Outlook.xls: Arbeitsblattansicht nach Änderung** 

![todo: Bild_alt_Text](worksheet-views_8.png)
## **Geteilte Scheiben**
Wenn Sie den Bildschirm teilen müssen, um zwei verschiedene Ansichten in demselben Arbeitsblatt zu erhalten, teilen Sie die Bereiche. Microsoft Excel bietet eine sehr praktische Funktion, mit der Sie mehr als eine Kopie Ihres Arbeitsblatts anzeigen und unabhängig voneinander durch jeden Bereich Ihres Arbeitsblatts scrollen können: geteilte Bereiche.

Die Scheiben arbeiten gleichzeitig. Wenn Sie in einem eine Änderung vornehmen, erscheint die Änderung gleichzeitig im anderen. Aspose.Cells stellt die Split-Pane-Funktion für die Benutzer bereit.
### **Anwenden und Entfernen von geteilten Scheiben**
#### **Teilen von Scheiben**
Aspose.Cells bietet eine[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse, die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Excel-Dateien. Um geteilte Ansichten zu implementieren, verwenden Sie die[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[Teilt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\) ) Methode. Um geteilte Fenster zu entfernen, verwenden Sie die[entfernenSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) Methode.

In dem Beispiel verwenden wir eine einfache Vorlagendatei, die geladen wird, dann wird die Funktion zum Festlegen von geteilten Fenstern auf eine Zelle im ersten Arbeitsblatt angewendet. Die aktualisierte Datei wird gespeichert.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Nach dem Ausführen des obigen Codes hat die generierte Datei eine geteilte Ansicht.

**Geteilte Bereiche in der Ausgabedatei** 

![todo: Bild_alt_Text](worksheet-views_9.png)
#### **Scheiben entfernen**
 Entwickler können geteilte Fenster mithilfe von entfernen[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse'[entfernenSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Themen vorantreiben**
- [Ausblenden der Anzeige von Nullwerten im Arbeitsblatt](/cells/de/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Legen Sie die Farbe des Arbeitsblatt-Tabs fest](/cells/de/java/set-worksheet-tab-color/)
- [Elemente ein- und ausblenden](/cells/de/java/show-and-hide-elements/)
- [Formeln statt Werte in einem Arbeitsblatt anzeigen](/cells/de/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Verwenden Sie die Optionen zur Fehlerprüfung](/cells/de/java/use-error-checking-options/)
