---
title: OLE Objekte aus Arbeitsbuch extrahieren mit Golang via C++
linktitle: OLE Objekte aus Arbeitsmappe extrahieren
type: docs
weight: 110
url: /de/go-cpp/extract-ole-objects-from-workbook/
description: Lernen Sie, wie man OLE Objekte aus einem Arbeitsbuch mit Aspose.Cells mit Golang via C++ extrahiert.
---

{{% alert color="primary" %}}

Manchmal müssen Sie OLE-Objekte aus einer Arbeitsmappe extrahieren. Aspose.Cells unterstützt das Extrahieren und Speichern dieser OLE-Objekte.

Dieser Artikel zeigt, wie Sie eine Konsolenanwendung in Visual Studio erstellen und verschiedene OLE-Objekte aus einer Arbeitsmappe mit wenigen Codezeilen extrahieren.

{{% /alert %}}

## **OLE-Objekte aus einer Arbeitsmappe extrahieren**

### **Erstellen einer Vorlagearbeitsmappe**

1. Erstellen Sie ein Arbeitsbuch in Microsoft Excel.
1. Fügen Sie ein Microsoft Word-Dokument, ein Excel-Arbeitsbuch und ein PDF-Dokument als OLE-Objekte auf das erste Arbeitsblatt ein.

|**Vorlagendokument mit OLE-Objekten (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

 Als nächstes extrahieren Sie die OLE-Objekte und speichern sie mit ihren jeweiligen Dateitypen auf der Festplatte.

### **Aspose.Cells herunterladen und installieren**

1. [Herunterladen Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/).
1. Installieren Sie es auf Ihrem Entwicklungscomputer.

Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.

### **Ein Projekt erstellen**

Starten Sie **Visual Studio** und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel zeigt eine C++-Konsolenanwendung.

1. Verweise hinzufügen
   1. Fügen Sie Ihrem Projekt eine Referenz zur Aspose.Cells-Komponente hinzu, z.B. fügen Sie eine Referenz zu ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll hinzu.

### **OLE-Objekte extrahieren**

Der unten stehende Code führt die eigentliche Arbeit beim Finden und Extrahieren von OLE-Objekten aus. Die OLE-Objekte (DOC, XLS und PDF Dateien) werden auf die Festplatte gespeichert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractOleObjectsFromWorkbook.go" >}}
