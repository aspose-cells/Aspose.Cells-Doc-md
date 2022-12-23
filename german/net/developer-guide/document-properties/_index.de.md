---
title: Dokumenteigenschaften verwalten
linktitle: Dokumenteigenschaften
type: docs
weight: 80
url: /de/net/managing-document-properties/
description: Dokumenteigenschaften von Tabellenkalkulationsdateien verwalten.
---
## **Einführung**

Microsoft Excel bietet die Möglichkeit, Tabellenkalkulationsdateien Eigenschaften hinzuzufügen. Diese Dokumenteigenschaften bieten nützliche Informationen und sind wie unten beschrieben in zwei Kategorien unterteilt.

- Systemdefinierte (eingebaute) Eigenschaften: Eingebaute Eigenschaften enthalten allgemeine Informationen über das Dokument wie Dokumenttitel, Autorenname, Dokumentstatistiken und so weiter.
- Benutzerdefinierte (benutzerdefinierte) Eigenschaften: Benutzerdefinierte Eigenschaften, die vom Endbenutzer in Form von Name-Wert-Paaren definiert werden.

{{% alert color="primary" %}}

Der wichtigste Punkt, den Sie über integrierte und benutzerdefinierte Eigenschaften wissen sollten, ist, dass auf integrierte Eigenschaften zugegriffen und diese geändert, aber nicht erstellt oder entfernt werden können. Es können jedoch benutzerdefinierte Eigenschaften erstellt und verwaltet werden.

{{% /alert %}}

## **Dokumenteigenschaften mit Microsoft Excel verwalten**

 Microsoft Mit Excel können Sie die Dokumenteigenschaften der Excel-Dateien WYSIWYG-artig verwalten. Bitte befolgen Sie die nachstehenden Schritte, um die zu öffnen**Eigenschaften** Dialogfeld in Excel 2016.

1.  Von dem**Datei** Menü, auswählen**Die Info**.

|**Auswählen des Info-Menüs**|
|:- |
|![todo: Bild_alt_Text](managing-document-properties_1.png)|
1.  Klicke auf**Eigenschaften**Überschrift und wählen Sie "Erweiterte Eigenschaften".

|**Klicken Sie auf Erweiterte Eigenschaftenauswahl**|
|:- |
|![todo: Bild_alt_Text](managing-document-properties_2.png)|
1. Verwalten Sie die Dokumenteigenschaften der Datei.

|**Eigenschaftendialog**|
|:- |
|![todo: Bild_alt_Text](managing-document-properties_3.png)|
Im Eigenschaftendialog gibt es verschiedene Registerkarten wie Allgemein, Zusammenfassung, Statistik, Inhalt und Benutzerdefiniert. Jede Registerkarte hilft bei der Konfiguration verschiedener Arten von Informationen in Bezug auf die Datei. Die Registerkarte Benutzerdefiniert wird verwendet, um benutzerdefinierte Eigenschaften zu verwalten.

## **Arbeiten mit Dokumenteigenschaften mit Aspose.Cells**

Entwickler können die Dokumenteigenschaften mithilfe der Aspose.Cells-APIs dynamisch verwalten. Diese Funktion hilft den Entwicklern, nützliche Informationen zusammen mit der Datei zu speichern, z. B. wann die Datei empfangen, verarbeitet, mit einem Zeitstempel versehen wurde und so weiter.

{{% alert color="primary" %}}

 Aspose.Cells for .NET schreibt die Informationen über API und die Versionsnummer direkt in Ausgabedokumente. Beispielsweise wird beim Rendern von Dokument an PDF Aspose.Cells for .NET ausgefüllt**Anwendung** Feld mit dem Wert 'Aspose.Cells' und**PDF Hersteller** Feld mit dem Wert, zB 'Aspose.Cells v17.9'.

Bitte beachten Sie, dass Sie Aspose.Cells for .NET nicht anweisen können, diese Informationen aus Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

### **Zugriff auf Dokumenteigenschaften**

Aspose.Cells APIs unterstützen beide Arten von Dokumenteigenschaften, integrierte und benutzerdefinierte. Aspose.Cells'[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse stellt eine Excel-Datei dar und wie eine Excel-Datei die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Die Klasse kann mehrere Arbeitsblätter enthalten, die jeweils durch dargestellt werden[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse, während die Sammlung von Arbeitsblättern durch die dargestellt wird[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Klasse.

 Verwenden Sie die[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), um wie unten beschrieben auf die Dokumenteigenschaften der Datei zuzugreifen.

-  Um auf integrierte Dokumenteigenschaften zuzugreifen, verwenden Sie[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Um auf benutzerdefinierte Dokumenteigenschaften zuzugreifen, verwenden Sie[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Beide[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) und[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) gibt die Instanz von zurück[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Diese Sammlung enthält[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)-Objekte, die jeweils eine einzelne integrierte oder benutzerdefinierte Dokumenteigenschaft darstellen.

 Es hängt von der Anwendungsanforderung ab, wie auf eine Eigenschaft zugegriffen wird, das heißt; indem Sie den Index oder Namen der Eigenschaft aus dem verwenden[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)wie im folgenden Beispiel gezeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 Das[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)-Klasse ermöglicht es, den Namen, Wert und Typ der Dokumenteigenschaft abzurufen:

-  Verwenden Sie zum Abrufen des Eigenschaftsnamens[**Dokumenteigenschaft.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Um den Eigenschaftswert zu erhalten, verwenden Sie[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)gibt den Wert als Objekt zurück.
-  Verwenden Sie zum Abrufen des Eigenschaftstyps[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Dies gibt eine der zurück[**Art der Immobilie**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype) Aufzählungswerte. Nachdem Sie den Eigenschaftstyp erhalten haben, verwenden Sie eine der**DocumentProperty.ToXXX** Methoden, um den Wert des entsprechenden Typs zu erhalten, anstatt zu verwenden[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . Das**DocumentProperty.ToXXX**Methoden sind in der folgenden Tabelle beschrieben.

{{% alert color="primary" %}}

 Das[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)Die Klasse stellt auch eine Reihe von Methoden bereit, die die Werte anderer Datentypen zurückgeben.

{{% /alert %}}

|**Mitgliedsname**|**Beschreibung**|**ToXXX-Methode**|
|:- |:- |:- |
|Boolesch|Der Eigenschaftsdatentyp ist Boolean|ToBool|
|Datum|Der Eigenschaftsdatentyp ist DateTime. Beachten Sie, dass Microsoft nur Excel speichert<br>B. dem Datumsteil, kann keine Uhrzeit in einer benutzerdefinierten Eigenschaft dieses Typs gespeichert werden|ToDateTime|
|Schweben|Der Eigenschaftsdatentyp ist Double|Verdoppeln|
|Anzahl|Der Eigenschaftsdatentyp ist Int32|ToInt|
|Schnur|Der Eigenschaftsdatentyp ist String|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Hinzufügen oder Entfernen von benutzerdefinierten Dokumenteigenschaften**

Wie wir bereits zu Beginn dieses Themas beschrieben haben, können Entwickler keine integrierten Eigenschaften hinzufügen oder entfernen, da diese Eigenschaften systemdefiniert sind, aber es ist möglich, benutzerdefinierte Eigenschaften hinzuzufügen oder zu entfernen, da diese benutzerdefiniert sind.

### **Hinzufügen von benutzerdefinierten Eigenschaften**

 Aspose.Cells APIs haben die ausgesetzt[**Addieren**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) Methode für die[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) -Klasse, um der Sammlung benutzerdefinierte Eigenschaften hinzuzufügen. Das[**Addieren**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) -Methode fügt die Eigenschaft der Excel-Datei hinzu und gibt einen Verweis auf die neue Dokumenteigenschaft als zurück[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)Objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Konfigurieren der benutzerdefinierten Eigenschaft „Link zum Inhalt“.**

 Um eine benutzerdefinierte Eigenschaft zu erstellen, die mit dem Inhalt eines bestimmten Bereichs verknüpft ist, rufen Sie die auf[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) -Methode und übergeben Sie den Eigenschaftsnamen und die Quelle. Sie können überprüfen, ob eine Eigenschaft als mit Inhalt verknüpft konfiguriert ist, indem Sie die verwenden[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) Eigentum. Darüber hinaus ist es auch möglich, den Quellbereich mithilfe von abzurufen[**Quelle**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) Eigentum der[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)Klasse.

 Wir verwenden im Beispiel eine einfache Vorlage Microsoft Excel-Datei. Die Arbeitsmappe hat einen definierten benannten Bereich mit der Bezeichnung**MeineRange** was sich auf einen Zellenwert bezieht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Benutzerdefinierte Eigenschaften entfernen**

 Um benutzerdefinierte Eigenschaften mit Aspose.Cells zu entfernen, rufen Sie die an[**DocumentPropertyCollection.Entfernen**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)-Methode und übergeben Sie den Namen der zu entfernenden Dokumenteigenschaft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Themen vorantreiben**
- [Hinzufügen von benutzerdefinierten Eigenschaften, die im Dokumentinformationsbereich sichtbar sind](/cells/de/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Festlegen der ScaleCrop- und LinksUpToDate-Eigenschaften der integrierten Dokumenteigenschaften](/cells/de/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Geben Sie die Dokumentversion der Excel-Datei mithilfe der integrierten Dokumenteigenschaften an](/cells/de/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Geben Sie die Sprache der Excel-Datei mithilfe der integrierten Dokumenteigenschaften an](/cells/de/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
