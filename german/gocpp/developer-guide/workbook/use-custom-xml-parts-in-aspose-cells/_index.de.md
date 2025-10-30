---
title: Benutzerdefinierte XML Teile in Aspose.Cells mit Golang über C++ verwenden
linktitle: Verwendung von benutzerdefinierten XML Teilen
type: docs
weight: 390
url: /de/go-cpp/use-custom-xml-parts-in-aspose-cells/
description: Erfahren Sie, wie Sie benutzerdefinierte XML Teile in Excel Dateien programmatisch mit Aspose.Cells in Golang über C++ verwenden.
---

## Verwendung von benutzerdefinierten XML-Teilen in Aspose.Cells

Benutzerdefinierte XML-Teile sind XML-Daten, die von verschiedenen Anwendungen wie SharePoint innerhalb einer Excel-Datei gespeichert werden. Diese Daten werden von verschiedenen Anwendungen benötigt und verarbeitet. Microsoft Excel verwendet diese Daten nicht, daher gibt es keine GUI, um sie hinzuzufügen. Sie können diese Daten anzeigen, indem Sie die Erweiterung **.xlsx** in **.zip** ändern und die Datei mit **WinZip** öffnen. Alternativ können Sie die ZIP-Datei auch mit einem beliebigen Drittanbieter-Windows-Zip-Programm wie WinRAR oder WinZip öffnen. Die Daten befinden sich im Ordner **customXml**.

Sie können benutzerdefinierte XML-Teile mit Aspose.Cells über die [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/)-Methode hinzufügen.

Das folgende Beispiel zeigt, wie Sie mit der [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/)-Methode die **Book Catalog XML** hinzufügen, deren Name **BookStore** ist. Das folgende Bild zeigt das Ergebnis dieses Codes. Wie Sie sehen können, ist das Book Catalog XML innerhalb des Knoten **BookStore** hinzugefügt worden, der der Name dieser Eigenschaft ist.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C++-Code zur Verwendung benutzerdefinierter XML-Teile

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseCustomXmlPartsInAsposeCells.go" >}}
## Verwandter Artikel

- [Hinzufügen benutzerdefinierter Eigenschaften, die im Dokumentinformationsbereich sichtbar sind](/cells/de/cpp/adding-custom-properties-visible-inside-document-information-panel/)
