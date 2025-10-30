---
title: Den Klassennamen des eingebetteten OLE Objekts mit Golang via C++ abrufen oder setzen
linktitle: Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE Objekts
type: docs
weight: 200
url: /de/go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Lernen Sie, wie man die Klassenkennung eingebetteter OLE Objekte mit Aspose.Cells mit Golang via C++ abruft oder setzt.
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells bietet die Eigenschaft [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/go-cpp/oleobject/getclassidentifier/), mit der Sie die Klassenkennung des eingebetteten OLE-Objekts abrufen oder setzen können. OLE-Objektklassenkennungen sind tatsächlich GUIDs, d.h. global eindeutige Identifikatoren. GUIDs sind immer 16 Byte lang, daher sind Klassenkennungen ebenfalls 16 Byte lang. Sie befinden sich häufig im Windows-Registrierungseditor und bieten der Host-Anwendung Informationen darüber, wie eingebettete OLE-Objekte mit verschiedenen eingebetteten Ressourcen im Client-Anwendungsprogramm geöffnet werden.

## **Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts**
Der folgende Screenshot zeigt den Klassen-Identifikator des OLE-Objekts, also die GUID, die aus der [Beispiel-Excel-Datei](5115190.xls) mit dem eingebetteten PowerPoint-OLE-Objekt gelesen wurde.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Beispielcode**
Bitte sehen Sie sich den folgenden Beispielcode an, der mit der [Beispiel-Excel-Datei](5115190.xls) ausgeführt wird, und die Konsolenausgabe, die den Klassen-Identifikator des OLE-Objekts, also die GUID, druckt. Die gedruckte GUID ist genau die gleiche wie im Screenshot gezeigt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetOrSetTheClassIdentifierOfTheEmbeddedOleObject.go" >}}
### **Konsolenausgabe**
Dies ist die Konsolenausgabe des obigen Beispielscodes, wenn er mit der [Beispiel-Excel-Datei](5115190.xls) ausgeführt wird.

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
