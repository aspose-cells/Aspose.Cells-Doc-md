---
title: Bereichsrahmen mit Golang via C++ festlegen
type: docs
weight: 600
url: /de/go-cpp/set-range-border/
description: Lernen Sie, mit Aspose.Cells in Golang über C++ Bereichsrahmen festzulegen.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie den Rand für einen Bereich festlegen möchten, müssen Sie nicht jede Zelle einzeln einstellen. Sie können den Rand für den gesamten Bereich festlegen. Aspose.Cells bietet diese Funktion. Dieser Artikel enthält einen Beispielcode, der zeigt, wie man mit Aspose.Cells den Bereichsrand setzt.

## **Bereichsgrenze in Excel festlegen**
Um die Grenze eines Bereichs in Excel festzulegen, befolgen Sie diese Schritte:
1. Wählen Sie den Zellenbereich aus, für den Sie die Grenze festlegen möchten.
2. Suchen Sie im Register „Start“ in der Gruppe „Schriftart“.
3. Klicken Sie in der Gruppe „Schriftart“ auf die Schaltfläche „Rahmen“.
<br>
<img src="border.png" />
4. Wählen Sie den zu verwendenden Randtyp aus den Optionen im Dropdown-Menü aus. Sie können aus voreingestellten Rahmenstilen wählen oder Ihren eigenen Rahmen anpassen.
5. Sobald Sie den gewünschten Rahmenstil ausgewählt haben, wird der Rahmen auf den ausgewählten Zellenbereich angewendet.

## **Bereichsgrenze mit Aspose.Cells festlegen**
Dieses Beispiel zeigt, wie Sie:

1. Ein Arbeitsbuch erstellen.
2. Daten in die Zellen des ersten Arbeitsblatts einfügen.
3. Erstellen Sie ein [**Range**](https://reference.aspose.com/cells/go-cpp/range).
4. Inneren Rand des Bereichs einstellen.
5. Äußeren Rand des Bereichs einstellen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetBorder.go" >}}
