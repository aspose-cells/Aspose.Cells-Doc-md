---
title: Verwaltung von Dokumenteigenschaften
type: docs
weight: 10
url: /de/java/managing-document-properties/
---

## **Einführung**

Microsoft Excel bietet die Möglichkeit, Eigenschaften zu Tabellendateien hinzuzufügen. Diese Dokumenteigenschaften liefern nützliche Informationen und sind in 2 Kategorien unterteilt, wie unten näher beschrieben.

- Systemdefinierte (eingebaute) Eigenschaften: Eingebaute Eigenschaften enthalten allgemeine Informationen zum Dokument wie Dokumententitel, Autorname, Dokumentenstatistiken und so weiter.
- Benutzerdefinierte (benutzerdefinierte) Eigenschaften: Benutzerdefinierte Eigenschaften, die vom Endbenutzer in Form von Schlüssel-Wert-Paar definiert werden.

{{% alert color="primary" %}}

Der wichtigste Punkt über eingebaute und benutzerdefinierte Eigenschaften ist, dass auf eingebaute Eigenschaften zugegriffen und diese geändert, aber nicht erstellt oder entfernt werden können, während benutzerdefinierte Dokumenteigenschaften erstellt und verwaltet werden können.

{{% /alert %}}

## **Verwalten von Dokumenteigenschaften mit Microsoft Excel**

Microsoft Excel ermöglicht das Verwalten von Dokumenteigenschaften der Excel-Dateien in einem WYSIWYG-Verfahren. Befolgen Sie bitte die folgenden Schritte, um den **Eigenschaften**-Dialog in Excel 2016 zu öffnen.

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

## **Arbeiten mit Dokumenteigenschaften mit Aspose.Cells**

Entwickler können die Dokumenteigenschaften dynamisch mit den Aspose.Cells APIs verwalten. Diese Funktion hilft den Entwicklern, nützliche Informationen zusammen mit der Datei zu speichern, z. B. wann die Datei empfangen, verarbeitet, zeitgestempelt wurde usw.

{{% alert color="primary" %}}

Aspose.Cells for Java schreibt die Informationen über API und Versionsnummer direkt in Ausgabedokumente. Beispielsweise füllt Aspose.Cells for Java beim Rendern des Dokuments in PDF das **Anwendungs**-Feld mit dem Wert 'Aspose.Cells' und das **PDF-Erstellungs**-Feld mit dem Wert, z. B. 'Aspose.Cells for Java v17.9'.

Bitte beachten Sie, dass Sie Aspose.Cells for Java nicht anweisen können, diese Informationen aus den Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

### **Zugriff auf Dokumenteigenschaften**

Aspose.Cells APIs unterstützen beide Arten von Dokumenteigenschaften, eingebaute und benutzerdefinierte. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) von Aspose.Cells repräsentiert eine Excel-Datei und, wie eine Excel-Datei, kann die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) mehrere Arbeitsblätter enthalten, die jeweils durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) repräsentiert werden, während die Sammlung von Arbeitsblättern durch die Klasse [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) repräsentiert wird.

Verwenden Sie [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), um die Dokumenteigenschaften der Datei wie unten beschrieben abzurufen.

- Um auf die integrierten Dokumenteigenschaften zuzugreifen, verwenden Sie [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
- Um auf benutzerdefinierte Dokumenteigenschaften zuzugreifen, verwenden Sie [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

Sowohl [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) als auch [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) geben eine Instanz von [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) zurück. Diese Sammlung enthält [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) Objekte, die jeweils eine einzelne eingebaute oder benutzerdefinierte Dokumenteigenschaft darstellen.

Es liegt an den Anwendungsanforderungen, wie auf eine Eigenschaft zugegriffen wird; durch Verwendung des Indexes oder des Namens der Eigenschaft aus [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection), wie im folgenden Beispiel demonstriert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

Die Klasse [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) erlaubt das Abrufen des Namens, Werts und Typs der Dokumenteigenschaft:

- Um den Eigenschaftsnamen zu erhalten, verwenden Sie [**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
- Um den Eigenschaftswert zu erhalten, verwenden Sie [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) gibt den Wert als Object zurück.
- Um den Eigenschaftstyp zu erhalten, verwenden Sie [**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type). Dies gibt einen der [**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType) Aufzählungswerte zurück.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Hinzufügen oder Entfernen benutzerdefinierter Dokumenteigenschaften**

Wie wir zu Beginn dieses Themas bereits beschrieben haben, können Entwickler integrierte Eigenschaften nicht hinzufügen oder entfernen, da diese Eigenschaften systemdefiniert sind, es ist jedoch möglich, benutzerdefinierte Eigenschaften hinzuzufügen oder zu entfernen, da diese benutzerdefiniert sind.

### **Hinzufügen von benutzerdefinierten Eigenschaften**

Aspose.Cells APIs haben die Methode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean)) für die Klasse [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) freigegeben, um benutzerdefinierte Eigenschaften in die Sammlung hinzuzufügen. Die Methode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean)) fügt die Eigenschaft der Excel-Datei hinzu und gibt eine Referenz auf die neue Dokumenteigenschaft als [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) Objekt zurück.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Konfigurieren der benutzerdefinierten Eigenschaft 'Verknüpfen mit Inhalt'**

Um eine benutzerdefinierte Eigenschaft zu erstellen, die mit dem Inhalt eines bestimmten Bereichs verknüpft ist, rufen Sie die Methode [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String)) auf und übergeben den Eigenschaftsnamen und die Quelle. Sie können über die Eigenschaft [**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) überprüfen, ob eine Eigenschaft als mit dem Inhalt verknüpft konfiguriert ist. Außerdem ist es auch möglich, den Quellbereich unter Verwendung der Eigenschaft [**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) der Klasse [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) zu erhalten.

Im Beispiel verwenden wir eine einfache Vorlage einer Microsoft Excel-Datei. Die Arbeitsmappe hat einen definierten benannten Bereich namens **MeinBereich**, der sich auf einen Zellenwert bezieht.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Entfernen von benutzerdefinierten Eigenschaften**

Um benutzerdefinierte Eigenschaften mit Aspose.Cells zu entfernen, rufen Sie die Methode [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) auf und übergeben den Namen der zu entfernenden Dokumenteigenschaft.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
