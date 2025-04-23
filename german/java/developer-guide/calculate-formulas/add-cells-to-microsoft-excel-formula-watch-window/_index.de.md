---
title: Zellen zur Microsoft Excel Formelüberwachung hinzufügen
type: docs
weight: 20
url: /de/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Mögliche Verwendungsszenarien**

Das Microsoft Excel Watch-Fenster ist ein nützliches Tool, um die Zellenwerte und ihre Formeln bequem in einem Fenster zu beobachten. Sie können das *Watch Window* in Microsoft Excel öffnen, indem Sie auf *Formeln > Überwachungsfenster* klicken. Es verfügt über die *Add Watch*-Schaltfläche, die zum Hinzufügen von Zellen zur Überwachung verwendet werden kann. Ebenso können Sie die *[**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add-int-int-)* Methode verwenden, um mit der Aspose.Cells-API Zellen in das *Watch Window* hinzuzufügen.

## **Zellen zur Microsoft Excel-Formelüberwachung hinzufügen**

Der folgende Beispielscode setzt die Formel der Zellen C1 und E1 und fügt beide dem *Watch Window* hinzu. Anschließend speichert er die Arbeitsmappe als [Ausgabedatei im Excel-Format](67338509.xlsx). Wenn Sie die Ausgabedatei öffnen und das *Watch Window* anzeigen, sehen Sie beide Zellen, wie in diesem Screenshot gezeigt.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
{{< app/cells/assistant language="java" >}}
