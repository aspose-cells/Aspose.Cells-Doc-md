---
title: Bereichsgrenze festlegen
type: docs
weight: 600
url: /de/python-net/set-range-border/
description: In diesem Artikel wird gezeigt, wie Sie mit der Aspose.Cells für Python via .NET API einen Bereichsrand setzen.
keywords: Python Excel Bibliothek, Bereichsgrenze mit Python setzen, Bereichsgrenze mit Python hinzufügen.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie den Rand für einen Bereich setzen möchten, müssen Sie nicht jede Zelle einzeln setzen. Sie können den Rand für den Bereich festlegen. Aspose.Cells für Python via .NET bietet diese Funktion.
Dieser Artikel enthält einen Beispielcode, der Aspose.Cells für Python via .NET verwendet, um den Bereichsrand zu setzen.

## **Wie man den Bereichsrand in Excel setzt**
Um die Grenze eines Bereichs in Excel festzulegen, befolgen Sie diese Schritte:
1. Wählen Sie den Zellenbereich aus, für den Sie die Grenze festlegen möchten.
2. Suchen Sie im Register „Start“ in der Gruppe „Schriftart“.
3. Klicken Sie in der Gruppe „Schriftart“ auf die Schaltfläche „Rahmen“.
<br>
<img src="border.png" />
4. Wählen Sie den zu verwendenden Randtyp aus den Optionen im Dropdown-Menü aus. Sie können aus voreingestellten Rahmenstilen wählen oder Ihren eigenen Rahmen anpassen.
5. Sobald Sie den gewünschten Rahmenstil ausgewählt haben, wird der Rahmen auf den ausgewählten Zellenbereich angewendet.

## **Wie man den Bereichsrand mit der Aspose.Cells für Python Excel-Bibliothek setzt**
Dieses Beispiel zeigt, wie Sie:

1. Ein Arbeitsbuch erstellen.
1. Daten zu Zellen im ersten Arbeitsblatt hinzufügen.
1. [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) erstellen.
1. Inneren Rand des Bereichs festlegen.
1. Äußeren Rand des Bereichs festlegen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-set-border.py" >}}
{{< app/cells/assistant language="python-net" >}}
