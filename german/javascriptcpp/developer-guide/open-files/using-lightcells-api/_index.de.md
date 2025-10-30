---
title: Verwendung der LightCells API mit JavaScript über C++
linktitle: Verwendung der LightCells API
type: docs
weight: 160
url: /de/javascript-cpp/using-lightcells-api/
description: Lernen Sie, wie Sie große Excel Dateien mit der LightCells API in JavaScript über C++ lesen und schreiben. Verbessern Sie Leistung und Effizienz bei geringeren Speicherverbrauch.
---

{{% alert color="primary" %}}  

Manchmal müssen Sie große Microsoft Excel-Dateien mit einer riesigen Menge an Daten oder Inhalten im Arbeitsblatt lesen und schreiben. Die LightCells API ist nützlich, um große Excel-Tabellenkalkulationen zu erstellen: Sie benötigen weniger Speicher und erhalten eine bessere Leistung und Effizienz.  

{{% /alert %}}  
# Ereignisgesteuerte Architektur  
Aspose.Cells bietet die LightCells API, die hauptsächlich darauf ausgelegt ist, Zellendaten einzeln zu manipulieren, ohne ein vollständiges Datenmodell (Verwendung der Zellensammlung usw.) in den Speicher zu laden. Es funktioniert im ereignisgesteuerten Modus.  

Um Arbeitsmappen zu speichern, geben Sie den Zellinhalt einzeln an, wenn Sie speichern, und das Komponente speichert ihn direkt in die Ausgabedatei.  

Beim Lesen von Vorlagendateien analysiert die Komponente jede Zelle und gibt deren Wert einzeln an.  

In beiden Verfahren wird eine Cell-Objekt verarbeitet und dann verworfen; das Workbook-Objekt hält die Sammlung nicht. In diesem Modus wird daher beim Importieren und Exportieren von Microsoft Excel-Dateien mit großem Datensatz Speicher gespart, der sonst viel Speicher verbrauchen würde.  

Obwohl die LightCells API die Zellen für XLSX- und XLS-Dateien auf dieselbe Weise verarbeitet (sie lädt nicht alle Zellen tatsächlich in den Speicher, sondern verarbeitet eine Zelle und verwirft sie dann), spart sie für XLSX-Dateien effektiver Speicher als für XLS-Dateien aufgrund der unterschiedlichen Datenmodelle und Strukturen der beiden Formate.  

Allerdings können Entwickler **bei XLS-Dateien** einen temporären Speicherort angeben, um während des Speicher-Vorgangs temporäre Daten zu speichern und somit mehr Speicher zu sparen. Häufig **kann die Verwendung der LightCells API zum Speichern von XLSX-Dateien 50 % oder mehr Speicher sparen** im Vergleich zur herkömmlichen Methode; **bei XLS-Dateien sind Einsparungen von ungefähr 20-40 % möglich**.  

## Schreiben einer großen Excel-Datei  
Aspose.Cells stellt eine Schnittstelle, `LightCellsDataProvider`, bereit, die in Ihrem Programm implementiert werden muss. Das Interface repräsentiert den Datenanbieter für das Speichern großer Tabellenkalkulationsdateien im leichten Modus.  

Beim Speichern eines Arbeitsbuchs in diesem Modus wird `StartSheet(int)` überprüft, wenn jedes Arbeitsblatt im Buch gespeichert wird. Für ein Blatt, wenn `StartSheet(int)` wahr ist, werden alle Daten und Eigenschaften der Zeilen und Zellen dieses Blattes durch diese Implementierung bereitgestellt. Zunächst wird `NextRow()` aufgerufen, um den nächsten zu speichernden Zeilenindex zu erhalten. Wird ein gültiger Zeilenindex zurückgegeben (der Zeilenindex muss in aufsteigender Reihenfolge für die zu speichernden Zeilen sein), wird ein `Row`-Objekt für diese Zeile bereitgestellt, um deren Eigenschaften mit `StartRow(Row)` festzulegen.  

Für eine Zeile wird zunächst `NextCell()` überprüft. Wenn ein gültiger Spaltenindex zurückgegeben wird (der Spaltenindex muss in aufsteigender Reihenfolge für alle Zellen einer Zeile sein), wird ein Cell-Objekt für diese Zelle bereitgestellt, um dessen Daten und Eigenschaften mit `StartCell(Cell)` festzulegen. Nachdem die Zelleinstellungen gemacht wurden, wird die Zelle direkt in die erstellte Tabellenkalkulationsdatei gespeichert, und die nächste Zelle wird überprüft und verarbeitet.  
### Schreiben einer großen Excel-Datei: Beispiel  
Bitte sehen Sie sich den folgenden Beispielcode an, um die Funktionsweise der LightCells API zu sehen. Fügen Sie Codeausschnitte hinzu, entfernen Sie diese oder aktualisieren Sie sie gemäß Ihren Anforderungen.  

Das Programm erstellt eine riesige Datei mit **10.000 (10000x30 Matrix) Datensätzen** in einem Arbeitsblatt und füllt sie mit Dummy-Daten. Sie können Ihre eigene Matrix festlegen, indem Sie die Variablen `rowsCount` und `colsCount` in der `Main()`-Methode ändern.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlSaveOptions } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        class TestDataProvider {
            constructor(workbook, maxRows, maxColumns) {
                this._workbook = workbook;
                this.maxRows = maxRows;
                this.maxColumns = maxColumns;
                this._row = -1;
                this._column = -1;
            }

            isGatherString() {
                return false;
            }

            nextCell() {
                this._column++;
                if (this._column < this.maxColumns) {
                    return this._column;
                } else {
                    this._column = -1;
                    return -1;
                }
            }

            nextRow() {
                this._row++;
                if (this._row < this.maxRows) {
                    this._column = -1;
                    return this._row;
                } else {
                    return -1;
                }
            }

            startCell(cell) {
                cell.value = this._row + this._column;
                if (this._row !== 1) {
                    cell.formula = "=Rand() + A2";
                }
            }

            startRow(row) {
            }

            startSheet(sheetIndex) {
                return sheetIndex === 0;
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            // The example does not require an input file; file input is optional.
            const rowsCount = 10000;
            const colsCount = 30;

            const workbook = new Workbook();
            const ooxmlSaveOptions = new OoxmlSaveOptions();

            ooxmlSaveOptions.lightCellsDataProvider = new TestDataProvider(workbook, rowsCount, colsCount);

            const outputData = workbook.save(SaveFormat.Xlsx, ooxmlSaveOptions);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the generated file.</p>';
        });
    </script>
</html>
```  

## Lesen großer Excel-Dateien  
Aspose.Cells stellt eine Schnittstelle, `LightCellsDataHandler`, bereit, die in Ihrem Programm implementiert werden muss. Das Interface repräsentiert den Datenanbieter für das Lesen großer Tabellenkalkulationsdateien im leichten Modus.  

Beim Lesen eines Arbeitsbuchs in diesem Modus wird `StartSheet` überprüft, wenn jedes Arbeitsblatt im Buch gelesen wird. Für ein Blatt, wenn `StartSheet` wahr ist, werden alle Daten und Eigenschaften der Zellen in Zeilen und Spalten des Blattes durch die Implementierung dieses Interfaces überprüft und verarbeitet. Für jede Zeile wird `StartRow` aufgerufen, um zu prüfen, ob sie verarbeitet werden soll. Wenn eine Zeile verarbeitet werden soll, werden ihre Eigenschaften zuerst gelesen, und der Entwickler kann mit `ProcessRow` auf ihre Eigenschaften zugreifen. Wenn die Zellen der Zeile ebenfalls verarbeitet werden sollen, sollte `ProcessRow` true zurückgeben, und `StartCell` wird für jede vorhandene Zelle in der Zeile aufgerufen, um zu prüfen, ob eine Zelle verarbeitet werden muss. Wenn eine Zelle verarbeitet werden soll, wird `ProcessCell` aufgerufen, um die Zelle gemäß diesem Interface zu verarbeiten.  
### Lesen großer Excel-Dateien: Beispiel  
Bitte sehen Sie sich den folgenden Beispielcode an, um die Funktionsweise der LightCells API zu sehen. Fügen Sie Codeausschnitte hinzu, entfernen Sie diese oder aktualisieren Sie sie gemäß Ihren Anforderungen.  

Das Programm liest eine riesige Datei mit Millionen von Datensätzen in einem Arbeitsblatt. Es dauert eine kleine Zeit, jedes Blatt im Arbeitsbuch zu lesen. Der Beispielcode liest die Datei und ermittelt die Gesamtzahl der Zellen, die Zahl der Strings und die Formelanzahl in jedem Arbeitsblatt.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>LightCells Data Handler Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, CellValueType, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        class LightCellsDataHandlerVisitCells {
            constructor() {
                this.cellCount = 0;
                this.formulaCount = 0;
                this.stringCount = 0;
            }

            get CellCount() {
                return this.cellCount;
            }

            get FormulaCount() {
                return this.formulaCount;
            }

            get StringCount() {
                return this.stringCount;
            }

            StartSheet(sheet) {
                console.log("Processing sheet[" + sheet.name + "]");
                return true;
            }

            StartRow(rowIndex) {
                return true;
            }

            ProcessRow(row) {
                return true;
            }

            StartCell(column) {
                return true;
            }

            ProcessCell(cell) {
                this.cellCount++;
                if (cell.isFormula()) {
                    this.formulaCount++;
                } else if (cell.type === CellValueType.IsString) {
                    this.stringCount++;
                }
                return false;
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const opts = new LoadOptions();
            const v = new LightCellsDataHandlerVisitCells();
            opts.lightCellsDataHandler = v;
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);
            const sheetCount = wb.worksheets.count;

            resultDiv.innerHTML = '<p style="color: green;">Total sheets: ' + sheetCount + ', cells: ' + v.CellCount
                + ', strings: ' + v.StringCount + ', formulas: ' + v.FormulaCount + '</p>';
        });
    </script>
</html>
```
