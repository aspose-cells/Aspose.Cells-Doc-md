---
title: Bereichsdaten nur kopieren
type: docs
weight: 330
url: /de/java/copy-range-data-only/
---

{{% alert color="primary" %}} 

Manchmal müssen Sie Daten aus einem Zellbereich in einen anderen kopieren, wobei nur die Daten und nicht das Format kopiert werden. Aspose.Cells bietet diese Funktion durch die Bereitstellung der [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData-com.aspose.cells.Range-) Methode.

{{% /alert %}} 
## **Nur Datenbereich kopieren**
Dieses Beispiel zeigt, wie Sie:

1. Ein Arbeitsbuch erstellen.
1. Daten zu Zellen im ersten Arbeitsblatt hinzufügen.
1. Erstellen Sie einen Bereich.
1. Erstellen Sie ein Style-Objekt mit angegebenen Formatierungseigenschaften.
1. Wenden Sie die Formatierung des Stils auf den Bereich an.
1. Einen weiteren Zellenbereich erstellen.
1. Kopieren Sie die Daten des ersten Bereichs mit der [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData-com.aspose.cells.Range-) Methode in diesen zweiten Bereich.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}
{{< app/cells/assistant language="java" >}}
