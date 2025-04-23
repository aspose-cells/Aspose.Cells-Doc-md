---
title: Benutzerdefinierte XML Teile hinzufügen und nach ID auswählen
type: docs
weight: 70
url: /de/net/add-custom-xml-parts-and-select-them-by-id/
---

## **Mögliche Verwendungsszenarien**

Benutzerdefinierte XML-Teile sind die XML-Daten, die innerhalb der Microsoft Excel-Dokumente gespeichert sind und von den Anwendungen verwendet werden, die mit ihnen umgehen. Es gibt derzeit keine direkte Möglichkeit, sie über die Microsoft Excel-Benutzeroberfläche hinzuzufügen. Sie können sie jedoch programmgesteuert auf verschiedene Weisen hinzufügen, z. B. unter Verwendung von VSTO, unter Verwendung von Aspose.Cells usw. Verwenden Sie die Methode [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add), wenn Sie benutzerdefinierte XML-Teile mit der Aspose.Cells API hinzufügen möchten. Sie können auch ihre ID mit der Eigenschaft [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) festlegen. Ebenso, wenn Sie einen benutzerdefinierten XML-Teil anhand der ID auswählen möchten, können Sie die Methode [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid) verwenden.

## **Benutzerdefinierte XML-Teile hinzufügen und nach ID auswählen**

Der folgende Beispielscode fügt zunächst vier benutzerdefinierte XML-Teile mit der Methode [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) hinzu. Danach setzt er ihre IDs mit der Eigenschaft [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). Schließlich findet oder wählt er einen der hinzugefügten benutzerdefinierten XML-Teile mit der Methode [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid). Bitte sehen Sie auch die Konsolenausgabe des unten stehenden Codes zur Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
