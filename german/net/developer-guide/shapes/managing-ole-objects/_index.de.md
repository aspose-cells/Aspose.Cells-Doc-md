---
title: Verwaltung von OLE Objekten
type: docs
weight: 50
url: /de/net/managing-ole-objects/
---

## **Einführung**

OLE (Object Linking and Embedding) ist Microsofts Rahmenwerk für eine Compound-Dokumententechnologie. Kurz gesagt ist ein Compound-Dokument etwas Ähnliches wie ein Anzeigebereich, der visuelle und Informationsobjekte aller Art enthalten kann: Text, Kalender, Animationen, Ton, Bewegtbilder, 3D, ständig aktualisierte Nachrichten, Steuerungen und so weiter. Jedes Anzeigebereichsobjekt ist eine unabhängige Programm-Entität, die mit einem Benutzer interagieren und auch mit anderen Objekten auf dem Anzeigebereich kommunizieren kann.

OLE (Object Linking and Embedding) wird von vielen verschiedenen Programmen unterstützt und dient dazu, Inhalte, die in einem Programm erstellt wurden, in einem anderen verfügbar zu machen. Sie können beispielsweise ein Microsoft Word-Dokument in Microsoft Excel einfügen. Um zu sehen, welche Arten von Inhalten Sie einfügen können, klicken Sie auf **Objekt** im **Einfügen**-Menü. Nur Programme, die auf dem Computer installiert sind und OLE-Objekte unterstützen, erscheinen im **Objekttyp**-Feld.

### **Einfügen von OLE-Objekten in das Arbeitsblatt**

Aspose.Cells unterstützt das Hinzufügen, Extrahieren und Manipulieren von OLE-Objekten in Arbeitsblättern. Aus diesem Grund hat Aspose.Cells die [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection)-Klasse, die verwendet wird, um ein neues OLE-Objekt zur Sammlungsliste hinzuzufügen. Eine weitere Klasse, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), stellt ein OLE-Objekt dar. Sie hat einige wichtige Elemente:

- Die [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)-Eigenschaft spezifiziert die Bilddaten im Byte-Array-Format. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt anzuzeigen.
- Die [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)-Eigenschaft spezifiziert die Objektdaten in Form eines Byte-Arrays. Diese Daten werden in ihrem zugehörigen Programm angezeigt, wenn Sie auf das OLE-Objektsymbol doppelklicken.

Das folgende Beispiel zeigt, wie man OLE-Objekte in ein Arbeitsblatt einfügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Extrahieren von OLE-Objekten in der Arbeitsmappe**

Das folgende Beispiel zeigt, wie man OLE-Objekte in einer Arbeitsmappe extrahiert. Das Beispiel erhält verschiedene OLE-Objekte aus einer vorhandenen XLS-Datei und speichert verschiedene Dateien (DOC, XLS, PPT, PDF usw.) basierend auf dem Dateiformattyp des OLE-Objekts.

Nachdem der Code ausgeführt wurde, können wir verschiedene Dateien basierend auf ihren jeweiligen OLE-Objektformattypen speichern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Extrahieren eingebetteter MOL-Datei**

Aspose.Cells unterstützt das Extrahieren von Objekten ungewöhnlicher Typen wie MOL(Moleküldaten-Datei mit Informationen über Atome und Bindungen). Der folgende Code-Schnipsel zeigt, wie eine eingebettete MOL-Datei extrahiert und unter Verwendung dieser [Beispieldatei für Excel](94896196.xlsx) auf die Festplatte gespeichert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **Erweiterte Themen**
- [Auf das Anzeigen des verknüpften Ole-Objekts zugreifen und es ändern](/cells/de/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [OLE-Objekt automatisch über Microsoft Excel aktualisieren mit Aspose.Cells](/cells/de/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahieren Sie OLE-Objekte aus der Arbeitsmappe](/cells/de/net/extract-ole-objects-from-workbook/)
- [Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts](/cells/de/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Einfügen einer WAV-Datei als OLE-Objekt](/cells/de/net/inserting-a-wav-file-as-an-ole-object/)

{{< app/cells/assistant language="csharp" >}}
