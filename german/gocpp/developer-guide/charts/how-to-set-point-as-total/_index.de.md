---
title: Wie man Punkt als Gesamtwert mit Golang über C++ setzt
linktitle: So setzen Sie einen Punkt als Gesamtwert
description: In einigen Excel Diagrammen, zum Beispiel Wasserfall Diagrammen, müssen Sie Punkte als Gesamtwert festlegen. Dieser Artikel beschreibt, wie man Aspose.Cells mit Golang über C++ verwendet, um dies zu tun.
keywords: WaterFall Diagramm, Punkt, als Total setzen.
type: docs
weight: 72
url: /de/go-cpp/how-to-set-point-as-total/
---

## Was bedeutet "Punkt als Gesamtwert setzen" in Excel-Diagrammen

In einigen Excel-Diagrammen, z.B. WaterFall-Diagrammen, sind einige Punkdaten die Summe der vorherigen Punkte. Sie müssen eventuell den Punkt als Gesamtwert "setzen". Das Beispiel zeigt den Code und die Illustrationen.

## Für ein WaterFall-Diagramm muss man den Punkt "Als Total setzen" 

![todo:image_alt_text](set-as-total1.png)

Dieses Bild zeigt ein Wasserfall-Diagramm in Excel. Wir können sehen, dass es vier Datenpunkte gibt, die mit "Total" beginnen, und sie werden verwendet, um alle vorherigen Datenpunkte zu zählen.
In diesem Bild sind die Einstellungen nicht ganz richtig. Wenn wir einen Punkt "Total 2024" auswählen, sehen wir, dass die Option "Als Total setzen" in Excel nicht aktiviert ist.
Unten ist die [Beispieldatei Excel](SampleSheet.xlsx), die geändert werden muss, und wir werden Aspose.Cells verwenden, um sie korrekt einzurichten.

## Verwendung von Aspose.Cells zum "Setzen des Punkts als Total" 

Wir verwenden den folgenden Code, um die Datei richtig einzurichten:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetPointAsTotal.go" >}}
Sie können die folgende korrekte [Ausgabedatei](output.xlsx) herunterladen

Wie im untenstehenden Bild gezeigt, sind die vier "Total"-Datenpunkte korrekt eingestellt, und Sie können den Unterschied zum vorherigen Diagramm erkennen.

![todo:image_alt_text](set-as-total2.png)
