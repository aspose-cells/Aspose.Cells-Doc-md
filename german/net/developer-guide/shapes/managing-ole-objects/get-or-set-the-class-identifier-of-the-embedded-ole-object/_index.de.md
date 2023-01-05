---
title: Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts
type: docs
weight: 200
url: /de/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **Mögliche Nutzungsszenarien**
 Aspose.Cells bietet die[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)Eigenschaft, die Sie verwenden können, um die Klassenkennung des eingebetteten Ole-Objekts abzurufen oder festzulegen. Ole Object Class Identifiers sind eigentlich GUIDs, dh Globally Unique Identifiers. Die GUID ist immer 16 Byte lang, daher sind Klassenbezeichner auch 16 Byte lang. Sie sind häufig in der Windows-Registrierung zu finden und stellen der Hostanwendung Informationen darüber bereit, wie eingebettete Ole-Objekte geöffnet werden können, die verschiedene eingebettete Ressourcen in der Clientanwendung enthalten.
## **Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts**
 Der folgende Screenshot zeigt den Ole Object Class Identifier, dh GUID, der aus dem gelesen wurde[Excel-Beispieldatei](5115190.xls) enthält das eingebettete Ole-Objekt PowerPoint.

![todo: Bild_alt_Text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **Beispielcode**
 Bitte sehen Sie sich den folgenden Beispielcode an, der mit ausgeführt wird[Excel-Beispieldatei](5115190.xls)und seine Konsolenausgabe, die den Klassenbezeichner des Ole-Objekts, dh die GUID, ausgibt. Die gedruckte GUID ist genau die gleiche wie im Screenshot gezeigt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **Konsolenausgabe**
 Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit ausgeführt wird[Excel-Beispieldatei](5115190.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
