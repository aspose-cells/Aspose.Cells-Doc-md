---
title: Smartes Importieren verschachtelter Objekte in Excel mit Smart Markern
type: docs
weight: 30
url: /de/net/how-to-import-nested-objects-with-smart-markers/
---

## **Warum verschachtelte Objekte für Smart Marker verwenden**
Smart Markers (in tools like FoxPro, reporting engines, or modern template systems) are placeholders that dynamically inject data into templates. Using nested objects (e.g., <<customer.address.city>>) enhances flexibility, organization, and expressiveness.

1. Hierarchische Datenrepräsentation: Echtzeitdaten sind inhärent verschachtelt (z.B. eine Bestellung enthält einen Kunden, der eine Adresse hat). Verschachtelte Objekte spiegeln diese Struktur wider und vermeiden vereinfachte/künstliche Felder wie kunden_stadt.
2. Vermeidung von Namenskonflikten: Flache Strukturen riskieren Kollisionen (z.B. produkt_name vs. lieferant_name). Verschachtelung schränkt Namen natürlich ein:
<<product.name>> vs. <<supplier.name>>.
3. Modularität & Wiederverwendbarkeit: Wiederverwendung von Sub-Objekten in verschiedenen Kontexten, Das Adresse-Objekt kann in Kunden-, Händler- oder Mitarbeitermarkern eingebettet werden. Änderungen an Adresse werden universell übernommen.
4. Simplified Data Binding: Bind entire nested objects to templates, <<order.customer>> auto-expands to all customer fields. Reduces manual mapping for sub-fields.
5. Dynamic Data Traversal: Traverse relationships on-demand, <<invoice.line_items[0].price>> accesses array elements or child objects. Enables complex queries without pre-processing.
6. Clearer Template Logic: Markers self-document relationships, <<user.profile.email>> is more intuitive than <<user_email>>. Reduces ambiguity in large templates.
7. Unterstützung durch Frameworks/Tools: Moderne Engines (z.B. Handlebars, React, FoxPro) lösen verschachtelte Pfade nativ auf. Entspricht JSON/APIs, bei denen verschachtelte Daten Standard sind.

## **Wie man anonyme Typen oder benutzerdefinierte Objekte mit Smart Markern importiert**
Aspose.Cells unterstützt auch anonyme Typen oder benutzerdefinierte Objekte in Smart Markern. Das folgende Beispiel zeigt, wie dies funktioniert. Für den Import von Daten aus dynamischen Objekten mithilfe von Smart Markern besuchen Sie den folgenden Artikel:

[Importieren aus dynamischem Objekt als Datenquelle](/cells/de/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}

## **Wie man verschachtelte Objekte mit Smart Markern importiert**
Aspose.Cells unterstützt verschachtelte Objekte in Smart Markern, die verschachtelten Objekte sollten einfach sein. Wir verwenden eine einfache Vorlagendatei. Sehen Sie die Designer-Tabelle, die einige verschachtelte Smart Marker enthält.

|**Die erste Arbeitsmappe der SM_NestedObjects.xlsx Datei zeigt verschachtelte Smart Marker.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Das folgende Beispiel zeigt, wie dies funktioniert.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Wie man generische Listen als verschachtelte Objekte mit Smart Markern importiert**
Aspose.Cells unterstützt nun auch die Verwendung einer generischen Liste als verschachteltes Objekt. Bitte überprüfen Sie den Screenshot der generierten Ausgabee Excel-Datei mit dem folgenden Code. Wie im Screenshot zu sehen ist, enthält ein Lehrerobjekt mehrere verschachtelte Schülerobjekte.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}

## **Wie man verschachtelte Objekte nicht zeilenweise mit Smart Markern importiert**
Die derzeitige Standardverarbeitungsmethode besteht darin, Smartmaker Zeile für Zeile zu verarbeiten. Manchmal müssen jedoch die Smart Marker derselben Datentabelle zusammen verarbeitet werden, unabhängig 
Wenn sie sich in der gleichen Zeile befinden oder nicht, müssen Sie einen benannten Bereich "_CellsSmartMarkers" angeben und WorkbookDesigner.LineByLine als falsch festlegen, bevor Sie die Verarbeitung aufrufen.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
