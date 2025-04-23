---
title: Verwaltung von OLE Objekten
type: docs
weight: 30
url: /de/java/managing-ole-objects/
---

## **Einführung**

OLE (Object Linking and Embedding) ist Microsofts Rahmenwerk für eine Compound-Dokumententechnologie. Kurz gesagt ist ein Compound-Dokument etwas Ähnliches wie ein Anzeigebereich, der visuelle und Informationsobjekte aller Art enthalten kann: Text, Kalender, Animationen, Ton, Bewegtbilder, 3D, ständig aktualisierte Nachrichten, Steuerungen und so weiter. Jedes Anzeigebereichsobjekt ist eine unabhängige Programm-Entität, die mit einem Benutzer interagieren und auch mit anderen Objekten auf dem Anzeigebereich kommunizieren kann.

OLE (Object Linking and Embedding) wird von vielen verschiedenen Programmen unterstützt und dient dazu, Inhalte, die in einem Programm erstellt wurden, in einem anderen verfügbar zu machen. Sie können beispielsweise ein Microsoft Word-Dokument in Microsoft Excel einfügen. Um zu sehen, welche Arten von Inhalten Sie einfügen können, klicken Sie auf **Objekt** im **Einfügen**-Menü. Nur Programme, die auf dem Computer installiert sind und OLE-Objekte unterstützen, erscheinen im **Objekttyp**-Feld.

## **Einfügen von OLE-Objekten in ein Arbeitsblatt**

Aspose.Cells unterstützt das Hinzufügen, Extrahieren und Manipulieren von OLE-Objekten in Arbeitsblättern. Aus diesem Grund verfügt Aspose.Cells über die [**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)-Klasse, die verwendet wird, um ein neues OLE-Objekt zur Sammlungsliste hinzuzufügen. Eine weitere Klasse, [**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), stellt ein OLE-Objekt dar. Sie hat einige wichtige Elemente:

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData) gibt die Bilddaten (Symbol) vom Typ Byte-Array an. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt anzuzeigen.
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData) gibt die Objektdaten in Form eines Byte-Arrays an. Diese Daten werden in ihrem entsprechenden Programm angezeigt, wenn Sie auf das Symbol des OLE-Objekts doppelklicken.

Das folgende Beispiel zeigt, wie man ein OLE-Objekt in ein Arbeitsblatt einfügt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Extrahieren von OLE-Objekten in der Arbeitsmappe**

Das folgende Beispiel zeigt, wie man OLE-Objekte in einer Arbeitsmappe extrahiert. Das Beispiel erhält verschiedene OLE-Objekte aus einer vorhandenen XLS-Datei und speichert verschiedene Dateien (DOC, XLS, PPT, PDF usw.) basierend auf dem Dateiformattyp des OLE-Objekts.

Hier ist der Screenshot der Vorlagen-XLS-Datei, sie enthält verschiedene eingebettete OLE-Objekte im ersten Arbeitsblatt.

**Die Vorlagendatei enthält vier OLE-Objekte** 

![todo:image_alt_text](managing-ole-objects_1.png)

Nach dem Ausführen des Codes können wir verschiedene Dateien basierend auf ihren jeweiligen OLE-Objektformaten speichern. Hier sind Screenshots von einigen der erstellten Dateien.

**Die extrahierte XLS-Datei** 

![todo:image_alt_text](managing-ole-objects_2.png)

**Die extrahierte PPT-Datei** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Extrahieren eingebetteter MOL-Datei**

Aspose.Cells unterstützt das Extrahieren von Objekten ungewöhnlicher Typen wie MOL (Moleküldaten-Datei, die Informationen über Atome und Bindungen enthält). Der folgende Code-Schnipsel zeigt, wie man eine eingebettete MOL-Datei extrahiert und sie auf die Festplatte speichert, indem man diese [Beispielsarbeitsmappe](EmbeddedMolSample.xlsx) verwendet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Erweiterte Themen**
- [Auf das Anzeigen des verknüpften Ole-Objekts zugreifen und es ändern](/cells/de/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [OLE-Objekt automatisch über Microsoft Excel aktualisieren mit Aspose.Cells](/cells/de/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahieren Sie OLE-Objekte aus der Arbeitsmappe](/cells/de/java/extract-ole-objects-from-workbook/)
- [Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts](/cells/de/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
{{< app/cells/assistant language="java" >}}
