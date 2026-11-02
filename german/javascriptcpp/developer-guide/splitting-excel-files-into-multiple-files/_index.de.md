---
title: Aufteilen von Excel-Dateien in mehrere Dateien
linktitle: Aufteilen von Excel-Dateien in mehrere Dateien
description: Aspose.Cells for JavaScript via C++ ist eine JavaScript‑via‑C++‑Bibliothek zum Arbeiten mit Tabellendateien, die das Aufteilen einer einzelnen Excel‑Datei in mehrere Dateien unterstützt. Dieser Artikel stellt vor, wie Excel‑Dateien durch Kopieren jedes Arbeitsblatts in eine separate Arbeitsmappe und durch Kopieren spezifischer Zellbereiche in andere Arbeitsmappen aufgeteilt werden können.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ Bibliothek, Tabellenkalkulation, Excel‑Datei aufteilen, Arbeitsblatt kopieren, Bereich kopieren, mehrere Arbeitsmappen, als separate Dateien speichern
type: docs
weight: 195
url: /de/javascript-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ unterstützt das Aufteilen einer einzelnen Excel‑Datei in mehrere Dateien. Es gibt zwei Hauptmethoden: (1) Kopieren jedes Arbeitsblatts der Quellarbeitsmappe in eine neue Arbeitsmappe und Speichern jeder als separate Datei, und (2) Kopieren eines bestimmten Zellbereichs aus einem Arbeitsblatt in eine neue Arbeitsmappe. Beide Ansätze sind nützlich, wenn Teilmengen von Daten verteilt, kleinere Berichte für verschiedene Empfänger erstellt oder Daten für die Einzelverarbeitung isoliert werden sollen.
{{% /alert %}}

## **Einleitung**
Es gibt viele reale Szenarien, in denen ein Entwickler eine einzelne Excel‑Datei in mehrere kleinere Dateien aufteilen muss. Beispielsweise kann eine Arbeitsmappe ein Arbeitsblatt pro Abteilung enthalten, und jede Abteilungsleitung muss nur ihr eigenes Blatt erhalten. In anderen Fällen möchte man eine bestimmte Tabelle oder einen Datenblock aus einem Arbeitsblatt extrahieren und als eigenständige Datei per E‑Mail versenden, ohne den Rest der Arbeitsmappe offenzulegen. Große konsolidierte Arbeitsmappen müssen ebenfalls in kleinere Teile aufgeteilt werden, um die Handhabung zu erleichtern, das Laden zu beschleunigen oder die Weiterverarbeitung durch andere Systeme zu ermöglichen.  
Aspose.Cells for JavaScript via C++ bietet zwei flexible Ansätze für diese Aufgabe. Der erste Ansatz iteriert durch jedes Arbeitsblatt der Quellarbeitsmappe und kopiert dessen Inhalt in eine brandneue `Workbook`‑Instanz, wobei jede als separate Datei gespeichert wird. Der zweite Ansatz konzentriert sich auf einen bestimmten Zellbereich innerhalb eines Arbeitsblatts und kopiert nur diesen Bereich in eine neue Arbeitsmappe. In beiden Fällen ist der allgemeine Ablauf derselbe: Laden der Quellarbeitsmappe mithilfe der `Workbook`‑Klasse, Zugriff auf die relevanten Daten über die `Worksheet`‑ und `Cells`‑Objekte, Übertragen des Inhalts in eine Ziel‑`Workbook` und anschließendes Speichern der Zielarbeitsmappe auf dem Datenträger.

## **Aufteilen einer Excel‑Datei durch Kopieren jedes Arbeitsblatts in eine neue Arbeitsmappe**

### **Übersicht des Ansatzes**
In diesem Ansatz wird die Quellarbeitsmappe einmal geöffnet und anschließend für jedes `Worksheet` in deren `Worksheets`‑Sammlung eine neue Ziel‑`Workbook`‑Instanz erstellt. Der Inhalt des Quellarbeitsblatts wird in das erste Arbeitsblatt der Zielarbeitsmappe kopiert und die Zielarbeitsmappe wird unter einem Namen gespeichert, der vom Namen des Quellarbeitsblatts abgeleitet ist. Das Ergebnis ist eine Ausgabedatei pro Arbeitsblatt, wobei jede Ausgabedatei die Daten eines einzelnen Quellblatts enthält.  
Diese Methode ist die richtige Wahl, wenn jedes Arbeitsblatt Ihrer Quellarbeitsmappe eine logisch unabhängige Informationseinheit darstellt (z. B. eine Abteilung, Region, Monat oder Produktlinie) und Sie jede Einheit separat bereitstellen oder verarbeiten möchten.

### **Schritte**
Die folgenden Schritte beschreiben, wie man eine Excel‑Datei durch Kopieren jedes Arbeitsblatts in eine neue Arbeitsmappe aufteilt:
1. Öffnen Sie die Quell‑Excel‑Datei, indem Sie ein `Workbook`‑Objekt instanziieren und den Dateipfad an dessen Konstruktor übergeben.
2. Durchlaufen Sie die `Workbook.Worksheets`‑Sammlung mit einer `for`‑ oder `for...of`‑Schleife, sodass jedes `Worksheet` in der Quelldatei verarbeitet wird.
3. Innerhalb der Schleife erstellen Sie eine neue Ziel‑`Workbook`‑Instanz (eine leere Arbeitsmappe) für das aktuelle Arbeitsblatt.
4. Kopieren Sie den Inhalt des Quellarbeitsblatts in das Zielarbeitsblatt. Dies kann erfolgen, indem Sie die Zellen der `Cells`‑Sammlung des Quellarbeitsblatts iterieren und deren Werte in die entsprechenden Zellen des Zielarbeitsblatts schreiben, oder indem Sie die Methode `Cells.Copy` verwenden, um einen gesamten Bereich auf einmal zu übertragen.
5. Erstellen Sie einen Ausgabepfad, der den Namen des Quellarbeitsblatts enthält (z. B. `dataDir + worksheet.Name + ".xls"`), sodass jede erzeugte Datei einen eindeutigen Namen hat.
6. Rufen Sie die Methode `Workbook.Save` der Zielarbeitsmappe auf, um die Datei auf dem Datenträger zu schreiben.
7. Wiederholen Sie die Schritte 3 bis 6 für das nächste Arbeitsblatt, bis alle Arbeitsblätter verarbeitet wurden.

### **Codebeispiel**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                const result = document.getElementById('result');
                try {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an .xls file.</p>';
                        return;
                    }
                    result.innerHTML = '<p>Processing...</p>';
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    const downloadLinks = document.createElement('div');
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const sourceSheet = workbook.worksheets.get(i);
                        const sheetName = sourceSheet.name;
                        const destWorkbook = new Workbook();
                        const destIndex = destWorkbook.worksheets.add();
                        const destSheet = destWorkbook.worksheets.get(destIndex);
                        destSheet.name = sheetName;
                        destSheet.copy(sourceSheet);
                        const outputData = destWorkbook.save(AsposeCells.SaveFormat.Excel97To2003);
                        const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                        const downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(blob);
                        downloadLink.download = `${sheetName}.xls`;
                        downloadLink.textContent = `Download ${sheetName}.xls`;
                        downloadLink.style.display = 'block';
                        downloadLink.style.marginTop = '8px';
                        downloadLinks.appendChild(downloadLink);
                    }
                    result.innerHTML = '<p style="color: green;">Done! Click a download link to get the result file.</p>';
                    result.appendChild(downloadLinks);
                } catch (error) {
                    console.error(error);
                    const errorMessage = document.createElement('p');
                    errorMessage.style.color = 'red';
                    errorMessage.textContent = `Error: ${error instanceof Error ? error.message : error}`;
                    result.replaceChildren(errorMessage);
                }
            });
        </script>
    </body>
</html>
```

Die erwartete Ausgabe ist ein Satz neuer Dateien im Datenverzeichnis, eine Datei pro Arbeitsblatt der Quellarbeitsmappe. Jede Datei wird nach dem entsprechenden Quellblatt benannt und enthält die Daten (und optional die Formatierung) dieses einzelnen Blatts.

## **Aufteilen einer Excel‑Datei durch Kopieren eines Bereichs in eine neue Arbeitsmappe**

### **Übersicht des Ansatzes**
Manchmal entspricht der zu trennende Datenumfang nicht einem gesamten Arbeitsblatt, sondern einer bestimmten rechteckigen Region eines Arbeitsblatts, z. B. `A1:D10` oder einem benannten Bereich, der eine bestimmte Tabelle darstellt. In solchen Fällen ist das Kopieren ganzer Arbeitsblätter verschwenderisch, und ein präziserer Ansatz ist erforderlich: den Quellbereich identifizieren, nur diesen Bereich in eine neue Arbeitsmappe kopieren und die neue Datei speichern.  
Dieser Ansatz ist ideal, wenn Sie eine einzelne Tabelle, einen Berichtblock oder ein Datenfeld aus einem größeren Arbeitsblatt extrahieren und dabei allen nicht relevanten Inhalt verwerfen möchten. Er ist auch nützlich, um vom Benutzer ausgewählte Bereiche eines Blatts als eigenständige Dateien zu exportieren.

### **Schritte**
Die folgenden Schritte beschreiben, wie man eine Excel‑Datei durch Kopieren eines bestimmten Bereichs in eine neue Arbeitsmappe aufteilt:
1. Öffnen Sie die Quell‑Excel‑Datei, indem Sie ein `Workbook`‑Objekt mit dem Dateipfad instanziieren.
2. Rufen Sie das Ziel‑`Worksheet` ab, das den zu kopierenden Bereich enthält, entweder über den Index (z. B. das erste Blatt) oder über den Namen aus der `Worksheets`‑Sammlung.
3. Identifizieren Sie den zu kopierenden Bereich. Dies kann ein fest codierter Zellbereich wie `A1:C10` sein, ein benannter Bereich, der über die `Worksheet.Cells`‑Sammlung erhalten wird, oder ein Bereich, der über `Worksheet.Cells.CreateRange` erstellt wird.
4. Erstellen Sie eine neue Ziel‑`Workbook`‑Instanz.
5. Greifen Sie auf das erste `Worksheet` der Zielarbeitsmappe zu (das Standardsheet).
6. Kopieren Sie den Quellbereich in das Zielarbeitsblatt, typischerweise beginnend bei Zelle `A1`. Die Methode `Cells.Copy` der Ziel‑`Cells`‑Sammlung kann verwendet werden, um einen gesamten Bereich zu kopieren, oder Sie können die Zellen des Quellbereichs iterieren und deren Werte mit `PutValue` in die Zielzellen schreiben. Optional können `CopyOptions` angegeben werden, um zu steuern, was übernommen wird (nur Werte, Werte + Stile, Formeln usw.).
7. Speichern Sie die Zielarbeitsmappe mit der Methode `Workbook.Save` unter einem neuen Dateipfad auf dem Datenträger.

### **Codebeispiel**
Die erwartete Ausgabe ist eine einzelne neue Datei im Datenverzeichnis, die nur die Werte (und optional die Formatierung) des angegebenen, aus der Quellarbeitsmappe extrahierten Bereichs enthält. Die Zieldatei steht in keinem Zusammenhang zu anderen Daten in der Quelldatei; sie enthält ausschließlich den extrahierten Bereich, beginnend bei Zelle `A1` ihres ersten Arbeitsblatts.

## Verwandte Artikel
- [Filterfelder zu einer Pivot‑Tabelle hinzufügen in Aspose.Cells for JavaScript via C++](/cells/de/javascript-cpp/add-page-field-in-pivot-table/)
- [Stile auf Pivot‑Tabellen anwenden in Aspose.Cells for JavaScript via C++](/cells/de/javascript-cpp/apply-style-to-pivot-table/)
- [Seitenfeldlayout in Pivot‑Tabelle ändern](/cells/de/javascript-cpp/change-page-field-layout/)
- [Sparkline in Bild und HTML konvertieren in Aspose.Cells for JavaScript via C++](/cells/de/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Excel in OFD‑Format konvertieren](/cells/de/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}