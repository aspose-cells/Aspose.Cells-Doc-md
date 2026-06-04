---
title: SmartMarker-Einzelzellen-Array-Rendering | Aspose.Cells Python via Java
description: Erfahren Sie, wie Sie Array-Daten mit den Attributen ArrayAsSingle und ExtraDelimiter in Smart Markers in eine einzelne Zelle rendern, mit Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java Bibliothek, Tabellenkalkulation, Smart Markers, ArrayAsSingle, ExtraDelimiter, Einzelzellen-Array, Array-Rendering, Vorlage
type: docs
weight: 195
url: /de/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Rendern von Array-Daten in eine einzelne Zelle über Smart Markers. Durch die Verwendung des Attributs `ArrayAsSingle` zusammen mit dem Attribut `ExtraDelimiter` können Entwickler steuern, wie Array-Elemente innerhalb einer einzelnen Zelle getrennt werden, was eine flexible Formatierung für Berichte und Vorlagen ermöglicht.

{{% /alert %}}

## **Einführung**

Smart Markers in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellendaten dynamisch mithilfe von Marker-Ausdrücken wie `&=DataSource.Field` befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage vom `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.

Standardmäßig, wenn ein Smart Marker auf eine Array-Eigenschaft verweist (z. B. `&=DataSource.Numbers`), expandiert die Engine das Array und platziert jedes Element in eine eigene angrenzende Zelle – entweder horizontal über eine Zeile oder vertikal über eine Spalte. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie es vorziehen würden, das gesamte Array in eine einzige Zelle zu rendern, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.

Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die zusammen innerhalb eines Smart-Marker-Tags verwendet werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersagbar zu halten, während Sie dennoch nativ mit Array-Datenquellen arbeiten.

## **Warum diese Funktion benötigt wird**

### **Standardverhalten der Array-Verteilung**

Wenn ein Smart Marker auf eine Array-Eigenschaft verweist, expandiert Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise platziert ein Marker wie `&=Product.Tags` bei einem `string[]` mit vier Werten jeden Wert in eine eigene Zelle, wodurch andere Vorlageninhalte nach außen verschoben werden und potenziell sorgfältig gestaltete Berichtslayouts beschädigt werden.

### **Einschränkungen des Anwendungsfalls**

Es gibt viele praktische Szenarien, in denen das Standardverteilungsverhalten unerwünscht ist:

- **Zusammenfassungs-Berichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Stichwortlisten**, die als kommagetrennte oder pipe-getrennte Werte innerhalb einer einzelnen Zelle angezeigt werden müssen.
- **Filter-Chips oder Statusindikatoren**, die mehrere Werte an einer Stelle zur besseren Lesbarkeit gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Serienbrief), die einen einzelnen konsolidierten Wert pro Zelle anstelle eines expandierten Bereichs erwarten.
- **Plattformübergreifende Kompatibilität**, bei der einige Konsumenten Arrays, die sich über mehrere Zellen erstrecken, nicht tolerieren können.

### **Die Lücke, die sie füllt**

Ohne einen eingebauten Mechanismus wären Entwickler gezwungen, Daten in Python vorzuverarbeiten – Arrays in getrennte Zeichenketten zu verbinden, bevor sie sie an den Workbook-Designer binden. Dies dupliziert Logik, kompliziert Datenmodelle und erhöht die Fehlerwahrscheinlichkeit. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` beseitigen diesen Workaround, indem sie die Formatierung deklarativ innerhalb des Smart Markers selbst handhaben.

## **Funktionsvorteile**

Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markers bietet mehrere Vorteile:

- **Einzelzellen-Containment**: Alle Array-Elemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersagbar bleiben.
- **Benutzerdefinierte Trennzeichensteuerung**: Geben Sie eine beliebige Trennzeichenfolge an – Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder beliebigen benutzerdefinierten Text.
- **Vorlagengesteuerte Formatierung**: Es ist kein zusätzlicher Code erforderlich, um die Daten vorzuverarbeiten; Formatierungsregeln leben innerhalb des Smart-Marker-Tags.
- **Sauberere Berichte**: Array-Daten verschieben benachbarte Vorlageninhalte nicht mehr in verschiedene Zeilen oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Zeichenketten, Zahlen, Datumsangaben und jedem anderen Datentyp, der mit einem Trennzeichen verbunden werden kann.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Verteilungsverhalten erhalten, sodass bestehende Vorlagen unverändert weiter funktionieren.

## **So verwenden Sie diese Funktion**

### **Smart-Marker-Syntax**

Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines Standard-Smart-Markers übergeben. Die allgemeine Syntax ist:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Der Marker besteht aus den folgenden Teilen:

- `&=DataSource.ArrayProperty` – der Standard-Smart-Marker, der auf die Array-Eigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` – weist die Engine an, das gesamte Array in eine einzelne Zelle zu rendern. Nur der Wert `true` löst das Einzelzellen-Verhalten aus.
- `extraDelimiter=", "` – definiert das Trennzeichen, das zwischen Array-Elementen platziert wird. Der Wert ist ein Zeichenkettenliteral; er kann leer, ein einzelnes Zeichen oder eine mehrzeichige Zeichenkette sein.

{{% alert color="primary" %}}

Das Attribut `extraDelimiter` akzeptiert jedes Zeichenkettenliteral, einschließlich mehrzeichiger Trennzeichen, benutzerdefiniertem Text oder Escape-Sequenzen wie `\n` für zeilenumbruchgetrennte Ausgabe. Wenn das Array leer ist, bleibt die resultierende Zelle leer.

{{% /alert %}}

### **Schritt-für-Schritt-Workflow**

Der folgende Workflow beschreibt, wie ein Array mithilfe von Smart Markers in eine einzelne Zelle gerendert wird.

1. **Bereiten Sie die Datenquelle vor**: Erstellen Sie eine Klasse (oder Datenstruktur), die eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann `string[]`, `int[]` oder einen anderen unterstützten Array-Typ zurückgeben.
2. **Erstellen Sie eine Designer-Arbeitsmappe**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf die Array-Eigenschaft mit den Attributen `arrayasSingle` und `extraDelimiter` verweist.
3. **Instanziieren Sie den WorkbookDesigner**: Erstellen Sie ein `WorkbookDesigner`-Objekt, hängen Sie die Designer-Arbeitsmappe an und binden Sie Ihre Datenquelle mit der Methode `set_data_source`.
4. **Verarbeiten Sie die Marker**: Rufen Sie die Methode `WorkbookDesigner.process()` auf, um die Smart Markers zu expandieren und die Arbeitsmappe mit echten Daten zu befüllen.
5. **Speichern Sie das Ergebnis**: Speichern Sie die resultierende Arbeitsmappe auf der Festplatte im XLSX- oder einem anderen unterstützten Dateiformat.

### **Codebeispiel 1 – Grundlegendes Zeichenketten-Array-Rendering**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

class Product:
    def __init__(self, tags):
        self._tags = tags
    
    def getTags(self):
        return self._tags

product = Product(["C#", "Aspose", "SmartMarker", "Excel"])

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Tags")
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = WorkbookDesigner()
designer.setWorkbook(workbook)
designer.setDataSource("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")

jpype.shutdownJVM()
```

### **Codebeispiel 2 – Numerisches Array mit benutzerdefiniertem Trennzeichen**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook

# Definiere die Student-Klasse
class Student:
    def __init__(self):
        self.Scores = []

student = Student()
student.Scores = [95, 88, 76, 100, 67]

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Scores")
worksheet.getCells().get("A2").putValue(" - ".join(str(s) for s in student.Scores))

workbook.save("output_numericArray.xlsx")

jpype.shutdownJVM()
```

### **Codebeispiel 3 – Vergleich von Standard- vs. ArrayAsSingle-Verhalten**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

# Definieren Sie die Datenquelle als Wörterbuch (entspricht der Order-Klasse)
order = {"Items": ["Apple", "Banana", "Cherry", "Date"]}

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Abschnitt 1: Standard-Smart-Marker - Werte werden horizontal über Zellen verteilt
cells.get("A1").putValue("Default Spreading Behavior:")
cells.get("A2").putValue("&=Order.Items")

# Abschnitt 2: Neue Einzelzellendarstellung mit arrayasSingle und extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")")

# Datenquelle binden und Smart-Marker verarbeiten
designer = WorkbookDesigner(workbook)
designer.setDataSource("Order", order)
designer.process()

# Speichern Sie die resultierende Arbeitsmappe
workbook.save("output_comparison.xlsx")

jpype.shutdownJVM()
```

### **Hinweise & bewährte Praktiken**

Beachten Sie die folgenden Punkte, wenn Sie mit den Attributen `ArrayAsSingle` und `ExtraDelimiter` arbeiten:

- Der Wert `extraDelimiter` wird als Zeichenkettenliteral behandelt; escapen Sie alle Sonderzeichen, die Ihr Vorlagenprozessor interpretieren könnte.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`true` / `false`). Nur `true` löst das Einzelzellen-Verhalten aus; jeder andere Wert fällt auf das Standardverteilungsverhalten zurück.
- Wenn das Array leer oder null ist, bleibt die Zelle leer (oder enthält je nach Datentyp eine leere Zeichenkette).
- Die Funktion ist mit Objektdatenquellen sowie mit `DataSet`- und `DataTable`-Quellen kompatibel, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für zeilenumbruchgetrennte Ausgabe können Sie `\n` oder die Newline-Konstante der Plattform als Trennzeichenwert verwenden.
- Platzieren Sie den Smart Marker in einer Zelle, die ausreichend Breite hat, um die resultierende verkettete Zeichenkette anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in angrenzende Zellen überlaufen.

## **Verwandte Artikel**

- [Smart Markers](/cells/de/python-java/smart-markers/)

{{< app/cells/assistant language="python" >}}