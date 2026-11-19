---
title: Smart Marker in Kopf- und Fußzeilen | Aspose.Cells .NET
linktitle: Kopf- und Fußzeilen-Smart-Marker | Aspose.Cells
description: Platzieren Sie Smart-Marker-Platzhalter in Seitenkopf- und Fußzeilen mit der Doppel-Spitze-Klammer-Syntax und dem Schalter WorkbookDesigner.EnableHeaderFooterMarkers unter Verwendung von DataTable- oder JSON-Datenquellen und binden Sie Bilder über Data-URIs in Aspose.Cells for .NET.
keywords: Aspose.Cells, Smart Marker, Kopfzeilen, Fußzeilen, Kopf- und Fußzeilen-Marker, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, Datenbindung, Bild, Data-URI, C#
type: docs
weight: 196
url: /de/net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Seitenkopf- und Fußzeilen enthalten häufig Berichtsmetadaten wie den Berichtstitel, den Berichtszeitraum, den Autor und die Abteilung. Wenn diese Informationen bereits in der Datenquelle vorhanden sind, die zum Befüllen der Arbeitsmappe verwendet wird, führt das manuelle Wiederholen zu unnötiger Duplizierung.
Die klassische Smart-Marker-Syntax `&=Source.Field` wird in Zellen des Arbeitsblatt-Körpers verarbeitet. Wenn Sie einen klassischen Marker über `PageSetup.SetHeader` oder `PageSetup.SetFooter` in einer Kopf- oder Fußzeile platzieren, bleibt er als wörtlicher Text erhalten, da Kopf- und Fußzeilen-Zeichenketten nicht Teil des Zellrasters des Arbeitsblatts sind, das von `WorkbookDesigner.Process()` gescannt wird.
Ab **Aspose.Cells for .NET 26.11** bewirkt der Schalter `WorkbookDesigner.EnableHeaderFooterMarkers`, der standardmäßig `false` ist, dass `Process()` Platzhalter, die als `<<Source.Field>>` in den Kopf- und Fußzeilen-Abschnittszeichenketten geschrieben wurden, auflöst – setzen Sie ihn vor dem Aufruf von `Process()` auf `true`. Kopf- und Fußzeilen-Platzhalter verwenden dieselbe Datenquelle wie Körper-Marker.
Jede Kopf- und Fußzeile enthält drei adressierbare Abschnitte:
- Abschnitt `0` ist der linke Abschnitt.
- Abschnitt `1` ist der mittlere Abschnitt.
- Abschnitt `2` ist der rechte Abschnitt.
Verwenden Sie `PageSetup.SetHeader(int section, string value)` und `PageSetup.SetFooter(int section, string value)`, um diese Abschnitte zu schreiben. Nach der Verarbeitung verwenden Sie `PageSetup.GetHeader(int section)` und `PageSetup.GetFooter(int section)`, um den fertigen Text abzurufen.

{{% alert color="primary" %}}
Ein Platzhalter wie `<<Source.Field>>` fügt den Feldwert als Text in die Abschnitts-Zeichenkette ein. Bilder werden mit dem Suffix `(picture)` und einem Data-URI-Wert gebunden.
{{% /alert %}}

## **Kopf- und Fußzeilen-Marker mit einer DataTable aktivieren**
Verwenden Sie die folgende Reihenfolge, um Kopf- und Fußzeilen-Platzhalter mit einer `DataTable` in **Aspose.Cells for .NET 26.11** aufzulösen:
1. Erzeugen Sie ein `Workbook` und holen Sie das erste `Worksheet` mit dem Index `0`.
2. Schreiben Sie `<<Source.Field>>`-Platzhalter in die gewünschten Kopf- und Fußzeilen-Abschnitte mit `PageSetup.SetHeader` und `PageSetup.SetFooter`.
3. Erstellen Sie eine `DataTable`, deren Tabellenname dem Quell-Präfix der Platzhalter entspricht. Beispielsweise unterstützt eine Tabelle namens `node` Platzhalter wie `<<node.Name>>`.
4. Erzeugen Sie einen `WorkbookDesigner` für die Arbeitsmappe.
5. Setzen Sie `designer.EnableHeaderFooterMarkers` vor der Verarbeitung auf `true`.
6. Binden Sie die Tabelle mit `designer.SetDataSource(table)` an.
7. Rufen Sie `designer.Process()` auf.
8. Nach der Verarbeitung sind die Platzhalter im Kopf- oder Fußzeilentext nicht mehr vorhanden. Verwenden Sie `GetHeader` und `GetFooter`, um die fertigen Abschnittszeichenketten abzurufen.

```csharp
using System;
using System.Data;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.PageSetup.SetHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.PageSetup.SetFooter(1, "Prepared by <<node.Author>>");
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Columns.Add("Author");
table.Rows.Add("Q4 2026", "Aspose.Cells");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
Console.WriteLine("Footer: " + worksheet.PageSetup.GetFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.Save("HeaderFooterSmartMarkers.xlsx");
```

## **JSON-Datenquelle verwenden**
Sie können JSON anstelle einer `DataTable` verwenden, wenn die Berichtsdaten bereits im JSON-Format vorliegen. Rufen Sie `WorkbookDesigner.SetJsonDataSource(string name, string json)` auf, um die Quelle anzubinden.
Das Argument `name` hat dieselbe Rolle wie der Name der `DataTable`. Beispielsweise unterstützt der Name `node` Platzhalter wie `<<node.Company>>` und `<<node.Title>>`.
Übergeben Sie Zeilendaten direkt an `SetJsonDataSource`:
- Ein Zeilen-Array, z. B. ein JSON-Array, das ein oder mehrere Zeilenobjekte enthält, wird unterstützt.
- Ein einzelnes Zeilenobjekt kann ebenfalls direkt übergeben werden.
- Umwickeln Sie die Zeilen nicht unter einem benannten Top-Level-Schlüssel wie `{"rows":[...]}`. Dieser Wrapper entspricht nicht der erwarteten zeilenorientierten Eingabeform für diesen Arbeitsablauf.
Eine JSON-Quelle kann beide Marker-Stile im selben `Process()`-Aufruf befüllen. Sie kann einen klassischen `&=`-Marker in einer Arbeitsblatt-Körperzelle und Doppel-Spitze-Klammer-Platzhalter `<<>>` in Kopf- und Fußzeilen-Abschnitten auflösen. Sie müssen weiterhin `EnableHeaderFooterMarkers` aktivieren, damit die Kopf- und Fußzeilen-Platzhalter aufgelöst werden.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.PageSetup.SetHeader(0, "<<node.Company>>");
worksheet.PageSetup.SetHeader(2, "Page <<node.Title>>");
worksheet.Cells["A1"].PutValue("&=node.Company");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
designer.Process();
Console.WriteLine("Left: " + worksheet.PageSetup.GetHeader(0));
Console.WriteLine("Right: " + worksheet.PageSetup.GetHeader(2));
Console.WriteLine("Body: " + worksheet.Cells["A1"].StringValue);
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.Save("HeaderFooterJsonMarkers.xlsx");
```

## **Schalter- und Mehrzeilen-Quellsemantik**
`EnableHeaderFooterMarkers` ist standardmäßig `false` und der Schalter steuert nur die Kopf- und Fußzeilen-Platzhalter `<<Source.Field>>`. Wenn der Schalter deaktiviert ist, löst `Process()` weiterhin klassische `&=`-Körper-Marker auf, aber ein `<<Source.Field>>`-Platzhalter in einer Kopf- oder Fußzeile bleibt wörtlicher Text.
Ein Kopf- oder Fußzeilen-Abschnitt ist eine einzelne Zeichenkette, kein wiederholender Band. Enthält die Datenquelle mehrere Zeilen, liefert die erste Zeile die Werte für Kopf- und Fußzeile. Nach der Auflösung werden die Werte zu gewöhnlichem Kopf- oder Fußzeilentext. Sie bleiben in der Arbeitsmappe erhalten, nachdem Sie `Save` aufgerufen haben, und sind beim erneuten Laden der gespeicherten Arbeitsmappe vorhanden.
Das folgende Beispiel erstellt zwei Arbeitsmappen anhand derselben mehrzeiligen `DataTable`, um das deaktivierte und aktivierte Verhalten gegenüberzustellen. Der `plainDesigner` lässt den Platzhalter unverändert, während der `enabledDesigner` ihn mit der ersten Zeile auflöst.

```csharp
using System;
using System.Data;
using Aspose.Cells;
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Rows.Add("First Row");
table.Rows.Add("Second Row");
// Without the switch the placeholder stays literal text
Workbook plainWorkbook = new Workbook();
Worksheet plainSheet = plainWorkbook.Worksheets[0];
plainSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
plainDesigner.SetDataSource(table);
plainDesigner.Process();
// With the switch on, the FIRST row of a multi-row source wins
Workbook enabledWorkbook = new Workbook();
Worksheet enabledSheet = enabledWorkbook.Worksheets[0];
enabledSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
enabledDesigner.EnableHeaderFooterMarkers = true;
enabledDesigner.SetDataSource(table);
enabledDesigner.Process();
Console.WriteLine("Without switch: " + plainSheet.PageSetup.GetHeader(1));
Console.WriteLine("With switch: " + enabledSheet.PageSetup.GetHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.Save("HeaderFooterMarkersEnabled.xlsx");
```

## **Ein Bild in einer Kopf- oder Fußzeile einbinden**
Das Suffix `(picture)` bindet ein Bild in einen Kopf- oder Fußzeilen-Abschnitt ein. Schreiben Sie `<<node.logo(picture)>>` an der Stelle, an der das Bild erscheinen soll, und liefern Sie den Feldwert als Data-URI — das Präfix `data:image/png;base64,` gefolgt vom Base64-Text der Bildbytes. Ein reiner Base64-String ohne das Präfix `data:` bettet kein Bild ein.
Nach `Process()`:
1. Der Platzhalter wird durch `&G` ersetzt, den standardmäßigen Bildcode für Kopf- und Fußzeilen. Da der Marker zu einem Code innerhalb der Abschnitts-Zeichenkette wird, kann er in längeren Texten wie `Logo: <<node.logo(picture)>>` eingebettet werden.
2. Die Bildbytes werden in der Arbeitsmappe als Medienteil eingebettet, der an die Zeichenebene der Kopf-/Fußzeile dieses Arbeitsblatts angehängt ist, sodass das Bild zusammen mit der Kopf- bzw. Fußzeile gedruckt wird.

```csharp
using System;
using System.Data;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.PageSetup.SetHeader(1, "Logo: <<node.logo(picture)>>");
DataTable table = new DataTable("node");
table.Columns.Add("logo");
table.Rows.Add("data:image/png;base64," + Convert.ToBase64String(File.ReadAllBytes("logo.png")));
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
// This prints:
// Header: Logo: &G
workbook.Save("HeaderFooterPicture.xlsx");
```

Das gedruckte `&G` ist der Bildcode, den Excel beim Rendern der Kopfzeile interpretiert – die `logo.png`-Bytes befinden sich nun in `HeaderFooterPicture.xlsx`, und das Bild wird anstelle des Codes gedruckt.
Um Kopf- und Fußzeilen-Smart-Marker zu verwenden, schreiben Sie `<<Source.Field>>`-Platzhalter in die linken, mittleren und rechten Kopf- bzw. Fußzeilen-Abschnitte mit `SetHeader` und `SetFooter`. Setzen Sie `EnableHeaderFooterMarkers` auf `true` beim `WorkbookDesigner`, bevor Sie `Process()` aufrufen, und übergeben Sie Werte entweder über `SetDataSource(DataTable)` oder `SetJsonDataSource`. Lesen Sie die fertigen Abschnitte mit `GetHeader` und `GetFooter`. Dieselbe Datenquelle kann sowohl Körper-Marker als auch Kopf- oder Fußzeilen-Platzhalter in einem Verarbeitungsdurchlauf befüllen. Fügen Sie das Suffix `(picture)` mit einem Data-URI-Wert hinzu, um ein Bild in einen Abschnitt einzubinden.

## Verwandte Artikel
- [SmartMarker Einzelzellen-Array-Rendering](/cells/de/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}