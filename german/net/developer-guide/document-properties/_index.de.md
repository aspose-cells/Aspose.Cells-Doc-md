---
title: Dokumenteigenschaften verwalten
linktitle: Dokumenteigenschaften
type: docs
weight: 80
url: /de/net/managing-document-properties/
description: Erfahren Sie, wie Sie die Dokumenteigenschaften durch die Aspose.Cells for NET APIs verwalten können.
keywords: Wie Sie Dokumenteigenschaften in C# verwalten, Dokumenteigenschaften in C# abrufen oder festlegen, Dokumenteigenschaften in C# hinzufügen oder löschen, Dokumenteigenschaften in C# einfügen oder entfernen, Dokumenteigenschaften mit Aspose.Cells for NET APIs abrufen.
---


## **Einführung**

Microsoft Excel bietet die Möglichkeit, Eigenschaften zu Tabellendateien hinzuzufügen. Diese Dokumenteigenschaften liefern nützliche Informationen und sind in 2 Kategorien unterteilt, wie unten näher beschrieben.

- Systemdefinierte (eingebaute) Eigenschaften: Eingebaute Eigenschaften enthalten allgemeine Informationen zum Dokument wie Dokumententitel, Autorname, Dokumentenstatistiken und so weiter.
- Benutzerdefinierte (benutzerdefinierte) Eigenschaften: Benutzerdefinierte Eigenschaften, die vom Endbenutzer in Form von Schlüssel-Wert-Paar definiert werden.

{{% alert color="primary" %}}

Der wichtigste Punkt über eingebaute und benutzerdefinierte Eigenschaften ist, dass auf eingebaute Eigenschaften zugegriffen und geändert, aber nicht erstellt oder entfernt werden kann. Benutzerdefinierte Eigenschaften hingegen können erstellt und verwaltet werden.

{{% /alert %}}

## **So verwalten Sie Dokumenteigenschaften mit Microsoft Excel**

Microsoft Excel ermöglicht es Ihnen, die Dokumenteigenschaften der Excel-Dateien auf eine WYSIWYG-Manier zu verwalten. Befolgen Sie bitte die untenstehenden Schritte, um den **Eigenschaften**-Dialog in Excel 2016 zu öffnen.

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

Aspose.Cells for .NET schreibt direkt die Informationen über API und Versionsnummer in Ausgabedokumente. Zum Beispiel füllt Aspose.Cells for .NET beim Rendern des Dokuments in PDF das Feld **Anwendung** mit dem Wert 'Aspose.Cells' und das Feld **PDF-Produzent** mit dem Wert, z. B. 'Aspose.Cells v17.9'.

Bitte beachten Sie, dass Sie Aspose.Cells for .NET nicht anweisen können, diese Informationen aus den Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

### **Wie Sie auf Dokumenteigenschaften zugreifen**

Aspose.Cells APIs unterstützen beide Arten von Dokumenteigenschaften, eingebaute und benutzerdefinierte. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) von Aspose.Cells repräsentiert eine Excel-Datei und, wie eine Excel-Datei, kann die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) mehrere Arbeitsblätter enthalten, die jeweils durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert werden, während die Sammlung von Arbeitsblättern durch die Klasse [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) repräsentiert wird.

Verwenden Sie [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), um die Dokumenteigenschaften der Datei wie unten beschrieben abzurufen.

- Um auf die integrierten Dokumenteigenschaften zuzugreifen, verwenden Sie [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
- Um auf benutzerdefinierte Dokumenteigenschaften zuzugreifen, verwenden Sie [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

Sowohl [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) als auch [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) geben die Instanz von [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection) zurück. Diese Sammlung enthält [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) Objekte, von denen jedes eine einzelne integrierte oder benutzerdefinierte Dokumenteigenschaft darstellt.

Es liegt an den Anwendungsanforderungen, wie auf eine Eigenschaft zugegriffen wird; durch Verwendung des Indexes oder des Namens der Eigenschaft aus [**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection), wie im folgenden Beispiel demonstriert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

Die Klasse [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) erlaubt das Abrufen des Namens, Werts und Typs der Dokumenteigenschaft:

- Um den Eigenschaftsnamen zu erhalten, verwenden Sie [**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
- Um den Eigenschaftswert zu erhalten, verwenden Sie [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) gibt den Wert als Object zurück.
- Um den Eigenschaftstyp zu erhalten, verwenden Sie [**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type). Dies gibt einen der [**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype) Aufzählungswerte zurück. Nachdem Sie den Eigenschaftstyp erhalten haben, verwenden Sie eine der **DocumentProperty.ToXXX**-Methoden, um den Wert des entsprechenden Typs zu erhalten, anstatt [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) zu verwenden. Die **DocumentProperty.ToXXX**-Methoden werden in der untenstehenden Tabelle beschrieben.

{{% alert color="primary" %}}

Die [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)-Klasse bietet auch eine Reihe von Methoden, die die Werte anderer Datentypen zurückgeben.

{{% /alert %}}

|**Member Name**|**Beschreibung**|**ToXXX Methode**|
| :- | :- | :- |
|Boolean|Der Eigenschaftsdatentyp ist Boolean|ToBool|
|Date|Der Eigenschaftsdatentyp ist DateTime. Beachten Sie, dass Microsoft Excel nur den Datumsanteil speichert, keine Zeit in einer benutzerdefinierten Eigenschaft dieses Typs gespeichert werden kann|ToDateTime|
|Float|Der Eigenschaftsdatentyp ist Double|ToDouble|
|Number|Der Eigenschaftsdatentyp ist Int32|ToInt|
|String|Der Eigenschaftsdatentyp ist String|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Hinzufügen oder Entfernen von benutzerdefinierten Dokumenteigenschaften**

Wie wir zu Beginn dieses Themas bereits beschrieben haben, können Entwickler integrierte Eigenschaften nicht hinzufügen oder entfernen, da diese Eigenschaften systemdefiniert sind, es ist jedoch möglich, benutzerdefinierte Eigenschaften hinzuzufügen oder zu entfernen, da diese benutzerdefiniert sind.

### **Hinzufügen von benutzerdefinierten Eigenschaften**

Aspose.Cells-APIs haben die Methode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) für die Klasse [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) freigelegt, um benutzerdefinierte Eigenschaften zur Sammlung hinzuzufügen. Die Methode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) fügt die Eigenschaft zur Excel-Datei hinzu und gibt eine Referenz für die neue Dokumenteigenschaft als [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)-Objekt zurück.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Wie konfiguriert man die benutzerdefinierte Eigenschaft „Verknüpfung zum Inhalt“?**

Um eine benutzerdefinierte Eigenschaft zu erstellen, die mit dem Inhalt eines bestimmten Bereichs verknüpft ist, rufen Sie die Methode [**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) auf und übergeben den Eigenschaftsnamen und die Quelle. Sie können über die Eigenschaft [**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) überprüfen, ob eine Eigenschaft als mit dem Inhalt verknüpft konfiguriert ist. Außerdem ist es auch möglich, den Quellbereich unter Verwendung der Eigenschaft [**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) der Klasse [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) zu erhalten.

Im Beispiel verwenden wir eine einfache Vorlage einer Microsoft Excel-Datei. Die Arbeitsmappe hat einen definierten benannten Bereich namens **MeinBereich**, der sich auf einen Zellenwert bezieht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Wie entfernt man benutzerdefinierte Eigenschaften**

Um benutzerdefinierte Eigenschaften mit Aspose.Cells zu entfernen, rufen Sie die Methode [**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove) auf und übergeben den Namen der zu entfernenden Dokumenteigenschaft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Erweiterte Themen**
- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind](/cells/de/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Festlegen der Eigenschaften ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften](/cells/de/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Festlegen der Dokumentversion der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften](/cells/de/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Festlegen der Sprache der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften](/cells/de/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
