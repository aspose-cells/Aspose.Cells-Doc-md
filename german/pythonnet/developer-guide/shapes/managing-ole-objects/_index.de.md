---
title: Verwaltung von OLE Objekten
type: docs
weight: 50
url: /de/python-net/managing-ole-objects/
---

## **Einführung**

OLE (Object Linking and Embedding) ist Microsofts Rahmenwerk für eine Compound-Dokumententechnologie. Kurz gesagt ist ein Compound-Dokument etwas Ähnliches wie ein Anzeigebereich, der visuelle und Informationsobjekte aller Art enthalten kann: Text, Kalender, Animationen, Ton, Bewegtbilder, 3D, ständig aktualisierte Nachrichten, Steuerungen und so weiter. Jedes Anzeigebereichsobjekt ist eine unabhängige Programm-Entität, die mit einem Benutzer interagieren und auch mit anderen Objekten auf dem Anzeigebereich kommunizieren kann.

OLE (Object Linking and Embedding) wird von vielen verschiedenen Programmen unterstützt und dient dazu, Inhalte, die in einem Programm erstellt wurden, in einem anderen verfügbar zu machen. Sie können beispielsweise ein Microsoft Word-Dokument in Microsoft Excel einfügen. Um zu sehen, welche Arten von Inhalten Sie einfügen können, klicken Sie auf **Objekt** im **Einfügen**-Menü. Nur Programme, die auf dem Computer installiert sind und OLE-Objekte unterstützen, erscheinen im **Objekttyp**-Feld.

### **Einfügen von OLE-Objekten in das Arbeitsblatt**

Aspose.Cells für Python via .NET unterstützt das Hinzufügen, Extrahieren und Manipulieren von OLE-Objekten in Arbeitsblättern. Aus diesem Grund verfügt Aspose.Cells für Python via .NET über die Klasse [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection), die verwendet wird, um ein neues OLE-Objekt zur Sammlungsliste hinzuzufügen. Eine weitere Klasse, [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject), repräsentiert ein OLE-Objekt. Es hat einige wichtige Mitglieder:

- Die [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data)-Eigenschaft spezifiziert die Bilddaten im Byte-Array-Format. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt anzuzeigen.
- Die [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data)-Eigenschaft spezifiziert die Objektdaten in Form eines Byte-Arrays. Diese Daten werden in ihrem zugehörigen Programm angezeigt, wenn Sie auf das OLE-Objektsymbol doppelklicken.

Das folgende Beispiel zeigt, wie man OLE-Objekte in ein Arbeitsblatt einfügt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-InsertingOLEObjects-1.py" >}}

### **Extrahieren von OLE-Objekten in der Arbeitsmappe**

Das folgende Beispiel zeigt, wie man OLE-Objekte in einer Arbeitsmappe extrahiert. Das Beispiel erhält verschiedene OLE-Objekte aus einer vorhandenen XLS-Datei und speichert verschiedene Dateien (DOC, XLS, PPT, PDF usw.) basierend auf dem Dateiformattyp des OLE-Objekts.

Nachdem der Code ausgeführt wurde, können wir verschiedene Dateien basierend auf ihren jeweiligen OLE-Objektformattypen speichern.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-ExtractingOLEObjects-1.py" >}}

### **Extrahieren eingebetteter MOL-Datei**

Aspose.Cells für Python via .NET unterstützt das Extrahieren von Objekten ungewöhnlicher Typen wie MOL (Molekül-Daten-Datei, die Informationen über Atome und Bindungen enthält). Der folgende Codeausschnitt demonstriert das Extrahieren einer eingebetteten MOL-Datei und das Speichern auf der Festplatte unter Verwendung dieser [Beispieldatei](94896196.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractEmbeddedMolFile-1.py" >}}

## **Erweiterte Themen**
- [Auf das Anzeigen des verknüpften Ole-Objekts zugreifen und es ändern](/cells/de/python-net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Automatisches Aktualisieren des OLE-Objekts](/cells/de/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extrahieren Sie OLE-Objekte aus der Arbeitsmappe](/cells/de/python-net/extract-ole-objects-from-workbook/)
- [Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts](/cells/de/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Einfügen einer WAV-Datei als OLE-Objekt](/cells/de/python-net/inserting-a-wav-file-as-an-ole-object/)

{{< app/cells/assistant language="python-net" >}}
