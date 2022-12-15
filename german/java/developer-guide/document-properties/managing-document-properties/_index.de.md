---
title: Dokumenteigenschaften verwalten
type: docs
weight: 10
url: /de/java/managing-document-properties/
---
## **Einführung**

Microsoft Excel bietet die Möglichkeit, Tabellenkalkulationsdateien Eigenschaften hinzuzufügen. Diese Dokumenteigenschaften bieten nützliche Informationen und sind wie unten beschrieben in zwei Kategorien unterteilt.

- Systemdefinierte (eingebaute) Eigenschaften: Eingebaute Eigenschaften enthalten allgemeine Informationen über das Dokument wie Dokumenttitel, Autorenname, Dokumentstatistiken und so weiter.
- Benutzerdefinierte (benutzerdefinierte) Eigenschaften: Benutzerdefinierte Eigenschaften, die vom Endbenutzer in Form von Name-Wert-Paaren definiert werden.

{{% alert color="primary" %}}

Der wichtigste Punkt, den Sie über integrierte und benutzerdefinierte Eigenschaften wissen sollten, ist, dass auf integrierte Eigenschaften zugegriffen und diese geändert, aber nicht erstellt oder entfernt werden können. Benutzerdefinierte Dokumenteigenschaften können jedoch erstellt und verwaltet werden.

{{% /alert %}}

## **Dokumenteigenschaften mit Microsoft Excel verwalten**

 Microsoft Excel ermöglicht die Verwaltung von Dokumenteigenschaften der Excel-Dateien auf WYSIWYG-Weise. Bitte befolgen Sie die nachstehenden Schritte, um die zu öffnen**Eigenschaften** Dialogfeld in Excel 2016.

1.  Von dem**Datei** Menü, auswählen**Die Info**.

|**Auswählen des Info-Menüs**|
|:- |
|![todo: Bild_alt_Text](managing-document-properties_1.png)|
1.  Klicke auf**Eigenschaften** Überschrift und wählen Sie "Erweiterte Eigenschaften".

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

 Aspose.Cells for Java schreibt die Informationen über API und die Versionsnummer direkt in Ausgabedokumente. Beim Rendern von Document in PDF wird beispielsweise Aspose.Cells for Java ausgefüllt**Anwendung** Feld mit dem Wert 'Aspose.Cells' und**PDF-Produzent** Feld mit dem Wert, zB 'Aspose.Cells for Java v17.9'.

Bitte beachten Sie, dass Sie Aspose.Cells for Java nicht anweisen können, diese Informationen aus Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

### **Zugriff auf Dokumenteigenschaften**

 Aspose.Cells APIs unterstützen beide Arten von Dokumenteigenschaften, integrierte und benutzerdefinierte. Aspose.Cells'[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse stellt eine Excel-Datei dar und wie eine Excel-Datei die[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Die Klasse kann mehrere Arbeitsblätter enthalten, die jeweils durch dargestellt werden[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse, während die Sammlung von Arbeitsblättern durch die dargestellt wird[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Klasse.

 Verwenden Sie die[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), um wie unten beschrieben auf die Dokumenteigenschaften der Datei zuzugreifen.

-  Um auf integrierte Dokumenteigenschaften zuzugreifen, verwenden Sie[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
-  Um auf benutzerdefinierte Dokumenteigenschaften zuzugreifen, verwenden Sie die[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

 Beide[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) und[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) gibt eine Instanz von zurück[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) . Diese Sammlung enthält[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)-Objekte, die jeweils eine einzelne integrierte oder benutzerdefinierte Dokumenteigenschaft darstellen.

 Es hängt von der Anwendungsanforderung ab, wie auf eine Eigenschaft zugegriffen wird, das heißt; indem Sie den Index oder Namen der Eigenschaft aus dem verwenden[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)wie im folgenden Beispiel gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

 Das[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)-Klasse ermöglicht es, den Namen, Wert und Typ der Dokumenteigenschaft abzurufen:

-  Verwenden Sie zum Abrufen des Eigenschaftsnamens[**Dokumenteigenschaft.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
-  Um den Eigenschaftswert zu erhalten, verwenden Sie[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)gibt den Wert als Objekt zurück.
-  Verwenden Sie zum Abrufen des Eigenschaftstyps[**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) . Dies gibt eine der zurück[**Art der Immobilie**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)Aufzählungswerte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Hinzufügen oder Entfernen von benutzerdefinierten Dokumenteigenschaften**

Wie wir bereits zu Beginn dieses Themas beschrieben haben, können Entwickler keine integrierten Eigenschaften hinzufügen oder entfernen, da diese Eigenschaften systemdefiniert sind, aber es ist möglich, benutzerdefinierte Eigenschaften hinzuzufügen oder zu entfernen, da diese benutzerdefiniert sind.

### **Hinzufügen von benutzerdefinierten Eigenschaften**

 Aspose.Cells APIs haben die ausgesetzt[**hinzufügen**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) Methode für die[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) -Klasse, um der Sammlung benutzerdefinierte Eigenschaften hinzuzufügen. Das[**hinzufügen**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) )-Methode fügt die Eigenschaft der Excel-Datei hinzu und gibt eine Referenz für die neue Dokumenteigenschaft als a[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)Objekt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Konfigurieren der benutzerdefinierten Eigenschaft „Link zum Inhalt“.**

 Um eine benutzerdefinierte Eigenschaft zu erstellen, die mit dem Inhalt eines bestimmten Bereichs verknüpft ist, rufen Sie die auf[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String))-Methode und übergeben Sie den Eigenschaftsnamen und die Quelle. Sie können überprüfen, ob eine Eigenschaft als mit Inhalt verknüpft konfiguriert ist, indem Sie die verwenden[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) Eigentum. Darüber hinaus ist es auch möglich, den Quellbereich mithilfe von abzurufen[**Quelle**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) Eigentum der[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)Klasse.

 Wir verwenden im Beispiel eine einfache Vorlage Microsoft Excel-Datei. Die Arbeitsmappe hat einen definierten benannten Bereich mit der Bezeichnung**MeineRange** was sich auf einen Zellenwert bezieht.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Benutzerdefinierte Eigenschaften entfernen**

 Um benutzerdefinierte Eigenschaften mit Aspose.Cells zu entfernen, rufen Sie die an[**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String))-Methode und übergeben Sie den Namen der zu entfernenden Dokumenteigenschaft.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
