---
title: Ändern Sie einen vorhandenen Stil
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die es Benutzern ermöglicht, vorhandene Zellstile zu ändern. In diesem Artikel erfahren Sie, wie Sie einen vorhandenen Zellenstil mit der Bibliothek Aspose.Cells ändern, sodass Benutzer das Erscheinungsbild der Zellen nach Bedarf ändern können.
keywords: Modify existing styles, customize the look and feel of your application, guides, tutorials, help documentation, development documentation, API references, sample code, downloads, support.
type: docs
weight: 90
url: /de/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

Um dieselben Formatierungsoptionen auf Zellen anzuwenden, erstellen Sie ein neues Formatierungsstilobjekt. Ein Formatierungsstilobjekt ist eine Kombination von Formatierungsmerkmalen wie Schriftart, Schriftgröße, Einzug, Zahl, Rahmen, Muster usw., die als Satz benannt und gespeichert werden. Bei der Anwendung werden alle Formatierungen in diesem Stil angewendet.

Sie können auch einen vorhandenen Stil verwenden, ihn mit der Arbeitsmappe speichern und zum Formatieren von Informationen mit denselben Attributen verwenden.

 Wenn Zellen nicht explizit formatiert sind, wird die**Normal** Der Stil (der Standardstil der Arbeitsmappe) wird angewendet. Microsoft Excel definiert zusätzlich zum Normalstil mehrere Stile vor, darunter Komma, Währung und Prozent.

Mit Aspose.Cells können Sie jeden dieser Stile oder jeden anderen Stil, den Sie mit Ihren gewünschten Attributen definieren, ändern.

{{% /alert %}}

##  **Mit Microsoft Excel**

So aktualisieren Sie einen Stil in Microsoft Excel 97-2003:

1.  Auf der**Format** Klicken Sie im Menü auf *Stil**.
1.  Wählen Sie den Stil aus, den Sie ändern möchten**Stilname** Liste.
1. Klicken Sie auf *Ändern**.
1. Wählen Sie mithilfe der Registerkarten im Dialogfeld „Format Cells“ die gewünschten Stiloptionen aus.
1. OK klicken**.
1. Geben Sie unter *Stil beinhaltet** die gewünschten Stilfunktionen an.
1.  Klicken**OK** , um den Stil zu speichern und auf den ausgewählten Bereich anzuwenden.

##  **Verwenden Sie Aspose.Cells**

 Die folgenden Beispiele veranschaulichen die Verwendung[**Style.Update**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)Methode.

###  **Erstellen und Ändern eines Stils**

 In diesem Beispiel wird ein erstellt[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt, wendet es auf einen Bereich von Zellen an und ändert das[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt. Die Änderungen werden automatisch auf die Zelle und den Bereich angewendet, auf den der Stil angewendet wurde.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

###  **Ändern eines vorhandenen Stils**

In diesem Beispiel wird eine einfache Excel-Vorlagendatei verwendet, in der ein Stil namens „Prozent“ bereits auf einen Bereich angewendet wurde. Das Beispiel:

1. bekommt den Stil,
1. erstellt ein Stilobjekt und
1. Ändert die Stilformatierung.

Die Änderungen werden automatisch auf den Bereich angewendet, auf den der Stil angewendet wurde.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
