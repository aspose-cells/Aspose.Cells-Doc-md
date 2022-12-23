---
title: Extrahieren Sie OLE-Objekte aus der Arbeitsmappe
type: docs
weight: 110
url: /de/net/extract-ole-objects-from-workbook/
---
{{% alert color="primary" %}}

Manchmal müssen Sie OLE-Objekte aus einer Arbeitsmappe extrahieren. Aspose.Cells unterstützt das Extrahieren und Speichern dieser Ole-Objekte.

Dieser Artikel zeigt, wie Sie eine Konsolenanwendung in Visual Studio.Net erstellen und mit ein paar einfachen Codezeilen verschiedene OLE-Objekte aus einer Arbeitsmappe extrahieren.

{{% /alert %}}

## **Extrahieren Sie OLE-Objekte aus einer Arbeitsmappe**

### **Erstellen einer Vorlagenarbeitsmappe**

1. Erstellt eine Arbeitsmappe in Microsoft Excel.
1. Fügen Sie ein Microsoft-Word-Dokument, eine Excel-Arbeitsmappe und ein PDF-Dokument als OLE-Objekte auf dem ersten Arbeitsblatt hinzu.

|**Vorlagendokument mit OLE-Objekten (OleFile.xls)**|
|:- |
|![todo: Bild_alt_Text](extract-ole-objects-from-workbook_1.png)|

Als nächstes extrahieren Sie die OLE-Objekte und speichern sie mit ihren jeweiligen Dateitypen auf der Festplatte.

### **Laden Sie Aspose.Cells herunter und installieren Sie es**

1. [Herunterladen Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Installieren Sie es auf Ihrem Entwicklungscomputer.

Alle Aspose-Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein.

### **Erstellen Sie ein Projekt**

Start**Visual Studio.Net** und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel zeigt eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden.

1. Referenzen hinzufügen
 1. Fügen Sie Ihrem Projekt einen Verweis auf die Komponente Aspose.Cells hinzu, z. B. einen Verweis auf ...\Programme\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Extrahieren Sie OLE-Objekte**

Der folgende Code erledigt die eigentliche Arbeit des Suchens und Extrahierens von OLE-Objekten. Die OLE-Objekte (DOC-, XLS- und PDF-Dateien) werden auf der Festplatte gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
