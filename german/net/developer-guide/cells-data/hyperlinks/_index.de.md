---
title: Fügen Sie Hyperlinks in Excel oder OpenOffice ein
linktitle: Hyperlinks verwalten
type: docs
weight: 45
url: /de/net/insert-hyperlinks-to-excel/
description: So fügen Sie Hyperlinks in eine Excel-Datei mit der Bibliothek Aspose.Cells ohne MS Excel ein.
keywords: Insert Hyperlinks into Excel, Add or Insert Hyperlinks, Add or Insert link to a URL, Add or Insert a Link to a Cell, Add a Link to an External File
---
{{% alert color="primary" %}} 

Ein Hyperlink wird verwendet, um eine Verbindung zwischen zwei Entitäten herzustellen. Jeder kennt die Verwendung von Hyperlinks, insbesondere auf Websites.
Mit Aspose.Cells können Entwickler verschiedene Arten von Hyperlinks in Microsoft Excel-Dateien erstellen. In diesem Thema wird erläutert, welche Arten von Hyperlinks von Aspose.Cells unterstützt werden und wie sie in unseren Excel-Dateien verwendet werden können.

{{% /alert %}} 
##  **Hyperlinks hinzufügen**
Mit Aspose.Cells können Entwickler Hyperlinks zu Excel-Dateien hinzufügen, indem sie entweder API oder Designer-Tabellenkalkulationen verwenden (Tabellenkalkulationen, in denen Hyperlinks manuell erstellt werden und Aspose.Cells verwendet wird, um sie in andere Tabellenkalkulationen zu importieren).

 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Dies ermöglicht den Zugriff auf jedes Arbeitsblatt in der Excel-Datei. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Die Klasse bietet verschiedene Methoden zum Hinzufügen unterschiedlicher Hyperlinks zu Excel-Dateien.
##  **Link zu einer URL hinzufügen**
 Der[Arbeitsblatt](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse enthält a[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) Sammlung. Jedes Element in der[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) Sammlung repräsentiert a[Hyperlink](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . Fügen Sie Hyperlinks zu URLs hinzu, indem Sie die aufrufen[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) Sammlung[Hinzufügen](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) Methode. Der[Hinzufügen](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)Die Methode benötigt die folgenden Parameter:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich
- URL, die URL-Adresse.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

Im obigen Beispiel wird ein Hyperlink zu einer URL in einer leeren Zelle *A1** hinzugefügt. Wenn in solchen Fällen eine Zelle leer ist, wird auch die URL-Adresse als Wert zu dieser leeren Zelle hinzugefügt. Wenn die Zelle nicht leer ist und ein Hyperlink hinzugefügt wird, sieht der Wert der Zelle wie einfacher Text aus. Damit es wie ein Hyperlink aussieht, wenden Sie die entsprechenden Formatierungseinstellungen auf diese Zelle an.

{{% /alert %}} 
##  **Hinzufügen eines Links zu einer Cell in derselben Datei**
 Es ist möglich, Hyperlinks zu Zellen in derselben Excel-Datei hinzuzufügen, indem Sie aufrufen[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) Sammlung[Hinzufügen](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) Methode. Der[Hinzufügen](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)Die Methode funktioniert sowohl für interne als auch für externe Hyperlinks. Eine Version der überladenen Methode akzeptiert die folgenden Parameter:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich.
- URL, die Adresse der Zielzelle.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
##  **Einen Link zu einer externen Datei hinzufügen**
 Es ist möglich, Hyperlinks zu externen Excel-Dateien hinzuzufügen, indem man den aufruft[Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) Sammlung[Hinzufügen](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) Methode. Der[Hinzufügen](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)Die Methode benötigt die folgenden Parameter:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich.
- URL, die Adresse des Ziels, externe Excel-Datei.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

##  **Vorabthemen**
- [Fügen Sie Bild-Hyperlinks hinzu](/cells/de/net/add-image-hyperlinks/)
- [Hyperlink-Typ erkennen](/cells/de/net/detect-hyperlink-type/)
- [Bearbeiten von Hyperlinks des Arbeitsblatts](/cells/de/net/editing-hyperlinks-of-worksheet/)
- [Holen Sie sich Hyperlinks in Reichweite](/cells/de/net/get-hyperlinks-in-range/)

