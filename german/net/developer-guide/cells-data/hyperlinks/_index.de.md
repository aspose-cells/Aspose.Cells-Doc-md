---
title: Fügen Sie Hyperlinks in Excel oder OpenOffice ein
linktitle: Verwalten von Hyperlinks
type: docs
weight: 45
url: /de/net/insert-hyperlinks-to-excel/
description: So fügen Sie Hyperlinks in eine Excel-Datei mit der Bibliothek Aspose.Cells ohne MS Excel ein.
---
{{% alert color="primary" %}} 

Ein Hyperlink wird verwendet, um eine Verknüpfung zwischen zwei Entitäten herzustellen. Jeder kennt die Verwendung von Hyperlinks, insbesondere auf Websites.
Mit Aspose.Cells können Entwickler verschiedene Arten von Hyperlinks in Microsoft Excel-Dateien erstellen. In diesem Thema wird erläutert, welche Arten von Hyperlinks von Aspose.Cells unterstützt werden und wie sie in unseren Excel-Dateien verwendet werden können.

{{% /alert %}} 
## **Hinzufügen von Hyperlinks**
Aspose.Cells ermöglicht Entwicklern das Hinzufügen von Hyperlinks zu Excel-Dateien entweder mithilfe von API oder Designer-Tabellenkalkulationen (Tabellenkalkulationen, in denen Hyperlinks manuell erstellt werden und Aspose.Cells verwendet wird, um sie in andere Tabellenkalkulationen zu importieren).

 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse bietet verschiedene Methoden zum Hinzufügen verschiedener Hyperlinks zu Excel-Dateien.
## **Link zu einer URL hinzufügen**
 Das[Arbeitsblatt](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse enthält a[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) Sammlung. Jeder Artikel in der[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) Sammlung repräsentiert a[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . Fügen Sie Hyperlinks zu URLs hinzu, indem Sie die aufrufen[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) Sammlung[Addieren](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) Methode. Das[Addieren](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)Die Methode nimmt die folgenden Parameter an:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Zeilenanzahl, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich
- URL, die URL-Adresse.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

 Im obigen Beispiel wird ein Hyperlink zu einer URL in einer leeren Zelle hinzugefügt,**A1**. Wenn in solchen Fällen eine Zelle leer ist, wird die URL-Adresse auch dieser leeren Zelle als Wert hinzugefügt. Wenn die Zelle nicht leer ist und ein Hyperlink hinzugefügt wird, sieht der Wert der Zelle wie einfacher Text aus. Damit es wie ein Hyperlink aussieht, wenden Sie die entsprechenden Formatierungseinstellungen auf diese Zelle an.

{{% /alert %}} 
## **Hinzufügen eines Links zu Cell in derselben Datei**
 Es ist möglich, Hyperlinks zu Zellen in derselben Excel-Datei hinzuzufügen, indem Sie die aufrufen[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) Sammlung[Addieren](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) Methode. Das[Addieren](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)-Methode funktioniert sowohl für interne als auch für externe Hyperlinks. Eine Version der überladenen Methode akzeptiert die folgenden Parameter:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Zeilenanzahl, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich.
- URL, die Adresse der Zielzelle.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Hinzufügen eines Links zu einer externen Datei**
 Es ist möglich, Hyperlinks zu externen Excel-Dateien hinzuzufügen, indem Sie die aufrufen[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) Sammlung[Addieren](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) Methode. Das[Addieren](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)Die Methode nimmt die folgenden Parameter an:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Zeilenanzahl, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich.
- URL, die Adresse des Ziels, externe Excel-Datei.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Themen vorantreiben**
- [Fügen Sie Bild-Hyperlinks hinzu](/cells/de/net/add-image-hyperlinks/)
- [Hyperlinktyp erkennen](/cells/de/net/detect-hyperlink-type/)
- [Bearbeiten von Hyperlinks des Arbeitsblatts](/cells/de/net/editing-hyperlinks-of-worksheet/)
- [Holen Sie sich Hyperlinks in Reichweite](/cells/de/net/get-hyperlinks-in-range/)

