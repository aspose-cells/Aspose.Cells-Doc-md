---
title: So passt man ein Bild an die Zellenbreite und höhe an
type: docs
weight: 130
url: /de/net/how-to-fit-image-to-cell-width-height/
description: Lernen Sie, wie Sie ein Bild mit Aspose.Cells an die Zellenbreite anpassen.
keywords: Wie man ein Bild an die Zellenbreite anpasst, Bild an die Zellenbreite anpassen, Wie man ein Bild an die Zellenbreite und höhe anpasst, Bild an die Zellenhöhe anpassen.
---


## **Warum Bilder an die Zellenbreite und -höhe anpassen**
Ein Bild an die Breite und Höhe einer bestimmten Zelle anzupassen, ist nicht nur eine ästhetische Entscheidung. Es geht vor allem um Präzision, Automatisierung und Datenorganisation.

1. Für professionelle Präsentation und Lesbarkeit: Beim Erstellen eines Dashboards benötigen Sie oft Symbole, Flaggen oder Produktbilder, die perfekt mit Datenpunkten ausgerichtet sind. Ein verschobenes Bild wirkt schlampig und unprofessionell. Wenn Sie eine Vorlage entwerfen, die andere verwenden sollen (z.B. einen Produktkatalog, ein Mitarbeitungsverzeichnis), möchten Sie, dass die Bilder automatisch in die vorgesehenen Felder passen, um Konsistenz bei jeder Verwendung der Vorlage zu gewährleisten. Überlaufende Bilder können unerwartete Seitenumbrüche und Formatierungsprobleme beim Drucken verursachen. Ein passendes Bild verhält sich vorhersagbar auf der gedruckten Seite.

2. Für Datenorganisation und Struktur: Dies ist der wichtigste funktionale Grund. Excel ist ein Raster für Daten. Wenn ein Bild "platziert" wird, anstatt an eine Zelle angepasst zu werden, verursacht dies Probleme. Problem mit frei schwebenden Bildern: Sie bewegen sich nicht mit den Zellen: Wenn Sie sortieren, filtern oder Zeilen einfügen/löschen, bleibt das Bild an seiner absoluten Position im Arbeitsblatt, was die Verbindung zu den Daten, die es repräsentieren soll, vollständig löst. Sie ändern die Größe nicht mit den Zellen: Wenn Sie die Zeilenhöhe oder die Spaltenbreite ändern, bleibt ein frei schwebendes Bild gleich groß und zerstört das Layout. Vorteil des Anpassens an eine Zelle: Die Zelle wird zum "Behälter" für das Bild: Wenn ein Bild an eine Zelle angepasst wird, sind seine Position und Größe durch die Rasterkoordinaten der Zelle festgelegt. Wenn Sie die Daten verschieben (z.B. eine Tabelle sortieren), bewegt sich das Bild mit seiner entsprechenden Zeile. Es schafft ein echtes Bild-Daten-Paar: Dies ermöglicht es, das Bild als visuelles Attribut der Daten in dieser Zeile zu behandeln, was für die Automatisierung unerlässlich ist.

3. Für Automatisierung und erweiterte Funktionalität: Hier werden Bilder an Zellen angepasst zu einer Superkraft. Dynamisches Verknüpfen von Bildern: Sie können eine Formel verwenden, um einen Bildpfad aus einer Zelle zu ziehen, und dann ein Makro (VBA) nutzen, um das Bild automatisch zu dimensionieren und in eine benachbarte Zelle einzufügen. So erstellen Sie einen dynamischen Produktkatalog, bei dem sich Name, Preis und Bild automatisch ändern, wenn die Produkt-ID geändert wird. Datenbankintegration: Wenn Sie Daten exportieren oder Excel mit einer Datenbank verknüpfen, macht die Eingabe der Bilder innerhalb spezifischer Zellen den gesamten Datensatz, einschließlich seiner Visuals, strukturierter und portabler.

## **Wie man Bild an Zellenbreite und -höhe in Excel anpasst**
Sie können das Bild in Excel auf die Breite und Höhe der Zelle in zwei Verfahren anpassen.

### **Bild an Zellenbreite und -höhe anpassen durch Platzierung in Zelle**
Zum Einfügen eines Bildes in eine Zelle in Excel befolgen Sie diese Schritte:

1. Gehen Sie zum Register 'Einfügen' und klicken Sie auf die Option 'Bilder'.
2. Wählen Sie **Platzieren in Zelle** aus. Wählen Sie eine der folgenden Quellen aus dem Dropdown-Menü 'Bild einfügen von' aus (**Dieses Gerät**, **Stockbilder** und **Online-Bilder**). Dieses Gerät zum Einfügen eines Bildes von Ihrem Gerät. Stockbilder zum Einfügen eines Bildes aus Stockbildern. Online-Bilder zum Einfügen eines Bildes aus dem Web.
<br>
<img src="1.png" width=60% />
3. Bild auswählen und Bild in Zelle einfügen.
<br>
<img src="8.png" width=60% />

### **Bild an Zellenbreite und -höhe anpassen durch Platzieren über Zellen**
Zum Einfügen eines Bildes über Zellen in Excel befolgen Sie diese Schritte:

1. Gehen Sie zum Register 'Einfügen' und klicken Sie auf die Option 'Bilder'.
2. Wählen Sie **Über Zellen platzieren** aus. Wählen Sie eine der folgenden Quellen aus dem Dropdown-Menü 'Bild einfügen von' aus (**Dieses Gerät**, **Stockbilder** und **Online-Bilder**). Dieses Gerät zum Einfügen eines Bildes von Ihrem Gerät. Stockbilder zum Einfügen eines Bildes aus Stockbildern. Online-Bilder zum Einfügen eines Bildes aus dem Web.
<br>
<img src="2.png" width=60% />
3. Bild auswählen und Bild über Zellen einfügen.
<br>
<img src="3.png" width=60% />
4. Manuelles Anpassen der Breite und Höhe des Bildes, um sie an die Breite und Höhe der Zellen anzupassen.
<br>
<img src="6.png" width=60% />

## **Wie man Bild in Aspose.Cells anpasst, auf die Zellenbreite und -höhe**
Aufgrund von Variationen in der Breite und Höhe der Zeilen und Spalten, abhängig von Sprache und Anzeigeverhältnis, kann die Anpassung der Breite und Höhe eines Bildes zu leichten Abweichungen führen und manchmal nicht vollständig mit den Zellen übereinstimmen. Sie können das Bild in Aspose.Cells auf die Zellenbreite und -höhe anpassen, indem Sie die folgenden zwei Methoden verwenden.

### **Wie man Bild in Aspose.Cells anpasst durch Platzierung in Zelle**
Bild in Zelle mit Aspose.Cells einfügen. Bitte beachten Sie den folgenden Beispielcode. Nach Ausführung des Beispielcodes wird ein Bild in eine Zelle eingefügt.
1. Erstellen Sie ein Workbook-Objekt. 
2. Holen Sie sich die Zelle, in die Sie das Bild einfügen möchten.
3. Setzen Sie die Eigenschaft Cell.EmbeddedImage. 
4. Schließlich wird die Arbeitsmappe im [XLSX-Ausgabeformat](out.xlsx) gespeichert. 

### **Beispielcode für Platzierung in Zelle**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-in-cell.cs" >}}
{{< app/cells/assistant language="csharp" >}}

### **Wie man Bild an Zellenbreite und -höhe anpasst durch Platzieren über Zellen**
Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur wenige Zeilen Code:
Rufen Sie einfach die Methode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) der Sammlung [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) auf, die im Objekt [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) eingebettet ist. Dann passen Sie die Breite und Höhe des Bildes anhand der Zellenbreite und -höhe an. Schließlich speichern Sie die Datei im [Output XLSX](out_net.xlsx)-Format. Die Methode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) akzeptiert die folgenden Parameter:

- **Index der oberen linken Zeile**, der Index der oberen linken Zeile.
- **Index der oberen linken Spalte**, der Index der oberen linken Spalte.
- **Bilddateiname**, der Name der Bilddatei inklusive des Pfads.


### **Beispielcode für Platzierung über Zellen**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-over-cells-fit-cell-width-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
