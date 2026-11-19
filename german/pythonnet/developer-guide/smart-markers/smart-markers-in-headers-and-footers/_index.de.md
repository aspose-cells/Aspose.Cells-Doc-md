---
title: Smart-Marker in Kopf- und Fußzeilen | Aspose.Cells for Python via .NET
linktitle: Kopf- und Fußzeilen-Smart-Marker | Aspose.Cells
description: Platzieren Sie Smart-Marker-Platzhalter in Seitenkopf- und Fußzeilen mit der Doppel-Spitzen-Klammer-Syntax und dem Schalter WorkbookDesigner.enable_header_footer_markers unter Verwendung benutzerdefinierter ICellsDataTable-Implementierungen oder JSON-Datenquellen und binden Sie Bilder über Data-URIs, in Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Smart-Marker, Kopfzeilen, Fußzeilen, Kopf- und Fußzeilen-Marker, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, benutzerdefinierte Datentabelle, Datenbindung, Bild, Data-URI, Aspose.Cells for Python via .NET
type: docs
weight: 196
url: /de/python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Seitenkopf- und Fußzeilen enthalten häufig Berichtsdaten wie den Berichtstitel, den Berichtszeitraum, den Autor und die Abteilung. Wenn diese Informationen bereits in der Datenquelle vorhanden sind, die zur Befüllung der Arbeitsmappe verwendet wird, führt das manuelle Wiederholen zu unnötiger Duplizierung.  
Die klassische Smart-Marker-Syntax `&=Source.Field` wird in Zellen des Arbeitsblatts verarbeitet. Wenn Sie einen klassischen Marker über `page_setup.set_header` oder `page_setup.set_footer` in einer Kopf- oder Fußzeile platzieren, bleibt er als wörtlicher Text erhalten, weil Kopf- und Fußzeilen-Strings nicht zum vom `workbook_designer.process()` gescannten Zellenraster des Arbeitsblatts gehören.  
Ab **Aspose.Cells for Python via .NET 26.11** löst der Schalter `workbook_designer.enable_header_footer_markers`, der standardmäßig `False` ist, in `process()` Platzhalter, die als `<<Source.Field>>` in den Kopf- und Fußzeilen-Abschnitts-Strings geschrieben wurden – setzen Sie ihn vor dem Aufruf von `process()` auf `True`. Kopf- und Fußzeilen-Platzhalter verwenden dieselbe Datenquelle wie Marker im Arbeitsblattkörper.  
Jede Kopf- und Fußzeile enthält drei adressierbare Abschnitte:
- Abschnitt `0` ist der linke Abschnitt.
- Abschnitt `1` ist der mittlere Abschnitt.
- Abschnitt `2` ist der rechte Abschnitt.  
Verwenden Sie `page_setup.set_header(section, value)` und `page_setup.set_footer(section, value)`, um diese Abschnitte zu schreiben. Nach der Verarbeitung können Sie mit `page_setup.get_header(section)` und `page_setup.get_footer(section)` den fertigen Text abrufen.

{{% alert color="primary" %}}
Ein Platzhalter wie `<<Source.Field>>` fügt den Feldwert als Text in die Abschnittszeichenkette ein. Bilder werden mit dem Suffix `(picture)` und einem Data-URI-Wert gebunden.
{{% /alert %}}

## **Kopf-/Fußzeilen-Marker mit einer benutzerdefinierten Datentabelle aktivieren**
Verwenden Sie die folgende Reihenfolge, um Kopf- und Fußzeilen-Platzhalter mit einer benutzerdefinierten tabellarischen Datenquelle in **Aspose.Cells for Python via .NET 26.11** zu lösen:
1. Erstellen Sie ein `Workbook` und greifen Sie auf dessen erstes `Worksheet` mit dem Index `0` zu.  
2. Schreiben Sie `<<Source.Field>>`-Platzhalter in die gewünschten Kopf- und Fußzeilenabschnitte mit `page_setup.set_header` und `page_setup.set_footer`.  
3. Definieren Sie eine kleine Klasse, die `ICellsDataTable` implementiert, um die tabellarischen Zeilendaten – Spaltennamen, Zeilenzahl und einen Cursor mit `before_first()`, `next()` und dem Indexer `__getitem__` – bereitzustellen, und verwenden Sie einen Quellnamen, der dem Präfix der Platzhalter entspricht. Beispielsweise liefert eine Quelle namens `node` Platzhalter wie `<<node.Name>>`. Eine einfache Python-Klasse oder eine Liste von Dictionaries bindet auf dieser Plattform nicht; die Implementierung von `ICellsDataTable` ist die benutzerdefinierte Objekt-Datenquelle.  
4. Erzeugen Sie einen `WorkbookDesigner` für die Arbeitsmappe.  
5. Setzen Sie `designer.enable_header_footer_markers` vor der Verarbeitung auf `True`.  
6. Verknüpfen Sie die Tabelle und den Quellnamen mit `designer.set_data_source("node", table)`.  
7. Rufen Sie `designer.process()` auf.  
8. Nach der Verarbeitung sind die Platzhalter nicht mehr im Kopf- oder Fußzeilentext enthalten. Verwenden Sie `get_header` und `get_footer`, um die fertigen Abschnitts-Strings abzurufen.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name", "Author"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.page_setup.set_header(1, "Quarterly Report - <<node.Name>>")
worksheet.page_setup.set_footer(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
print("Footer: " + worksheet.page_setup.get_footer(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
```

## **Verwendung einer JSON-Datenquelle**
Sie können JSON anstelle einer benutzerdefinierten `ICellsDataTable` nutzen, wenn die Berichtsdaten bereits im JSON-Format vorliegen. Rufen Sie `workbook_designer.set_json_data_source(name, json)` auf, um die Quelle anzuhängen.  
Das Argument `name` hat dieselbe Funktion wie der Quellname, der bei tabellarischen Daten verwendet wird. Beispielsweise liefert der Name `node` Platzhalter wie `<<node.Company>>` und `<<node.Title>>`.  
Übergeben Sie Zeilendaten direkt an `set_json_data_source`:
- Ein Zeilen-Array, etwa ein JSON-Array, das ein oder mehrere Zeilen-Objekte enthält, wird unterstützt.  
- Ein einzelnes Zeilen-Objekt kann ebenfalls direkt übergeben werden.  
- Wickeln Sie die Zeilen nicht unter einem benannten Top-Level-Schlüssel wie `{"rows":[...]}` ein. Dieser Wrapper entspricht nicht der erwarteten zeilenorientierten Eingabeform für diesen Workflow.  
Eine JSON-Quelle kann beide Marker-Stile während desselben `process()`-Aufrufs befüllen. Sie kann einen klassischen `&=`-Marker in einer Zelle im Arbeitsblattkörper und Doppel-Spitzen-Klammer-Platzhalter `<<>>` in Kopf- und Fußzeilen-Abschnitten auflösen. Sie müssen weiterhin `enable_header_footer_markers` aktivieren, damit die Kopf- und Fußzeilen-Platzhalter aufgelöst werden.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.page_setup.set_header(0, "<<node.Company>>")
worksheet.page_setup.set_header(2, "Page <<node.Title>>")
worksheet.cells.get("A1").put_value("&=node.Company")
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_json_data_source(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.page_setup.get_header(0))
print("Right: " + worksheet.page_setup.get_header(2))
print("Body: " + worksheet.cells.get("A1").string_value)
# This prints:
# Left: Aspose Pty Ltd
# Right: Page Half-Year Report
# Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx")
```

## **Schalter- und Mehrzeilen-Quell-Semantik**
`enable_header_footer_markers` ist standardmäßig `False`, und der Schalter steuert nur die `<<Source.Field>>`-Platzhalter in Kopf- und Fußzeilen. Wenn der Schalter deaktiviert ist, löst `process()` weiterhin klassische `&=`-Marker im Arbeitsblattkörper auf, aber ein `<<Source.Field>>`-Platzhalter in einer Kopf- oder Fußzeile bleibt wörtlicher Text.  
Ein Kopf- oder Fußzeilenabschnitt ist ein einzelner String, kein wiederholender Block. Enthält die Datenquelle mehrere Zeilen, liefert die erste Zeile die Werte für Kopf- und Fußzeile. Nach der Auflösung werden die Werte zu gewöhnlichem Kopf- bzw. Fußzeilentext. Sie bleiben in der Arbeitsmappe erhalten, nachdem Sie `save` aufgerufen haben, und sind beim erneuten Laden der gespeicherten Arbeitsmappe vorhanden.  
Im folgenden Beispiel werden zwei Arbeitsmappen über derselben mehrzeiligen tabellarischen Datenquelle erstellt, um das deaktivierte und aktivierte Verhalten zu kontrastieren. Der `plain_designer` lässt den Platzhalter unverändert, während der `enabled_designer` ihn mithilfe der ersten Zeile auflöst.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
rows = [("First Row",), ("Second Row",)]
# Without the switch the placeholder stays literal text
plain_workbook = ac.Workbook()
plain_sheet = plain_workbook.worksheets[0]
plain_sheet.page_setup.set_header(1, "<<node.Name>>")
plain_designer = ac.WorkbookDesigner(plain_workbook)
plain_designer.set_data_source("node", NodeTable(rows))
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = ac.Workbook()
enabled_sheet = enabled_workbook.worksheets[0]
enabled_sheet.page_setup.set_header(1, "<<node.Name>>")
enabled_designer = ac.WorkbookDesigner(enabled_workbook)
enabled_designer.enable_header_footer_markers = True
enabled_designer.set_data_source("node", NodeTable(rows))
enabled_designer.process()
print("Without switch: " + plain_sheet.page_setup.get_header(1))
print("With switch: " + enabled_sheet.page_setup.get_header(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
```

## **Ein Bild in einer Kopf- oder Fußzeile einbinden**
Das Suffix `(picture)` bindet ein Bild in einen Kopf- oder Fußzeilenabschnitt. Schreiben Sie `<<node.logo(picture)>>` an die Stelle, an der das Bild erscheinen soll, und übergeben Sie den Feldwert als Data-URI – das Präfix `data:image/png;base64,` gefolgt vom Base64-Text der Bildbytes. Ein reiner Base64-String ohne das `data:`-Präfix bettet kein Bild ein.  
Nach `process()`:
1. Der Platzhalter wird durch `&G` ersetzt, den standardmäßigen Bild-Code für Kopf- und Fußzeilen. Da der Marker zu einem Code im Abschnitts-String wird, kann er in längerem Text wie `Logo: <<node.logo(picture)>>` stehen.  
2. Die Bildbytes werden als Medien-Teil in die Arbeitsmappe eingebettet und dem Zeichen-Layer der Kopf-/Fußzeile dieses Arbeitsblatts zugeordnet, sodass das Bild zusammen mit der Kopf- bzw. Fußzeile gedruckt wird.

```python
import aspose.cells as ac
import base64
class LogoTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["logo"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.page_setup.set_header(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    logo_data_uri = "data:image/png;base64," + base64.b64encode(image_file.read()).decode("ascii")
table = LogoTable([(logo_data_uri,)])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
```

Der gedruckte `&G` ist der Bild-Code, den Excel beim Rendern der Kopfzeile interpretiert – die `logo.png`-Bytes befinden sich nun in `HeaderFooterPicture.xlsx`, und das Bild wird anstelle des Codes angezeigt.  
Um Kopf- und Fußzeilen-Smart-Marker zu verwenden, schreiben Sie `<<Source.Field>>`-Platzhalter in die linken, mittleren und rechten Abschnitte der Kopf- bzw. Fußzeile mit `set_header` und `set_footer`. Setzen Sie `enable_header_footer_markers` auf `True` beim `WorkbookDesigner`, bevor Sie `process()` aufrufen, und übergeben Sie Werte über `set_data_source("node", table)` mit einer benutzerdefinierten `ICellsDataTable`-Implementierung oder `set_json_data_source(name, json)`. Lesen Sie die fertigen Abschnitte über `get_header` und `get_footer`. Dieselbe Datenquelle kann sowohl Arbeitsblatt-Marker als auch Kopf- und Fußzeilen-Platzhalter in einem Verarbeitungsschritt befüllen. Fügen Sie das Suffix `(picture)` mit einem Data-URI-Wert hinzu, um ein Bild in einen Abschnitt einzubinden.

## Verwandte Artikel
- [SmartMarker Einzelzell-Array-Rendering](/cells/de/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}