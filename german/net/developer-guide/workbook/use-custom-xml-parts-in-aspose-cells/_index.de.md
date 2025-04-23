---
title: Verwenden von benutzerdefinierten XML Teilen in Aspose.Cells
type: docs
weight: 390
url: /de/net/use-custom-xml-parts-in-aspose-cells/
---

## Verwendung von benutzerdefinierten XML-Teilen in Aspose.Cells

Benutzerdefinierte XML-Teile sind die in verschiedenen Anwendungen wie SharePoint usw. gespeicherten XML-Daten innerhalb der Excel-Datei. Diese Daten werden von verschiedenen Anwendungen verwendet, die sie benötigen. Microsoft Excel nutzt diese Daten nicht, daher gibt es keine grafische Benutzeroberfläche, um sie hinzuzufügen. Sie können diese Daten anzeigen, indem Sie die Erweiterung von **.xlsx** in **.zip** ändern und sie dann mit **WinZip** öffnen. Sie können die ZIP-Datei auch mit einem Windows-Zip-Dienstprogramm eines Drittanbieters wie WinRAR oder WinZip öffnen. Die Daten sind im **customXml**-Ordner vorhanden.

Sie können benutzerdefinierte XML-Teile mithilfe von Aspose.Cells über die [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)-Methode hinzufügen.

Der folgende Beispielcode verwendet die [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)-Methode und fügt das **Buchkatalog-XML** hinzu und dessen Name ist **Buchhandlung**. Das folgende Bild zeigt das Ergebnis dieses Codes. Wie Sie sehen können, wird das Buchkatalog-XML innerhalb des Knotens Buchhandlung hinzugefügt, was der Name dieser Eigenschaft ist.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C#-Code zur Verwendung von benutzerdefinierten XML-Teilen

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Verwandter Artikel

- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind](/cells/de/net/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="csharp" >}}
