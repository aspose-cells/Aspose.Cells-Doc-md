---
title: Verschiedene Möglichkeiten, Dateien zu öffnen
type: docs
weight: 10
url: /de/python-net/different-ways-to-open-files/
description: Dieser Artikel erklärt, wie man eine Excel Datei mit der Aspose.Cells for Python via .NET API öffnet.
keywords: Python Öffnen einer Excel Datei ohne Excel, Wie öffne ich eine Excel Datei.
---

{{% alert color="primary" %}}

Mit Aspose.Cells for Python via .NET ist es einfach, Dateien zu öffnen, zum Beispiel, um Daten abzurufen oder um eine Designer-Vorlage zu verwenden, um den Entwicklungsprozess zu beschleunigen.

{{% /alert %}}

## **Wie man eine Excel-Datei über einen Pfad öffnet**

Entwickler können eine Microsoft Excel-Datei anhand ihres Dateipfads auf dem lokalen Computer öffnen, indem sie sie im Konstruktor der [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse angeben. Übergeben Sie einfach den Pfad als *String* im Konstruktor. Aspose.Cells for Python via .NET erkennt automatisch den Dateiformattyp.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **Wie man eine Excel-Datei über einen Stream öffnet**

Es ist auch einfach, eine Excel-Datei als Stream zu öffnen. Verwenden Sie dazu eine überladene Version des Konstruktors, die das *Stream*-Objekt enthält, das die Datei enthält.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **Wie man eine Datei nur mit Daten öffnet**

Um eine Datei nur mit den Daten zu öffnen, verwenden Sie die [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions)- und [**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter)-Klassen, um die relevanten Attribute und Optionen der Klassen für die zu ladende Vorlagendatei festzulegen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

