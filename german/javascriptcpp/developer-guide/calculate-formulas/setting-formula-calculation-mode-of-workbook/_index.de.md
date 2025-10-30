---
title: Festlegen des Formel Berechnungsmodus des Arbeitsbuchs mit JavaScript via C++
linktitle: Einstellen des Formelberechnungsmodus der Arbeitsmappe
description: Dieser Artikel führt ein, wie man den Formel Berechnungsmodus eines Arbeitsbuchs in Microsoft Excel mit Aspose.Cells for JavaScript via C++ setzt. Durch Laden einer bestehenden Excel Datei oder Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellte Eigenschaft verwenden, um den Formel Berechnungsmodus festzulegen und das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf Festplatte.
keywords: Aspose.Cells, Excel, Arbeitsmappe, Formelberechnungsmodus, Einstellungen, JavaScript via C++
type: docs
weight: 110
url: /de/javascript-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}  
Microsoft Excel ermöglicht es Ihnen, den Formelberechnungsmodus festzulegen, d.h. die Art und Weise, wie Formeln berechnet werden. Es gibt drei mögliche Werte:  

- Automatisch - Neu berechnen, wenn sich etwas ändert, und jedes Mal, wenn eine Arbeitsmappe geöffnet wird.  
- Automatisch mit Ausnahme von Datentabellen - Neu berechnen, wenn sich etwas ändert, aber Auslassen von Datentabellen.  
- Manuell - Nur neu berechnen, wenn der Benutzer dies explizit durch Drücken von F9 oder STRG+ALT+F9 anfordert oder wenn die Arbeitsmappe gespeichert wird.  
{{% /alert %}}  

Um den Formelberechnungsmodus in Microsoft Excel festzulegen:  

1. Wählen Sie **Formeln** und dann **Berechnungsoptionen**.  
1. Wählen Sie eine der Optionen aus.  

Aspose.Cells for JavaScript via C++ ermöglicht es auch, den **Formelberechnungsmodus** mit der [**FormulaSettings.calculationMode**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#calculationMode--)-Eigenschaft zu setzen. Sie können ihn auf den [**CalcModeType**](https://reference.aspose.com/cells/javascript-cpp/calcmodetype)-Wert aus der Aufzählung setzen, die folgende Werte enthält:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

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
            // Creating a workbook
            const workbook = new Workbook();

            // Set the Formula Calculation Mode to Manual
            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
