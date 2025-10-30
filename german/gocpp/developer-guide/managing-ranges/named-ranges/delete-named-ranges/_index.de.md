---
title: Benannte Bereiche mit Golang über C++ löschen
linktitle: Benannte Bereiche löschen
type: docs
weight: 90
url: /de/go-cpp/delete-named-ranges/
description: Erfahren Sie, wie Sie definierte Namen oder benannte Bereiche aus Excel oder OpenOffice Dateien mit Aspose.Cells for C++ entfernen.
---

## **Einführung**
Wenn es zu viele definierte Namen oder benannte Bereiche in den Excel-Dateien gibt, müssen wir einige davon löschen, da sie nicht mehr referenziert werden.

## **Benannten Bereich in MS Excel entfernen**

Um einen benannten Bereich aus Excel zu entfernen, können Sie folgende Schritte befolgen:
1. Öffnen Sie Microsoft Excel und die Arbeitsmappe, die den benannten Bereich enthält.
2. Gehen Sie zum Register "Formeln" in der Excel-Menüleiste.
3. Klicken Sie auf die Schaltfläche "Namensmanager" in der Gruppe "Definierte Namen". Dadurch wird das Dialogfeld Namensmanager geöffnet.
4. Wählen Sie im Dialogfeld Namensmanager den benannten Bereich aus, den Sie entfernen möchten.
5. Klicken Sie auf die Schaltfläche "Löschen". Bestätigen Sie die Löschung beim Auffordern.
6. Klicken Sie auf die Schaltfläche "Schließen", um das Dialogfeld Namensmanager zu schließen.
7. Speichern Sie die Arbeitsmappe, um die Änderungen beizubehalten.

## **Benannten Bereich mit Aspose.Cells for C++ löschen**
Mit Aspose.Cells for C++ können Sie benannte Bereiche oder definierte Namen in der Liste per [Text](https://reference.aspose.com/cells/go-cpp/namecollection/remove_stringarray/) oder [Index](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) entfernen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges.go" >}}
Hinweis: Wenn der definierte Name sich auf Formeln bezieht, kann er nicht entfernt werden. Wir können nur die Formel des definierten Namens entfernen.

## **Einige benannte Bereiche entfernen**
Beim Entfernen eines definierten Namens müssen wir überprüfen, ob er von allen Formeln in der Datei referenziert wird.
Um die Leistung beim Entfernen benannter Bereiche zu verbessern, können wir einige gleichzeitig entfernen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-1.go" >}}
## **Doppelte definierte Namen entfernen**
Einige Excel-Dateien sind beschädigt, weil einige definierte Namen doppelt vorhanden sind. Daher können wir diese doppelten Namen entfernen, um die Datei zu reparieren.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-2.go" >}}
