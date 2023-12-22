---
title: Benannte Bereiche löschen
type: docs
weight: 90
url: /de/net/Delete-named-ranges/
description: Mit Aspose.Cells für .Net erfahren Sie, wie Sie definierte Namen oder benannte Bereiche aus Excel- oder OpenOffice-Dateien entfernen.
---
##  **Einführung**
Wenn in den Excel-Dateien zu viele definierte Namen oder benannte Bereiche vorhanden sind, müssen wir einige löschen, da sie nicht erneut referenziert werden.

##  **Entfernen Sie den benannten Bereich in MS Excel**

Um einen benannten Bereich aus Excel zu entfernen, können Sie die folgenden Schritte ausführen:
1. Öffnen Sie Microsoft Excel und öffnen Sie die Arbeitsmappe, die den benannten Bereich enthält.
2. Gehen Sie im Excel-Menüband auf die Registerkarte „Formeln“.
3. Klicken Sie in der Gruppe „Definierte Namen“ auf die Schaltfläche „Namensmanager“. Dadurch wird das Dialogfeld „Namensmanager“ geöffnet.
4. Wählen Sie im Dialogfeld „Namensmanager“ den benannten Bereich aus, den Sie entfernen möchten.
5. Klicken Sie auf die Schaltfläche „Löschen“. Bestätigen Sie den Löschvorgang, wenn Sie dazu aufgefordert werden.
6. Klicken Sie auf die Schaltfläche „Schließen“, um das Dialogfeld „Namensmanager“ zu schließen.
7. Speichern Sie die Arbeitsmappe, um die Änderungen beizubehalten.


##  ** Löscht den benannten Bereich unter Verwendung von Aspose.Cells für .Net**
 Mit Aspose.Cells für .Net können Sie benannte Bereiche oder definierte Namen entfernen[Text](https://reference.aspose.com/cells/net/aspose.cells/namecollection/remove/#remove) oder[Index](https://reference.aspose.com/cells/net/aspose.cells/namecollection/removeat/#removeat) In der Liste.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-range.cs" >}}

Hinweis: Wenn der definierte Name durch Formeln referenziert wird, kann er nicht entfernt werden. Wir können nur Formeln mit dem definierten Namen entfernen.

##  **Entfernt einige benannte Bereiche**
Wenn wir einen definierten Namen entfernen, müssen wir prüfen, ob alle Formeln in der Datei auf ihn verweisen.
Um die Leistung beim Entfernen benannter Bereiche zu verbessern, können wir einige gemeinsam entfernen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-named-ranges.cs" >}}

##  **Entfernen Sie doppelt definierte Namen**
Einige Excel-Felder sind beschädigt, weil einige definierte Namen doppelt vorhanden sind. So können wir diese doppelten Namen entfernen, um die Datei zu reparieren.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Delete-duplicate-defined-names.cs" >}}



