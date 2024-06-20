---
title: OLE Objekte aus Arbeitsmappe extrahieren
type: docs
weight: 110
url: /de/net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

Manchmal müssen OLE-Objekte aus einer Arbeitsmappe extrahiert werden. Aspose.Cells unterstützt das Extrahieren und Speichern dieser Ole-Objekte.

In diesem Artikel wird gezeigt, wie Sie eine Konsolenanwendung in Visual Studio .NET erstellen und mit ein paar einfachen Codezeilen verschiedene OLE-Objekte aus einer Arbeitsmappe extrahieren können.

{{% /alert %}}

## **OLE-Objekte aus einer Arbeitsmappe extrahieren**

### **Erstellen einer Vorlagearbeitsmappe**

1. Erstellen einer Arbeitsmappe in Microsoft Excel.
1. Fügen Sie ein Microsoft-Word-Dokument, eine Excel-Arbeitsmappe und ein PDF-Dokument als OLE-Objekte auf dem ersten Arbeitsblatt hinzu.

|**Vorlagendokument mit OLE-Objekten (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Extrahieren Sie dann die OLE-Objekte und speichern Sie sie auf der Festplatte mit ihren jeweiligen Dateitypen.

### **Aspose.Cells herunterladen und installieren**

1. [Laden Sie Aspose.Cells for .NET herunter](https://downloads.aspose.com/cells/net).
1. Installieren Sie es auf Ihrem Entwicklungscomputer.

Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.

### **Ein Projekt erstellen**

Starten Sie **Visual Studio.Net** und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel zeigt eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden.

1. Verweise hinzufügen
   1. Fügen Sie Ihrem Projekt einen Verweis auf die Aspose.Cells-Komponente hinzu, beispielsweise einen Verweis auf...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **OLE-Objekte extrahieren**

Der folgende Code führt die eigentliche Arbeit des Auffindens und Extrahierens von OLE-Objekten durch. Die OLE-Objekte (DOC-, XLS- und PDF-Dateien) werden auf der Festplatte gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
