---
title: Fügen Sie benutzerdefinierte XML-Teile hinzu und wählen Sie sie nach ID aus
type: docs
weight: 10
url: /de/java/add-custom-xml-parts-and-select-them-by-id/
---
## **Mögliche Nutzungsszenarien**

Benutzerdefinierte XML-Teile sind die XML-Daten, die in den Microsoft Excel-Dokumenten gespeichert sind und von den Anwendungen verwendet werden, die sich damit befassen. Derzeit gibt es keine direkte Möglichkeit, sie über die Excel-Benutzeroberfläche Microsoft hinzuzufügen. Sie können sie jedoch auf verschiedene Weise programmgesteuert hinzufügen, z. B. mit*VSTO*, verwenden*Aspose.Cells*etc. Bitte verwenden[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object))-Methode, wenn Sie einen benutzerdefinierten XML-Teil mithilfe von Aspose.Cells API hinzufügen möchten. Sie können auch seine ID mithilfe von festlegen[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)Eigentum. Wenn Sie benutzerdefiniertes XML-Teil nach ID auswählen möchten, können Sie auf ähnliche Weise verwenden[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) Methode.

## **Fügen Sie benutzerdefinierte XML-Teile hinzu und wählen Sie sie nach ID aus**

Der folgende Beispielcode fügt zunächst vier benutzerdefinierte XML-Teile hinzu[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) Methode. Anschließend legt sie ihre IDs mit fest[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)Eigentum. Schließlich findet oder wählt es einen der hinzugefügten benutzerdefinierten XML-Teile aus[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) Methode. Bitte beachten Sie auch die Konsolenausgabe des unten angegebenen Codes als Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
