---
title: Smart-Marker Einzelzell-Array-Rendering | Aspose.Cells for Node.js via Java
description: Erfahren Sie, wie Array-Daten mit den Attributen ArrayAsSingle und ExtraDelimiter in Smart Markers in eine einzelne Zelle gerendert werden können – mit Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java-Bibliothek, Tabellenkalkulation, Smart Markers, ArrayAsSingle, ExtraDelimiter, Einzelzell-Array, Array-Rendering, Vorlage
type: docs
weight: 195
url: /de/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Rendern von Array-Daten in eine einzelne Zelle über Smart Markers. Durch die Verwendung des Attributs `ArrayAsSingle` zusammen mit dem Attribut `ExtraDelimiter` können Entwickler steuern, wie Array-Elemente innerhalb einer einzelnen Zelle getrennt werden, und so eine flexible Formatierung für Berichte und Vorlagen ermöglichen.

{{% /alert %}}

## **Einführung**

Smart Markers in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellendaten mithilfe von Marker-Ausdrücken wie `&=DataSource.Field` dynamisch befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage durch den `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.

Standardmäßig expandiert die Engine das Array, wenn ein Smart-Marker auf eine Array-Eigenschaft verweist (z. B. `&=DataSource.Numbers`), und platziert jedes Element in eine separate, angrenzende Zelle – entweder horizontal über eine Zeile oder vertikal über eine Spalte. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie das gesamte Array lieber in einer einzigen Zelle rendern möchten, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.

Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die zusammen innerhalb eines Smart-Marker-Tags verwendet werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersagbar zu halten und gleichzeitig nativ mit Array-Datenquellen zu arbeiten.

## **Warum diese Funktion benötigt wird**

### **Standardmäßiges Array-Spreizverhalten**

Wenn ein Smart-Marker auf eine Array-Eigenschaft verweist, expandiert Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise platziert ein Marker wie `&=Product.Tags` bei einem `string[]` mit vier Werten jeden Wert in eine eigene Zelle, wodurch andere Vorlageninhalte nach außen verschoben werden und sorgfältig gestaltete Berichtslayouts möglicherweise beschädigt werden.

### **Einschränkungen im Anwendungsfall**

Es gibt viele praktische Szenarien, in denen das standardmäßige Spreizverhalten unerwünscht ist:

- **Zusammenfassungsberichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Stichwortlisten**, die als kommagetrennte oder pipe-getrennte Werte innerhalb einer einzelnen Zelle angezeigt werden sollen.
- **Filter-Chips oder Status-Indikatoren**, die mehrere Werte zur besseren Lesbarkeit an einem Ort gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Serienbrief), die einen einzigen konsolidierten Wert pro Zelle erwarten, anstatt einen erweiterten Bereich.
- **Plattformübergreifende Kompatibilität**, bei der einige Konsumenten keine Arrays tolerieren können, die sich über mehrere Zellen erstrecken.

### **Die Lücke, die sie füllt**

Ohne einen eingebauten Mechanismus wären Entwickler gezwungen, Daten in JavaScript vorzuverarbeiten – Arrays zu begrenzten Zeichenketten zusammenzufügen, bevor sie sie an den Workbook-Designer binden. Dies dupliziert Logik, verkompliziert Datenmodelle und erhöht die Fehlerwahrscheinlichkeit. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` beseitigen diesen Workaround, indem sie die Formatierung deklarativ innerhalb des Smart-Markers selbst handhaben.

## **Funktionsvorteile**

Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markers bietet mehrere Vorteile:

- **Einzelzell-Containment**: Alle Array-Elemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersagbar bleiben.
- **Benutzerdefinierte Trennzeichensteuerung**: Geben Sie eine beliebige Trennzeichenfolge an – Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder beliebiger benutzerdefinierter Text.
- **Vorlagengesteuerte Formatierung**: Es ist kein zusätzlicher Code zur Vorverarbeitung der Daten erforderlich; Formatierungsregeln befinden sich im Smart-Marker-Tag.
- **Sauberere Berichte**: Array-Daten verschieben benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Zeichenketten, Zahlen, Datumsangaben und jedem anderen Datentyp, der mit einem Trennzeichen zusammengefügt werden kann.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Spreizverhalten erhalten, sodass bestehende Vorlagen unverändert weiter funktionieren.

## **So verwenden Sie diese Funktion**

### **Smart-Marker-Syntax**

Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines Standard-Smart-Markers übergeben. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Der Marker setzt sich aus folgenden Teilen zusammen:

- `&=DataSource.ArrayProperty` – der Standard-Smart-Marker, der auf die Array-Eigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` – weist die Engine an, das gesamte Array in einer einzelnen Zelle zu rendern. Nur der Wert `true` löst das Einzelzellverhalten aus.
- `extraDelimiter=", "` – definiert das Trennzeichen, das zwischen Array-Elementen platziert wird. Der Wert ist ein Zeichenkettenliteral; er kann leer sein, ein einzelnes Zeichen oder eine mehrzeichige Zeichenkette.

{{% alert color="primary" %}}

Das Attribut `extraDelimiter` akzeptiert jedes Zeichenkettenliteral, einschließlich mehrzeichiger Trennzeichen, benutzerdefiniertem Text oder Escape-Sequenzen wie `\n` für zeilenumbruch-getrennte Ausgabe. Wenn das Array leer ist, bleibt die resultierende Zelle leer.

{{% /alert %}}

### **Schritt-für-Schritt-Workflow**

Der folgende Workflow beschreibt, wie ein Array mit Smart Markers in eine einzelne Zelle gerendert wird.

1. **Bereiten Sie die Datenquelle vor**: Erstellen Sie eine Klasse (oder Datenstruktur), die eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann `string[]`, `int[]` oder einen anderen unterstützten Array-Typ zurückgeben.
2. **Erstellen Sie eine Designer-Arbeitsmappe**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf die Array-Eigenschaft mit den Attributen `arrayasSingle` und `extraDelimiter` verweist.
3. **Instanziieren Sie den WorkbookDesigner**: Erstellen Sie ein `WorkbookDesigner`-Objekt, weisen Sie die Designer-Arbeitsmappe zu und binden Sie Ihre Datenquelle mit der Methode `setDataSource`.
4. **Verarbeiten Sie die Marker**: Rufen Sie die Methode `workbookDesigner.process()` auf, um die Smart-Marker zu expandieren und die Arbeitsmappe mit echten Daten zu befüllen.
5. **Speichern Sie das Ergebnis**: Speichern Sie die resultierende Arbeitsmappe auf der Festplatte im XLSX-Format oder in einem anderen unterstützten Dateiformat.

### **Codebeispiel 1 – Grundlegendes Rendern von Zeichenketten-Arrays**

```javascript
class Product {
    constructor() {
        this.Tags = null;
    }
}

const product = new Product();
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

const designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **Codebeispiel 2 – Numerisches Array mit benutzerdefiniertem Trennzeichen**

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

### **Codebeispiel 3 – Vergleich von Standard- vs. ArrayAsSingle-Verhalten**

```javascript
const AsposeCells = require("aspose.cells");

function main() {
    const order = {
        Items: ["Apple", "Banana", "Cherry", "Date"]
    };

    const workbook = new AsposeCells.Workbook();
    const sheet = workbook.getWorksheets().get(0);
    const cells = sheet.getCells();

    // Abschnitt 1: Standard-Smart-Marker - Werte werden horizontal über Zellen verteilt
    cells.get("A1").putValue("Default Spreading Behavior:");
    cells.get("A2").putValue("&=Order.Items");

    // Abschnitt 2: Neue Einzelzellendarstellung mit arrayasSingle und extraDelimiter
    cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
    cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Datenquelle binden und Smart Marker verarbeiten
    const designer = new AsposeCells.WorkbookDesigner(workbook);
    designer.setDataSource("Order", order);
    designer.process();

    // Die resultierende Arbeitsmappe speichern
    workbook.save("output_comparison.xlsx");
}

main();
```

### **Hinweise & Best Practices**

Beachten Sie die folgenden Punkte, wenn Sie mit den Attributen `ArrayAsSingle` und `ExtraDelimiter` arbeiten:

- Der Wert von `extraDelimiter` wird als Zeichenkettenliteral behandelt; escapen Sie alle Sonderzeichen, die Ihr Vorlagenprozessor interpretieren könnte.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`true` / `false`). Nur `true` löst das Einzelzellverhalten aus; jeder andere Wert fällt auf das standardmäßige Spreizverhalten zurück.
- Wenn das Array leer oder null ist, bleibt die Zelle leer (oder enthält je nach Datentyp eine leere Zeichenkette).
- Die Funktion funktioniert mit Objekt-Datenquellen sowie mit `DataSet`- und `DataTable`-Datenquellen, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für eine zeilenumbruch-getrennte Ausgabe können Sie `\n` als Trennzeichenwert verwenden.
- Platzieren Sie den Smart-Marker in einer Zelle, die ausreichend Breite hat, um die resultierende verkettete Zeichenkette anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in benachbarte Zellen überlaufen.



{{< app/cells/assistant language="javascript" >}}