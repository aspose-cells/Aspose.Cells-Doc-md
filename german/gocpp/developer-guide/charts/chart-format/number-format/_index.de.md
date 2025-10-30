---
title: Setzen Sie das Werte Formatierungscode der Diagrammserie mit Golang über C++
linktitle: Zahlenformat
type: docs
weight: 100
url: /de/go-cpp/set-the-values-format-code-of-chart-series/
description: Lernen Sie, wie Sie den Werte Formatcode der Diagrammserie in Aspose.Cells for C++ einstellen. Unser Leitfaden hilft Ihnen, Ihre Diagrammseriendaten mit dem geeigneten Formatcode zu formatieren, um Ihre Daten genau und professionell zu präsentieren.
keywords: Aspose.Cells for C++, Diagrammserie, Werte Formatcode, Formatierung, Datenpräsentation, Genauigkeit, Professionalität.
---

## **Mögliche Verwendungsszenarien**
Sie können den Werte-Formatierungscode der Diagrammserie mit der Eigenschaft [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) festlegen. Diese Eigenschaft ist nicht nur für Serien nützlich, die auf dem Bereich im Arbeitsblatt basieren, sondern funktioniert auch gut für Serien, die mit einem Array von Werten erstellt wurden.

## **Setzen des Werteformatcodes der Diagrammserie**
Das folgende Beispiel fügt einer leeren Grafik, die zuvor keine Serie hatte, eine Serie hinzu. Es fügt die Serie anhand des Werte-Arrays hinzu. Sobald die Serie hinzugefügt wurde, wird sie mit dem Code `$#,##0` formatiert, unter Verwendung der Eigenschaft [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/), und die Zahl `10000` wird zu `$10.000`. Der Screenshot zeigt die Auswirkung des Codes auf die [Beispieldatei Excel](51740712.xlsx) und die [Ausgabedatei Excel](51740713.xlsx) nach der Ausführung.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Beispielcode**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberFormat.go" >}}
