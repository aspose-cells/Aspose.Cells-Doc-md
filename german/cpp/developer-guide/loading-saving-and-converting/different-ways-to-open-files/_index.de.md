---
title: Verschiedene Möglichkeiten zum Öffnen von Dateien
linktitle: Verschiedene Möglichkeiten zum Öffnen von Dateien
type: docs
weight: 10
url: /de/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Mit Aspose.Cells ist es möglich, Dateien zu öffnen, um beispielsweise Daten abzurufen, oder eine Designer-Vorlage zu verwenden, um den Entwicklungsprozess zu beschleunigen. Aspose.Cells kann eine Reihe verschiedener Dateien öffnen, z. B. Microsoft Excel-Tabellen (XLS, XLSX, XLSM, XLSB), CSV oder TabDelimited-Dateien.

{{% /alert %}} 
##  **Öffnen einer Datei über einen Pfad**
 Entwickler können eine Excel-Datei Microsoft über ihren Dateipfad auf dem lokalen Computer öffnen, indem sie ihn im angeben[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)Klassenkonstruktor. Übergeben Sie den Pfad einfach im Konstruktor als String. Aspose.Cells erkennt automatisch den Dateiformattyp.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

##  **Öffnen einer Datei mithilfe eines Streams**
 Es ist auch möglich, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, der die übernimmt*Strom*Objekt, das die Datei enthält.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

