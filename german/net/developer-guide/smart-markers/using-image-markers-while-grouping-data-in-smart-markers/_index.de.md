---
title: Wie man Bildmarkierungen in Smart Markers verwendet
type: docs
weight: 30
url: /de/net/how-to-use-image-markers-in-smart-markers/
alias: [/net/using-image-markers-while-grouping-data-in-smart-markers/]
---

## **Mögliche Verwendungsszenarien**
Bildmarkierungen sind spezialisierte Platzhalter in Templating-Systemen (wie FoxPro, Handlebars oder moderne UI-Frameworks), die Bilder oder visuelle Assets dynamisch in Vorlagen einfügen. Manchmal ist es notwendig, Bilder mit Smart Markern einzufügen. Aspose.Cells ermöglicht es, Bilder zu Smart Markern hinzuzufügen.

## **Bildparameter in Smart Markern**
Smart Marker-Parameter zur Verwaltung von Bildern.

- **Bild:PassendZurZelle** - Das Bild automatisch an die Zeilenhöhe und Spaltenbreite der Zelle anpassen.
- **Bild:Skalierung N** - Höhe und Breite auf N Prozent skalieren.
- **Bild:Breite:Nin&Höhe:Nin** - Das Bild N Zoll hoch und N Zoll breit darstellen. Sie können auch die Positionen Links und Oben angeben (in Punkten).

## **So verwenden Sie Bildmarkierungen in Smart Markern**
Bitte sehen Sie sich den folgenden Beispielcode an, der zeigt, wie Bilder mit Smart Markern eingefügt werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}

## **So verwenden Sie Bildmarker beim Gruppieren von Daten in Smart Markern**
Das folgende Beispiel erstellt eine Arbeitsmappe und fügt dann folgende Smart-Marker-Tags in die Zellen D2, E2 und F2 ein.

{{< highlight java >}}

&=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Dann füllt es die Datenquelle mit Daten und ruft die [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) Methode auf, um die Smart-Marker-Tags zu verarbeiten. Der Code verwendet diese Bilder, d.h. [moon.png](5115492.png) und [moon2.png](5115491.png), aber Sie können jedes Bild verwenden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}

{{< app/cells/assistant language="csharp" >}}
