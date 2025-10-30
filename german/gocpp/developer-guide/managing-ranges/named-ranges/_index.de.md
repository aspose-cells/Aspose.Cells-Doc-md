---
title: Erstellen Sie Arbeitsmappen und Arbeitsblatt gebundene benannte Bereiche mit Golang via C++
linktitle: Benannten Bereich
type: docs
weight: 40
url: /de/go-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Lernen Sie, mit Golang über C++ Arbeitsmappen und Arbeitsblatt gebundene benannte Bereiche mit Aspose.Cells zu erstellen.
---

{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Benutzern, benannte Bereiche mit zwei verschiedenen Bereichen zu definieren: arbeitsmappe (auch als globaler Bereich bekannt) und tabellenblatt.

- Benannte Bereiche mit arbeitsmappenbereich können von jedem Arbeitsblatt innerhalb dieser Arbeitsmappe aus durch einfaches Verwenden ihres Namens aufgerufen werden.
- Auf tabellenblattbeschränkte benannte Bereiche werden mithilfe des Verweises auf das bestimmte Arbeitsblatt, in dem sie erstellt wurden, aufgerufen.

Aspose.Cells bietet dieselbe Funktionalität wie Microsoft Excel zum Hinzufügen von arbeitsmappe- und tabellenblattumfassenden benannten Bereichen. Beim Erstellen eines tabellenblattumfassenden benannten Bereichs sollte der Verweis auf das tabellenblatt im benannten Bereich verwendet werden, um ihn als tabellenblattumfassenden benannten Bereich zu kennzeichnen.

{{% /alert %}} 

## **Hinzufügen eines benannten Bereichs mit arbeitsmappenbereich**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges.go" >}}
## **Hinzufügen eines benannten Bereichs mit tabellenblattbereich**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NamedRanges-1.go" >}}
## **Erweiterte Themen**
- [Zugriff erstellen und benannte Bereiche kopieren](/cells/de/cpp/create-access-and-copy-named-ranges/)
- [Benannte Bereiche formatieren und ändern](/cells/de/cpp/format-and-modify-named-ranges/)
- [Bereich mit externen Links abrufen](/cells/de/cpp/get-range-with-external-links/)
- [Implementierung nicht aufeinanderfolgender Bereiche](/cells/de/cpp/implementing-non-sequential-ranges/)

