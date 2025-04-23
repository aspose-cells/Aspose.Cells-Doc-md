---
title: Einen vorhandenen Stil ändern
linktitle: Einen vorhandenen Stil ändern
description: Aspose.Cells ist eine Node.js Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien, mit der Benutzer bestehende Zellstile ändern können. Dieser Artikel führt ein, wie man einen bestehenden Zellenstil mit der Aspose.Cells Bibliothek anpasst, um das Erscheinungsbild der Zellen nach Bedarf zu ändern.
keywords: Existierende Stile ändern, das Erscheinungsbild Ihrer Anwendung anpassen, Anleitungen, Tutorials, Hilfedokumentationen, Entwicklerdokumentationen, API Referenzen, Beispielcode, Downloads, Support.
type: docs
weight: 90
url: /de/nodejs-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Um dieselben Formatierungsoptionen auf Zellen anzuwenden, erstellen Sie ein neues Formatierungsstil-Objekt. Ein Formatierungsstil-Objekt ist eine Kombination von Formatierungseigenschaften, wie Schriftart, Schriftgröße, Einzug, Nummer, Rand, Muster usw., benannt und als Satz gespeichert. Wenn angewendet, werden alle Formatierungen in diesem Stil angewendet.

Sie können auch einen vorhandenen Stil verwenden, diesen mit der Arbeitsmappe speichern und zur Formatierung von Informationen mit den gleichen Attributen verwenden.

Wenn Zellen nicht explizit formatiert sind, wird der **Normal**-Stil (der Standardstil der Arbeitsmappe) angewendet. Microsoft Excel definiert neben dem Normalstil mehrere Stile, darunter Komma, Währung und Prozent.

Aspose.Cells ermöglicht die Änderung aller dieser Stile oder eines anderen Stils, den Sie mit Ihren gewünschten Attributen definieren.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

So aktualisieren Sie einen Stil in Microsoft Excel 97-2003:

1. Klicken Sie im Menü **Format** auf **Stil**.
1. Wählen Sie den Stil aus, den Sie aus der Liste **Stilname** ändern möchten.
1. Klicken Sie auf **Ändern**.
1. Wählen Sie die Stiloptionen aus, die Sie mithilfe der Registerkarten im Dialogfeld Zellen formatieren möchten.
1. Klicken Sie auf **OK**.
1. Legen Sie unter **Stil enthält** die gewünschten Stileigenschaften fest.
1. Klicken Sie auf **OK**, um den Stil zu speichern und auf den ausgewählten Bereich anzuwenden.

## **Mit Aspose.Cells for Node.js via C++**

Die folgenden Beispiele zeigen, wie man die [**Style.update()**](https://reference.aspose.com/cells/nodejs-cpp/style/#update--)-Methode verwendet.

### **Erstellen und Ändern eines Stils**

Dieses Beispiel erstellt ein [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt, wendet es auf einen Zellbereich an und ändert das [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt. Die Änderungen werden automatisch auf die Zellen und den Bereich angewendet, auf den die Stil angewendet wurde.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-CreateAndModifyStyle.js" >}}


### **Ändern eines vorhandenen Stils**

Dieses Beispiel verwendet eine einfache Vorlagendatei in Excel, auf die bereits ein Stil namens Prozent auf einen Bereich angewendet wurde. Das Beispiel:

1. holt den Stil,
1. erstellt ein Stil-Objekt und
1. ändert die Formatierung des Stils.

Die Änderungen werden automatisch auf den Bereich angewendet, auf den der Stil angewendet wurde.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ModifyExistingStyle.js" >}}


