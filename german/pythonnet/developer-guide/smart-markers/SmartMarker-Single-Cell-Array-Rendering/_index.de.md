---
title: SmartMarker Einzelzellen-Array-Rendering | Aspose.Cells for Python via .NET
linktitle: SmartMarker Einzelzellen-Array-Rendering | Aspose.Cells
description: Erfahren Sie, wie Sie Array-Daten mit den Attributen ArrayAsSingle und ExtraDelimiter in Smart Markers in eine einzelne Zelle rendern können – mit Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET-Bibliothek, Tabellenkalkulation, Smart Markers, ArrayAsSingle, ExtraDelimiter, Einzelzellen-Array, Array-Rendering, Vorlage
type: docs
weight: 195
url: /de/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Rendern von Array-Daten in eine einzelne Zelle über Smart Markers. Durch die Verwendung des Attributs `ArrayAsSingle` zusammen mit dem Attribut `ExtraDelimiter` können Entwickler steuern, wie Array-Elemente innerhalb einer einzelnen Zelle getrennt werden, und so eine flexible Formatierung für Berichte und Vorlagen bereitstellen.

{{% /alert %}}

## **Einführung**

Smart Markers in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellendaten dynamisch mithilfe von Marker-Ausdrücken wie `&=DataSource.Field` befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage vom `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.

Wenn ein Smart Marker auf eine Array-Eigenschaft verweist (z. B. `&=DataSource.Numbers`), expandiert die Engine standardmäßig das Array und platziert jedes Element in eine separate angrenzende Zelle – entweder horizontal über eine Zeile oder vertikal über eine Spalte. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie das gesamte Array lieber in einer einzigen Zelle rendern möchten, wobei die Elemente verkettet und durch ein frei wählbares Trennzeichen getrennt sind.

Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die zusammen innerhalb eines Smart-Marker-Tags verwendet werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersehbar zu halten und dennoch nativ mit Array-Datenquellen zu arbeiten.

## **Warum diese Funktion benötigt wird**

### **Standardmäßiges Array-Spreizverhalten**

Wenn ein Smart Marker auf eine Array-Eigenschaft verweist, expandiert Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise platziert ein Marker wie `&=Product.Tags` jeden Wert in eine eigene Zelle, wenn er auf ein `string[]` mit vier Werten verweist, wodurch andere Vorlageninhalte nach außen verschoben werden und sorgfältig gestaltete Berichtslayouts möglicherweise beschädigt werden.

### **Einschränkungen des Anwendungsfalls**

Es gibt viele praktische Szenarien, in denen das standardmäßige Spreizverhalten unerwünscht ist:

- **Zusammenfassungs-Berichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Stichwortlisten**, die als kommagetrennte oder pipe-getrennte Werte innerhalb einer einzelnen Zelle angezeigt werden sollen.
- **Filter-Chips oder Statusindikatoren**, die mehrere Werte zur besseren Lesbarkeit an einer Stelle gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Serienbrief), die einen einzelnen konsolidierten Wert pro Zelle erwarten, anstatt eines expandierten Bereichs.
- **Plattformübergreifende Kompatibilität**, bei der einige Konsumenten Arrays, die sich über mehrere Zellen erstrecken, nicht tolerieren können.

### **Die Lücke, die es füllt**

Ohne einen eingebauten Mechanismus wären Entwickler gezwungen, Daten in Python vorzuverarbeiten – Arrays zu getrennten Zeichenketten zusammenzufügen, bevor sie sie an den Workbook-Designer binden. Dies dupliziert Logik, kompliziert Datenmodelle und erhöht die Fehlerwahrscheinlichkeit. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` beseitigen diesen Workaround, indem sie die Formatierung deklarativ innerhalb des Smart Markers selbst übernehmen.

## **Funktionsvorteile**

Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markers bietet mehrere Vorteile:

- **Einzelzellen-Containment**: Alle Array-Elemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersehbar bleiben.
- **Benutzerdefinierte Trennzeichensteuerung**: Geben Sie eine beliebige Trennzeichenfolge an – Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder beliebiger benutzerdefinierter Text.
- **Vorlagengesteuerte Formatierung**: Es ist kein zusätzlicher Code zur Vorverarbeitung der Daten erforderlich; Formatierungsregeln befinden sich innerhalb des Smart-Marker-Tags.
- **Sauberere Berichte**: Array-Daten verschieben benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Zeichenketten, Zahlen, Daten und jedem anderen Datentyp, der mit einem Trennzeichen zusammengefügt werden kann.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Spreizverhalten erhalten, sodass bestehende Vorlagen unverändert weiter funktionieren.

## **Wie man diese Funktion verwendet**

### **Smart-Marker-Syntax**

Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines Standard-Smart-Markers übergeben. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Der Marker setzt sich aus den folgenden Teilen zusammen:

- `&=DataSource.ArrayProperty` — der Standard-Smart-Marker, der auf die Array-Eigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` — weist die Engine an, das gesamte Array in eine einzelne Zelle zu rendern. Nur der Wert `true` löst das Einzelzellen-Verhalten aus.
- `extraDelimiter=", "` — definiert das Trennzeichen, das zwischen Array-Elementen platziert wird. Der Wert ist ein Zeichenketten-Literal; er kann leer, ein einzelnes Zeichen oder eine mehrzeichige Zeichenkette sein.

{{% alert color="primary" %}}

Das Attribut `extraDelimiter` akzeptiert jedes Zeichenketten-Literal, einschließlich mehrzeichiger Trennzeichen, benutzerdefiniertem Text oder Escape-Sequenzen wie `\n` für zeilenumbruchgetrennte Ausgabe. Wenn das Array leer ist, bleibt die resultierende Zelle leer.

{{% /alert %}}

### **Schritt-für-Schritt-Workflow**

Der folgende Workflow beschreibt, wie ein Array mithilfe von Smart Markers in eine einzelne Zelle gerendert wird.

1. **Datenquelle vorbereiten**: Erstellen Sie eine Klasse (oder Datenstruktur), die eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann `list[str]`, `list[int]` oder einen anderen unterstützten Array-Typ zurückgeben.
2. **Designer-Arbeitsmappe erstellen**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf die Array-Eigenschaft mit den Attributen `arrayasSingle` und `extraDelimiter` verweist.
3. **WorkbookDesigner instanziieren**: Erstellen Sie ein `WorkbookDesigner`-Objekt, weisen Sie ihm die Designer-Arbeitsmappe zu und binden Sie Ihre Datenquelle mithilfe der Methode `set_data_source`.
4. **Marker verarbeiten**: Rufen Sie die Methode `WorkbookDesigner.process()` auf, um die Smart Markers zu expandieren und die Arbeitsmappe mit echten Daten zu befüllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe auf der Festplatte im Format XLSX oder einem anderen unterstützten Dateiformat.

### **Codebeispiel 1 — Grundlegendes String-Array-Rendering**

```python
class Product:
    def __init__(self):
        self.Tags = []

product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Tags")
worksheet.cells["A2"].put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")
```

### **Codebeispiel 2 — Numerisches Array mit benutzerdefiniertem Trennzeichen**

```python
class Student:
    def __init__(self):
        self.scores = []


student = Student()
student.scores = [95, 88, 76, 100, 67]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Scores")
worksheet.cells["A2"].put_value(" - ".join(str(s) for s in student.scores))

workbook.save("output_numericArray.xlsx")
```

### **Codebeispiel 3 — Vergleich des Standardverhaltens mit dem ArrayAsSingle-Verhalten**

```python
class Order:
    def __init__(self, items):
        self._items = items

    @property
    def Items(self):
        return self._items

    @Items.setter
    def Items(self, value):
        self._items = value

order = Order(["Apple", "Banana", "Cherry", "Date"])

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Abschnitt 1: Standard Smart Marker - Werte werden horizontal über Zellen verteilt
cells["A1"].put_value("Default Spreading Behavior:")
cells["A2"].put_value("&=Order.Items")

# Abschnitt 2: Neue Einzelzellendarstellung mit arrayasSingle und extraDelimiter
cells["A4"].put_value("Single Cell Rendering (arrayasSingle=true):")
cells["A5"].put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')

# Datenquelle binden und Smart Marker verarbeiten
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()

# Die resultierende Arbeitsmappe speichern
workbook.save("output_comparison.xlsx")
```

### **Hinweise & bewährte Verfahren**

Beachten Sie die folgenden Punkte, wenn Sie mit den Attributen `ArrayAsSingle` und `ExtraDelimiter` arbeiten:

- Der Wert `extraDelimiter` wird als Zeichenketten-Literal behandelt; escapen Sie alle Sonderzeichen, die Ihr Vorlagenprozessor interpretieren könnte.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`True` / `False`). Nur `True` löst das Einzelzellen-Verhalten aus; jeder andere Wert fällt auf das standardmäßige Spreizverhalten zurück.
- Wenn das Array leer oder null ist, bleibt die Zelle leer (oder enthält je nach Datentyp eine leere Zeichenkette).
- Die Funktion funktioniert sowohl mit Objekt-Datenquellen als auch mit `DataSet`- und `DataTable`-Quellen, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für zeilenumbruchgetrennte Ausgaben können Sie `\n` oder `os.linesep` als Trennzeichenwert verwenden.
- Platzieren Sie den Smart Marker in einer Zelle, die breit genug ist, um die resultierende verkettete Zeichenkette anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in benachbarte Zellen überlaufen.

## **Verwandte Artikel**

- [Smart Markers](/cells/de/python-net/smart-markers/)
- [Zellen zusammenführen und trennen](/cells/de/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}