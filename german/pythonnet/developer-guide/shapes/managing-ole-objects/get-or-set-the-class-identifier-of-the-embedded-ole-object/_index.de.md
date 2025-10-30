---
title: Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE Objekts
type: docs
weight: 200
url: /de/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells für Python via .NET stellt die Eigenschaft [OleObject.class_identifier](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/class_identifier) bereit, mit der Sie die Klassenkennung des eingebetteten OLE-Objekts abfragen oder setzen können. Klassenkennungen von OLE-Objekten sind eigentlich GUIDs, also weltweit eindeutige Kennungen. GUIDs sind immer 16 Byte lang, daher sind auch Klassenkennungen 16 Byte lang. Sie sind häufig im Windows-Registrierungseditor zu finden und liefern der Host-Anwendung Informationen darüber, wie das eingebettete OLE-Objekt mit verschiedenen eingebetteten Ressourcen im Client-Anwendungsfenster geöffnet werden soll.

## **Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts**
Das folgende Bild zeigt den Ole Object Class Identifier, d. h. die GUID, die aus der [Beispiel-Excel-Datei](5115190.xls) mit dem eingebetteten PowerPoint-Ole-Objekt gelesen wurde.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Beispielcode**
Bitte sehen Sie sich den folgenden Beispielscode an, der mit der [Beispiel-Excel-Datei](5115190.xls) ausgeführt wurde, sowie dessen Konsolenausgabe, die den Klassenbezeichner des Ole-Objekts, d. h. die GUID, ausgibt. Die ausgegebene GUID ist genau die gleiche wie in dem Screenshot angezeigt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-GetSetClassIdentifierEmbedOleObject.py" >}}

### **Konsolenausgabe**
Dies ist die Konsolenausgabe des obigen Beispielscodes, wenn er mit der [Beispiel-Excel-Datei](5115190.xls) ausgeführt wird.

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
