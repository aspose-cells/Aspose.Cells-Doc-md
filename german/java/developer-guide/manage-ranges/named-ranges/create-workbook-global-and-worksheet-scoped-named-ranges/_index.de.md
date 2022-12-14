---
title: Arbeitsmappe (global) und benannte Bereiche mit Arbeitsblattbereich erstellen
type: docs
weight: 10
url: /de/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, benannte Bereiche mit zwei verschiedenen Bereichen zu definieren: Arbeitsmappe (auch bekannt als globaler Bereich) und Arbeitsblatt.

- Auf benannte Bereiche mit einem Arbeitsmappenbereich kann von jedem Arbeitsblatt innerhalb dieser Arbeitsmappe aus zugegriffen werden, indem einfach der Name verwendet wird.
- Auf benannte Bereiche im Arbeitsblattbereich wird mit der Referenz des jeweiligen Arbeitsblatts zugegriffen, in dem sie erstellt wurden.

Aspose.Cells bietet die gleiche Funktionalität wie Microsoft Excel zum Hinzufügen von benannten Bereichen mit Arbeitsmappen- und Arbeitsblattbereich. Beim Erstellen eines benannten Bereichs im Bereich des Arbeitsblatts sollte die Arbeitsblattreferenz im benannten Bereich verwendet werden, um ihn als benannten Bereich im Bereich des Arbeitsblatts anzugeben.

{{% /alert %}}

 Die folgenden Codebeispiele zeigen, wie bereichsbezogene Namensbereiche für Arbeitsmappen und Arbeitsblätter mithilfe von erstellt werden[**Bereich**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) Klasse.

## **Hinzufügen eines benannten Bereichs mit Arbeitsmappenbereich**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Hinzufügen eines benannten Bereichs mit Arbeitsblattbereich**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
