---
title: Verschiedene Möglichkeiten, Dateien zu öffnen
linktitle: Verschiedene Möglichkeiten, Dateien zu öffnen
type: docs
weight: 10
url: /de/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

Mit Aspose.Cells ist es möglich, Dateien zu öffnen, um z. B. Daten abzurufen oder eine Designer-Vorlage für die Beschleunigung des Entwicklungsprozesses zu verwenden. Aspose.Cells kann eine Reihe verschiedener Dateien öffnen, wie z. B. Microsoft Excel-Arbeitsmappen (XLS, XLSX, XLSM, XLSB), CSV- oder Tabulatorgetrennte Dateien.

{{% /alert %}} 
## **Öffnen einer Datei über einen Pfad**
Entwickler können eine Microsoft Excel-Datei mithilfe ihres Dateipfads auf dem lokalen Computer öffnen, indem sie ihn im Konstruktor der [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse angeben. Übergeben Sie einfach den Pfad als String im Konstruktor. Aspose.Cells erkennt automatisch den Dateiformattyp.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **Öffnen einer Datei mit einem Stream**
Es ist auch möglich, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, der das *Stream*-Objekt enthält, das die Datei enthält.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

