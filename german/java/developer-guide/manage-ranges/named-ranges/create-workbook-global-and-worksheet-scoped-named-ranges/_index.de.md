---
title: Arbeitsmappen (global) erstellen und arbeitsblattspezifische benannte Bereiche erstellen
type: docs
weight: 10
url: /de/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, benannte Bereiche mit zwei verschiedenen Bereichen zu definieren: arbeitsmappe (auch als globaler Bereich bekannt) und tabellenblatt.

- Benannte Bereiche mit arbeitsmappenbereich können von jedem Arbeitsblatt innerhalb dieser Arbeitsmappe aus durch einfaches Verwenden ihres Namens aufgerufen werden.
- Auf tabellenblattbeschränkte benannte Bereiche werden mithilfe des Verweises auf das bestimmte Arbeitsblatt, in dem sie erstellt wurden, aufgerufen.

Aspose.Cells bietet dieselbe Funktionalität wie Microsoft Excel zum Hinzufügen von arbeitsmappe- und tabellenblattumfassenden benannten Bereichen. Beim Erstellen eines tabellenblattumfassenden benannten Bereichs sollte der Verweis auf das tabellenblatt im benannten Bereich verwendet werden, um ihn als tabellenblattumfassenden benannten Bereich zu kennzeichnen.

{{% /alert %}}

Die folgenden Codebeispiele zeigen, wie Arbeitsmappen- und Arbeitsblattbereichsnamen mithilfe der [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)-Klasse erstellt werden.

## **Hinzufügen eines benannten Bereichs mit Arbeitsmappenbereich**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Hinzufügen eines benannten Bereichs mit tabellenblattbereich**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
{{< app/cells/assistant language="java" >}}
