---
title: Smart-Marker Einzelzellen-Array-Rendering | Aspose.Cells for Node.js via C++
linktitle: Smart-Marker Einzelzellen-Array-Rendering | Aspose.Cells
description: Erfahren Sie, wie Sie Array-Daten mithilfe der Attribute ArrayAsSingle und ExtraDelimiter in Smart Markers in eine einzelne Zelle rendern können – mit Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js Bibliothek, Tabellenkalkulation, Smart Markers, ArrayAsSingle, ExtraDelimiter, Einzelzellen-Array, Array-Rendering, Vorlage
type: docs
weight: 195
url: /de/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Rendern von Array-Daten in eine einzelne Zelle über Smart Markers. Durch die Verwendung des Attributs `ArrayAsSingle` zusammen mit dem Attribut `ExtraDelimiter` können Entwickler steuern, wie Array-Elemente innerhalb einer einzelnen Zelle getrennt werden, was eine flexible Formatierung für Berichte und Vorlagen ermöglicht.

{{% /alert %}}

## **Einführung**

Smart Markers in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellenkalkulationsdaten dynamisch mithilfe von Marker-Ausdrücken wie `&=DataSource.Field` befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage durch den `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.

Standardmäßig, wenn ein Smart Marker auf eine Array-Eigenschaft verweist (zum Beispiel `&=DataSource.Numbers`), expandiert die Engine das Array und platziert jedes Element in eine separate angrenzende Zelle – entweder horizontal über eine Zeile oder vertikal über eine Spalte. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie es vorziehen würden, das gesamte Array in eine einzige Zelle zu rendern, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.

Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die zusammen in einem Smart-Marker-Tag verwendet werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersehbar zu halten, während Sie weiterhin nativ mit Array-Datenquellen arbeiten.

## **Warum diese Funktion benötigt wird**

### **Standard-Array-Spreizverhalten**

Wenn ein Smart Marker auf eine Array-Eigenschaft verweist, expandiert Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise platziert ein Marker wie `&=Product.Tags` bei einem `string[]` mit vier Werten jeden Wert in eine eigene Zelle, wodurch andere Vorlageninhalte nach außen verschoben werden und sorgfältig gestaltete Berichtslayouts möglicherweise beschädigt werden.

### **Einschränkungen bei Anwendungsfällen**

Es gibt viele praktische Szenarien, in denen das Standard-Spreizverhalten unerwünscht ist:

- **Zusammenfassungsberichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Keyword-Listen**, die als kommagetrennte oder pipe-getrennte Werte innerhalb einer einzelnen Zelle angezeigt werden müssen.
- **Filter-Chips oder Status-Indikatoren**, die mehrere Werte an einer Stelle zur besseren Lesbarkeit gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Serienbrief), die einen einzigen konsolidierten Wert pro Zelle erwarten, anstatt einen erweiterten Bereich.
- **Plattformübergreifende Kompatibilität**, bei der einige Konsumenten keine Arrays tolerieren können, die sich über mehrere Zellen erstrecken.

### **Die Lücke, die es schließt**

Ohne einen eingebauten Mechanismus wären Entwickler gezwungen, Daten in JavaScript vorzuverarbeiten – Arrays zu getrennten Zeichenketten zusammenzufügen, bevor sie sie an den Workbook-Designer binden. Dies dupliziert die Logik, verkompliziert Datenmodelle und erhöht die Fehlerwahrscheinlichkeit. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` eliminieren diesen Workaround, indem sie die Formatierung deklarativ innerhalb des Smart Markers selbst behandeln.

## **Funktionsvorteile**

Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markers bietet mehrere Vorteile:

- **Einzelzellen-Containment**: Alle Array-Elemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersehbar bleiben.
- **Benutzerdefinierte Trennzeichensteuerung**: Geben Sie eine beliebige Trennzeichenfolge an – Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder beliebigen benutzerdefinierten Text.
- **Vorlagengesteuerte Formatierung**: Es ist kein zusätzlicher Code erforderlich, um die Daten vorzuverarbeiten; Formatierungsregeln leben innerhalb des Smart-Marker-Tags.
- **Sauberere Berichte**: Array-Daten verschieben benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Zeichenketten, Zahlen, Datumswerten und jedem anderen Datentyp, der mit einem Trennzeichen zusammengefügt werden kann.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Spreizverhalten erhalten, sodass bestehende Vorlagen unverändert weiter funktionieren.

## **So verwenden Sie diese Funktion**

### **Smart-Marker-Syntax**

Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines Standard-Smart-Markers übergeben. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Der Marker besteht aus den folgenden Teilen:

- `&=DataSource.ArrayProperty` — der Standard-Smart-Marker, der auf die Array-Eigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` — weist die Engine an, das gesamte Array in eine einzelne Zelle zu rendern. Nur der Wert `true` löst das Einzelzellen-Verhalten aus.
- `extraDelimiter=", "` — definiert das Trennzeichen, das zwischen Array-Elementen platziert wird. Der Wert ist ein Zeichenfolgenliteral; er kann leer, ein einzelnes Zeichen oder eine mehrzeichige Zeichenkette sein.

{{% alert color="primary" %}}

Das Attribut `extraDelimiter` akzeptiert jedes Zeichenfolgenliteral, einschließlich mehrzeichiger Trennzeichen, benutzerdefiniertem Text oder Escape-Sequenzen wie `\n` für zeilenumbruchgetrennte Ausgabe. Wenn das Array leer ist, bleibt die resultierende Zelle leer.

{{% /alert %}}

### **Schritt-für-Schritt-Workflow**

Der folgende Workflow beschreibt, wie Sie ein Array mithilfe von Smart Markers in eine einzelne Zelle rendern.

1. **Bereiten Sie die Datenquelle vor**: Erstellen Sie eine Klasse (oder Datenstruktur), die eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann `string[]`, `int[]` oder einen anderen unterstützten Array-Typ zurückgeben.
2. **Erstellen Sie eine Designer-Arbeitsmappe**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf die Array-Eigenschaft mit den Attributen `arrayasSingle` und `extraDelimiter` verweist.
3. **Instanziieren Sie den WorkbookDesigner**: Erstellen Sie ein `WorkbookDesigner`-Objekt, hängen Sie die Designer-Arbeitsmappe an und binden Sie Ihre Datenquelle mithilfe der Methode `setDataSource`.
4. **Verarbeiten Sie die Marker**: Rufen Sie die Methode `workbookDesigner.process()` auf, um die Smart Markers zu expandieren und die Arbeitsmappe mit echten Daten zu füllen.
5. **Speichern Sie das Ergebnis**: Speichern Sie die resultierende Arbeitsmappe als XLSX oder ein anderes unterstütztes Dateiformat auf der Festplatte.

### **Codebeispiel 1 — Grundlegendes String-Array-Rendering**

```javascript
let product = {
    Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
};

let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue('&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")');

let designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **Codebeispiel 2 — Numerisches Array mit benutzerdefiniertem Trennzeichen**

```javascript
class Student {
    constructor() {
        this.Scores = [];
    }
}

const student = new Student();
student.Scores = [95, 88, 76, 100, 67];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Scores");
worksheet.getCells().get("A2").putValue(student.Scores.join(" - "));

workbook.save("output_numericArray.xlsx");
```

### **Codebeispiel 3 — Vergleich von Standard- vs. ArrayAsSingle-Verhalten**

```javascript
var order = {
    Items: ["Apple", "Banana", "Cherry", "Date"]
};

var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Abschnitt 1: Standard-Smart-Marker - Werte werden horizontal über Zellen verteilt
cells.get("A1").putValue("Default Spreading Behavior:");
cells.get("A2").putValue("&=Order.Items");

// Abschnitt 2: Neue Einzelzellen-Darstellung mit arrayasSingle und extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

// Datenquelle binden und Smart-Marker verarbeiten
var designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setDataSource("Order", order);
designer.process();

// Die resultierende Arbeitsmappe speichern
workbook.save("output_comparison.xlsx");
```

### **Hinweise & Best Practices**

Beachten Sie die folgenden Punkte, wenn Sie mit den Attributen `ArrayAsSingle` und `ExtraDelimiter` arbeiten:

- Der Wert `extraDelimiter` wird als Zeichenfolgenliteral behandelt; escapen Sie alle Sonderzeichen, die Ihr Vorlagenprozessor interpretieren könnte.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`true` / `false`). Nur `true` löst das Einzelzellen-Verhalten aus; jeder andere Wert fällt auf das Standard-Spreizverhalten zurück.
- Wenn das Array leer oder null ist, bleibt die Zelle leer (oder enthält je nach Datentyp eine leere Zeichenkette).
- Die Funktion funktioniert mit Objektdatenquellen sowie `DataSet`- und `DataTable`-Quellen, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für zeilenumbruchgetrennte Ausgabe können Sie `\n` oder `os.EOL` als Trennzeichenwert verwenden.
- Platzieren Sie den Smart Marker in einer Zelle, die ausreichend Breite hat, um die resultierende verkettete Zeichenkette anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in benachbarte Zellen überlaufen.

## **Verwandte Artikel**

- [Zellen zusammenführen und trennen](/cells/de/nodejs-cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="javascript" >}}