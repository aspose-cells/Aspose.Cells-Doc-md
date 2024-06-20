---
title: Hyperlinks in Excel oder OpenOffice einfügen
linktitle: Hyperlinks verwalten
type: docs
weight: 45
url: /de/net/insert-hyperlinks-to-excel/
description: Wie man Hyperlinks in eine Excel Datei mit der Bibliothek Aspose.Cells ohne MS Excel einfügt
keywords: Hyperlinks in Excel einfügen, Hyperlinks hinzufügen oder einfügen, Link zu einer URL hinzufügen oder einfügen, Link zu einer Zelle hinzufügen oder einfügen, Link zu einer externen Datei hinzufügen
---

{{% alert color="primary" %}} 

Ein Hyperlink wird verwendet, um eine Verknüpfung zwischen zwei Entitäten herzustellen. Jeder kennt die Verwendung von Hyperlinks, insbesondere auf Websites.
Mithilfe von Aspose.Cells können Entwickler verschiedene Arten von Hyperlinks in Microsoft Excel-Dateien erstellen. Dieses Thema erläutert, welche Arten von Hyperlinks von Aspose.Cells unterstützt werden und wie sie in unseren Excel-Dateien verwendet werden können.

{{% /alert %}} 
## **Hinzufügen von Hyperlinks**
Aspose.Cells ermöglicht Entwicklern, Hyperlinks zu Excel-Dateien entweder über die API oder Designer-Arbeitsmappen (Arbeitsmappen, in denen Hyperlinks manuell erstellt und Aspose.Cells verwendet werden, um sie in andere Arbeitsmappen zu importieren) hinzuzufügen.

Aspose.Cells stellt eine Klasse, [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) zur Verfügung, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) dargestellt. Die Klasse [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet verschiedene Methoden zum Hinzufügen verschiedener Hyperlinks zu Excel-Dateien.
## **Hinzufügen eines Links zu einer URL**
Die Klasse [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) enthält eine [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)-Sammlung. Jedes Element in der [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)-Sammlung repräsentiert einen [Hyperlink](https://reference.aspose.com/cells/net/aspose.cells/hyperlink). Fügen Sie Hyperlinks zu URLs hinzu, indem Sie die [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection)-Sammlungsmethode [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) aufrufen. Die [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)-Methode nimmt folgende Parameter entgegen:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlink-Bereich.
- URL, die URL-Adresse.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

Im obigen Beispiel wird einem leeren Zellfeld **A1** ein Hyperlink zu einer URL hinzugefügt. In solchen Fällen, wenn eine Zelle leer ist, wird auch die URL-Adresse zu dieser leeren Zelle als ihr Wert hinzugefügt. Wenn die Zelle nicht leer ist und ein Hyperlink hinzugefügt wird, sieht der Wert der Zelle wie normaler Text aus. Um ihn wie einen Hyperlink aussehen zu lassen, wenden Sie die entsprechenden Formatierungseinstellungen auf diese Zelle an.

{{% /alert %}} 
## **Hinzufügen eines Links zu einer Zelle in derselben Datei**
Es ist möglich, Hyperlinks zu Zellen in derselben Excel-Datei hinzuzufügen, indem Sie die [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection)-Sammlungsmethode [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) aufrufen. Die [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)-Methode funktioniert für interne und externe Hyperlinks. Eine Version der überladenen Methode nimmt folgende Parameter entgegen:

- Zellenname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse der Zielzelle.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Hinzufügen eines Links zu einer externen Datei**
Es ist möglich, Hyperlinks zu externen Excel-Dateien hinzuzufügen, indem Sie die [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection)-Sammlungsmethode [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) aufrufen. Die [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)-Methode nimmt folgende Parameter entgegen:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse des Ziels, externen Excel-Datei.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Erweiterte Themen**
- [Bild-Hyperlinks hinzufügen](/cells/de/net/add-image-hyperlinks/)
- [Hyperlink-Typ erkennen](/cells/de/net/detect-hyperlink-type/)
- [Hyperlinks im Arbeitsblatt bearbeiten](/cells/de/net/editing-hyperlinks-of-worksheet/)
- [Hyperlinks im Bereich abrufen](/cells/de/net/get-hyperlinks-in-range/)

