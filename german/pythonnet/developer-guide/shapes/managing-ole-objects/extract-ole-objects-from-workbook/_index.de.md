---
title: OLE Objekte aus Arbeitsmappe extrahieren
type: docs
weight: 110
url: /de/python-net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

Manchmal müssen Sie OLE-Objekte aus einer Arbeitsmappe extrahieren. Aspose.Cells für Python via .NET unterstützt das Extrahieren und Speichern dieser OLE-Objekte.

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

### **OLE-Objekte mit Aspose.Cells für Python Excel-Bibliothek extrahieren**

Der folgende Code führt die eigentliche Arbeit des Auffindens und Extrahierens von OLE-Objekten durch. Die OLE-Objekte (DOC-, XLS- und PDF-Dateien) werden auf der Festplatte gespeichert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
