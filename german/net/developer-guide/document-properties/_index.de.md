---
title: Dokumenteigenschaften verwalten
linktitle: Dokumenteigenschaften
type: docs
weight: 80
url: /de/net/managing-document-properties/
description: Erfahren Sie, wie Sie Dokumenteigenschaften über die APIs Aspose.Cells für NET verwalten.
keywords: How to Manage Document Properties in C#, Get or Set Document Properties using C#, Add or Delete Document Properties via C#, Insert or Remove Document Properties with C#, How to Access Document Properties using Aspose.Cells for NET APIs.
---
##  **Einführung**

Microsoft Excel bietet die Möglichkeit, Eigenschaften zu Tabellendateien hinzuzufügen. Diese Dokumenteigenschaften bieten nützliche Informationen und sind in zwei Kategorien unterteilt, wie unten beschrieben.

- Systemdefinierte (integrierte) Eigenschaften: Integrierte Eigenschaften enthalten allgemeine Informationen über das Dokument wie Dokumenttitel, Name des Autors, Dokumentstatistiken usw.
- Benutzerdefinierte (benutzerdefinierte) Eigenschaften: Benutzerdefinierte Eigenschaften, die vom Endbenutzer in Form eines Name-Wert-Paares definiert werden.

{{% alert color="primary" %}}

Der wichtigste Punkt, den Sie über integrierte und benutzerdefinierte Eigenschaften wissen sollten, ist, dass auf integrierte Eigenschaften zugegriffen und diese geändert, aber nicht erstellt oder entfernt werden können. Es können jedoch benutzerdefinierte Eigenschaften erstellt und verwaltet werden.

{{% /alert %}}

##  **So verwalten Sie Dokumenteigenschaften mit Microsoft Excel**

 Microsoft Mit Excel können Sie die Dokumenteigenschaften der Excel-Dateien im WYSIWYG-Stil verwalten. Bitte befolgen Sie die folgenden Schritte, um das zu öffnen**Eigenschaften** Dialog in Excel 2016.

1.  Von dem**Datei** Wählen Sie im Menü *Info**.

|**Info-Menü auswählen**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1.  Klicke auf**Eigenschaften** Überschrift und wählen Sie „Erweiterte Eigenschaften“.

|**Klicken Sie auf „Erweiterte Eigenschaftenauswahl“.**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Verwalten Sie die Dokumenteigenschaften der Datei.

|**Eigenschaftendialog**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Im Eigenschaftendialog gibt es verschiedene Registerkarten wie Allgemein, Zusammenfassung, Statistik, Inhalt und Zoll. Auf jeder Registerkarte können Sie verschiedene Arten von Informationen im Zusammenhang mit der Datei konfigurieren. Die Registerkarte „Benutzerdefiniert“ wird zum Verwalten benutzerdefinierter Eigenschaften verwendet.

##  **So arbeiten Sie mit Dokumenteigenschaften mithilfe von Aspose.Cells**

Entwickler können die Dokumenteigenschaften mithilfe der Aspose.Cells-APIs dynamisch verwalten. Diese Funktion hilft den Entwicklern, nützliche Informationen zusammen mit der Datei zu speichern, z. B. wann die Datei empfangen, verarbeitet, mit einem Zeitstempel versehen usw. wurde.

{{% alert color="primary" %}}

 Aspose.Cells for .NET schreibt die Informationen zu API und der Versionsnummer direkt in Ausgabedokumente. Wenn beispielsweise das Dokument in PDF gerendert wird, wird Aspose.Cells for .NET ausgefüllt**Anwendung** Feld mit dem Wert 'Aspose.Cells' und**PDF Produzent** Feld mit dem Wert, z. B. „Aspose.Cells v17.9“.

Bitte beachten Sie, dass Sie Aspose.Cells for .NET nicht anweisen können, diese Informationen aus Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

###  **So greifen Sie auf Dokumenteigenschaften zu**

 Aspose.Cells APIs unterstützen beide Arten von Dokumenteigenschaften, integrierte und benutzerdefinierte. Aspose.Cells'[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Die Klasse stellt eine Excel-Datei dar und, wie eine Excel-Datei, die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Die Klasse kann mehrere Arbeitsblätter enthalten, die jeweils durch dargestellt werden[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse, während die Sammlung von Arbeitsblättern durch dargestellt wird[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Klasse.

 Benutzen Sie die[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)um wie unten beschrieben auf die Dokumenteigenschaften der Datei zuzugreifen.

- Um auf integrierte Dokumenteigenschaften zuzugreifen, verwenden Sie[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  Um auf benutzerdefinierte Dokumenteigenschaften zuzugreifen, verwenden Sie[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Beide[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) Und[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) Gibt die Instanz von zurück[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Diese Sammlung enthält[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)Objekte, von denen jedes eine einzelne integrierte oder benutzerdefinierte Dokumenteigenschaft darstellt.

 Es liegt an der Antragsanforderung, wie auf eine Immobilie zugegriffen wird, d. h.; indem Sie den Index oder Namen der Eigenschaft aus dem verwenden[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)wie im Beispiel unten gezeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 Der[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)Mit der Klasse können Name, Wert und Typ der Dokumenteigenschaft abgerufen werden:

-  Um den Eigenschaftsnamen zu erhalten, verwenden Sie[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  Um den Eigenschaftswert zu erhalten, verwenden Sie[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)gibt den Wert als Objekt zurück.
-  Um den Eigenschaftstyp zu erhalten, verwenden Sie[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Dies gibt einen der zurück[**Art der Immobilie**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)Aufzählungswerte. Nachdem Sie den Eigenschaftstyp erhalten haben, verwenden Sie einen der**DocumentProperty.ToXXX** Methoden, um den Wert des entsprechenden Typs zu erhalten, anstatt ihn zu verwenden[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . Der**DocumentProperty.ToXXX**Die Methoden werden in der folgenden Tabelle beschrieben.

{{% alert color="primary" %}}

 Der[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)Die Klasse stellt außerdem eine Reihe von Methoden bereit, die die Werte anderer Datentypen zurückgeben.

{{% /alert %}}

|**Mitgliedsname**|**Beschreibung**|**ToXXX-Methode**|
| :- | :- | :- |
|Boolescher Wert|Der Eigenschaftsdatentyp ist Boolean|ToBool|
|Datum| Der Eigenschaftsdatentyp ist DateTime. Beachten Sie, dass Microsoft nur Excel speichert<br>Im Datumsteil kann in einer benutzerdefinierten Eigenschaft dieses Typs keine Uhrzeit gespeichert werden|ToDateTime|
|Schweben|Der Eigenschaftsdatentyp ist Double|Verdoppeln|
|Nummer|Der Eigenschaftsdatentyp ist Int32|ToInt|
|String|Der Eigenschaftsdatentyp ist String|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

###  **So fügen Sie benutzerdefinierte Dokumenteigenschaften hinzu oder entfernen sie**

Wie bereits zu Beginn dieses Themas beschrieben, können Entwickler keine integrierten Eigenschaften hinzufügen oder entfernen, da diese Eigenschaften systemdefiniert sind. Es ist jedoch möglich, benutzerdefinierte Eigenschaften hinzuzufügen oder zu entfernen, da diese benutzerdefiniert sind.

###  **So fügen Sie benutzerdefinierte Eigenschaften hinzu**

 Aspose.Cells APIs haben das offengelegt[**Hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) Methode für die[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) Klasse, um der Sammlung benutzerdefinierte Eigenschaften hinzuzufügen. Der[**Hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) Die Methode fügt die Eigenschaft zur Excel-Datei hinzu und gibt eine Referenz für die neue Dokumenteigenschaft als zurück[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)Objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

###  **So konfigurieren Sie die benutzerdefinierte Eigenschaft „Link zum Inhalt“.**

 Um eine benutzerdefinierte Eigenschaft zu erstellen, die mit dem Inhalt eines bestimmten Bereichs verknüpft ist, rufen Sie auf[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) Methode und übergeben Sie den Eigenschaftsnamen und die Quelle. Mithilfe von können Sie überprüfen, ob eine Eigenschaft als mit Inhalt verknüpft konfiguriert ist[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) Eigentum. Darüber hinaus ist es auch möglich, den Quellbereich mithilfe von zu ermitteln[**Quelle**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) Eigentum der[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)Klasse.

Im Beispiel verwenden wir eine einfache Excel-Vorlage Microsoft. Die Arbeitsmappe verfügt über einen definierten benannten Bereich mit der Bezeichnung**MyRange** was sich auf einen Zellwert bezieht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

###  **So entfernen Sie benutzerdefinierte Eigenschaften**

 Um benutzerdefinierte Eigenschaften mit Aspose.Cells zu entfernen, rufen Sie auf[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)-Methode und übergeben Sie den Namen der Dokumenteigenschaft, die entfernt werden soll.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

##  **Vorabthemen**
- [Hinzufügen benutzerdefinierter Eigenschaften, die im Dokumentinformationsbereich sichtbar sind](/cells/de/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Festlegen der ScaleCrop- und LinksUpToDate-Eigenschaften der integrierten Dokumenteigenschaften](/cells/de/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Geben Sie die Dokumentversion der Excel-Datei mithilfe der integrierten Dokumenteigenschaften an](/cells/de/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Geben Sie die Sprache der Excel-Datei mithilfe der integrierten Dokumenteigenschaften an](/cells/de/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
