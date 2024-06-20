---
title: Arbeitsmappe und tabellenblattumfassende benannte Bereiche erstellen
linktitle: Benannten Bereich
type: docs
weight: 40
url: /de/python-net/create-workbook-and-worksheet-scoped-named-ranges/
description: Dieser Artikel zeigt, wie man Arbeitsmappen und Arbeitsblatt spezifische benannte Bereiche mit der Aspose.Cells für Python via .NET API erstellt.
keywords: Python Excel Bibliothek, Python Erstellen von Arbeitsmappen und Arbeitsblatt spezifischen benannten Bereichen, Python Hinzufügen eines benannten Bereichs mit Arbeitsmappen Bereich, Python Hinzufügen eines benannten Bereichs mit Arbeitsblatt Bereich.
---

{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Benutzern, benannte Bereiche mit zwei verschiedenen Bereichen zu definieren: arbeitsmappe (auch als globaler Bereich bekannt) und tabellenblatt.

- Benannte Bereiche mit arbeitsmappenbereich können von jedem Arbeitsblatt innerhalb dieser Arbeitsmappe aus durch einfaches Verwenden ihres Namens aufgerufen werden.
- Auf tabellenblattbeschränkte benannte Bereiche werden mithilfe des Verweises auf das bestimmte Arbeitsblatt, in dem sie erstellt wurden, aufgerufen.

Aspose.Cells für Python via .NET bietet die gleiche Funktionalität wie Microsoft Excel zum Hinzufügen von Arbeitsmappe- und Arbeitsblattbasierten benannten Bereichen. Bei der Erstellung eines auf das Arbeitsblatt bezogenen benannten Bereichs sollte der Arbeitsblattverweis im benannten Bereich verwendet werden, um ihn als auf das Arbeitsblatt bezogenen benannten Bereich zu spezifizieren.


{{% /alert %}} 
## **Benannten Bereich mit Arbeitsmappenbereich hinzufügen**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-AddWorkbookScopedNamedRange-1.py" >}}
## **Benannten Bereich mit Arbeitsblattbereich hinzufügen**


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-WorkbookScopedNamedRanges-WorksheetNamedRange-1.py" >}}

## **Erweiterte Themen**
- [Zugriff erstellen und benannte Bereiche kopieren](/cells/de/python-net/create-access-and-copy-named-ranges/)
- [Benannte Bereiche formatieren und ändern](/cells/de/python-net/format-and-modify-named-ranges/)
- [Bereich mit externen Links abrufen](/cells/de/python-net/get-range-with-external-links/)
- [Implementierung nicht aufeinanderfolgender Bereiche](/cells/de/python-net/implementing-non-sequential-ranges/)
