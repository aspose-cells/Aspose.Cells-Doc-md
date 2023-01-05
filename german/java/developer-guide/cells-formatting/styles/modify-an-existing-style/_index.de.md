---
title: Ändern Sie einen vorhandenen Stil
type: docs
weight: 50
url: /de/java/modify-an-existing-style/
description: Erfahren Sie, wie Sie Stile in Excel mit Microsoft Excel und mit Aspose.Cells for Java API ändern.
keywords: modify an existing style excel, modify an existing style excel java, modify existing style excel, modify existing style excel java, change existing style in excel, change existing style in excel java, how to change style in excel, how to change style in excel with java, how to change style in excel with java, how to change style in excel using java, changing existing style in excel java, changing existing style in excel
---
{{% alert color="primary" %}}

Um dieselben Formatierungsoptionen auf Zellen anzuwenden, erstellen Sie ein neues Formatierungsstilobjekt. Ein Formatierungsstilobjekt ist eine Kombination aus Formatierungsmerkmalen wie Schriftart, Schriftgröße, Einzug, Zahl, Rahmen, Muster usw., die als Satz benannt und gespeichert werden. Bei der Anwendung werden alle Formatierungen in diesem Stil angewendet.

Sie können auch einen vorhandenen Stil verwenden, ihn mit der Arbeitsmappe speichern und verwenden, um Informationen mit denselben Attributen zu formatieren.

 Wenn Zellen nicht explizit formatiert sind, wird die**Normal** Stil (der Standardstil der Arbeitsmappe) wird angewendet. Microsoft Excel definiert zusätzlich zum normalen Stil mehrere Stile vor, einschließlich Komma, Währung und Prozent.

Aspose.Cells ermöglicht das Ändern jedes dieser Stile oder jedes anderen Stils, den Sie mit Ihren gewünschten Attributen definieren.

{{% /alert %}}

## **Mit Microsoft Excel**

So aktualisieren Sie einen Stil in Microsoft Excel 97-2003:

1.  Auf der**Format** Menü, klicken**Stil**.
1.  Wählen Sie den Stil aus, den Sie ändern möchten**Stilname** aufführen.
1.  Klicken**Ändern**.
1. Wählen Sie die gewünschten Stiloptionen mithilfe der Registerkarten im Dialogfeld Format Cells aus.
1.  Klicken**OK**.
1.  Unter**Stil beinhaltet**, geben Sie die gewünschten Stilmerkmale an.
1.  Klicken**OK** , um den Stil zu speichern und auf den ausgewählten Bereich anzuwenden.

## **Mit Aspose.Cells**

 Aspose.Cells bietet die[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update())-Methode zum Aktualisieren eines vorhandenen Stils.

 Um einen benannten Stil zu ändern, egal ob er dynamisch mit Aspose.Cells erstellt oder vordefiniert ist, rufen Sie die[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update())-Methode, um alle Stiländerungen widerzuspiegeln, die auf eine Zelle oder einen Bereich angewendet wurden.

 Das[**Style.update**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update() ) Methode verhält sich wie die**OK** Schaltfläche im Stildialog: Nachdem Sie Änderungen an einem vorhandenen Stil vorgenommen haben, rufen Sie auf, um die Änderung zu implementieren. Wenn Sie bereits einen Stil auf einen Zellbereich angewendet haben, die Stilattribute ändern und die Methode aufrufen, wird die Formatierung dieser Zellen automatisch aktualisiert

### **Erstellen und Ändern eines Stils**

Dieses Beispiel erstellt ein Stilobjekt, wendet es auf einen Zellbereich an und ändert das Stilobjekt. Die Änderungen werden automatisch auf die Zelle und den Bereich angewendet, auf den der Stil angewendet wurde.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Ändern eines vorhandenen Stils**

In diesem Beispiel wird eine einfache Excel-Vorlagendatei verwendet, in der ein Stil namens „Prozent“ bereits auf einen Bereich angewendet wurde. Das Beispiel:

1. bekommt den Stil,
1. erstellt ein Stilobjekt und
1. ändert die Stilformatierung.

Die Änderungen werden automatisch auf den Bereich angewendet, auf den der Stil angewendet wurde.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
