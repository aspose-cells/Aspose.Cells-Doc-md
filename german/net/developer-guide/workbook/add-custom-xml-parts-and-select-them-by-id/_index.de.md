---
title: Fügen Sie benutzerdefinierte XML-Teile hinzu und wählen Sie sie nach ID aus
type: docs
weight: 70
url: /de/net/add-custom-xml-parts-and-select-them-by-id/
---
## **Mögliche Nutzungsszenarien**

Benutzerdefinierte XML-Teile sind die XML-Daten, die in den Microsoft Excel-Dokumenten gespeichert sind und von den Anwendungen verwendet werden, die sich damit befassen. Derzeit gibt es keine direkte Möglichkeit, sie über die Excel-Benutzeroberfläche Microsoft hinzuzufügen. Sie können sie jedoch auf verschiedene Weise programmgesteuert hinzufügen, z. B. mit VSTO, mit Aspose.Cells usw. Bitte verwenden[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)-Methode, wenn Sie einen benutzerdefinierten XML-Teil mit Aspose.Cells API hinzufügen möchten. Sie können auch seine ID festlegen, indem Sie die verwenden[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)Eigentum. Wenn Sie benutzerdefiniertes XML-Teil nach ID auswählen möchten, können Sie auf ähnliche Weise verwenden[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)Methode.

## **Fügen Sie benutzerdefinierte XML-Teile hinzu und wählen Sie sie nach ID aus**

Der folgende Beispielcode fügt zunächst vier benutzerdefinierte XML-Teile hinzu[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)Methode. Anschließend setzt es ihre IDs mit[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) Eigentum. Schließlich findet oder wählt es einen der hinzugefügten benutzerdefinierten XML-Teile aus[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)Methode. Bitte beachten Sie auch die Konsolenausgabe des unten angegebenen Codes als Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
