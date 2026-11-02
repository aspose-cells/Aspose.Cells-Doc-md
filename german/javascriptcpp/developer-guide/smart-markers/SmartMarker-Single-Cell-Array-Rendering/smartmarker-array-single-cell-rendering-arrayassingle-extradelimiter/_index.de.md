---
title: "SmartMarker: Darstellung eines Arrays in einer einzelnen Zelle | Aspose.Cells for JavaScript via C++"
description: "Erfahren Sie, wie Sie mit Aspose.Cells for JavaScript via C++ unter Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Smart Markers Arraydaten in eine einzelne Zelle rendern."
linktitle: "SmartMarker: Darstellung eines Arrays in einer einzelnen Zelle | Aspose.Cells"
url: /de/javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++-Bibliothek, Tabellenkalkulation, Smart Markers, ArrayAsSingle, ExtraDelimiter, Einzelzell-Array, Arraydarstellung, Vorlage
type: docs
weight: 195
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Rendern von Arraydaten in eine einzelne Zelle mithilfe von Smart Markers. Durch die Verwendung des Attributs `ArrayAsSingle` zusammen mit dem Attribut `ExtraDelimiter` können Entwickler steuern, wie Arrayelemente innerhalb einer einzelnen Zelle getrennt werden, wodurch flexible Formatierungen für Berichte und Vorlagen ermöglicht werden.
{{% /alert %}}

## **Einführung**
Smart Markers in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellenkalkulationsdaten dynamisch mithilfe von Markerausdrücken wie `&=DataSource.Field` befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage durch den `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.
Standardmäßig wird ein Array, auf das ein Smart Marker verweist (z. B. `&=DataSource.Numbers`), vom Verarbeitungsmodul aufgeteilt und jedes Element in einer separaten angrenzenden Zelle platziert – entweder horizontal entlang einer Zeile oder vertikal in einer Spalte nach unten. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie das gesamte Array lieber in einer einzigen Zelle rendern möchten, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.
Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die gemeinsam in einem Smart-Marker-Tag verwendet werden, erfüllen genau diese Anforderung. Sie halten Berichtslayouts kompakt und vorhersehbar und arbeiten gleichzeitig nativ mit Array-Datenquellen.

## **Warum diese Funktion benötigt wird**

### **Standardverhalten bei der Arrayverteilung**
Wenn ein Smart Marker auf eine Arrayeigenschaft verweist, verteilt Aspose.Cells das Array standardmäßig auf mehrere Zellen. Ein Marker wie `&=Product.Tags`, der auf ein Array mit vier Zeichenfolgen verweist, platziert beispielsweise jeden Wert in einer eigenen Zelle. Dadurch werden andere Vorlageninhalte nach außen verschoben, was sorgfältig gestaltete Berichtslayouts beeinträchtigen kann.

### **Einschränkungen bei Anwendungsfällen**
In vielen praktischen Szenarien ist das standardmäßige Verhalten der Arrayverteilung unerwünscht:
- **Zusammenfassungsberichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Beschriftungs- oder Stichwortlisten**, die in einer einzelnen Zelle als durch Komma oder Pipe getrennte Werte angezeigt werden sollen.
- **Filterchips oder Statusindikatoren**, die mehrere Werte zur besseren Lesbarkeit an einem Ort zusammenfassen.
- **Nachgelagerte Verarbeitungspipelines** (CSV-Export, PDF-Rendering, Serienbrieferstellung), die statt eines erweiterten Bereichs einen einzelnen konsolidierten Wert pro Zelle erwarten.
- **Plattformübergreifende Kompatibilität**, bei der einige Anwendungen keine Arrays tolerieren können, die sich über mehrere Zellen erstrecken.

### **Die Lücke, die sie schließt**
Ohne einen integrierten Mechanismus müssten Entwickler die Daten in JavaScript vorverarbeiten und Arrays zu durch Trennzeichen getrennten Zeichenfolgen zusammenführen, bevor sie sie an den `WorkbookDesigner` binden. Dadurch würde Logik dupliziert, die Datenmodelle wären komplizierter und die Fehlerwahrscheinlichkeit höher. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` machen diesen Umweg überflüssig, indem sie die Formatierung deklarativ innerhalb des Smart Markers übernehmen.

## **Vorteile der Funktion**
Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markers bietet mehrere Vorteile:
- **Darstellung in einer einzelnen Zelle**: Alle Arrayelemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersehbar bleiben.
- **Steuerung des Trennzeichens**: Legen Sie eine beliebige Trennzeichenfolge fest – Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder beliebiger benutzerdefinierter Text.
- **Vorlagenbasierte Formatierung**: Für die Vorverarbeitung der Daten ist kein zusätzlicher Code erforderlich; die Formatierungsregeln befinden sich im Smart-Marker-Tag.
- **Übersichtlichere Berichte**: Arraydaten verschieben benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielseitige Datentypen**: Die Funktion unterstützt Zeichenfolgen, Zahlen, Datumswerte und alle anderen Datentypen, die mit einem Trennzeichen zusammengeführt werden können.
- **Abwärtskompatibilität**: Wenn die Attribute ausgelassen werden, bleibt das ursprüngliche Verhalten der Arrayverteilung erhalten, sodass vorhandene Vorlagen unverändert weiter funktionieren.

## **Verwendung dieser Funktion**

### **Syntax für Smart Marker**
Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines standardmäßigen Smart Markers übergeben. Die allgemeine Syntax lautet:

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
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Der Marker setzt sich aus den folgenden Teilen zusammen:
- `&=DataSource.ArrayProperty` – der standardmäßige Smart Marker, der auf die Arrayeigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` – weist das Verarbeitungsmodul an, das gesamte Array in einer einzelnen Zelle zu rendern. Nur der Wert `true` löst das Verhalten für eine einzelne Zelle aus.
- `extraDelimiter=", "` – definiert das Trennzeichen, das zwischen den Arrayelementen eingefügt wird. Der Wert ist ein Zeichenfolgenliteral; er kann leer, ein einzelnes Zeichen oder eine Zeichenfolge mit mehreren Zeichen sein.

{{% alert color="primary" %}}
Das Attribut `extraDelimiter` akzeptiert jedes Zeichenfolgenliteral, einschließlich Trennzeichen mit mehreren Zeichen, benutzerdefiniertem Text oder Escape-Sequenzen wie `\n` für eine durch Zeilenumbrüche getrennte Ausgabe. Ist das Array leer, bleibt die resultierende Zelle leer.
{{% /alert %}}

### **Schritt-für-Schritt-Workflow**
Der folgende Workflow beschreibt, wie Sie mithilfe von Smart Markers ein Array in einer einzelnen Zelle rendern.
1. **Datenquelle vorbereiten**: Erstellen Sie ein Objekt (oder eine Datenstruktur), das eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann ein Array aus Zeichenfolgen, Zahlen oder anderen unterstützten Wertetypen zurückgeben.
2. **Designer-Arbeitsmappe erstellen**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die mithilfe der Attribute `arrayasSingle` und `extraDelimiter` auf die Arrayeigenschaft verweist.
3. **WorkbookDesigner instanziieren**: Erstellen Sie ein `WorkbookDesigner`-Objekt, weisen Sie ihm die Designer-Arbeitsmappe zu und binden Sie Ihre Datenquelle mithilfe der Methode `setDataSource`.
4. **Marker verarbeiten**: Rufen Sie die Methode `workbookDesigner.process()` auf, um die Smart Markers zu verarbeiten und die Arbeitsmappe mit realen Daten zu befüllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe auf der Festplatte im XLSX-Format oder in einem anderen unterstützten Dateiformat.

### **Codebeispiel 1 – Grundlegendes Rendering eines Zeichenfolgenarrays**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Codebeispiel 2 – Numerisches Array mit benutzerdefiniertem Trennzeichen**

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
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Abschnitt 1: Standard-Smart-Marker – Werte werden horizontal auf Zellen verteilt
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // Abschnitt 2: Neue Einzelzellendarstellung mit arrayasSingle und extraDelimiter
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // Datenquelle binden und Smart Markers verarbeiten
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // Resultierende Arbeitsmappe speichern
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Codebeispiel 3 – Vergleich des Standardverhaltens mit dem Verhalten von ArrayAsSingle**

### **Hinweise und bewährte Vorgehensweisen**
Beachten Sie die folgenden Punkte bei der Arbeit mit den Attributen `ArrayAsSingle` und `ExtraDelimiter`:
- Der Wert `extraDelimiter` wird als Zeichenfolgenliteral behandelt; maskieren Sie alle Sonderzeichen, die Ihr Vorlagenverarbeiter möglicherweise interpretiert.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`true` / `false`). Nur `true` löst das Verhalten für eine einzelne Zelle aus; jeder andere Wert führt zum Standardverhalten der Arrayverteilung zurück.
- Ist das Array leer oder null, bleibt die Zelle leer (oder enthält abhängig vom Datentyp eine leere Zeichenfolge).
- Die Funktion unterstützt sowohl Objekt-Datenquellen als auch tabellarische Datenquellen, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für eine durch Zeilenumbrüche getrennte Ausgabe verwenden Sie `\n` als Trennzeichenwert.

{{< app/cells/assistant language="javascript-cpp" >}}