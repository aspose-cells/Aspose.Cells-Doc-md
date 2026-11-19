---
title: Smart Marker in Kopfzeilen und Fußzeilen | Aspose.Cells for Python via Java
linktitle: Kopf- und Fußzeilen-Smart-Marker | Aspose.Cells
description: Platzieren Sie Smart-Marker-Platzhalter in Seiten-Kopf- und Fußzeilen mit der Doppel-Spitze-Klammer-Syntax und dem Schalter WorkbookDesigner.setEnableHeaderFooterMarkers unter Verwendung tabellarischer Zeilen- oder JSON-Datenquellen und binden Sie Bilder über Daten-URIs ein, in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, Smart Marker, Kopfzeilen, Fußzeilen, Kopf- und Fußzeilen-Marker, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, benutzerdefinierte Datentabelle, Datenbindung, Bild, Daten-URI, Python via Java
type: docs
weight: 196
url: /de/python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Seitenkopf- und Fußzeilen enthalten typischerweise Bericht-Metadaten wie Berichtstitel, Berichtszeitraum, Autor und Abteilung. Wenn diese Informationen bereits in der Datenquelle vorhanden sind, die zum Befüllen der Arbeitsmappe verwendet wird, führt das manuelle Wiederholen zu unnötiger Duplizierung.  
Die klassische Smart-Marker-Syntax `&=Source.Field` wird in den Zellen des Arbeitsblattkörpers ausgewertet. Wenn Sie einen klassischen Marker über `PageSetup.setHeader` oder `PageSetup.setFooter` in eine Kopf- oder Fußzeile einfügen, bleibt er als wörtlicher Text erhalten, weil Kopf- und Fußzeilen-Zeichenketten nicht zum Zellenraster gehören, das von `WorkbookDesigner.process()` gescannt wird.  
Ab **Aspose.Cells for Python via Java 26.11** sorgt der Schalter `WorkbookDesigner.setEnableHeaderFooterMarkers`, der standardmäßig `False` ist, dafür, dass `process()` Platzhalter im Format `<<Source.Field>>` in den Kopf- und Fußzeilen-Abschnittszeichenketten auflöst – setzen Sie ihn vor dem Aufruf von `process()` auf `True`. Kopf- und Fußzeilen-Platzhalter verwenden dieselbe Datenquelle wie Arbeitsblatt-Marker.  
Jede Kopf- und Fußzeile enthält drei adressierbare Abschnitte:
- Abschnitt `0` ist der linke Abschnitt.
- Abschnitt `1` ist der mittlere Abschnitt.
- Abschnitt `2` ist der rechte Abschnitt.  
Verwenden Sie `PageSetup.setHeader(int section, str value)` und `PageSetup.setFooter(int section, str value)`, um diese Abschnitte zu schreiben. Nach der Verarbeitung rufen Sie `PageSetup.getHeader(int section)` und `PageSetup.getFooter(int section)` auf, um den fertigen Text abzurufen.

{{% alert color="primary" %}}
Ein Platzhalter wie `<<Source.Field>>` fügt den Feldwert als Text in die Abschnittszeichenkette ein. Bilder werden mit dem Suffix `(picture)` und einem Daten-URI-Wert gebunden.
{{% /alert %}}

## **Kopf- und Fußzeilen-Marker mit einer benutzerdefinierten Datentabelle aktivieren**
1. Erzeugen Sie eine `Workbook`-Instanz und holen Sie das erste `Worksheet` mit Index `0` mittels `workbook.getWorksheets().get(0)`.  
2. Schreiben Sie `<<Source.Field>>`-Platzhalter in die gewünschten Kopf- und Fußzeilen-Abschnitte mit `worksheet.getPageSetup().setHeader(section, value)` bzw. `worksheet.getPageSetup().setFooter(section, value)`.  
3. Definieren Sie eine kleine Klasse, die `ICellsDataTable` implementiert, um die tabellarischen Zeilendaten bereitzustellen – die Spaltennamen, die Zeilenzahl und einen Cursor mit `beforeFirst()`, `next()` und `get()` – und verwenden Sie einen Quellnamen, der dem im Platzhalter verwendeten Präfix entspricht. Zum Beispiel unterstützt eine Quelle mit dem Namen `node` Platzhalter wie `<<node.Name>>`. Eine einfache Python-Klasse oder eine Liste von Dictionaries wird auf dieser Plattform NICHT gebunden; die `ICellsDataTable`-Implementierung ist die benutzerdefinierte Objekt-Datenquelle.  
4. Erzeugen Sie einen `WorkbookDesigner` für die Arbeitsmappe.  
5. Rufen Sie vor der Verarbeitung `designer.setEnableHeaderFooterMarkers(True)` auf.  
6. Binden Sie die Tabelle und den Quellnamen mit `designer.setDataSource("node", table)`.  
7. Rufen Sie `designer.process()` auf.  
8. Nach der Verarbeitung sind die Platzhalter im Kopf- oder Fußzeilentext nicht mehr vorhanden. Verwenden Sie `worksheet.getPageSetup().getHeader(section)` und `worksheet.getPageSetup().getFooter(section)`, um die fertigen Abschnittszeichenketten abzurufen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name", "Author"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>")
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
print("Footer: " + worksheet.getPageSetup().getFooter(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
jpype.shutdownJVM()
```

## **JSON-Datenquelle verwenden**
Sie können JSON anstelle einer benutzerdefinierten `ICellsDataTable` verwenden, wenn die Berichtsdaten bereits im JSON-Format vorliegen. Rufen Sie `designer.setJsonDataSource(name, json)` auf, um die Quelle anzubinden.  
Das Argument `name` hat dieselbe Rolle wie der Quellname, der bei tabellarischen Daten verwendet wird. Beispielsweise unterstützt der Name `node` Platzhalter wie `<<node.Company>>` und `<<node.Title>>`.  
Übergeben Sie Zeilendaten direkt an `setJsonDataSource`:
- Ein Zeilen-Array, z. B. ein JSON-Array mit einem oder mehreren Zeilenobjekten, wird unterstützt.
- Ein einzelnes Zeilenobjekt kann ebenfalls direkt übergeben werden.
- Wickeln Sie die Zeilen nicht unter einem benannten Top-Level-Schlüssel wie `{"rows":[...]}` ein. Diese Hülle entspricht nicht der erwarteten zeilenorientierten Eingabeform für diesen Workflow.  
Eine JSON-Quelle kann beide Marker-Stile während desselben `process()`-Aufrufs befüllen. Sie kann einen klassischen `&=`-Marker in einer Arbeitsblatt-Zelle sowie Doppel-Spitze-Klammer-Platzhalter `<<>>` in Kopf- und Fußzeilen-Abschnitten auflösen. Sie müssen weiterhin `setEnableHeaderFooterMarkers` aktivieren, damit die Kopf- und Fußzeilen-Platzhalter aufgelöst werden.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>")
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>")
worksheet.getCells().get("A1").putValue("&=node.Company")
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setJsonDataSource(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.getPageSetup().getHeader(0))
print("Right: " + worksheet.getPageSetup().getHeader(2))
print("Body: " + worksheet.getCells().get("A1").getStringValue())
workbook.save("HeaderFooterJsonMarkers.xlsx")
jpype.shutdownJVM()
```

## **Schalter- und Mehrzeilen-Quellsemantik**
Die Kopf- und Fußzeilen-Marker-Einstellung ist standardmäßig `False`, und `designer.setEnableHeaderFooterMarkers(True)` steuert nur die Kopf- und Fußzeilen-Platzhalter `<<Source.Field>>`. Wenn der Schalter deaktiviert ist, löst `process()` weiterhin klassische `&=`-Arbeitsblatt-Marker auf, aber ein `<<Source.Field>>`-Platzhalter in einer Kopf- oder Fußzeile bleibt wörtlicher Text.  
Ein Kopf- oder Fußzeilen-Abschnitt ist eine einzige Zeichenkette, kein wiederholbarer Bereich. Enthält die Datenquelle mehrere Zeilen, liefert die erste Zeile die Werte für Kopf- und Fußzeile. Nach der Auflösung werden die Werte zu gewöhnlichem Kopf- oder Fußzeilentext. Sie bleiben in der Arbeitsmappe erhalten, nachdem Sie `workbook.save(...)` aufgerufen haben, und sind beim erneuten Laden der gespeicherten Arbeitsmappe vorhanden.  
Das folgende Beispiel erstellt zwei Arbeitsmappen über derselben mehrzeiligen tabellarischen Datenquelle, um das Verhalten bei deaktivierten und aktivierten Einstellungen zu vergleichen. Der `plainDesigner` lässt den Platzhalter unverändert, während der `enabledDesigner` ihn mithilfe der ersten Zeile auflöst.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
table = NodeTable([
    ("First Row",),
    ("Second Row",),
])
# Without the switch the placeholder stays literal text
plain_workbook = Workbook()
plain_sheet = plain_workbook.getWorksheets().get(0)
plain_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
plain_designer = WorkbookDesigner(plain_workbook)
plain_designer.setDataSource("node", table)
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = Workbook()
enabled_sheet = enabled_workbook.getWorksheets().get(0)
enabled_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
enabled_designer = WorkbookDesigner(enabled_workbook)
enabled_designer.setEnableHeaderFooterMarkers(True)
enabled_designer.setDataSource("node", table)
enabled_designer.process()
print("Without switch: " + plain_sheet.getPageSetup().getHeader(1))
print("With switch: " + enabled_sheet.getPageSetup().getHeader(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
jpype.shutdownJVM()
```

## **Ein Bild in Kopf- oder Fußzeile einbinden**
Das Suffix `(picture)` bindet ein Bild in einen Kopf- oder Fußzeilen-Abschnitt ein. Schreiben Sie `<<node.logo(picture)>>` an der Stelle, an der das Bild erscheinen soll, und übergeben Sie den Feldwert als Daten-URI – das Präfix `data:image/png;base64,` gefolgt vom Base64-Text der Bildbytes. Das dekodierte Bild wird als `byte[]`-Array behandelt. Ein reiner Base64-String ohne das `data:`-Präfix bettet kein Bild ein.  
Nach `process()`:
1. Der Platzhalter wird durch `&G` ersetzt, den standardmäßigen Kopf-/Fußzeilen-Bildcode. Da der Marker zu einem Code innerhalb der Abschnittszeichenkette wird, kann er in längeren Texten wie `Logo: <<node.logo(picture)>>` eingebettet werden.
2. Die Bildbytes werden in die Arbeitsmappe als Medienteil eingebettet, der an die Zeichenebene der Kopf-/Fußzeile jenes Arbeitsblatts angehängt ist, sodass das Bild zusammen mit der Kopf- bzw. Fußzeile gedruckt wird.

```python
import base64
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["logo"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    image_bytes = image_file.read()
logo_data = "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
table = NodeTable([(logo_data,)])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
jpype.shutdownJVM()
```

Der gedruckte `&G` ist der Bildcode, den Excel beim Rendern der Kopfzeile interpretiert – die `logo.png`-Bytes befinden sich nun in `HeaderFooterPicture.xlsx`, und das Bild wird anstelle des Codes gedruckt.  
Um Kopf- und Fußzeilen-Smart Marker zu verwenden, schreiben Sie `<<Source.Field>>`-Platzhalter in die linken, mittleren und rechten Kopf- bzw. Fußzeilen-Abschnitte mit `setHeader` und `setFooter`. Rufen Sie vor dem Aufruf von `process()` `designer.setEnableHeaderFooterMarkers(True)` auf und übergeben Sie Werte entweder über `designer.setDataSource("node", table)` mit einer benutzerdefinierten `ICellsDataTable`-Implementierung oder `designer.setJsonDataSource(name, json)`. Lesen Sie die fertigen Abschnitte mit `getHeader` und `getFooter`. Dieselbe Datenquelle kann sowohl Arbeitsblatt-Marker als auch Kopf- oder Fußzeilen-Platzhalter in einem Verarbeitungsschritt befüllen. Fügen Sie das Suffix `(picture)` mit einem Daten-URI-Wert hinzu, um ein Bild in einen Abschnitt einzubinden.

## **Verwandte Artikel**
- [SmartMarker Single-Cell-Array-Rendering](/cells/de/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}