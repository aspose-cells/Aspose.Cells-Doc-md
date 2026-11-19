---
title: SmartMarker-Rendering eines Arrays in einer einzelnen Zelle | Aspose.Cells Python via Java
description: Erfahren Sie, wie Sie Arraydaten mithilfe der Smart-Marker-Attribute `arrayassingle` und `arraydelimiter` in Aspose.Cells for Python via Java in einer einzigen Zelle rendern.
linktitle: SmartMarker-Rendering in einer einzelnen Zelle | Aspose.Cells
url: /de/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Bibliothek für Python via Java, Tabellenverarbeitung, Smart-Marker, arrayassingle, arraydelimiter, Array in einer einzelnen Zelle, Array-Rendering, Vorlage
type: docs
weight: 195
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells kann eine Array-Datenquelle mithilfe von Smart-Markern in einer einzigen Zelle rendern. Das Attribut `arrayassingle` deaktiviert die standardmäßige elementweise Verteilung, und das Attribut `arraydelimiter` legt das Trennzeichen zwischen den zusammengeführten Elementen fest – standardmäßig ein Komma, alternativ ein einzelnes Zeichen oder eine angegebene Zeichenfolge aus mehreren Zeichen in Anführungszeichen.
{{% /alert %}}

## **Einführung**

Smart-Marker in Aspose.Cells sind eine vorlagenbasierte Funktion, die Tabellendaten dynamisch mithilfe von Markerausdrücken wie `&=DataSource.Field` befüllt. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage durch den `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.
Standardmäßig wird das Array von der Engine über mehrere Zellen verteilt, wenn sich ein Smart-Marker auf ein Arrayfeld bezieht (beispielsweise `&=Product.Tags`, das an eine Liste mit vier Werten gebunden ist), und jedes Element wird in einer eigenen Zelle platziert. Dabei werden die Werte unterhalb des Markers vertikal nach unten in der Spalte verteilt. Dieses Verhalten ist in vielen Szenarien praktisch, es gibt jedoch Situationen, in denen Sie das gesamte Array lieber in einer einzigen Zelle rendern möchten, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.
Die Attribute `arrayassingle` und `arraydelimiter`, die in den Klammern eines Smart-Markers im Format `name:value` angegeben werden, erfüllen genau diese Anforderung. Sie ermöglichen kompakte und vorhersehbare Berichtslayouts und arbeiten zugleich nativ mit Array-Datenquellen.

## **Warum diese Funktion benötigt wird**

### **Standardverhalten bei der Arrayverteilung**

Wenn sich ein Smart-Marker auf ein Arrayfeld bezieht, verteilt Aspose.Cells das Array standardmäßig über mehrere Zellen. Ein Marker wie `&=Product.Tags`, der auf eine Liste mit vier Werten verweist, platziert beispielsweise jeden Wert in einer eigenen Zelle unterhalb des Markers. Dadurch werden andere Vorlageninhalte nach unten verschoben und sorgfältig entworfene Berichtslayouts möglicherweise beeinträchtigt.

### **Einschränkungen bei Anwendungsfällen**

In vielen praktischen Szenarien ist das standardmäßige Verteilungsverhalten unerwünscht:
- **Zusammenfassende Berichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Stichwortlisten**, die in einer einzelnen Zelle als durch Kommas oder senkrechte Striche getrennte Werte angezeigt werden sollen.
- **Filter-Chips oder Statusindikatoren**, die mehrere Werte an einer Stelle zwecks besserer Lesbarkeit gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Serienbriefverarbeitung), die für jede Zelle einen einzelnen konsolidierten Wert statt eines erweiterten Bereichs erwarten.
- **Plattformübergreifende Kompatibilität**, bei der einige Verbraucher keine Arrays tolerieren, die sich über mehrere Zellen erstrecken.

### **Die Lücke, die diese Funktion schließt**

Ohne einen integrierten Mechanismus müssten Entwickler die Daten in Python vorverarbeiten und Listen vor der Bindung an den `WorkbookDesigner` in durch Trennzeichen getrennte Zeichenfolgen umwandeln. Dadurch würde Logik dupliziert, die Datenmodelle wären komplizierter und die Fehlerwahrscheinlichkeit höher. Die Attribute `arrayassingle` und `arraydelimiter` beseitigen diesen Umweg, indem sie die Formatierung deklarativ im Smart-Marker selbst übernehmen.

## **Vorteile der Funktion**

Die Verwendung der Attribute `arrayassingle` und `arraydelimiter` in Smart-Markern bietet mehrere Vorteile:
- **Einbindung in eine einzelne Zelle**: Alle Arrayelemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersagbar bleiben.
- **Steuerung des Trennzeichens**: Legen Sie das gewünschte Trennzeichen fest – das Standardkomma, ein Semikolon, einen Bindestrich, einen senkrechten Strich oder eine Zeichenfolge aus mehreren Zeichen in Anführungszeichen, etwa `" | "`.
- **Vorlagenbasierte Formatierung**: Für die Vorverarbeitung der Daten ist kein zusätzlicher Code erforderlich; die Formatierungsregeln stehen im Smart-Marker-Tag.
- **Bereinigtere Berichte**: Arraydaten verschieben benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielseitige Datentypen**: Die Funktion unterstützt Zeichenkettenarrays, die als JSON-Zeilen bereitgestellt werden, einschließlich numerischer Werte, die als Zeichenfolge dargestellt werden.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Verteilungsverhalten erhalten, sodass vorhandene Vorlagen unverändert weiter funktionieren.

## **So verwenden Sie diese Funktion**

### **Smart-Marker-Syntax**

Die Attribute `arrayassingle` und `arraydelimiter` verwenden die Attributgrammatik `name:value` von Aspose.Cells innerhalb der Klammern eines standardmäßigen Smart-Markers. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Der Marker besteht aus den folgenden Komponenten:
- `&=DataSource.ArrayField` – der standardmäßige Smart-Marker, der auf das Arrayfeld der gebundenen Datenquelle verweist.
- `arrayassingle:true` – weist die Engine an, das gesamte Array in einer einzigen Zelle statt der Verteilung der Elemente zu rendern.
- `arraydelimiter:;` – optional; definiert das Trennzeichen zwischen den Arrayelementen. Wenn es weggelassen wird, wird ein Komma verwendet.

{{% alert color="warning" %}}
Schreiben Sie Attribute im Format `name:value` (mit einem Doppelpunkt, nicht mit einem Gleichheitszeichen) und trennen Sie mehrere Attribute durch ein Komma **ohne Leerzeichen**. Ein Leerzeichen nach dem Komma verschiebt den geparsten Wert um ein Zeichen – `(arrayassingle:true, arraydelimiter:;)` würde die Elemente mit dem fehlerhaften Trennzeichen `:;` statt `;` verbinden.
{{% /alert %}}

### **Formen des Trennzeichens**

- Ein einzelnes Zeichen folgt unmittelbar auf den Doppelpunkt: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Ein Trennzeichen aus mehreren Zeichen wird in doppelten Anführungszeichen geschrieben: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Workflow Schritt für Schritt**

Der folgende Workflow beschreibt, wie ein Array mithilfe von Smart-Markern in einer einzigen Zelle gerendert wird.
1. **Datenquelle vorbereiten**: Ordnen Sie jeden Datensatz als JSON-Objekt an, dessen Feld ein Array enthält, beispielsweise `{"Tags": ["C#", "Aspose"]}`. Einfache Python-Klasseninstanzen und Wörterbücher, die an `setDataSource` übergeben werden, werden auf dieser Plattform nicht gebunden – JSON-Zeilen sind die unterstützte tabellenförmige Darstellung.
2. **Designer-Arbeitsmappe erstellen**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf das Arrayfeld verweist und das Attribut `arrayassingle` enthält (sowie `arraydelimiter`, wenn ein benutzerdefiniertes Trennzeichen benötigt wird).
3. **`WorkbookDesigner` instanziieren**: Erstellen Sie einen `WorkbookDesigner` für die Arbeitsmappe und fügen Sie die JSON-Zeilen mit `setJsonDataSource` hinzu.
4. **Marker verarbeiten**: Rufen Sie die Methode `WorkbookDesigner.process()` auf, um die Smart-Marker zu erweitern und die Arbeitsmappe mit den tatsächlichen Daten zu befüllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe im XLSX-Format oder in einem anderen unterstützten Dateiformat auf der Festplatte.

### **Codebeispiel 1 – Grundlegendes Rendering eines Zeichenkettenarrays**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-single.xlsx")
```

Das Beispiel gibt den zusammengeführten Wert des gesamten Arrays aus. Die vier Tags werden in einer Zelle durch das Standardkomma getrennt:

```
C#,Aspose,SmartMarker,Excel
```

### **Codebeispiel 2 – Numerische Werte mit einem benutzerdefinierten Trennzeichen**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Scores")
# arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-numeric.xlsx")
```

Wenn die Punktzahlen als JSON-Zeichenfolgen bereitgestellt werden, bleiben in der zusammengeführten Ausgabe die einfachen Zahlen erhalten:

```
95-88-76-100-67
```

{{% alert color="note" %}}
JSON-Zahlen, die durch die Java-Engine verarbeitet werden, treffen als Doubles ein, sodass `[95, 88]` zu `95.0-88.0` zusammengeführt würde. Setzen Sie die Zahlen in den JSON-Zeilen in Anführungszeichen, wenn der exakte Ganzzahlentext in der zusammengeführten Zelle erhalten bleiben soll.
{{% /alert %}}

### **Codebeispiel 3 – Vergleich des Standard-Renderings mit dem Rendering in einer einzelnen Zelle**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
cells = workbook.getWorksheets().get(0).getCells()
# Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default")
cells.get("B2").putValue("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell")
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).getStringValue() or ""
    c = cells.get(row, 2).getStringValue() or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

Der Standardmarker füllt in Spalte B für jedes Element eine eigene Zelle, während der `arrayassingle`-Marker dasselbe Array in Spalte C in einer einzigen Zelle zusammenfasst:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Hinweise und bewährte Verfahren**

Beachten Sie beim Arbeiten mit den Attributen `arrayassingle` und `arraydelimiter` folgende Punkte:
- Attributwerte verwenden das Format `name:value`. Die Form mit einem Gleichheitszeichen, etwa `arrayassingle=true`, wird nicht erkannt und führt stillschweigend zum Standardverhalten der Verteilung zurück.
- Trennen Sie Attribute durch ein Komma ohne Leerzeichen; ein Leerzeichen nach dem Komma verschiebt den Wert des Trennzeichens um ein Zeichen (siehe Warnung oben).
- Der Wert von `arraydelimiter` kann ein einzelnes Zeichen sein, das unmittelbar nach dem Doppelpunkt steht, oder eine Zeichenfolge aus mehreren Zeichen in doppelten Anführungszeichen.
- Wenn `arraydelimiter` weggelassen wird, werden die Elemente durch ein Komma verbunden.
- Stellen Sie Arrayfelder über Zeilenobjekte von `setJsonDataSource` bereit; einfache Python-Objekte und Wörterbücher, die an `setDataSource` übergeben werden, werden auf dieser Plattform nicht gebunden.
- JSON-Zahlen treffen über die Java-Engine als Doubles ein (`95` wird zu `95.0`); setzen Sie numerische Werte in den JSON-Zeilen in Anführungszeichen, wenn der exakte Ganzzahlentext wichtig ist.
- Platzieren Sie den Smart-Marker in einer Zelle mit ausreichender Breite, um die resultierende verkettete Zeichenfolge anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in benachbarte Zellen überlaufen.

## **Verwandte Artikel**
- [Filterfelder zu einer PivotTable in Aspose.Cells for Python via Java](/cells/de/python-java/add-page-field-in-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen in Aspose.Cells for Python via Java](/cells/de/python-java/apply-style-to-pivot-table/)
- [Ändern des Seitenfeldlayouts in einer Pivot-Tabelle](/cells/de/python-java/change-page-field-layout/)
- [Sparkline in Aspose.Cells for Python via Java in Bild und HTML konvertieren](/cells/de/python-java/convert-sparkline-to-image-and-html/)
- [Konvertieren von Excel in das OFD-Format](/cells/de/python-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python" >}}