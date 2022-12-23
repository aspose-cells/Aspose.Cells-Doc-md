---
title: Fügen Sie Hyperlinks in Excel oder OpenOffice ein
linktitle: Verwalten von Hyperlinks
type: docs
weight: 160
url: /de/java/insert-hyperlinks-to-excel/
---
## **Hinzufügen von Hyperlinks zu Linkdaten**
{{% alert color="primary" %}} 

Ein Hyperlink wird verwendet, um eine Verknüpfung zwischen zwei Entitäten herzustellen. Jeder kennt die Verwendung von Hyperlinks, insbesondere auf Websites.

Mit Aspose.Cells können Entwickler verschiedene Arten von Hyperlinks in Microsoft Excel-Dateien erstellen. In diesem Thema wird erläutert, welche Arten von Hyperlinks von Aspose.Cells unterstützt werden und wie sie in unseren Excel-Dateien verwendet werden können.

{{% /alert %}} 
## **Hinzufügen von Hyperlinks**
Mit Aspose.Cells können einer Zelle drei Arten von Hyperlinks hinzugefügt werden:

- [Hinzufügen eines Links zu einer URL](/cells/de/java/working-with-hyperlinks-to-link-data/).
- [Hinzufügen eines Links zu einer anderen Zelle in derselben Datei](/cells/de/java/working-with-hyperlinks-to-link-data/).
- [Hinzufügen eines Links zu einer externen Datei](/cells/de/java/working-with-hyperlinks-to-link-data/).

 Aspose.Cells ermöglicht es Entwicklern, Hyperlinks zu Excel-Dateien hinzuzufügen, entweder mithilfe der API oder[Designer-Tabellen](/cells/de/java/what-is-a-designer-spreadsheet/)(Tabellenkalkulationen, in denen Hyperlinks manuell erstellt werden und Aspose.Cells verwendet wird, um sie in andere Tabellenkalkulationen zu importieren).

Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse bietet verschiedene Methoden zum Hinzufügen verschiedener Hyperlinks zu Excel-Dateien.
## **Link zu einer URL hinzufügen**
 Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse enthält a[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) Sammlung. Jeder Artikel in der[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) Sammlung repräsentiert a[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) . Fügen Sie Hyperlinks zu URLs hinzu, indem Sie die aufrufen[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) Sammlung[Addieren](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )Methode. Das[Addieren](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))-Methode nimmt die folgenden Parameter an:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Zeilenanzahl, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten dieses Hyperlinkbereichs
- URL, die URL-Adresse.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


 Im obigen Beispiel wird ein Hyperlink zu einer URL in einer leeren Zelle hinzugefügt,**A1**Wenn in solchen Fällen eine Zelle leer ist, wird die URL-Adresse auch dieser leeren Zelle als Wert hinzugefügt. Wenn die Zelle nicht leer ist und ein Hyperlink hinzugefügt wird, sieht der Wert der Zelle wie einfacher Text aus. Damit es wie ein Hyperlink aussieht, wenden Sie die entsprechenden Formatierungseinstellungen auf diese Zelle an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Hinzufügen eines Links zu Cell in derselben Datei**
 Es ist möglich, Hyperlinks zu Zellen in derselben Excel-Datei hinzuzufügen, indem Sie die aufrufen[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) Sammlung[Addieren](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )Methode. Das[Addieren](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))-Methode funktioniert sowohl für interne als auch für externe Hyperlinks. Eine Version der überladenen Methode akzeptiert die folgenden Parameter:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Zeilenanzahl, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich.
- URL, die Adresse der Zielzelle.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Hinzufügen eines Links zu einer externen Datei**
 Es ist möglich, Hyperlinks zu externen Excel-Dateien hinzuzufügen, indem Sie die aufrufen[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) Sammlung[Addieren](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )Methode. Das[Addieren](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))-Methode nimmt die folgenden Parameter an:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Zeilenanzahl, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich.
- URL, die Adresse des Ziels, externe Excel-Datei.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Themen vorantreiben**
- [Fügen Sie Bild-Hyperlinks hinzu](/cells/de/java/add-image-hyperlinks/)
- [Hyperlinktyp erkennen](/cells/de/java/detect-hyperlink-type/)
- [Bearbeiten von Hyperlinks des Arbeitsblatts](/cells/de/java/editing-hyperlinks-of-worksheet/)
- [Holen Sie sich Hyperlinks in Reichweite](/cells/de/java/get-hyperlinks-in-range/)


