---
title: Verwenden Sie benutzerdefinierte XML-Teile in Aspose.Cells
type: docs
weight: 390
url: /de/net/use-custom-xml-parts-in-aspose-cells/
---
## Verwenden von benutzerdefinierten XML-Teilen in Aspose.Cells

Benutzerdefinierte XML-Teile sind die XML-Daten, die von verschiedenen Anwendungen wie SharePoint usw. in der Excel-Datei gespeichert werden. Diese Daten werden von verschiedenen Anwendungen verbraucht, die sie benötigen. Microsoft Excel verwendet diese Daten nicht, daher gibt es keine GUI zum Hinzufügen. Sie können diese Daten anzeigen, indem Sie die Erweiterung von ändern**.xlsx** hinein**.Postleitzahl** und dann durch Öffnen mit**WinZip** . Sie können die ZIP-Datei auch mit einem beliebigen Windows-ZIP-Hilfsprogramm eines Drittanbieters wie WinRAR oder WinZip usw. öffnen. Die Daten befinden sich in der**benutzerdefiniertes XML** Mappe.

 Sie können benutzerdefinierte XML-Teile mit Aspose.Cells über die hinzufügen[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)Methode.

 Der folgende Beispielcode verwendet[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) Methode und fügt die hinzu**Buchkatalog XML** und sein Name ist**Buchhandlung**. Das folgende Bild zeigt das Ergebnis dieses Codes. Wie Sie sehen können, wird Buchkatalog-XML innerhalb des BookStore-Knotens hinzugefügt, der der Name dieser Eigenschaft ist.

![todo: Bild_alt_Text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo: Bild_alt_Text](use-custom-xml-parts-in-aspose-cells_2.png)

## C#-Code zur Verwendung benutzerdefinierter XML-Teile

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Verwandter Artikel

- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsbereich sichtbar sind](/cells/de/net/adding-custom-properties-visible-inside-document-information-panel/)
