---
title: Benutzerdefinierte XML Teile hinzufügen und nach ID auswählen
type: docs
weight: 70
url: /de/python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **Mögliche Verwendungsszenarien**

Benutzerdefinierte XML-Teile sind die XML-Daten, die innerhalb der Microsoft Excel-Dokumente gespeichert sind und von den Anwendungen verwendet werden, die mit ihnen arbeiten. Es gibt derzeit keinen direkten Weg, sie über die Benutzeroberfläche von Microsoft Excel hinzuzufügen. Sie können sie jedoch programmatisch auf verschiedene Weisen hinzufügen, z.B. mit VSTO, mit Aspose.Cells usw. Bitte verwenden Sie die [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes)-Methode, wenn Sie benutzerdefinierte XML-Teile mit der Aspose.Cells für Python via .NET API hinzufügen möchten. Sie können auch deren ID setzen, mit der [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id)-Eigenschaft. Wenn Sie ein benutzerdefiniertes XML-Teil per ID auswählen möchten, können Sie die [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str)-Methode verwenden.

## **Benutzerdefinierte XML-Teile hinzufügen und nach ID auswählen**

Der folgende Beispielscode fügt zunächst vier benutzerdefinierte XML-Teile mit der Methode [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) hinzu. Danach setzt er ihre IDs mit der Eigenschaft [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id). Schließlich findet oder wählt er einen der hinzugefügten benutzerdefinierten XML-Teile mit der Methode [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str). Bitte sehen Sie auch die Konsolenausgabe des unten stehenden Codes zur Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **Konsolenausgabe**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

