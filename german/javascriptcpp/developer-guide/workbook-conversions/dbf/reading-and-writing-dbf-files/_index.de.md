---
title: DBF-Dateien lesen und schreiben
linktitle: DBF-Dateien lesen und schreiben
description: Aspose.Cells ist eine JavaScript-via-C++-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien und unterstützt das Lesen und Schreiben von dBASE-III- und dBASE-IV-Dateien (DBF). Dieser Artikel erläutert, wie Sie mit Aspose.Cells Daten aus DBF-Dateien importieren und in DBF-Dateien exportieren, einschließlich Angaben zum Dateiformat, zu unterstützten Funktionen und schrittweisen Beispielen.
keywords: Aspose.Cells, JavaScript-via-C++-Bibliothek, DBF, dBASE, DBF lesen, DBF schreiben, DBF importieren, DBF exportieren, Dateiformat, .dbf
type: docs
weight: 200
url: /de/javascript-cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet vollständige Unterstützung für das Lesen und Schreiben von DBF-Dateien (dBASE). Sie können vorhandene dBASE-III- und dBASE-IV-Dateien in eine Arbeitsmappe laden, die Daten mithilfe der umfangreichen Aspose.Cells API bearbeiten und die Arbeitsmappe anschließend wieder im DBF-Format speichern, um sie in herkömmlichen Datenbankanwendungen verwenden zu können.
{{% /alert %}}

## **Einführung**
DBF (Datenbankdatei) ist ein herkömmliches Datenbankdateiformat, das dBASE Anfang der 1980er-Jahre einführte. Trotz des Alters des Formats werden DBF-Dateien in vielen Branchen weiterhin häufig zur Speicherung strukturierter Daten verwendet, insbesondere in der Buchhaltung, in GIS-Anwendungen und in anderen spezialisierten Anwendungen. Mit Aspose.Cells können Sie diese herkömmlichen Dateien nahtlos in moderne Arbeitsabläufe für Tabellenkalkulationen integrieren.
Die Bibliothek unterstützt sowohl das Lesen als auch das Schreiben von DBF-Dateien und bietet Ihnen damit folgende Möglichkeiten:
- Importieren von Daten aus vorhandenen DBF-Dateien in Arbeitsmappenobjekte von Aspose.Cells zur weiteren Verarbeitung oder Konvertierung in andere Formate.
- Erstellen neuer DBF-Dateien von Grund auf oder durch die Umwandlung von Daten aus anderen Tabellenkalkulationsformaten.
- Beibehalten von Felddefinitionen, Datentypen und Datensatzstrukturen beim Transfer von Daten in das und aus dem DBF-Format.
DBF-Dateien können außerdem direkt in Microsoft Excel und anderen Tabellenkalkulationsanwendungen geöffnet werden. Dadurch bilden sie eine bequeme Brücke zwischen herkömmlichen Systemen und modernen Tools für Tabellenkalkulationen.

## **Unterstützte DBF-Versionen und Funktionen**
Aspose.Cells unterstützt die folgenden DBF-Formatversionen:
- **dBASE III** — die ursprüngliche und am weitesten unterstützte Variante des DBF-Formats.
- **dBASE IV** — eine erweiterte Version, die zusätzliche Datentypen und größere Feldgrößen unterstützt.

### Unterstützte Funktionen
Die Bibliothek bietet umfassende Unterstützung für die folgenden Vorgänge:
- Lesen von DBF-Daten in eine Arbeitsmappe, wobei alle Datensätze und Felddefinitionen erhalten bleiben.
- Rückschreiben von Arbeitsmappendaten in das DBF-Format zum Export in dBASE-kompatible Anwendungen.
- Verarbeitung gängiger Datentypen in DBF-Dateien, einschließlich Zeichen-, numerischer, Datums- und logischer Felder.
- Beibehaltung von Felddefinitionen wie Feldname, Typ und Länge während Lese- und Schreibvorgängen.

### Einschränkungen und Hinweise
Beachten Sie bei der Arbeit mit DBF-Dateien die folgenden Einschränkungen:
- Die maximale Anzahl von Feldern pro Datei beträgt **128**.
- Die maximale Datensatzgröße beträgt **4000 Bytes**.
- Feldnamen sind auf **10 Zeichen** begrenzt, müssen in Großbuchstaben geschrieben sein und dürfen keine Leerzeichen enthalten.
- Datumswerte in DBF-Dateien werden im Format `YYYYMMDD` gespeichert.
- Die Zeichenkodierung kann je nach erstellender Anwendung variieren; häufig werden Windows-1252- oder OEM-Codeseiten verwendet.

## **Lesen einer DBF-Datei**
Mit Aspose.Cells lassen sich Daten einfach aus einer DBF-Datei in eine Arbeitsmappe laden. Die Bibliothek verwendet die Klasse `LoadOptions`, um das Quellformat anzugeben und sicherzustellen, dass die Daten beim Laden korrekt interpretiert werden.

### Lesen einer DBF-Datei mit Aspose.Cells
Um eine DBF-Datei zu lesen, erstellen Sie eine `LoadOptions`-Instanz, legen Sie die Eigenschaft `loadFormat` auf `LoadFormat.Dbf` fest und übergeben Sie die Instanz zusammen mit dem Dateipfad an den `Workbook`-Konstruktor. Nach dem Laden sind die Daten über die `Worksheets`-Sammlung zugänglich. In dieser können Sie die Zellen durchlaufen, Werte extrahieren oder die Daten nach Bedarf bearbeiten.
Das folgende Beispiel zeigt, wie Sie eine vorhandene DBF-Datei in Aspose.Cells laden, auf das erste Arbeitsblatt zugreifen und die Zellenwerte lesen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".dbf" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select a DBF file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const fileData = new Uint8Array(await file.arrayBuffer());
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Dbf);
                const workbook = new Workbook(fileData, loadOptions);
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const maxRow = cells.maxDataRow;
                const maxCol = cells.maxDataColumn;
                const lines = [];
                for (let i = 0; i <= maxRow; i++) {
                    let line = "";
                    for (let j = 0; j <= maxCol; j++) {
                        const cell = cells.get(i, j);
                        const value = cell.stringValue;
                        line += "|" + value;
                    }
                    line += "|";
                    lines.push(line);
                }
                const output = document.createElement('pre');
                output.textContent = lines.join("\n");
                result.replaceChildren(output);
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                const message = document.createElement('p');
                message.style.color = "green";
                message.textContent = "DBF file loaded successfully. Converted XLSX saved as output.xlsx.";
                result.appendChild(message);
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Sie können DBF-Dateien direkt in Microsoft Excel öffnen, indem Sie die Datei im Dialogfeld Öffnen auswählen. Excel behandelt die DBF-Datei als Tabellenkalkulation und zeigt die Datensätze in einem tabellarischen Layout an. Dies ist hilfreich, um die Daten nach dem Lesen oder Schreiben mit Aspose.Cells schnell zu überprüfen.
{{% /alert %}}

## **Schreiben einer DBF-Datei**
Das Schreiben von Daten in eine DBF-Datei folgt einem ähnlichen Muster wie das Speichern in einem beliebigen anderen Tabellenkalkulationsformat mit Aspose.Cells. Sie erstellen oder laden eine Arbeitsmappe, füllen das Arbeitsblatt mit Daten und rufen anschließend die Methode `save` mit `SaveFormat.Dbf` als Zielformat auf.

### Schreiben einer DBF-Datei mit Aspose.Cells
Gehen Sie wie folgt vor, um eine DBF-Datei zu erstellen:
1. Erstellen Sie eine neue `Workbook`-Instanz.
2. Rufen Sie das erste Arbeitsblatt aus der `Worksheets`-Sammlung ab.
3. Füllen Sie das Arbeitsblatt mit Ihren Daten, einschließlich der Überschriften in der ersten Zeile und der Datensätze in den folgenden Zeilen.
4. Rufen Sie die Methode `Workbook.save` auf und übergeben Sie den Dateipfad sowie `SaveFormat.Dbf` als Parameter.
Das folgende Beispiel zeigt, wie Sie eine neue DBF-Datei von Grund auf erstellen. Dabei wird ein Arbeitsblatt mit Beispieldaten gefüllt, die unterschiedliche Datentypen (Zeichenketten, Zahlen und Datumswerte) enthalten. So wird veranschaulicht, wie Feldtypen beim Export in das DBF-Format behandelt werden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Spaltenüberschriften
            cells.get(0, 0).value = "ID";
            cells.get(0, 1).value = "Name";
            cells.get(0, 2).value = "Department";
            cells.get(0, 3).value = "Salary";
            cells.get(0, 4).value = "HireDate";
            // Datenzeile 1
            cells.get(1, 0).value = 101;
            cells.get(1, 1).value = "John Smith";
            cells.get(1, 2).value = "Engineering";
            cells.get(1, 3).value = 75000.50;
            cells.get(1, 4).value = new Date(2020, 2, 15);
            // Datenzeile 2
            cells.get(2, 0).value = 102;
            cells.get(2, 1).value = "Jane Doe";
            cells.get(2, 2).value = "Marketing";
            cells.get(2, 3).value = 68000.75;
            cells.get(2, 4).value = new Date(2019, 6, 22);
            // Datenzeile 3
            cells.get(3, 0).value = 103;
            cells.get(3, 1).value = "Bob Johnson";
            cells.get(3, 2).value = "Finance";
            cells.get(3, 3).value = 82000.00;
            cells.get(3, 4).value = new Date(2021, 0, 10);
            // Datenzeile 4
            cells.get(4, 0).value = 104;
            cells.get(4, 1).value = "Alice Brown";
            cells.get(4, 2).value = "Human Resources";
            cells.get(4, 3).value = 71000.25;
            cells.get(4, 4).value = new Date(2018, 10, 5);
            // Datenzeile 5
            cells.get(5, 0).value = 105;
            cells.get(5, 1).value = "Charlie Wilson";
            cells.get(5, 2).value = "Operations";
            cells.get(5, 3).value = 79500.80;
            cells.get(5, 4).value = new Date(2022, 4, 30);
            // Spaltenbreiten für bessere Lesbarkeit festlegen
            cells.setColumnWidth(0, 8);
            cells.setColumnWidth(1, 20);
            cells.setColumnWidth(2, 20);
            cells.setColumnWidth(3, 12);
            cells.setColumnWidth(4, 14);
            const outputData = workbook.save(AsposeCells.SaveFormat.Dbf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.dbf";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Stellen Sie beim Schreiben von Daten in eine DBF-Datei sicher, dass Ihre Daten den Einschränkungen des Formats entsprechen. Feldnamen dürfen höchstens 10 Zeichen lang sein und keine Leerzeichen enthalten. Datensätze, die insgesamt mehr als 4000 Bytes überschreiten, werden nicht ordnungsgemäß gespeichert. Datumswerte sollten gültig sein und sich im Format YYYYMMDD darstellen lassen.
{{% /alert %}}

## **Hinweise zu Datentypen und Formatierung**
Beim Transfer von Daten zwischen Aspose.Cells und dem DBF-Format ist es wichtig, die Zuordnung der Datentypen zwischen den beiden Systemen zu verstehen, um die Datenintegrität sicherzustellen.

### Zuordnung von Zelltypen zu DBF-Feldtypen
Die Zellwerte von Aspose.Cells werden beim Speichern automatisch in die entsprechenden DBF-Feldtypen konvertiert:
- **Zeichenketten** werden Zeichenfeldern (C) zugeordnet.
- **Numerische Werte** (Ganzzahlen und Dezimalzahlen) werden numerischen Feldern (N) zugeordnet.
- **Datumswerte** werden Datumsfeldern (D) im Format `YYYYMMDD` zugeordnet.
- **Boolesche Werte** werden logischen Feldern (L) zugeordnet.

### Zeichenkodierung
DBF-Dateien verwenden je nach der Anwendung, die sie erstellt hat, möglicherweise unterschiedliche Zeichenkodierungen. Aspose.Cells übernimmt die Zeichenkodierung in den meisten Fällen automatisch. Bei Problemen mit der Zeichenanzeige kann es jedoch erforderlich sein, die Kodierung der Quelldatei zu überprüfen.

### Regeln für Feldnamen
Für DBF-Feldnamen gelten die folgenden Regeln:
- Maximale Länge von 10 Zeichen.
- Der Feldname muss mit einem Buchstaben beginnen.
- Er darf keine Leerzeichen oder Sonderzeichen enthalten.
- Er wird unabhängig von der bei der Eingabe verwendeten Groß- und Kleinschreibung in Großbuchstaben gespeichert.

### Überprüfung der Ausgabe
Nach dem Schreiben einer DBF-Datei können Sie das Ergebnis überprüfen, indem Sie die Datei in Microsoft Excel oder einer beliebigen dBASE-kompatiblen Anwendung öffnen. Die Daten sollten in einem tabellarischen Layout erscheinen, die Feldnamen als Spaltenüberschriften und die Datensätze entsprechend den bereitgestellten Daten befüllt sein.

## **Konvertierung zwischen DBF und anderen Formaten**
Einer der praktischsten Anwendungsfälle für das Lesen und Schreiben von DBF-Dateien mit Aspose.Cells ist die Konvertierung von Daten zwischen dem DBF-Format und modernen Tabellenkalkulationsformaten wie XLSX, XLS oder CSV. Da Aspose.Cells eine breite Palette von Formaten unterstützt, können Sie eine DBF-Datei problemlos laden und in einem beliebigen anderen unterstützten Format erneut speichern und umgekehrt verfahren.

{{< app/cells/assistant language="javascript-cpp" >}}