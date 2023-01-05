---
title: Verschiedene Möglichkeiten zum Öffnen von Dateien
linktitle: Verschiedene Möglichkeiten zum Öffnen von Dateien
type: docs
weight: 10
url: /de/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Mit Aspose.Cells ist es möglich, Dateien zu öffnen, um beispielsweise Daten abzurufen, oder eine Designer-Vorlage zu verwenden, um den Entwicklungsprozess zu beschleunigen. Aspose.Cells kann eine Reihe unterschiedlicher Dateien öffnen, wie z.

{{% /alert %}} 
## **Öffnen einer Datei über einen Pfad**
 Entwickler können eine Microsoft-Excel-Datei mit ihrem Dateipfad auf dem lokalen Computer öffnen, indem sie ihn in der Datei angeben[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Klassenkonstrukteur. Übergeben Sie den Pfad einfach im Konstruktor als String. Aspose.Cells erkennt automatisch den Dateiformattyp.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath.cpp" >}}

## **Öffnen einer Datei mit einem Stream**
 Es ist auch möglich, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, der die akzeptiert*Strom*Objekt, das die Datei enthält.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream.cpp" >}}

