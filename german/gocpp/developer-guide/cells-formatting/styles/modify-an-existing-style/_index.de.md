---
title: Ändern eines bestehenden Stils mit Golang über C++
description: Aspose.Cells ist eine C++ Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien, die Benutzern ermöglicht, bestehende Zellstile zu modifizieren. Dieser Artikel beschreibt, wie man einen bestehenden Zellstil mit der Aspose.Cells Bibliothek ändert, sodass Benutzer das Aussehen der Zellen nach Bedarf anpassen können.
keywords: Existierende Stile ändern, das Erscheinungsbild Ihrer Anwendung anpassen, Anleitungen, Tutorials, Hilfedokumentationen, Entwicklerdokumentationen, API Referenzen, Beispielcode, Downloads, Support.
type: docs
weight: 90
url: /de/go-cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Um dieselben Formatierungsoptionen auf Zellen anzuwenden, erstellen Sie ein neues Formatierungsstil-Objekt. Ein Formatierungsstil-Objekt ist eine Kombination von Formatierungseigenschaften, wie Schriftart, Schriftgröße, Einzug, Nummer, Rand, Muster usw., benannt und als Satz gespeichert. Wenn angewendet, werden alle Formatierungen in diesem Stil angewendet.

Sie können auch einen vorhandenen Stil verwenden, ihn mit der Arbeitsmappe speichern und zum Formatieren von Informationen mit denselben Attributen verwenden.

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

## **Verwendung von Aspose.Cells**

Die folgenden Beispiele zeigen, wie man die [**Style.Update**](https://reference.aspose.com/cells/go-cpp/style/update/)-Methode verwendet.

### **Erstellen und Ändern eines Stils**

Dieses Beispiel erstellt ein [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-Objekt, wendet es auf einen Zellbereich an und modifiziert das [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-Objekt. Die Änderungen werden automatisch auf die Zellen und den Bereich angewendet, auf den der Stil angewendet wurde.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ModifyAnExistingStyle.go" >}}
### **Ändern eines vorhandenen Stils**

Dieses Beispiel verwendet eine einfache Vorlagendatei in Excel, auf die bereits ein Stil namens Prozent auf einen Bereich angewendet wurde. Das Beispiel:

1. holt den Stil,
1. erstellt ein Stil-Objekt und
1. ändert die Formatierung des Stils.

Die Änderungen werden automatisch auf den Bereich angewendet, auf den der Stil angewendet wurde.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ModifyAnExistingStyle-1.go" >}}
