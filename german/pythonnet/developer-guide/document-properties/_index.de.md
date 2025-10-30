---
title: Dokumenteigenschaften verwalten
linktitle: Dokumenteigenschaften
type: docs
weight: 80
url: /de/python-net/managing-document-properties/
description: Erfahren Sie, wie Sie Dokumenteigenschaften mit den Aspose.Cells für Python via .NET APIs verwalten.
keywords: Wie man Dokumenteigenschaften in C# verwaltet, Dokumenteigenschaften abrufen oder festlegen mit C#, Dokumenteigenschaften hinzufügen oder löschen mit C#, Dokumenteigenschaften einfügen oder entfernen mit C#, Zugriff auf Dokumenteigenschaften mit Aspose.Cells für Python via .NET APIs.
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

Entwickler können die Dokumenteigenschaften dynamisch mit den Aspose.Cells für Python via .NET APIs verwalten. Diese Funktion hilft den Entwicklern, nützliche Informationen zusammen mit der Datei zu speichern, wie z.B. wann die Datei empfangen, verarbeitet, zeitgestempelt wurde usw.

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET schreibt direkt die API- und Versionsnummer-Informationen in Ausgabedokumente. Zum Beispiel, bei der Konvertierung eines Dokuments in PDF füllt Aspose.Cells für Python via .NET das **Application**-Feld mit dem Wert 'Aspose.Cells' und das **PDF Producer**-Feld mit dem Wert, z.B. 'Aspose.Cells for Python via .NET v17.9'.

Bitte beachten Sie, dass Sie Aspose.Cells für Python via .NET nicht anweisen können, diese Informationen aus Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}


### **Hinzufügen oder Entfernen von benutzerdefinierten Dokumenteigenschaften**

Wie wir zu Beginn dieses Themas bereits beschrieben haben, können Entwickler integrierte Eigenschaften nicht hinzufügen oder entfernen, da diese Eigenschaften systemdefiniert sind, es ist jedoch möglich, benutzerdefinierte Eigenschaften hinzuzufügen oder zu entfernen, da diese benutzerdefiniert sind.

### **Hinzufügen von benutzerdefinierten Eigenschaften**

Die Aspose.Cells für Python via .NET APIs haben die [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) Methode für die [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection) Klasse bereitgestellt, um benutzerdefinierte Eigenschaften zur Sammlung hinzuzufügen. Die [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) Methode fügt die Eigenschaft in die Excel-Datei ein und gibt eine Referenz auf die neue Dokumenteigenschaft als [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/documentproperty) Objekt zurück.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **Erweiterte Themen**
- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsfeld sichtbar sind](/cells/de/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [Festlegen der Eigenschaften ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften](/cells/de/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Festlegen der Dokumentversion der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften](/cells/de/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Festlegen der Sprache der Excel-Datei unter Verwendung eingebauter Dokumenteigenschaften](/cells/de/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

{{< app/cells/assistant language="python-net" >}}
