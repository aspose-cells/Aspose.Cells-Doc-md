---
title: Hyperlinks in Excel oder OpenOffice einfügen
linktitle: Hyperlinks verwalten
type: docs
weight: 45
url: /de/python-net/insert-hyperlinks-to-excel/
description: Wie man Hyperlinks in eine Excel Datei mit der Aspose.Cells for Python via .NET Bibliothek ohne MS Excel einfügt.
keywords: Python Excel Bibliothek, Python Hyperlinks in Excel einfügen, Python Hyperlinks hinzufügen oder einfügen, Python Link zu einer URL hinzufügen oder einfügen, Python Link zu einer Zelle hinzufügen oder einfügen, Python Link zu einer externen Datei hinzufügen
---

{{% alert color="primary" %}} 

Ein Hyperlink wird verwendet, um eine Verknüpfung zwischen zwei Entitäten herzustellen. Jeder kennt die Verwendung von Hyperlinks, insbesondere auf Websites.
Mit Aspose.Cells für Python via .NET können Entwickler verschiedene Arten von Hyperlinks in Microsoft Excel-Dateien erstellen. In diesem Thema wird diskutiert, welche Arten von Hyperlinks von Aspose.Cells für Python via .NET unterstützt werden und wie sie in unseren Excel-Dateien verwendet werden können.

{{% /alert %}} 
## **Wie man Hyperlinks hinzufügt**
Aspose.Cells für Python via .NET ermöglicht Entwicklern, Hyperlinks zu Excel-Dateien hinzuzufügen, entweder über die API oder Designer-Tabellenkalkulationen (Tabellenkalkulationen, in denen Hyperlinks manuell erstellt werden und Aspose.Cells für Python via .NET verwendet wird, um sie in andere Tabellenkalkulationen zu importieren).

Aspose.Cells für Python via .NET stellt eine Klasse, [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) zur Verfügung, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) stellt verschiedene Methoden zum Hinzufügen verschiedener Hyperlinks zu Excel-Dateien bereit.

## **Wie man einen Link zu einer URL hinzufügt**
Die Klasse [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) enthält eine [Hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)-Sammlung. Jedes Element in der [Hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)-Sammlung repräsentiert einen [Hyperlink](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink). Fügen Sie Hyperlinks zu URLs hinzu, indem Sie die [Hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)-Sammlungsmethode [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) aufrufen. Die [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) Methode nimmt die folgenden Parameter an:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlink-Bereich.
- URL, die URL-Adresse.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

Im obigen Beispiel wird einem leeren Zellfeld **A1** ein Hyperlink zu einer URL hinzugefügt. In solchen Fällen, wenn eine Zelle leer ist, wird auch die URL-Adresse zu dieser leeren Zelle als ihr Wert hinzugefügt. Wenn die Zelle nicht leer ist und ein Hyperlink hinzugefügt wird, sieht der Wert der Zelle wie normaler Text aus. Um ihn wie einen Hyperlink aussehen zu lassen, wenden Sie die entsprechenden Formatierungseinstellungen auf diese Zelle an.

{{% /alert %}} 

## **Wie man einen Link zu einer Zelle in derselben Datei hinzufügt**
Es ist möglich, Hyperlinks zu Zellen in derselben Excel-Datei hinzuzufügen, indem Sie die [Hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)-Sammlungsmethode [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) aufrufen. Die [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) Methode funktioniert sowohl für interne als auch externe Hyperlinks. Eine Version der überladenen Methode nimmt die folgenden Parameter an:

- Zellenname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse der Zielzelle.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **Wie man einen Link zu einer externen Datei hinzufügt**
Es ist möglich, Hyperlinks zu externen Excel-Dateien hinzuzufügen, indem Sie die Methode [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) der [Hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)-Sammlung aufrufen. Die Methode [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) hat folgende Parameter:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse des Ziels, externen Excel-Datei.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **Erweiterte Themen**
- [Bild-Hyperlinks hinzufügen](/cells/de/python-net/add-image-hyperlinks/)
- [Hyperlink-Typ erkennen](/cells/de/python-net/detect-hyperlink-type/)
- [Hyperlinks im Arbeitsblatt bearbeiten](/cells/de/python-net/editing-hyperlinks-of-worksheet/)
- [Hyperlinks im Bereich abrufen](/cells/de/python-net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="python-net" >}}
