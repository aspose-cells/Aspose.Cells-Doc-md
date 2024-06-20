---
title: Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE Objekts
type: docs
weight: 920
url: /de/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells bietet die Eigenschaft [OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier), die Sie zum Abrufen oder Setzen des Klassenidentifikators eines eingebetteten OLE-Objekts verwenden können. Ole Object Class Identifiers sind tatsächlich GUIDs, d. h. Globally Unique Identifiers. GUID ist immer 16 Bytes lang, daher sind auch die Klassenidentifikatoren 16 Bytes lang. Sie befinden sich oft in der Windows-Registrierung und geben der Hostanwendung Informationen darüber, wie sie das eingebettete Ole-Objekt mit verschiedenen eingebetteten Ressourcen in der Clientanwendung öffnen soll.
## **Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts**
Der folgende Screenshot zeigt den Ole Object Class Identifier, d. h. die GUID, die aus der [Beispiel-Excel-Datei](5473378.xls) mit dem eingebetteten PowerPoint-Ole-Objekt gelesen wurde.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **Beispielcode**
Bitte sehen Sie den folgenden Beispielcode, der mit der [Beispiel-Excel-Datei](5473378.xls) ausgeführt wurde, und die Konsolenausgabe, die die *Klassenkennung* des Ole-Objekts, d. h. der GUID, ausdruckt. Die gedruckte GUID ist genau die gleiche wie im Screenshot gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **Konsolenausgabe**
Dies ist die Konsolenausgabe des oben genannten Beispielcodes, das mit der [Beispiel-Excel-Datei](5473378.xls) ausgeführt wurde.

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
