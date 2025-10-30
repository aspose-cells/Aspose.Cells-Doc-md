---
title: Hinzufügen benutzerdefinierter Eigenschaften, die im Dokumentinformationsfenster sichtbar sind, mit Node.js über C++
linktitle: Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind
type: docs
weight: 300
url: /de/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Lernen Sie, wie Sie benutzerdefinierte Eigenschaften mit Aspose.Cells for Node.js via C++ zu einem Arbeitsmappenobjekt hinzufügen. Diese Eigenschaften können im Dokumentinformationsbereich angezeigt werden.
---

## **Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind**

Aspose.Cells for Node.js via C++ kann verwendet werden, um benutzerdefinierte Eigenschaften innerhalb des Arbeitsmappenobjekts hinzuzufügen, die im Dokumentinformationsbereich sichtbar sind. Sie können den Dokumentinformationsbereich in Microsoft Excel über die Menübefehle Datei > Info > Eigenschaften > Dokumentbereich anzeigen öffnen.

Bitte verwenden Sie die [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/#add-string-string-)-Methode, um eine benutzerdefinierte Eigenschaft hinzuzufügen, die im Dokumentinformationsbereich sichtbar ist.

Der folgende Beispielcode fügt zwei benutzerdefinierte Eigenschaften hinzu. Die erste Eigenschaft hat keinen Typ, die zweite Eigenschaft hat den Typ DateTime. Sobald Sie die Ausgabedatei im Excel öffnen, die mit diesem Code generiert wurde, sehen Sie diese beiden Eigenschaften im Dokumentinformationsbereich.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Add simple property without any type
workbook.getContentTypeProperties().add("MK31", "Simple Data");

// Add date time property with type
workbook.getContentTypeProperties().add("MK32", "04-Mar-2015", "DateTime");

// Save the workbook
workbook.save(path.join(dataDir, "AddingCustomPropertiesVisible_out.xlsx"));
```

### **Verwandter Artikel**

{{% alert color="primary" %}}

- [Verwendung von benutzerdefinierten XML-Teilen in Aspose.Cells](/cells/de/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
