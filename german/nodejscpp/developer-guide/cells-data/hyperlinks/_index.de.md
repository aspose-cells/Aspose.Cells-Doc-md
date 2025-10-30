---
title: Hyperlinks in Excel oder OpenOffice einfügen
linktitle: Hyperlinks verwalten
type: docs
weight: 45
url: /de/nodejs-cpp/insert-hyperlinks-to-excel/
description: Wie man Hyperlinks in eine Excel Datei mit der Aspose.Cells Bibliothek ohne MS Excel in Node.js via C++ einfügt.
keywords: Hyperlinks in Excel einfügen Node.js via C++, Hyperlinks hinzufügen oder einfügen Node.js via C++, Link zu einer URL hinzufügen oder einfügen Node.js via C++, Link zu einer Zelle hinzufügen oder einfügen Node.js via C++, Link zu einer externen Datei hinzufügen Node.js via C++
---

{{% alert color="primary" %}} 

Ein Hyperlink wird verwendet, um eine Verknüpfung zwischen zwei Entitäten herzustellen. Jeder kennt die Verwendung von Hyperlinks, insbesondere auf Websites.
Mithilfe von Aspose.Cells können Entwickler verschiedene Arten von Hyperlinks in Microsoft Excel-Dateien erstellen. Dieses Thema erläutert, welche Arten von Hyperlinks von Aspose.Cells unterstützt werden und wie sie in unseren Excel-Dateien verwendet werden können.

{{% /alert %}} 

## **Hinzufügen von Hyperlinks**
Aspose.Cells ermöglicht es Entwicklern, Hyperlinks entweder über die API oder Designer-Tabellen (Tabellen, in denen Hyperlinks manuell erstellt und mit Aspose.Cells in andere Tabellen importiert werden) hinzuzufügen.

Aspose.Cells stellt eine Klasse [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse dargestellt. Die [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet verschiedene Methoden zum Hinzufügen verschiedener Hyperlinks zu Excel-Dateien.
## **Hinzufügen eines Links zu einer URL**
Die [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse enthält eine [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks-) Sammlung. Jedes Element in der Sammlung [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks-) stellt einen [Hyperlink](https://reference.aspose.com/cells/nodejs-cpp/hyperlink) dar. Fügen Sie Hyperlinks zu URLs hinzu, indem Sie die [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection)-Sammlung mit der [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) Methode aufrufen. Die [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) Methode akzeptiert die folgenden Parameter:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die URL-Adresse.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToURL.js" >}}


{{% alert color="primary" %}} 

Im obigen Beispiel wird einem leeren Zellfeld **A1** ein Hyperlink zu einer URL hinzugefügt. In solchen Fällen, wenn eine Zelle leer ist, wird auch die URL-Adresse zu dieser leeren Zelle als ihr Wert hinzugefügt. Wenn die Zelle nicht leer ist und ein Hyperlink hinzugefügt wird, sieht der Wert der Zelle wie normaler Text aus. Um ihn wie einen Hyperlink aussehen zu lassen, wenden Sie die entsprechenden Formatierungseinstellungen auf diese Zelle an.

{{% /alert %}} 
## **Hinzufügen eines Links zu einer Zelle in derselben Datei**
Es ist möglich, Hyperlinks zu Zellen in derselben Excel-Datei hinzuzufügen, indem die [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection)-Sammlung mit der [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) Methode aufgerufen wird. Die [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) Methode funktioniert sowohl für interne als auch externe Hyperlinks. Eine Version der überladenen Methode akzeptiert die folgenden Parameter:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse der Zielzelle.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToCell.js" >}}


## **Hinzufügen eines Links zu einer externen Datei**
Es ist möglich, Hyperlinks zu externen Excel-Dateien hinzuzufügen, indem die [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection)-Sammlung mit der [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) Methode aufgerufen wird. Die [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) Methode akzeptiert die folgenden Parameter:

- Zellname, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Anzahl der Zeilen, die Anzahl der Zeilen im Hyperlink-Bereich.
- Anzahl der Spalten, die Anzahl der Spalten im Hyperlink-Bereich.
- URL, die Adresse des Ziels, externen Excel-Datei.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToExternalFile.js" >}}



## **Erweiterte Themen**
- [Bild-Hyperlinks hinzufügen](/cells/de/nodejs-cpp/add-image-hyperlinks/)
- [Hyperlink-Typ erkennen](/cells/de/nodejs-cpp/detect-hyperlink-type/)
- [Hyperlinks im Arbeitsblatt bearbeiten](/cells/de/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [Hyperlinks im Bereich abrufen](/cells/de/nodejs-cpp/get-hyperlinks-in-range/)

{{< app/cells/assistant language="nodejs-cpp" >}}
