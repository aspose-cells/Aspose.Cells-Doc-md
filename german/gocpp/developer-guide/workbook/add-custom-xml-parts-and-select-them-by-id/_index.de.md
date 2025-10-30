---
title: Benutzerdefinierte XML Teile hinzufügen und nach ID auswählen mit Golang via C++
linktitle: Benutzerdefinierte XML Teile hinzufügen und nach ID auswählen
type: docs
weight: 70
url: /de/go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Lernen, wie man benutzerdefinierte XML Teile in Excel Dateien mit Aspose.Cells mit Golang via C++ hinzufügt und auswählt.
---

## **Mögliche Verwendungsszenarien**

Benutzerdefinierte XML-Parts sind XML-Daten, die in Microsoft Excel-Dokumenten gespeichert werden und von Anwendungen genutzt werden, die mit ihnen interagieren. Derzeit gibt es keine direkte Möglichkeit, sie mit der Microsoft Excel-Benutzeroberfläche hinzuzufügen. Sie können sie jedoch programmatisch auf verschiedene Weisen hinzufügen, z.B. mit VSTO oder Aspose.Cells. Verwenden Sie die [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/)-Methode, um einen benutzerdefinierten XML-Teil mit der API von Aspose.Cells hinzuzufügen. Sie können auch seine ID mit der [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)-Eigenschaft festlegen. Wenn Sie einen benutzerdefinierten XML-Teil nach ID auswählen möchten, können Sie die [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)-Methode verwenden.

## **Benutzerdefinierte XML-Teile hinzufügen und nach ID auswählen**

Der folgende Beispielcode fügt zunächst vier benutzerdefinierte XML-Parts mit der [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/)-Methode hinzu. Dann setzt er ihre IDs mit der [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)-Eigenschaft. Schließlich findet oder wählt er einen der hinzugefügten benutzerdefinierten XML-Parts mit der [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)-Methode. Bitte sehen Sie sich auch die Konsolenausgabe des unten angegebenen Codes zur Referenz an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **Konsolenausgabe**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
