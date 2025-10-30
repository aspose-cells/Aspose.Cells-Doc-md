---
title: Zahleneinstellungen
linktitle: Zahleneinstellungen
description: Aspose.Cells ist eine JavaScript Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien, die viele verschiedene Einstellungen für die Zellenummern unterstützt. Dieser Artikel erklärt, wie man die Aspose.Cells Bibliothek verwendet, um die Nummerneinstellungen der Zellen zur Anpassung der Zahlenformate in Tabellenkalkulationen zu verwalten.
keywords: Aspose.Cells, JavaScript Bibliothek, elektronische Tabellenkalkulation, Zellenummerneinstellungen, Formatierung, Verwaltung, Formate für Zahlen und Daten
type: docs
weight: 10
url: /de/javascript-cpp/cells-number-settings/
---

## **Wie man Anzeigeformate von Zahlen und Daten einstellt**  

Eine sehr starke Funktion von Microsoft Excel ist die Möglichkeit, das Anzeigeformat numerischer Werte und Daten festzulegen. Wir wissen, dass numerische Daten verwendet werden können, um verschiedene Werte darzustellen, darunter Dezimalzahlen, Währungen, Prozentsätze, Brüche oder Buchhaltungswerte usw. Alle diese numerischen Werte werden je nach Art der Information, die sie repräsentieren, in unterschiedlichen Formaten angezeigt. Ebenso gibt es viele Formate, in denen Datum oder Uhrzeit dargestellt werden können.  
Aspose.Cells unterstützt diese Funktionalität und ermöglicht Entwicklern, jedes Anzeigeformat für eine Zahl oder ein Datum festzulegen.  

### **Wie man Anzeigeformate in Microsoft Excel festlegt**  

Um Anzeigeformate in Microsoft Excel festzulegen:  

1. Klicken Sie mit der rechten Maustaste auf eine Zelle.  
2. Wählen Sie **Zellen formatieren**. Es erscheint ein Dialog, mit dem Sie die Anzeigeformate jeglicher Art von Wert festlegen können.  

Auf der linken Seite des Dialogs gibt es viele Kategorien von Werten wie **Allgemein**, **Zahl**, **Währung**, **Buchhaltung**, **Datum**, **Uhrzeit**, **Prozentsatz** usw. Aspose.Cells unterstützt all diese Anzeigeformate.  

Aspose.Cells bietet ein Modul, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), das eine Excel-Datei repräsentiert. Das [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Modul enthält eine [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch das [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Modul dargestellt. Das [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Modul stellt eine [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung bereit. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung repräsentiert ein Objekt des [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Moduls.  

Aspose.Cells bietet die [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)-Eigenschaft für das [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-Modul. Diese Eigenschaft wird verwendet, um das Format einer Zelle abzurufen und festzulegen. Das [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Modul stellt einige nützliche Eigenschaften für die Behandlung der Anzeigeformate von Zahlen und Daten bereit.  

### **Wie man eingebaute Zahlenformate verwendet**  

Aspose.Cells bietet einige integrierte Zahlenformate zur Konfiguration der Anzeigeformate von Zahlen und Daten. Diese integrierten Zahlenformate können mit der [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-)-Eigenschaft des [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekts angewendet werden. Alle integrierten Zahlenformate sind mit eindeutigen numerischen Werten versehen. Entwickler können jedem gewünschten numerischen Wert die [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-)-Eigenschaft des [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekts zuweisen, um das Anzeigeformat anzuwenden. Dieser Ansatz ist schnell. Die von Aspose.Cells unterstützten integrierten Zahlenformate sind unten aufgelistet.  

|**Wert**|**Typ**|**Formatzeichenfolge**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = new Date();

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 20;

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 2546;

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  


### **Wie man benutzerdefinierte Zahlenformate verwendet**  

Um eine eigene, angepasste Formatzeichenfolge für die Einstellung des Anzeigeformats zu definieren, verwenden Sie die [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)-Eigenschaft des [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekts. Dieser Ansatz ist nicht so schnell wie die Verwendung vordefinierter Formate, bietet aber mehr Flexibilität.  

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
        const { Workbook, SaveFormat } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // Instantiate or open workbook depending on whether a file is provided
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.putValue(new Date());

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.putValue(20);

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.putValue(2546);

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


{{% alert color="primary" %}}  

Wenn Sie die [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)-Eigenschaft zum Festlegen des Zahlenformats verwenden, wird jedes zuvor mit der [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-)-Eigenschaft gesetzte Format überschrieben und umgekehrt.  

{{% /alert %}}  

## **Erweiterte Themen**  
- [Benutzerdefiniertes Zahlenformat beim Festlegen von Style.Custom-Eigenschaft überprüfen](/cells/de/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Liste der unterstützten Zahlenformate](/cells/de/javascript-cpp/list-of-supported-number-formats/)  
- [Benutzerdefiniertes Datumsformatmuster g und ge mm dd anzeigen](/cells/de/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Benutzerdefinierte Dezimal- und Gruppentrennzeichen für Arbeitsmappe festlegen](/cells/de/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Benutzerdefiniertes DBNum-Formatmusterformat festlegen](/cells/de/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)
