---
title: Verwalten von OLE-Objekten
type: docs
weight: 30
url: /de/java/managing-ole-objects/
---
## **Einführung**

OLE (Object Linking and Embedding) ist das Framework von Microsoft für eine zusammengesetzte Dokumenttechnologie. Kurz gesagt, ein zusammengesetztes Dokument ist so etwas wie ein Anzeigedesktop, der visuelle und Informationsobjekte aller Art enthalten kann: Text, Kalender, Animationen, Ton, bewegtes Video, 3D, ständig aktualisierte Nachrichten, Steuerelemente und so weiter. Jedes Desktop-Objekt ist eine unabhängige Programmentität, die mit einem Benutzer interagieren und auch mit anderen Objekten auf dem Desktop kommunizieren kann.

 OLE (Object Linking and Embedding) wird von vielen verschiedenen Programmen unterstützt und dient dazu, Inhalte, die in einem Programm erstellt wurden, in einem anderen verfügbar zu machen. Beispielsweise können Sie ein Microsoft-Word-Dokument in Microsoft-Excel einfügen. Um zu sehen, welche Inhaltstypen Sie einfügen können, klicken Sie auf**Objekt** auf der**Einfügung** Speisekarte. In der werden nur Programme angezeigt, die auf dem Computer installiert sind und OLE-Objekte unterstützen**Objekttyp** Kasten.

## **Einfügen von OLE-Objekten in ein Arbeitsblatt**

Aspose.Cells unterstützt das Hinzufügen, Extrahieren und Bearbeiten von OLE-Objekten in Arbeitsblättern. Aus diesem Grund hat Aspose.Cells die[**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection)Klasse, die zum Hinzufügen eines neuen OLE-Objekts zur Sammlungsliste verwendet wird. Eine andere Klasse,[**OLE-Objekt**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), stellt ein OLE-Objekt dar. Es hat einige wichtige Mitglieder:

- [**Bilddaten**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData)spezifiziert die Bild-(Icon-)Daten des Byte-Array-Typs. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt anzuzeigen.
- [**Objektdaten**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData)gibt die Objektdaten in Form eines Byte-Arrays an. Diese Daten werden im zugehörigen Programm angezeigt, wenn Sie auf das OLE-Objekt-Symbol doppelklicken.

Das folgende Beispiel zeigt, wie Sie einem Arbeitsblatt ein OLE-Objekt hinzufügen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Extrahieren von OLE-Objekten in der Arbeitsmappe**

Das folgende Beispiel zeigt, wie OLE-Objekte in einer Arbeitsmappe extrahiert werden. Das Beispiel ruft verschiedene OLE-Objekte aus einer vorhandenen XLS-Datei ab und speichert verschiedene Dateien (DOC, XLS, PPT, PDF usw.) basierend auf dem Dateiformattyp des OLE-Objekts.

Hier ist der Screenshot der Vorlagendatei XLS, sie hat verschiedene OLE-Objekte, die in das erste Arbeitsblatt eingebettet sind.

**Die Vorlagendatei enthält vier OLE-Objekte** 

![todo: Bild_alt_Text](managing-ole-objects_1.png)

Nach dem Ausführen des Codes können wir verschiedene Dateien basierend auf ihren jeweiligen OLE-Objektformattypen speichern. Es folgen Screenshots für einige der erstellten Dateien.

**Die extrahierte XLS-Datei** 

![todo: Bild_alt_Text](managing-ole-objects_2.png)

**Die extrahierte PPT-Datei** 

![todo: Bild_alt_Text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Extrahieren der eingebetteten MOL-Datei**

Aspose.Cells unterstützt das Extrahieren von Objekten ungewöhnlicher Typen wie MOL (Molekulardatendatei mit Informationen zu Atomen und Bindungen). Das folgende Code-Snippet demonstriert das Extrahieren der eingebetteten MOL-Datei und das Speichern auf der Festplatte, indem Sie diese verwenden[Excel-Beispieldatei](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Themen vorantreiben**
- [Greifen Sie auf das Anzeigeetikett des verknüpften Ole-Objekts zu und ändern Sie es](/cells/de/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aktualisieren Sie das OLE-Objekt automatisch über Microsoft Excel mit Aspose.Cells](/cells/de/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahieren Sie OLE-Objekte aus der Arbeitsmappe](/cells/de/java/extract-ole-objects-from-workbook/)
- [Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts](/cells/de/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
