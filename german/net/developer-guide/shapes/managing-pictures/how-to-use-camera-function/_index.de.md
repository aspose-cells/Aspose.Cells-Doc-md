---
title: Wie man Kamera für Bereich hinzufügt
type: docs
weight: 10
url: /de/net/how-to-add-camera-for-range/
description: Dieser Artikel stellt vor, wie man eine Kamera für den Bereichsinhalte API Aspose.Cells for .NET hinzufügt.
keywords: Wie man die Kamerafunktion verwendet, wie man eine Kamera für den Bereichinhalt hinzufügt, wie man das Kamera Tool verwendet, Kamerafunktion in Excel, wie man die Kamerafunktion in Aspose.Cells for .NET benutzt
---

## **Mögliche Verwendungsszenarien**
Das Kamera-Tool in Excel ist eine versteckte, aber leistungsstarke Funktion, mit der Sie eine Live-, verlinkte Momentaufnahme eines beliebigen Zellbereichs erstellen können. Hier warum und wann Sie es verwenden sollten.

Was das Kamera-Tool macht:
1. Macht ein "Bild" von einem ausgewählten Zellbereich.
2. Das "Bild" ist eine Live-Verbindung — wenn sich die Quelzellen ändern, wird das Bild automatisch aktualisiert.
3. Sie können das Bild beliebig auf dem Blatt verschieben oder in der Größe anpassen, sogar auf ein anderes Blatt.


## **So verwenden Sie das Kamerafunktion in Excel**
Hier ist eine Schritt-für-Schritt-Anleitung zur Verwendung des Kamera-Tools in Excel — eine leistungsstarke Methode, um dynamische, lebendige Bilder von Zellbereichen zu erstellen.

### Kamera-Tool aktivieren

Das Kamera-Tool ist standardmäßig ausgeblendet. Hier erfahren Sie, wie Sie es hinzufügen:

1. Klicken Sie auf den Abwärtspfeil auf der Symbolleiste für den Schnellzugriff (oberer linker Rand von Excel).
2. Wählen Sie Weitere Befehle....
3. Im Dialog: Wählen Sie im Dropdown “Befehle auswählen” die Option Befehle nicht im Menüband. Scrollen Sie nach unten und wählen Sie Kamera. Klicken Sie auf >> Hinzufügen, um es der Symbolleiste hinzuzufügen.
4. Klicken Sie auf OK. Sie sehen nun ein kleines Kamerasymbol in Ihrer Symbolleiste.

### Verwendung des Kamera-Tools
1. Wählen Sie den Zellbereich aus, den Sie erfassen möchten (z.B. A1:C5).
2. Klicken Sie auf das Kamera-Symbol in der Symbolleiste für den Schnellzugriff.
3. Der Mauszeiger ändert sich in ein Fadenkreuz.
4. Klicken Sie irgendwo im Arbeitsblatt, wo Sie das Bild platzieren möchten. Es wird ein Live-BBild des ausgewählten Bereichs eingefügt.

### Dynamisches Verknüpfen
Das Bild ist mit den Originalzellen verknüpft. Wenn sich die Werte oder die Formatierung im Quellbereich ändern, aktualisiert sich das Bild automatisch.


## **Wie man Kamera für Bereich in Aspose.Cells for .NET hinzufügt**
Aspose.Cells unterstützt die Anzeige des Inhalts einer Zelle oder eines Bereichs in einer Bildform. Sie können das Bild mit der Zelle oder dem Bereich verknüpfen, das die anzuzeigenden Daten enthält. Da die Zelle oder der Bereich mit dem Grafikobjekt verknüpft ist, erscheinen Änderungen an den Daten in dieser Zelle oder diesem Bereich automatisch im Grafikobjekt. 

Hier ist ein einfaches Beispiel, wie man die Kamerafunktion mit [Beispieldatei](camera.xlsx) in Aspose.Cells for .NET verwendet:

1. Laden Sie die Beispieldatei mit der Klasse [Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook).
1. Fügen Sie ein Bild zum Arbeitsblatt hinzu, indem Sie die Methode [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) der Sammlung [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) aufrufen (eingeschlossen im Objekt [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). 
1. Geben Sie den Zellbereich mit dem Attribut [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) des Objekts [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) an.
1. Aktualisieren Sie den ausgewählten Wert der Formen im Arbeitsblatt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-how-to-use-camera-function.cs" >}}

## **Ausgabeergebnis**
Der folgende Screenshot zeigt die Kamera des Bereichs(A1:E12), erstellt von Aspose.Cells for .NET in der Ausgabedatei der Excel.
<br>
Vor dem Hinzufügen von Daten:
<br>
<img src="1.png" width=70% />
<br>
Nach dem Hinzufügen von Daten:
<br>
<img src="2.png" width=70% />
{{< app/cells/assistant language="csharp" >}}
