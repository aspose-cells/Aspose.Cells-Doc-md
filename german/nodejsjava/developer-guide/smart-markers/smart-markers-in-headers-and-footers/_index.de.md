---
title: Smart-Marker in Kopf- und Fußzeilen | Aspose.Cells for Node.js via Java
linktitle: Kopf- und Fußzeilen-Smart-Marker | Aspose.Cells for Node.js via Java
description: Platzieren Sie Smart-Marker-Platzhalter in Seitenkopf- und -fußzeilen mit der Doppelwinkelklammer-Syntax und dem Schalter WorkbookDesigner.setEnableHeaderFooterMarkers unter Verwendung von JSON-Datenquellen und binden Sie Bilder über Daten-URIs ein, in Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells for Node.js via Java, Smart-Marker, Kopf- und Fußzeilen, Kopf- und Fußzeilen-Markierungen, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, JSON-Zeilen, Datenbindung, Bild, Daten-URI, JavaScript
type: docs
weight: 196
url: /de/nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Seitenkopf- und -fußzeilen enthalten häufig Bericht-Metadaten wie den Berichtstitel, den Berichtszeitraum, den Autor und die Abteilung. Wenn diese Informationen bereits in der Datenquelle vorhanden sind, die zum Befüllen der Arbeitsmappe verwendet wird, führt das manuelle Wiederholen zu unnötigen Duplikaten.  
Die klassische Smart-Marker-Syntax `&=Source.Field` wird in den Zellen des Arbeitsblatt-Körpers verarbeitet. Wenn Sie einen klassischen Marker über `PageSetup.setHeader` oder `PageSetup.setFooter` in einer Kopf- oder Fußzeile einfügen, bleibt er als wörtlicher Text erhalten, weil Kopf- und Fußzeilen-Zeichenketten nicht zum Arbeitsblatt-Zellengitter gehören, das von `WorkbookDesigner.process()` gescannt wird.  
Ab **Aspose.Cells for Node.js via Java 26.11** löst die Einstellung `WorkbookDesigner.setEnableHeaderFooterMarkers`, die standardmäßig `false` ist, beim Aufruf von `process()` Platzhalter, die als `<<Source.Field>>` in den Kopf- und Fußzeilen-Abschnittszeichenketten geschrieben wurden. Rufen Sie `designer.setEnableHeaderFooterMarkers(true)` auf, bevor Sie `process()` aufrufen. Kopf- und Fußzeilen-Platzhalter verwenden dieselbe Datenquelle wie Körper-Marker.  
Jede Kopf- und Fußzeile enthält drei adressierbare Abschnitte:
- Abschnitt `0` ist der linke Abschnitt.
- Abschnitt `1` ist der mittlere Abschnitt.
- Abschnitt `2` ist der rechte Abschnitt.  
Verwenden Sie `PageSetup.setHeader(int section, String value)` und `PageSetup.setFooter(int section, String value)`, um diese Abschnitte zu schreiben. Nach dem Verarbeiten rufen Sie `PageSetup.getHeader(int section)` und `PageSetup.getFooter(int section)` auf, um den fertigen Text abzurufen.

{{% alert color="primary" %}}
Ein Platzhalter wie `<<Source.Field>>` fügt den Feldwert als Text in die Abschnittszeichenkette ein. Bilder werden mit dem Suffix `(picture)` und einem Daten-URI-Wert gebunden.
{{% /alert %}}

## **Kopf-/Fußzeilen-Markierungen mit JSON-Zeilendaten aktivieren**
Verwenden Sie die folgende Reihenfolge, um Kopf- und Fußzeilen-Platzhalter mit JSON-Zeilendaten in **Aspose.Cells for Node.js via Java 26.11** zu lösen:
1. Erstellen Sie eine Arbeitsmappe und erhalten Sie das erste Arbeitsblatt mit `workbook.getWorksheets().get(0)`.
2. Schreiben Sie `<<Source.Field>>`-Platzhalter in die gewünschten Kopf- und Fußzeilen-Abschnitte mit `PageSetup.setHeader` und `PageSetup.setFooter`.
3. Bereiten Sie die Zeilendaten als JSON-Array von Zeilenobjekten vor und wählen Sie einen Quellnamen, der dem Quellenpräfix der Platzhalter entspricht. Zum Beispiel unterstützt eine Quelle namens `node` Platzhalter wie `<<node.Name>>`. Reine JavaScript-Objekte und -Arrays, die an `setDataSource` übergeben werden, binden auf dieser Plattform nicht — JSON ist die unterstützte tabellarische Form.
4. Erstellen Sie einen `WorkbookDesigner` für die Arbeitsmappe.
5. Rufen Sie `designer.setEnableHeaderFooterMarkers(true)` vor dem Verarbeiten auf.
6. Binden Sie das JSON mit `designer.setJsonDataSource("node", '[{"Name":"...","Author":"..."}]')`.
7. Rufen Sie `designer.process()` auf.
8. Nach dem Verarbeiten sind die Platzhalter nicht mehr im Kopf- oder Fußzeilentext enthalten. Verwenden Sie `getHeader` und `getFooter`, um die fertigen Abschnittszeichenketten abzurufen.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource(
  "node",
  '[{"Name":"Q4 2026","Author":"Aspose.Cells"}]'
);
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
console.log("Footer: " + worksheet.getPageSetup().getFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx");
```

## **Verwendung einer JSON-Datenquelle**
Wenn die Berichtsdaten bereits als JSON vorliegen, kann ein Aufruf von `setJsonDataSource` jeden Markerstil versorgen. Rufen Sie `WorkbookDesigner.setJsonDataSource(String name, String json)` auf, um die Quelle zu binden.  
Das Argument `name` ist der Quellname, der von den Platzhaltern verwendet wird. Zum Beispiel unterstützt der Name `node` Platzhalter wie `<<node.Company>>` und `<<node.Title>>`.  
Übergeben Sie Zeilendaten direkt an `setJsonDataSource`:
- Ein Zeilen-Array, z. B. ein JSON-Array, das ein oder mehrere Zeilenobjekte enthält, wird unterstützt.
- Ein einzelnes Zeilenobjekt kann ebenfalls direkt übergeben werden.
- Wickeln Sie die Zeilen nicht unter einem benannten Top-Level-Schlüssel wie `{"rows":[...]}` ein. Diese Wrapper-Struktur entspricht nicht der erwarteten zeilenorientierten Eingabe für diesen Arbeitsablauf.  
Eine JSON-Quelle kann beide Markerstile während desselben `process()`-Aufrufs befüllen. Sie kann einen klassischen `&=`-Marker in einer Arbeitsblatt-Körperzelle und Doppelwinkelklammer-Platzhalter `<<>>` in Kopf- und Fußzeilen-Abschnitten auflösen. Sie müssen weiterhin `designer.setEnableHeaderFooterMarkers(true)` aufrufen, damit die Kopf- und Fußzeilen-Platzhalter aufgelöst werden.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
worksheet.getCells().get("A1").putValue("&=node.Company");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]');
designer.process();
console.log("Left: " + worksheet.getPageSetup().getHeader(0));
console.log("Right: " + worksheet.getPageSetup().getHeader(2));
console.log("Body: " + worksheet.getCells().get("A1").getStringValue());
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx");
```

## **Schalter- und Mehrzeilen-Quellsemantik**
`setEnableHeaderFooterMarkers` ist standardmäßig `false` und steuert nur die Kopf- und Fußzeilen-Platzhalter `<<Source.Field>>`. Wenn der Schalter deaktiviert ist, löst `process()` weiterhin klassische `&=`-Körper-Marker auf, aber ein `<<Source.Field>>`-Platzhalter in einer Kopf- oder Fußzeile bleibt wörtlicher Text.  
Ein Kopf- oder Fußzeilen-Abschnitt ist eine einzelne Zeichenkette, kein wiederholender Block. Enthält die Datenquelle mehrere Zeilen, liefert die erste Zeile die Werte für Kopf- und Fußzeile. Nach der Auflösung werden die Werte zu gewöhnlichem Kopf- bzw. Fußzeilentext. Sie bleiben in der Arbeitsmappe erhalten, wenn Sie `save` aufrufen, und sind beim erneuten Laden der gespeicherten Arbeitsmappe vorhanden.  
Das folgende Beispiel erstellt zwei Arbeitsmappen über derselben mehrzeiligen JSON-Quelle, um das deaktivierte und aktivierte Verhalten gegenüberzustellen. Der `plainDesigner` lässt den Platzhalter unverändert, während der `enabledDesigner` ihn mithilfe der ersten Zeile auflöst.

```javascript
const AsposeCells = require("aspose.cells");
const table = '[{"Name":"First Row"},{"Name":"Second Row"}]';
// Without the switch the placeholder stays literal text
const plainWorkbook = new AsposeCells.Workbook();
const plainSheet = plainWorkbook.getWorksheets().get(0);
plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const plainDesigner = new AsposeCells.WorkbookDesigner(plainWorkbook);
plainDesigner.setJsonDataSource("node", table);
plainDesigner.process();
// With the switch on, the FIRST row of a multi-row source wins
const enabledWorkbook = new AsposeCells.Workbook();
const enabledSheet = enabledWorkbook.getWorksheets().get(0);
enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const enabledDesigner = new AsposeCells.WorkbookDesigner(enabledWorkbook);
enabledDesigner.setEnableHeaderFooterMarkers(true);
enabledDesigner.setJsonDataSource("node", table);
enabledDesigner.process();
console.log("Without switch: " + plainSheet.getPageSetup().getHeader(1));
console.log("With switch: " + enabledSheet.getPageSetup().getHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
```

## **Ein Bild in eine Kopf- oder Fußzeile einbinden**
Das Suffix `(picture)` bindet ein Bild in einen Kopf- oder Fußzeilen-Abschnitt ein. Schreiben Sie `<<node.logo(picture)>>` an die Stelle, an der das Bild erscheinen soll, und geben Sie den Feldwert als Daten-URI an — das Präfix `data:image/png;base64,` gefolgt vom Base64-Text der Bildbytes. Eine reine Base64-Zeichenkette ohne das Präfix `data:` bettet kein Bild ein.  
Nach `process()`:
1. Der Platzhalter wird durch `&G` ersetzt, den Standard-Header- und-Footer-Bildcode. Da der Marker zu einem Code innerhalb der Abschnittszeichenkette wird, kann er in längeren Texten wie `Logo: <<node.logo(picture)>>` eingebettet werden.
2. Die Bildbytes werden in der Arbeitsmappe als Medienteil eingebettet, das an die Zeichenebene der Kopf-/Fußzeile dieses Arbeitsblatts angehängt ist, sodass das Bild zusammen mit der Kopf- bzw. Fußzeile gedruckt wird.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
const table = [
    {
        logo: "data:image/png;base64," + fs.readFileSync("logo.png").toString("base64")
    }
];
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", JSON.stringify(table));
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
// This prints:
// Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx");
```

Das gedruckte `&G` ist der Bildcode, den Excel beim Rendern der Kopfzeile interpretiert — die `logo.png`-Bytes befinden sich jetzt in `HeaderFooterPicture.xlsx`, und das Bild wird anstelle des Codes gedruckt.  
Um Smart-Marker in Kopf- und Fußzeilen zu verwenden, schreiben Sie `<<Source.Field>>`-Platzhalter in die linken, mittleren und rechten Kopf- bzw. Fußzeilen-Abschnitte mit `setHeader` und `setFooter`. Rufen Sie `designer.setEnableHeaderFooterMarkers(true)` vor dem Aufruf von `process()` auf und übergeben Sie Werte über `designer.setJsonDataSource(name, json)`. Lesen Sie die fertigen Abschnitte mit `getHeader` und `getFooter`. Die gleiche Datenquelle kann sowohl Körper-Marker als auch Kopf- bzw. Fußzeilen-Platzhalter in einem Verarbeitungsdurchlauf befüllen. Fügen Sie das Suffix `(picture)` mit einem Daten-URI-Wert hinzu, um ein Bild in einen Abschnitt einzubinden.

## Verwandte Artikel
- [SmartMarker Einzelzellen-Array-Rendering](/cells/de/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}