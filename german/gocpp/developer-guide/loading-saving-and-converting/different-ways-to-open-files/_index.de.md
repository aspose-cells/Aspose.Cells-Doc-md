---
title: Verschiedene Möglichkeiten, Dateien zu öffnen
linktitle: Verschiedene Möglichkeiten, Dateien zu öffnen
type: docs
weight: 10
url: /de/go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie Dateien öffnen, z.B. um Daten abzurufen oder ein Designer-Template zu verwenden, um den Entwicklungsprozess zu beschleunigen. Aspose.Cells kann eine Reihe verschiedener Dateitypen öffnen, wie Microsoft Excel Tabellen (XLS, XLSX, XLSM, XLSB), CSV oder TabDelimited Dateien.

{{% /alert %}}

## **Öffnen einer Datei über einen Pfad**

Entwickler können eine Microsoft Excel-Datei über ihren Dateipfad auf dem lokalen Computer öffnen, indem sie diesen im Konstruktor der [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse angeben. Übergeben Sie den Pfad als String im Konstruktor. Aspose.Cells erkennt automatisch den Dateiformttyp.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **Öffnen einer Datei mit Stream**

Es ist auch möglich, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, der das *Stream*-Objekt enthält, das die Datei enthält.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
