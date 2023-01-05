---
title: Verwalten von OLE-Objekten
type: docs
weight: 50
url: /de/net/managing-ole-objects/
---
## **Einführung**

OLE (Object Linking and Embedding) ist das Framework von Microsoft für eine zusammengesetzte Dokumenttechnologie. Kurz gesagt, ein zusammengesetztes Dokument ist so etwas wie ein Anzeigedesktop, der visuelle und Informationsobjekte aller Art enthalten kann: Text, Kalender, Animationen, Ton, bewegtes Video, 3D, ständig aktualisierte Nachrichten, Steuerelemente und so weiter. Jedes Desktop-Objekt ist eine unabhängige Programmentität, die mit einem Benutzer interagieren und auch mit anderen Objekten auf dem Desktop kommunizieren kann.

 OLE (Object Linking and Embedding) wird von vielen verschiedenen Programmen unterstützt und dient dazu, Inhalte, die in einem Programm erstellt wurden, in einem anderen verfügbar zu machen. Beispielsweise können Sie ein Microsoft-Word-Dokument in Microsoft-Excel einfügen. Um zu sehen, welche Inhaltstypen Sie einfügen können, klicken Sie auf**Objekt** auf der**Einfügung** Speisekarte. In der werden nur Programme angezeigt, die auf dem Computer installiert sind und OLE-Objekte unterstützen**Objekttyp** Kasten.

### **Einfügen von OLE-Objekten in das Arbeitsblatt**

Aspose.Cells unterstützt das Hinzufügen, Extrahieren und Bearbeiten von OLE-Objekten in Arbeitsblättern. Aus diesem Grund hat Aspose.Cells die[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) Klasse, die zum Hinzufügen eines neuen OLE-Objekts zur Sammlungsliste verwendet wird. Eine andere Klasse,[**OLE-Objekt**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), stellt ein OLE-Objekt dar. Es hat einige wichtige Mitglieder:

-  Das[**Bilddaten**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)Die Eigenschaft gibt die Bilddaten (Symboldaten) vom Typ Byte-Array an. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt anzuzeigen.
-  Das[**Objektdaten**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)Die Eigenschaft gibt die Objektdaten in Form eines Byte-Arrays an. Diese Daten werden im zugehörigen Programm angezeigt, wenn Sie auf das OLE-Objekt-Symbol doppelklicken.

Das folgende Beispiel zeigt, wie Sie einem Arbeitsblatt ein oder mehrere OLE-Objekte hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Extrahieren von OLE-Objekten in der Arbeitsmappe**

Das folgende Beispiel zeigt, wie OLE-Objekte in einer Arbeitsmappe extrahiert werden. Das Beispiel ruft verschiedene OLE-Objekte aus einer vorhandenen XLS-Datei ab und speichert verschiedene Dateien (DOC, XLS, PPT, PDF usw.) basierend auf dem Dateiformattyp des OLE-Objekts.

Nach dem Ausführen des Codes können wir verschiedene Dateien basierend auf ihren jeweiligen OLE-Objektformattypen speichern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Extrahieren der eingebetteten MOL-Datei**

Aspose.Cells unterstützt das Extrahieren von Objekten ungewöhnlicher Typen wie MOL (Molekulardatendatei mit Informationen zu Atomen und Bindungen). Das folgende Code-Snippet demonstriert das Extrahieren der eingebetteten MOL-Datei und das Speichern auf der Festplatte, indem Sie diese verwenden[Excel-Beispieldatei](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **Themen vorantreiben**
- [Greifen Sie auf das Anzeigeetikett des verknüpften Ole-Objekts zu und ändern Sie es](/cells/de/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aktualisieren Sie das OLE-Objekt automatisch über Microsoft Excel mit Aspose.Cells](/cells/de/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahieren Sie OLE-Objekte aus der Arbeitsmappe](/cells/de/net/extract-ole-objects-from-workbook/)
- [Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts](/cells/de/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Einfügen einer WAV-Datei als Ole-Objekt](/cells/de/net/inserting-a-wav-file-as-an-ole-object/)

