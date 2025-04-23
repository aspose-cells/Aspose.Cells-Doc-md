---
title: Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE Objekts
type: docs
weight: 200
url: /de/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells bietet die Eigenschaft [OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)  an, die Sie zum Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts verwenden können. Ole Object Class Identifiers sind tatsächlich GUIDs, d. h. global eindeutige Bezeichner. GUIDs sind immer 16 Byte lang, daher sind auch die Klassenbezeichner 16 Byte lang. Sie befinden sich häufig in der Windows-Registrierung und geben der Hostanwendung Informationen darüber, wie das eingebettete OLE-Objekt mit verschiedenen eingebetteten Ressourcen in der Clientanwendung geöffnet werden soll.
## **Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts**
Das folgende Bild zeigt den Ole Object Class Identifier, d. h. die GUID, die aus der [Beispiel-Excel-Datei](5115190.xls) mit dem eingebetteten PowerPoint-Ole-Objekt gelesen wurde.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Beispielcode**
Bitte sehen Sie sich den folgenden Beispielscode an, der mit der [Beispiel-Excel-Datei](5115190.xls) ausgeführt wurde, sowie dessen Konsolenausgabe, die den Klassenbezeichner des Ole-Objekts, d. h. die GUID, ausgibt. Die ausgegebene GUID ist genau die gleiche wie in dem Screenshot angezeigt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Konsolenausgabe**
Dies ist die Konsolenausgabe des obigen Beispielscodes, wenn er mit der [Beispiel-Excel-Datei](5115190.xls) ausgeführt wird.

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
