---
title: Hyperlinks in Excel oder OpenOffice einfügen
linktitle: Hyperlinks verwalten
type: docs
weight: 160
url: /de/java/insert-hyperlinks-to-excel/
---

## **Hyperlinks hinzufügen, um Daten zu verknüpfen**
{{% alert color="primary" %}} 

Ein Hyperlink wird verwendet, um eine Verknüpfung zwischen zwei Entitäten herzustellen. Jeder kennt die Verwendung von Hyperlinks, insbesondere auf Websites.

Mithilfe von Aspose.Cells können Entwickler verschiedene Arten von Hyperlinks in Microsoft Excel-Dateien erstellen. Dieses Thema erläutert, welche Arten von Hyperlinks von Aspose.Cells unterstützt werden und wie sie in unseren Excel-Dateien verwendet werden können.

{{% /alert %}} 
## **Hinzufügen von Hyperlinks**
Drei Arten von Hyperlinks können mithilfe von Aspose.Cells zu einer Zelle hinzugefügt werden:

- [Hinzufügen eines Links zu einer URL](/cells/de/java/working-with-hyperlinks-to-link-data/).
- [Hinzufügen eines Links zu einer anderen Zelle in derselben Datei](/cells/de/java/working-with-hyperlinks-to-link-data/).
- [Hinzufügen eines Links zu einer externen Datei](/cells/de/java/working-with-hyperlinks-to-link-data/).

Mit Aspose.Cells können Entwickler Hyperlinks zu Excel-Dateien entweder über die API oder [Designer-Arbeitsmappen](/cells/de/java/what-is-a-designer-spreadsheet/) (Arbeitsmappen, bei denen Hyperlinks manuell erstellt werden und Aspose.Cells verwendet wird, um sie in andere Arbeitsmappen zu importieren) hinzufügen.

Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse dargestellt. Die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse bietet verschiedene Methoden zum Hinzufügen verschiedener Hyperlinks zu Excel-Dateien.
## **Hinzufügen eines Links zu einer URL**
Die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse enthält eine [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)-Sammlung. Jedes Element in der [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)-Sammlung stellt einen [Hyperlink](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) dar. Fügen Sie Hyperlinks zu URLs hinzu, indem Sie die Methode [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) der [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks)-Sammlung aufrufen. Die Methode [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) nimmt die folgenden Parameter an:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die URL-Adresse.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


In obigem Beispiel wird einem Hyperlink eine URL in einer leeren Zelle, **A1**, hinzugefügt. In solchen Fällen, wenn eine Zelle leer ist, wird auch die URL-Adresse zu dieser leeren Zelle als Wert hinzugefügt. Ist die Zelle nicht leer und wird ein Hyperlink hinzugefügt, sieht der Wert der Zelle wie normaler Text aus. Um ihn wie einen Hyperlink aussehen zu lassen, wenden Sie die entsprechenden Formatierungseinstellungen auf diese Zelle an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Hinzufügen eines Links zu einer Zelle in derselben Datei**
Es ist möglich, Hyperlinks zu Zellen in derselben Excel-Datei hinzuzufügen, indem Sie die Methode [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) der [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)-Sammlung aufrufen. Die Methode [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) funktioniert sowohl für interne als auch externe Hyperlinks. Eine Version der überladenen Methode nimmt die folgenden Parameter an:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse der Zielzelle.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Hinzufügen eines Links zu einer externen Datei**
Es ist möglich, Hyperlinks zu externen Excel-Dateien hinzuzufügen, indem die Methode [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) der [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) -Sammlung aufgerufen wird. Die Methode [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) nimmt die folgenden Parameter an:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse des Ziels, externen Excel-Datei.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Erweiterte Themen**
- [Bild-Hyperlinks hinzufügen](/cells/de/java/add-image-hyperlinks/)
- [Hyperlink-Typ erkennen](/cells/de/java/detect-hyperlink-type/)
- [Hyperlinks im Arbeitsblatt bearbeiten](/cells/de/java/editing-hyperlinks-of-worksheet/)
- [Hyperlinks im Bereich abrufen](/cells/de/java/get-hyperlinks-in-range/)


