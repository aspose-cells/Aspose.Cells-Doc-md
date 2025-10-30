---
title: Hinzufügen benutzerdefinierter Eigenschaften, die im Dokumentinformationen Panel sichtbar sind, mit Golang über C++
linktitle: Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind
type: docs
weight: 300
url: /de/go-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Lernen Sie, wie Sie benutzerdefinierte Eigenschaften hinzufügen, die im Dokumentinformationen Panel mit Aspose.Cells und Golang über C++ sichtbar sind.
---

## **Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind**

Aspose.Cells kann verwendet werden, um benutzerdefinierte Eigenschaften im Arbeitsmappenobjekt hinzuzufügen, die im Dokumentinformationsfeld sichtbar sind. Sie können das Dokumentinformationsfeld in Microsoft Excel über die Befehle Datei > Informationen > Eigenschaften > Dokumentinformationsfeld anzeigen öffnen.

Bitte verwenden Sie die [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/)-Methode, um eine benutzerdefinierte Eigenschaft hinzuzufügen, die im Dokumentinformationsbereich sichtbar ist.

Der folgende Beispielcode fügt zwei benutzerdefinierte Eigenschaften hinzu. Die erste Eigenschaft hat keinen Typ, die zweite Eigenschaft hat den Typ DateTime. Sobald Sie die Ausgabedatei im Excel öffnen, die mit diesem Code generiert wurde, sehen Sie diese beiden Eigenschaften im Dokumentinformationsbereich.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingCustomPropertiesVisibleInsideDocumentInformationPanel.go" >}}
### **Verwandter Artikel**

{{% alert color="primary" %}}

- [Verwendung von benutzerdefinierten XML-Teilen in Aspose.Cells](/cells/de/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
