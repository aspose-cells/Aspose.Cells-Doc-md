---
title: Darstellung eines Arrays in einer einzelnen Zelle mit SmartMarker | Aspose.Cells for Node.js via Java
linktitle: Darstellung eines Arrays in einer einzelnen Zelle mit SmartMarker | Aspose.Cells for Node.js via Java
description: Erfahren Sie, wie Sie mithilfe der Smart-Marker-Attribute `arrayassingle` und `arraydelimiter` in Aspose.Cells for Node.js via Java Arraydaten in einer einzelnen Zelle darstellen.
keywords: Aspose.Cells, Node.js via Java-Bibliothek, Tabelle, Smart Marker, arrayassingle, arraydelimiter, Array in einer einzelnen Zelle, Arraydarstellung, Vorlage
type: docs
weight: 195
url: /de/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells kann eine Array-Datenquelle mithilfe von Smart Markern in einer einzigen Zelle darstellen. Das Attribut `arrayassingle` deaktiviert die standardmäßige Verteilung der Elemente auf einzelne Zellen, und das Attribut `arraydelimiter` legt das Trennzeichen zwischen den zusammengefügten Elementen fest. Standardmäßig wird ein Komma verwendet; alternativ können Sie ein beliebiges einzelnes Zeichen oder eine in Anführungszeichen gesetzte mehrzeichnige Zeichenfolge angeben.
{{% /alert %}}

## **Einführung**
Smart Markers in Aspose.Cells sind eine vorlagenbasierte Funktion, mit der Tabellendaten dynamisch mithilfe von Markerausdrücken wie `&=DataSource.Field` befüllt werden. Der Marker wird in einer Designer-Arbeitsmappe platziert. Wenn die Vorlage durch den `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.

Standardmäßig entfaltet Aspose.Cells ein Array, auf das ein Smart Marker verweist – beispielsweise `&=Product.Tags`, das an ein Array aus vier Werten gebunden ist – und fügt jedes Element in eine eigene Zelle ein. Dadurch werden die Werte vertikal in der Spalte unterhalb des Markers verteilt. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie das gesamte Array lieber in einer einzigen Zelle darstellen möchten, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.

Die Attribute `arrayassingle` und `arraydelimiter`, die innerhalb der Klammern eines Smart Markers in der Form `name:value` geschrieben werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersehbar zu halten und gleichzeitig nativ mit Array-Datenquellen zu arbeiten.

## **Warum diese Funktion erforderlich ist**

### **Standardmäßiges Verteilen von Arrays**
Wenn ein Smart Marker auf ein Array-Feld verweist, verteilt Aspose.Cells das Array standardmäßig auf mehrere Zellen. Beispielsweise füllt ein Marker wie `&=Product.Tags` bei einem Array aus vier Werten jeden Wert in eine eigene Zelle unterhalb des Markers ein. Dadurch werden andere Vorlageninhalte verschoben, und sorgfältig entworfene Berichtslayouts können beeinträchtigt werden.

### **Einschränkungen bei der Verwendung**
Es gibt zahlreiche praxisnahe Szenarien, in denen das standardmäßige Verteilen unerwünscht ist:
- **Zusammenfassende Berichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Bezeichnungs- oder Stichwortlisten**, die in einer einzelnen Zelle als durch Komma oder Pipe getrennte Werte angezeigt werden sollen.
- **Filter-Chips oder Statusanzeigen**, die mehrere Werte zur Verbesserung der Lesbarkeit an einer Stelle bündeln.
- **Nachgelagerte Verarbeitungsketten** (CSV-Export, PDF-Darstellung, Serienbrief), die pro Zelle einen einzelnen konsolidierten Wert statt eines erweiterten Bereichs erwarten.
- **Plattformübergreifende Kompatibilität**, bei der einige Verarbeitungskomponenten keine Arrays tolerieren können, die sich über mehrere Zellen erstrecken.

### **Die Lücke, die diese Funktion schließt**
Ohne einen integrierten Mechanismus wären Entwickler gezwungen, die Daten in JavaScript vorzuverarbeiten und Arrays vor der Bindung an den `WorkbookDesigner` zu durch Trennzeichen getrennten Zeichenfolgen zusammenzuführen. Dies dupliziert die Logik, erschwert die Datenmodelle und erhöht die Fehlerwahrscheinlichkeit. Die Attribute `arrayassingle` und `arraydelimiter` machen diesen Umweg überflüssig, indem sie die Formatierung deklarativ im Smart Marker selbst übernehmen.

## **Vorteile der Funktion**
Die Verwendung der Attribute `arrayassingle` und `arraydelimiter` in Ihren Smart Markers bietet mehrere Vorteile:
- **Zusammenfassung in einer einzigen Zelle**: Alle Array-Elemente werden in genau einer Zelle dargestellt, sodass Layouts kompakt und vorhersehbar bleiben.
- **Flexible Steuerung des Trennzeichens**: Legen Sie das gewünschte Trennzeichen fest – das Standardkomma, ein Semikolon, einen Bindestrich, ein Pipe-Zeichen oder eine in Anführungszeichen gesetzte mehrzeichnige Zeichenfolge wie `" | "`.
- **Vorlagengesteuerte Formatierung**: Für die Vorverarbeitung der Daten ist kein zusätzlicher Code erforderlich; die Formatierungsregeln sind im Smart-Marker-Tag enthalten.
- **Übersichtlichere Berichte**: Arraydaten verschieben benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielseitige Datentypen**: Die Funktion unterstützt Arrays aus Zeichenfolgen, die als JSON-Zeilen bereitgestellt werden, einschließlich Zahlenwerten, die als Zeichenfolge dargestellt werden.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Verteilungsverhalten erhalten, sodass vorhandene Vorlagen unverändert weiter funktionieren.

## **So verwenden Sie diese Funktion**

### **Smart-Marker-Syntax**
Die Attribute `arrayassingle` und `arraydelimiter` verwenden die Attributgrammatik `name:value` von Aspose.Cells innerhalb der Klammern eines standardmäßigen Smart Markers. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Der Marker besteht aus den folgenden Teilen:
- `&=DataSource.ArrayField` – der standardmäßige Smart Marker, der auf das Array-Feld der gebundenen Datenquelle verweist.
- `arrayassingle:true` – weist die Verarbeitungs-Engine an, das gesamte Array in einer einzigen Zelle darzustellen, statt die Elemente zu verteilen.
- `arraydelimiter:;` – optional; legt das Trennzeichen fest, das zwischen den Array-Elementen platziert wird. Wenn es weggelassen wird, wird ein Komma verwendet.

{{% alert color="warning" %}}
Schreiben Sie Attribute im Format `name:value` (mit einem Doppelpunkt und nicht mit einem Gleichheitszeichen) und trennen Sie mehrere Attribute mit einem Komma **ohne Leerzeichen**. Ein Leerzeichen nach dem Komma verschiebt den geparsten Wert um ein Zeichen – `(arrayassingle:true, arraydelimiter:;)` würde die Elemente mit dem fehlerhaften Trennzeichen `:;` anstelle von `;` zusammenfügen.
{{% /alert %}}

### **Schreibweisen für Trennzeichen**
- Ein einzelnes Zeichen wird unmittelbar nach dem Doppelpunkt angegeben: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Ein mehrzeichniges Trennzeichen wird in doppelten Anführungszeichen geschrieben: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Schritt-für-Schritt-Workflow**
Der folgende Workflow beschreibt, wie Sie mithilfe von Smart Markers ein Array in einer einzigen Zelle darstellen.
1. **Datenquelle vorbereiten**: Strukturieren Sie jeden Datensatz als JSON-Objekt, dessen Feld ein Array enthält, beispielsweise `{"Tags": ["C#", "Aspose"]}`. Einfache JavaScript-Objekte und Arrays, die an `setDataSource` übergeben werden, werden auf dieser Plattform nicht gebunden; JSON-Zeilen sind die unterstützte tabellarische Form.
2. **Designer-Arbeitsmappe erstellen**: Erstellen Sie eine neue Instanz von `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie in einer Zelle einen Smart Marker, der auf das Array-Feld verweist und das Attribut `arrayassingle` enthält (sowie `arraydelimiter`, wenn ein benutzerdefiniertes Trennzeichen erforderlich ist).
3. **`WorkbookDesigner` instanziieren**: Erstellen Sie einen `WorkbookDesigner` für die Arbeitsmappe und binden Sie Ihre JSON-Zeilen mithilfe von `setJsonDataSource` an.
4. **Marker verarbeiten**: Rufen Sie die Methode `workbookDesigner.process()` auf, um die Smart Marker zu verarbeiten und die Arbeitsmappe mit den tatsächlichen Daten zu befüllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe auf der Festplatte im XLSX-Format oder in einem anderen unterstützten Dateiformat.

### **Codebeispiel 1 – Grundlegende Darstellung eines Arrays aus Zeichenfolgen**

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Tags");
// No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-single.xlsx");
```

Das Beispiel gibt den zusammengefügten Wert des gesamten Arrays aus. Die vier Tags werden in einer Zelle dargestellt und durch das Standardkomma getrennt:

```
C#,Aspose,SmartMarker,Excel
```

### **Codebeispiel 2 – Zahlenwerte mit einem benutzerdefinierten Trennzeichen**

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Scores");
// arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-numeric.xlsx");
```

Wenn die Punktzahlen als JSON-Zeichenfolgen bereitgestellt werden, bleiben in der zusammengefügten Ausgabe die reinen Zahlenwerte erhalten:

```
95-88-76-100-67
```

{{% alert color="note" %}}
JSON-Zahlen, die über die Java-Engine geleitet werden, liegen als Double-Werte vor. Daher würde `[95, 88]` zu `95.0-88.0` zusammengefügt. Setzen Sie die Zahlen in den JSON-Zeilen in Anführungszeichen, wenn Sie in der zusammengefügten Zelle die exakte ganzzahlige Darstellung benötigen.
{{% /alert %}}

### **Codebeispiel 3 – Vergleich des Standardverhaltens mit der Darstellung in einer einzigen Zelle**

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();
// Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default");
cells.get("B2").putValue("&=Order.Items");
// Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell");
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]');
designer.process();
for (let row = 1; row <= 5; row++) {
    const b = cells.get(row, 1).getStringValue() || "";
    const c = cells.get(row, 2).getStringValue() || "";
    if (b || c) console.log(`B${row + 1}=[${b}]  C${row + 1}=[${c}]`);
}
workbook.save("output-array-comparison.xlsx");
```

Der Standardmarker füllt in Spalte B für jedes Element eine eigene Zelle, während der Marker `arrayassingle` dasselbe Array in Spalte C in einer einzigen Zelle zusammenfasst:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Hinweise und bewährte Verfahren**
Beachten Sie die folgenden Punkte bei der Arbeit mit den Attributen `arrayassingle` und `arraydelimiter`:
- Attributwerte verwenden das Format `name:value`. Die Form mit einem Gleichheitszeichen, etwa `arrayassingle=true`, wird nicht erkannt und führt stillschweigend zum standardmäßigen Verteilungsverhalten zurück.
- Trennen Sie Attribute mit einem Komma und ohne Leerzeichen; ein Leerzeichen nach dem Komma verschiebt den Wert des Trennzeichens um ein Zeichen (siehe Warnung oben).
- Der Wert von `arraydelimiter` kann entweder ein einzelnes Zeichen, das direkt nach dem Doppelpunkt geschrieben wird, oder eine mehrzeichnige Zeichenfolge in doppelten Anführungszeichen sein.
- Wenn `arraydelimiter` weggelassen wird, werden die Elemente mit einem Komma zusammengefügt.
- Binden Sie Array-Felder über Zeilenobjekte ein, die an `setJsonDataSource` übergeben werden; einfache JavaScript-Objekte und Arrays, die an `setDataSource` übergeben werden, werden auf dieser Plattform nicht gebunden.
- JSON-Zahlen werden über die Java-Engine als Double-Werte verarbeitet (`95` wird zu `95.0` zusammengefügt); setzen Sie Zahlenwerte in den JSON-Zeilen in Anführungszeichen, wenn die exakte ganzzahlige Textdarstellung wichtig ist.
- Platzieren Sie den Smart Marker in einer Zelle, die breit genug für die Anzeige der resultierenden zusammengefügten Zeichenfolge ist; andernfalls kann der Inhalt je nach Formatierung visuell in benachbarte Zellen überlaufen.

## Verwandte Artikel
- [Filterfelder zu einer PivotTable in Aspose.Cells for Node.js via Java hinzufügen](/cells/de/nodejs-java/add-page-field-in-pivot-table/)
- [Stile auf PivotTables in Aspose.Cells for Node.js via Java anwenden](/cells/de/nodejs-java/apply-style-to-pivot-table/)
- [Seitenfeld-Layout in PivotTable ändern](/cells/de/nodejs-java/change-page-field-layout/)
- [Eine Sparkline in Aspose.Cells for Node.js via Java in ein Bild und HTML konvertieren](/cells/de/nodejs-java/convert-sparkline-to-image-and-html/)
- [Excel in das OFD-Format konvertieren](/cells/de/nodejs-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-java" >}}