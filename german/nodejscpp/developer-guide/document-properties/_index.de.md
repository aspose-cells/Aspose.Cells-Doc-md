---
title: Verwalten von Dokumenteigenschaften mit Node.js via C++
linktitle: Dokumenteigenschaften
type: docs
weight: 80
url: /de/nodejs-cpp/managing-document-properties/
description: Erfahren Sie, wie Sie Dokumenteigenschaften durch die APIs von Aspose.Cells for Node.js via C++ verwalten.
keywords: Wie man Dokumenteigenschaften in Node.js über C++ verwaltet, Dokumenteigenschaften mit Node.js über C++ abruft oder festlegt, Dokumenteigenschaften via Node.js über C++ hinzufügt oder löscht, Dokumenteigenschaften mit Node.js über C++ einfügt oder entfernt, Zugriff auf Dokumenteigenschaften mit Aspose.Cells for Node.js via C++ APIs.
---


## **Einführung**

Microsoft Excel bietet die Möglichkeit, Eigenschaften zu Tabellendateien hinzuzufügen. Diese Dokumenteigenschaften liefern nützliche Informationen und sind in 2 Kategorien unterteilt, wie unten näher beschrieben.

- Systemdefinierte (eingebaute) Eigenschaften: Eingebaute Eigenschaften enthalten allgemeine Informationen zum Dokument wie Dokumententitel, Autorname, Dokumentenstatistiken und so weiter.
- Benutzerdefinierte (benutzerdefinierte) Eigenschaften: Benutzerdefinierte Eigenschaften, die vom Endbenutzer in Form von Schlüssel-Wert-Paar definiert werden.

{{% alert color="primary" %}}

Der wichtigste Punkt über eingebaute und benutzerdefinierte Eigenschaften ist, dass auf eingebaute Eigenschaften zugegriffen und geändert, aber nicht erstellt oder entfernt werden kann. Benutzerdefinierte Eigenschaften hingegen können erstellt und verwaltet werden.

{{% /alert %}}

## **So verwalten Sie Dokumenteigenschaften mit Microsoft Excel**

Microsoft Excel ermöglicht es, die Dokumenteigenschaften der Excel-Dateien WYSIWYG-mäßig zu verwalten. Bitte folgen Sie den unten stehenden Schritten, um den **Eigenschaften**-Dialog in Excel 2016 zu öffnen.

1. Wählen Sie im **Datei**-Menü **Info** aus.

|**Auswahl des Info-Menüs**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Klicken Sie auf die Überschrift **Eigenschaften** und wählen Sie "Erweiterte Eigenschaften" aus.

|**Klicken Sie auf die Auswahl der erweiterten Eigenschaften**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Verwalten Sie die Dokumenteigenschaften der Datei.

|**Eigenschaften Dialog**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Im Eigenschaften-Dialog gibt es verschiedene Registerkarten wie Allgemein, Zusammenfassung, Statistiken, Inhalt und Benutzerdefinierte. Jede Registerkarte dient dazu, verschiedene Arten von Informationen im Zusammenhang mit der Datei zu konfigurieren. Die Registerkarte Benutzerdefiniert wird verwendet, um benutzerdefinierte Eigenschaften zu verwalten.

## **So arbeiten Sie mit Dokumenteigenschaften mit Aspose.Cells**

Entwickler können die Dokumenteigenschaften dynamisch mit den Aspose.Cells APIs verwalten. Diese Funktion hilft den Entwicklern, nützliche Informationen zusammen mit der Datei zu speichern, z. B. wann die Datei empfangen, verarbeitet, zeitgestempelt wurde usw.

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ schreibt direkt die Informationen über API und Versionsnummer in die Ausgabedokumente. Zum Beispiel, beim Rendern eines Dokuments zu PDF füllt Aspose.Cells for Node.js via C++ die Felder **Anwendung** mit dem Wert 'Aspose.Cells' und **PDF-Ersteller** mit dem Wert, z.B. 'Aspose.Cells v17.9'.

Bitte beachten Sie, dass Sie Aspose.Cells for Node.js via C++ nicht anweisen können, diese Informationen aus Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

### **Wie Sie auf Dokumenteigenschaften zugreifen**

Aspose.Cells APIs unterstützen beide Arten von Dokumenteigenschaften, eingebaut und benutzerdefiniert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) von Aspose.Cells repräsentiert eine Excel-Datei und, wie eine Excel-Datei, kann die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) mehrere Arbeitsblätter enthalten, die jeweils durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dargestellt werden, während die Sammlung der Arbeitsblätter durch die Klasse [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) repräsentiert wird.

Verwenden Sie den [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), um auf die Dokumenteigenschaften der Datei wie unten beschrieben zuzugreifen.

- Um auf die integrierten Dokumenteigenschaften zuzugreifen, verwenden Sie [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--).
- Um auf benutzerdefinierte Dokumenteigenschaften zuzugreifen, verwenden Sie [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--).

Sowohl [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--) als auch [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--) geben die Instanz von [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/) zurück. Diese Sammlung enthält [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) Objekte, die jeweils eine einzelne eingebaut oder benutzerdefinierte Dokumenteigenschaft repräsentieren.

Es liegt an der Anwendungsanforderung, wie man auf eine Eigenschaft zugreift; d.h. entweder durch Verwendung des Index oder des Namens der Eigenschaft aus [**DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/), wie im Beispiel unten demonstriert.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property by using the property name
const customProperty1 = customProperties.get("ContentTypeId");
console.log(`${customProperty1.getName()} ${customProperty1.getValue()}`);

// Accessing the same custom document property by using the property index
const customProperty2 = customProperties.get(0);
console.log(`${customProperty2.getName()} ${customProperty2.getValue()}`);
```

Die Klasse [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) erlaubt das Abrufen des Namens, Werts und Typs der Dokumenteigenschaft:

- Um den Eigenschaftsnamen zu erhalten, verwenden Sie [**DocumentProperty.getName()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getName--).
- Um den Eigenschaftswert zu erhalten, verwenden Sie [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) gibt den Wert als Objekt zurück.
- Um den Eigenschaftstyp zu erhalten, verwenden Sie [**DocumentProperty.getType()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getType--). Dies gibt einen der [**PropertyType**](https://reference.aspose.com/cells/nodejs-cpp/propertytype/) Aufzählungswerte zurück. Nachdem Sie den Eigenschaftstyp erhalten haben, nutzen Sie eine der Methoden **DocumentProperty.ToXXX**, um den Wert des entsprechenden Typs zu erhalten, anstatt [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) zu verwenden. Die **DocumentProperty.ToXXX**-Methoden sind in der Tabelle unten beschrieben.

{{% alert color="primary" %}}

Die Klasse [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) bietet auch eine Reihe von Methoden, die die Werte anderer Datentypen zurückgeben.

{{% /alert %}}

|**Member Name**|**Beschreibung**|**ToXXX Methode**|
| :- | :- | :- |
|Boolean|Der Eigenschaftsdatentyp ist Boolean|ToBool|
|Date|Der Eigenschaftsdatentyp ist DateTime. Beachten Sie, dass Microsoft Excel nur den Datumsanteil speichert, keine Zeit in einer benutzerdefinierten Eigenschaft dieses Typs gespeichert werden kann|ToDateTime|
|Float|Der Eigenschaftsdatentyp ist Double|ToDouble|
|Number|Der Eigenschaftsdatentyp ist Int32|ToInt|
|String|Der Datentyp der Eigenschaft ist string|ToString|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property
const customProperty1 = customProperties.get(0);

// Storing the value of the document property as an object
const objectValue = customProperty1.getValue();

// Accessing a custom document property
const customProperty2 = customProperties.get(1);

// Checking the type of the document property and then storing the value of the
// document property according to that type
if (customProperty2.getType() === AsposeCells.PropertyType.String) {
const value = customProperty2.getValue().toString();
console.log(`${customProperty2.getName()} : ${value}`);
}
```

### **Hinzufügen oder Entfernen von benutzerdefinierten Dokumenteigenschaften**

Wie wir zu Beginn dieses Themas bereits beschrieben haben, können Entwickler integrierte Eigenschaften nicht hinzufügen oder entfernen, da diese Eigenschaften systemdefiniert sind, es ist jedoch möglich, benutzerdefinierte Eigenschaften hinzuzufügen oder zu entfernen, da diese benutzerdefiniert sind.

### **Hinzufügen von benutzerdefinierten Eigenschaften**

Aspose.Cells APIs haben die Methode [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) für die Klasse [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/) bereitgestellt, um benutzerdefinierte Eigenschaften zur Sammlung hinzuzufügen. Die Methode [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) fügt die Eigenschaft in die Excel-Datei ein und gibt eine Referenz auf die neue Dokumenteigenschaft als [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) Objekt zurück.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Adding a custom document property to the Excel file
customProperties.add("Publisher", "Aspose");

// Saving resultant spreadsheet
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Wie konfiguriert man die benutzerdefinierte Eigenschaft „Verknüpfung zum Inhalt“?**

Um eine benutzerdefinierte Eigenschaft zu erstellen, die mit dem Inhalt eines bestimmten Bereichs verknüpft ist, rufen Sie die Methode [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) auf und übergeben den Eigenschaftsnamen und die Quelle. Sie können überprüfen, ob eine Eigenschaft als mit Inhalt verknüpft konfiguriert ist, indem Sie die [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#isLinkedToContent--) Eigenschaft verwenden. Außerdem ist es möglich, den Quellenbereich mit der [**getSource()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getSource--) Eigenschaft der [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) Klasse abzurufen.

Im Beispiel verwenden wir eine einfache Vorlage einer Microsoft Excel-Datei. Die Arbeitsmappe hat einen definierten benannten Bereich namens **MeinBereich**, der sich auf einen Zellenwert bezieht.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate an object of Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getWorksheets().getCustomDocumentProperties();

// Add link to content.
customProperties.addLinkToContent("Owner", "MyRange");

// Accessing the custom document property by using the property name
const customProperty1 = customProperties.get("Owner");

// Check whether the property is linked to content
const isLinkedToContent = customProperty1.isLinkedToContent();

// Get the source for the property
const source = customProperty1.getSource();

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Wie entfernt man benutzerdefinierte Eigenschaften**

Um benutzerdefinierte Eigenschaften mit Aspose.Cells zu entfernen, rufen Sie die Methode [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/#remove-string-) auf und übergeben den Namen der zu entfernenden Dokumenteigenschaft.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Removing a custom document property
customProperties.remove("Publisher");

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

## **Erweiterte Themen**
- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind](/cells/de/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Festlegen der Eigenschaften ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften](/cells/de/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Festlegen der Dokumentversion der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften](/cells/de/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Festlegen der Sprache der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften](/cells/de/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
{{< app/cells/assistant language="nodejs-cpp" >}}
