---
title: Einen vorhandenen Stil ändern
type: docs
weight: 50
url: /de/java/modify-an-existing-style/
description: Erfahren Sie, wie Sie mit Microsoft Excel und der Aspose.Cells for Java API Style in Excel ändern können.
keywords: bestehenden Stil in Excel ändern, bestehenden Stil in Excel java ändern, bestehenden Stil in Excel ändern, bestehenden Stil in Excel java ändern, bestehenden Stil in Excel ändern, bestehenden Stil in Excel java ändern, wie man den Stil in Excel ändert, wie man den Stil in Excel mit Java ändert, wie man den Stil in Excel mit Java ändert, wie man den Stil in Excel mit Java ändert, bestehenden Stil in Excel ändern, bestehenden Stil in Excel ändern
---

{{% alert color="primary" %}}

Um die gleichen Formatierungsoptionen auf Zellen anzuwenden, erstellen Sie ein neues Formatierungsstile-Objekt. Ein Formatierungsstile-Objekt ist eine Kombination von Formatierungseigenschaften wie Schriftart, Schriftgröße, Einzug, Nummer, Rand, Muster usw., die benannt und als Satz gespeichert werden. Bei Verwendung werden all diese Formatierungen in diesem Stil angewendet.

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

Aspose.Cells bietet die Methode [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) zur Aktualisierung eines vorhandenen Stils.

Um einen benannten Stil zu ändern, ob dynamisch erstellt mit Aspose.Cells oder vordefiniert, rufen Sie die Methode [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) auf, um etwaige Änderungen im auf eine Zelle oder Bereich angewendeten Stil widerzuspiegeln.

Die Methode [**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update--) verhält sich wie die Schaltfläche **OK** im Stildialog: Nachdem Änderungen an einem vorhandenen Stil vorgenommen wurden, rufen Sie diese auf, um die Änderung zu implementieren. Wenn Sie bereits einen Stil auf einen Zellenbereich angewendet haben, ändern Sie die Stilattribute und rufen Sie die Methode auf, um die Formatierung dieser Zellen automatisch zu aktualisieren.

### **Erstellen und Ändern eines Stils**

In diesem Beispiel wird ein Stilobjekt erstellt, auf einen Zellenbereich angewendet und das Stilobjekt modifiziert. Die Änderungen werden automatisch auf die Zelle und den Bereich angewendet, auf den der Stil angewendet wurde.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Ändern eines vorhandenen Stils**

Dieses Beispiel verwendet eine einfache Vorlagendatei in Excel, auf die bereits ein Stil namens Prozent auf einen Bereich angewendet wurde. Das Beispiel:

1. holt den Stil,
1. erstellt ein Stil-Objekt und
1. ändert die Formatierung des Stils.

Die Änderungen werden automatisch auf den Bereich angewendet, auf den der Stil angewendet wurde.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
