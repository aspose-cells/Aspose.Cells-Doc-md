---
title: Verwenden Sie Optionen zur Fehlerprüfung
type: docs
weight: 140
url: /de/net/use-error-checking-options/
description: In diesem Artikel finden Sie Beispielcode, der programmgesteuert Fehlerprüfoptionen von Excel-Arbeitsblättern verwendet, z. B. Numbers, gespeichert als Text mithilfe der Bibliothek C#, API oder .NET.
keywords: store number as text in excel using c#, error check excel options c#
---
{{% alert color="primary" %}}

Microsoft Excel ermöglicht Benutzern das Definieren von Fehlerprüfungsoptionen und -regeln. Benutzer sehen beim Erstellen von Formeln häufig Fehlerprüfungen. Ein kleines Dreieck in der oberen rechten Ecke einer Zelle zeigt an, wenn ein Problem mit einer Zelle vorliegt. Excel stellt Informationen bereit, die Benutzern bei der Behebung häufiger Probleme helfen.

{{% /alert %}}

##  **Arten von Fehlern**

Fehler, die dazu führen, dass die Formel kein Ergebnis zurückgeben kann (z. B. die Division einer Zahl durch Null), erfordern sofortige Aufmerksamkeit und in der Zelle wird ein Fehlerwert angezeigt. Wenn Sie auf das grüne Dreieck klicken, wird ein Ausrufezeichen angezeigt. Wenn Sie darauf klicken, wird eine Liste mit Optionen geöffnet.

Der Fehler kann über die Optionen behoben oder ignoriert werden. Das Ignorieren eines Fehlers bedeutet, dass dieser Fehler bei weiteren Fehlerprüfungen nicht angezeigt wird.

 Aspose.Cells bietet Optionen zur Fehlerprüfung. Der[**ErrorCheckOption**](https://reference.aspose.com/cells/net/aspose.cells/errorcheckoption) Die Klasse verwaltet verschiedene Arten von Fehlerprüfungen, z. B. als Text gespeicherte Zahlen, Formelberechnungsfehler und Validierungsfehler. Benutzen Sie die[**ErrorCheckType**](https://reference.aspose.com/cells/net/aspose.cells/errorchecktype)Aufzählung, um die gewünschte Fehlerprüfung festzulegen.

##  **Numbers Als Text gespeichert**

Gelegentlich werden Zahlen möglicherweise formatiert und als Text in Zellen gespeichert. Dies kann zu Problemen bei Berechnungen oder zu verwirrenden Sortierreihenfolgen führen. Numbers, die als Text formatiert sind, werden in der Zelle links statt rechts ausgerichtet. Wenn eine Formel, die eine mathematische Operation an Zellen ausführen soll, keinen Wert zurückgibt, überprüfen Sie die Ausrichtung in den Zellen, auf die sich die Formel bezieht – einige oder alle dieser Zellen können als Text formatierte Zahlen sein.

Mithilfe der Optionen zur Fehlerprüfung können Sie als Text gespeicherte Zahlen schnell in reelle Zahlen umwandeln. In Microsoft Excel 2003:

1.  Auf der**Werkzeug** Klicken Sie im Menü auf *Optionen**.
1. Wählen Sie die Registerkarte Fehlerprüfung.
   **Nummer als Text gespeichert** Die Option ist standardmäßig aktiviert.
1. Deaktivieren Sie es.

Der folgende Beispielcode zeigt, wie die als Option zur Textfehlerprüfung gespeicherten Zahlen für ein Arbeitsblatt in der Vorlagendatei XLS mithilfe der Aspose.Cells-APIs deaktiviert werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ErrorCheckingOptions-1.cs" >}}
