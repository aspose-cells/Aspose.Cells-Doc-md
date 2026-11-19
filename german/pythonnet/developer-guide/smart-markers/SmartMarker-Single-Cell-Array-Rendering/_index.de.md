---
title: SmartMarker-Arraydarstellung in einer Einzelzelle | Aspose.Cells for Python via .NET
description: Erfahren Sie, wie Sie Arraydaten mithilfe der Smart-Marker-Attribute `arrayassingle` und `arraydelimiter` in Aspose.Cells for Python via .NET in einer einzigen Zelle rendern.
linktitle: SmartMarker-Arraydarstellung in einer Einzelzelle | Aspose.Cells
url: /de/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Bibliothek für Python via .NET, Tabellenkalkulation, Smart Markers, arrayassingle, arraydelimiter, Einzelzellen-Array, Arraydarstellung, Vorlage
type: docs
weight: 195
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells kann eine Array-Datenquelle mithilfe von Smart Markers in genau einer Zelle rendern. Das Attribut `arrayassingle` deaktiviert die standardmäßige elementweise Verteilung, und das Attribut `arraydelimiter` legt das Trennzeichen fest, das zwischen den zusammengefügten Elementen eingefügt wird – standardmäßig ein Komma oder, sofern angegeben, ein beliebiges einzelnes Zeichen beziehungsweise eine Zeichenfolge aus mehreren Zeichen in Anführungszeichen.
{{% /alert %}}

## **Einführung**

Smart Markers in Aspose.Cells sind eine vorlagenbasierte Funktion, die Tabellenkalkulationsdaten dynamisch mithilfe von Markerausdrücken wie `&=DataSource.Field` befüllt. Der Marker wird in einer Design-Arbeitsmappe platziert. Wenn die Vorlage mit `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.
Standardmäßig klappt die Verarbeitungslogik bei einem Smart Marker, der auf ein Arrayfeld verweist – beispielsweise `&=Product.Tags`, das an eine Liste mit vier Werten gebunden ist –, das Array auf und legt jedes Element in eine eigene Zelle. Dabei werden die Werte unterhalb des Markers vertikal in der Spalte nach unten verteilt. Dieses Verhalten ist in vielen Szenarien praktisch, es gibt jedoch Situationen, in denen Sie das gesamte Array lieber in einer einzigen Zelle rendern möchten, wobei die Elemente durch ein Trennzeichen Ihrer Wahl getrennt werden.
Die Attribute `arrayassingle` und `arraydelimiter`, die in den Klammern eines Smart Markers im Format `name:value` angegeben werden, erfüllen genau diese Anforderung. Sie ermöglichen kompakte und vorhersagbare Berichtslayouts und arbeiten zugleich nativ mit Array-Datenquellen.

## **Warum diese Funktion erforderlich ist**

### **Standardmäßiges Verteilen von Arrays**

Wenn ein Smart Marker auf ein Arrayfeld verweist, klappt Aspose.Cells das Array standardmäßig über mehrere Zellen auf. Ein Marker wie `&=Product.Tags` für eine Liste mit vier Werten legt beispielsweise jeden Wert in eine eigene Zelle unterhalb des Markers. Dadurch werden andere Inhalte der Vorlage nach außen verschoben, und sorgfältig entworfene Berichtslayouts können beeinträchtigt werden.

### **Einschränkungen bei der Verwendung**

Es gibt viele praktische Szenarien, in denen das standardmäßige Verteilungsverhalten unerwünscht ist:
- **Zusammenfassungsberichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Kennzeichnungs-, Etikett- oder Stichwortlisten**, die in einer einzelnen Zelle als kommagetrennte oder durch senkrechte Striche getrennte Werte angezeigt werden sollen.
- **Filterchips oder Statusanzeigen**, die mehrere Werte zur Verbesserung der Lesbarkeit an einer Stelle zusammenfassen.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Ausgabe, Serienbriefverarbeitung), die pro Zelle einen einzigen konsolidierten Wert statt eines aufgeklappten Bereichs erwarten.
- **Plattformübergreifende Kompatibilität**, bei der einige Systeme keine über mehrere Zellen verteilten Arrays tolerieren.

### **Die dadurch geschlossene Lücke**

Ohne einen integrierten Mechanismus müssten Entwickler die Daten in Python vorverarbeiten und Listen zu durch Trennzeichen getrennten Zeichenketten verbinden, bevor sie diese an den `WorkbookDesigner` binden. Dadurch wird Logik dupliziert, werden Datenmodelle komplizierter und die Fehlerwahrscheinlichkeit steigt. Die Attribute `arrayassingle` und `arraydelimiter` eliminieren diesen Umweg, indem sie die Formatierung deklarativ im Smart Marker selbst übernehmen.

## **Vorteile der Funktion**

Die Verwendung der Attribute `arrayassingle` und `arraydelimiter` in Ihren Smart Markers bietet mehrere Vorteile:
- **Enthalten in einer einzelnen Zelle**: Alle Arrayelemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersagbar bleiben.
- **Steuerung des Trennzeichens**: Legen Sie das gewünschte Trennzeichen fest – das Standardkomma, ein Semikolon, einen Bindestrich, einen senkrechten Strich oder eine Zeichenfolge aus mehreren Zeichen in Anführungszeichen, beispielsweise `" | "`.
- **Vorlagenbasierte Formatierung**: Für die Vorverarbeitung der Daten ist kein zusätzlicher Code erforderlich; die Formatierungsregeln sind im Smart-Marker-Tag enthalten.
- **Übersichtlichere Berichte**: Arraydaten verschieben benachbarte Inhalte der Vorlage nicht mehr in andere Zeilen oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Listen aus Zeichenketten und Zahlen, die als JSON-Zeilen bereitgestellt werden.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Verteilungsverhalten erhalten, sodass vorhandene Vorlagen unverändert weiter funktionieren.

## **Verwendung dieser Funktion**

### **Smart-Marker-Syntax**

Die Attribute `arrayassingle` und `arraydelimiter` verwenden die Attributgrammatik `name:value` von Aspose.Cells innerhalb der Klammern eines standardmäßigen Smart Markers. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Der Marker besteht aus den folgenden Teilen:
- `&=DataSource.ArrayField` – der standardmäßige Smart Marker, der auf das Arrayfeld der gebundenen Datenquelle verweist.
- `arrayassingle:true` – weist die Verarbeitungslogik an, das gesamte Array in einer einzigen Zelle zu rendern, statt die Elemente zu verteilen.
- `arraydelimiter:;` – optional; legt das Trennzeichen fest, das zwischen den Arrayelementen eingefügt wird. Wenn es weggelassen wird, wird ein Komma verwendet.

{{% alert color="warning" %}}
Schreiben Sie Attribute im Format `name:value` (mit Doppelpunkt statt Gleichheitszeichen) und trennen Sie mehrere Attribute durch ein Komma **ohne Leerzeichen**. Ein Leerzeichen nach dem Komma verschiebt den geparsten Wert um ein Zeichen – `(arrayassingle:true, arraydelimiter:;)` fügt die Elemente dann mit dem fehlerhaften Trennzeichen `:;` statt `;` zusammen.
{{% /alert %}}

### **Formen des Trennzeichens**

- Ein einzelnes Zeichen folgt unmittelbar auf den Doppelpunkt: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Ein Trennzeichen aus mehreren Zeichen wird in doppelten Anführungszeichen geschrieben: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Arbeitsablauf Schritt für Schritt**

Der folgende Arbeitsablauf beschreibt, wie ein Array mithilfe von Smart Markers in einer einzigen Zelle gerendert wird.
1. **Datenquelle vorbereiten**: Ordnen Sie jeden Datensatz als JSON-Objekt an, dessen Feld ein Array enthält, beispielsweise `{"Tags": ["C#", "Aspose"]}`. Instanzen gewöhnlicher Python-Klassen, Wörterbücher und Listen, die an `set_data_source` übergeben werden, binden auf dieser Plattform keine Arrayfelder – JSON-Zeilen sind die unterstützte tabellarische Form.
2. **Design-Arbeitsmappe erstellen**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf das Arrayfeld verweist und das Attribut `arrayassingle` enthält (sowie bei Bedarf `arraydelimiter`).
3. **WorkbookDesigner instanziieren**: Erstellen Sie einen `WorkbookDesigner` für die Arbeitsmappe und binden Sie Ihre JSON-Zeilen mit `set_json_data_source` an.
4. **Marker verarbeiten**: Rufen Sie die Methode `WorkbookDesigner.process()` auf, um die Smart Markers aufzuklappen und die Arbeitsmappe mit echten Daten zu befüllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe im XLSX-Format oder in einem anderen unterstützten Dateiformat auf der Festplatte.

### **Codebeispiel 1 – Grundlegende Darstellung eines Zeichenkettenarrays**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-single.xlsx")
```

Das Beispiel gibt den zusammengefügten Wert des gesamten Arrays aus. Die vier Tags werden in einer Zelle durch das Standardkomma getrennt:

```
C#,Aspose,SmartMarker,Excel
```

### **Codebeispiel 2 – Numerisches Array mit einem benutzerdefinierten Trennzeichen**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
# arraydelimiter:- joins the numbers with a hyphen
worksheet.cells.get("A2").put_value("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Student",
    '[{"Scores": [95, 88, 76, 100, 67]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-numeric.xlsx")
```

JSON-Zahlen werden genauso wie Zeichenketten zusammengefügt – jedes Element behält seine rein numerische Textdarstellung:

```
95-88-76-100-67
```

### **Codebeispiel 3 – Vergleich des Standardverhaltens mit der Darstellung in einer einzigen Zelle**

```python
import aspose.cells as ac

workbook = ac.Workbook()
cells = workbook.worksheets[0].cells
# Column B: default marker — values spread vertically down the column
cells.get("B1").put_value("Default")
cells.get("B2").put_value("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").put_value("Single cell")
cells.get("C2").put_value("&=Order.Items(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).string_value or ""
    c = cells.get(row, 2).string_value or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

Der Standardmarker füllt in Spalte B eine Zelle pro Element, während der Marker `arrayassingle` dasselbe Array in Spalte C in einer einzigen Zelle zusammenfasst:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Hinweise und bewährte Vorgehensweisen**

Beachten Sie beim Arbeiten mit den Attributen `arrayassingle` und `arraydelimiter` folgende Punkte:
- Attributwerte verwenden das Format `name:value`. Eine Form mit Gleichheitszeichen, etwa `arrayassingle=true`, wird nicht erkannt und fällt stillschweigend auf das standardmäßige Verteilungsverhalten zurück.
- Trennen Sie Attribute durch ein Komma ohne Leerzeichen; ein Leerzeichen nach dem Komma verschiebt den Wert des Trennzeichens um ein Zeichen (siehe Warnung oben).
- Der Wert von `arraydelimiter` kann ein einzelnes Zeichen sein, das unmittelbar nach dem Doppelpunkt steht, oder eine Zeichenfolge aus mehreren Zeichen in doppelten Anführungszeichen.
- Wenn `arraydelimiter` weggelassen wird, werden die Elemente mit einem Komma verbunden.
- Bereitstellen Sie Arrayfelder über die Zeilenobjekte von `set_json_data_source`. Gewöhnliche Python-Objekte und Wörterbücher, die an `set_data_source` übergeben werden, werden auf dieser Plattform nicht gebunden, und eine benutzerdefinierte `ICellsDataTable`, deren Spalte eine Python-Liste zurückgibt, rendert den Text des Listencontainers, statt die Elemente zusammenzufügen.
- JSON-Zahlen behalten in der zusammengefügten Ausgabe ihre einfache Ganzzahlform.

## **Verwandte Artikel**
- [Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for Python via .NET hinzufügen](/cells/de/python-net/add-page-field-in-pivot-table/)
- [Stile auf Pivot-Tabellen in Aspose.Cells for Python via .NET anwenden](/cells/de/python-net/apply-style-to-pivot-table/)
- [Ändern des Seitenfeldlayouts in einer Pivot-Tabelle](/cells/de/python-net/change-page-field-layout/)
- [Sparklines in Bild und HTML konvertieren in Aspose.Cells for Python via .NET](/cells/de/python-net/convert-sparkline-to-image-and-html/)
- [Konvertieren von Excel in das OFD-Format](/cells/de/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}