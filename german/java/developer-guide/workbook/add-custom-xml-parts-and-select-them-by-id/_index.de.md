---
title: Benutzerdefinierte XML Teile hinzufügen und nach ID auswählen
type: docs
weight: 10
url: /de/java/add-custom-xml-parts-and-select-them-by-id/
---

## **Mögliche Verwendungsszenarien**

Benutzerdefinierte XML-Teile sind die XML-Daten, die in den Microsoft Excel-Dokumenten gespeichert sind und von den Anwendungen verwendet werden, die mit ihnen umgehen. Es gibt derzeit keine direkte Möglichkeit, sie über die Microsoft Excel-Benutzeroberfläche hinzuzufügen. Sie können sie jedoch programmgesteuert auf verschiedene Arten hinzufügen, z.B. mit VSTO, mit Aspose.Cells usw. Verwenden Sie die Methode [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add-java.lang.Object-), wenn Sie benutzerdefinierte XML-Teile über die Aspose.Cells-API hinzufügen möchten. Sie können auch deren ID festlegen, indem Sie die Eigenschaft [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID) verwenden. Ebenso können Sie, falls Sie ein benutzerdefiniertes XML-Teil nach ID auswählen möchten, die Methode [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID-java.lang.String-) verwenden.

## **Benutzerdefinierte XML-Teile hinzufügen und nach ID auswählen**

Der folgende Beispielcode fügt zunächst vier benutzerdefinierte XML-Teile mit der Methode [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add-java.lang.Object-) hinzu. Anschließend werden ihre IDs mit der Eigenschaft [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID) festgelegt. Schließlich wird eines der hinzugefügten benutzerdefinierten XML-Teile mit der Methode [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID-java.lang.String-) gefunden oder ausgewählt. Bitte sehen Sie auch die Konsolenausgabe des unten gegebenen Codes zur Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
