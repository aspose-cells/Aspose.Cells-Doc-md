---  
title: Anwendung des erweiterten Filters von Microsoft Excel zur Anzeige von Datensätzen, die komplexe Kriterien erfüllen
type: docs  
weight: 280  
url: /de/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: Erfahren Sie, wie Sie den erweiterten Filter von Microsoft Excel verwenden, um Datensätze anzuzeigen, die komplexen Kriterien entsprechen, mithilfe der API Aspose.Cells for Node.js via C++.  
keywords: Erweiterter Filter in Node.js über C++ anwenden, Erweiterter Filter in Node.js über C++ setzen, Erweiterter Filter in Node.js über C++ hinzufügen, Erweiterter Filter in Node.js über C++ erstellen, Wie man einen erweiterten Filter in einen Bereich in Node.js über C++ hinzufügt  
---  

## **Mögliche Verwendungsszenarien**  

Microsoft Excel ermöglicht es, *Erweiterte Filter* auf Tabellenblatt-Daten anzuwenden, um Datensätze zu filtern, die komplexen Kriterien entsprechen. Sie können den erweiterten Filter in Excel über den Befehl *Daten > Erweitert* ausführen, wie im Screenshot gezeigt.  

![todo:image_alt_text](1.png)  

Aspose.Cells for Node.js via C++ ermöglicht es auch, den erweiterten Filter mit der [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-)-Methode anzuwenden. Genau wie Microsoft Excel akzeptiert es die folgenden Parameter.  

**isFilter**  

Gibt an, ob die Liste am gleichen Ort gefiltert wird.  

**listRange**  

Der Listenbereich.  

**criteriaRange**  

Der Kriterienbereich.  

**copyTo**  

Der Bereich, in den Daten kopiert werden.  

**uniqueRecordOnly**  

Nur eindeutige Zeilen anzeigen oder kopieren.  

## **Erweiterten Filter von Microsoft Excel anwenden, um Datensätze anhand komplexer Kriterien anzuzeigen**  

Der folgende Beispielcode wendet den erweiterten Filter auf die [Beispiel-Excel-Datei](48496692.xlsx) an und erstellt die [Ausgabe-Excel-Datei](48496691.xlsx). Der Screenshot zeigt beide Dateien zum Vergleich. Wie im Screenshot sichtbar ist, wurden die Daten innerhalb der Ausgabedatei entsprechend komplexer Kriterien gefiltert.  

![todo:image_alt_text](2.png)  

## **Beispielcode**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-AdvancedFilter.js" >}}


