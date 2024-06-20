---
title: Verwenden von Fehlerüberprüfungsoptionen
type: docs
weight: 140
url: /de/net/use-error-checking-options/
description: In diesem Artikel finden Sie Beispielcode, um programmgesteuert Fehlerüberprüfungsoptionen von Excel Arbeitsblättern wie z. B. als Text gespeicherte Zahlen mithilfe der C# API oder der .NET Bibliothek zu verwenden.
keywords: In Microsoft Excel können Benutzer Fehlerüberprüfungsoptionen und Regeln definieren. Benutzer sehen häufig Fehlerüberprüfungen beim Erstellen von Formeln, ein kleines Dreieck in der oberen rechten Ecke einer Zelle zeigt an, wenn es ein Problem mit einer Zelle gibt. Excel stellt Informationen zur Verfügung, die Benutzern helfen, übliche Probleme zu korrigieren.
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, Fehlerprüfoptionen und -regeln zu definieren. Benutzer sehen oft Fehlerprüfungen beim Erstellen von Formeln, ein kleines Dreieck in der oberen rechten Ecke einer Zelle markiert, wenn ein Problem mit einer Zelle vorliegt. Excel bietet Informationen, die den Benutzern helfen, häufige Probleme zu korrigieren.

{{% /alert %}}

## **Arten von Fehlern**

Fehler, die bedeuten, dass die Formel kein Ergebnis zurückgeben kann - wie beispielsweise die Division durch Null - erfordern sofortige Aufmerksamkeit, und ein Fehlerwert wird in der Zelle angezeigt. Durch Klicken auf das grüne Dreieck wird ein Ausrufezeichen angezeigt, und ein Klick darauf öffnet eine Liste von Optionen.

Der Fehler kann mithilfe der Optionen behoben oder ignoriert werden. Das Ignorieren eines Fehlers bedeutet, dass dieser bei weiteren Fehlerprüfungen nicht mehr angezeigt wird.

Aspose.Cells bietet Optionen zur Fehlerprüfung. Die Klasse [**ErrorCheckOption**](https://reference.aspose.com/cells/net/aspose.cells/errorcheckoption) verwaltet verschiedene Arten von Fehlerprüfungen, wie beispielsweise Zahlen, die als Text gespeichert sind, Formelberechnungsfehler und Validierungsfehler. Verwenden Sie die Aufzählung [**ErrorCheckType**](https://reference.aspose.com/cells/net/aspose.cells/errorchecktype), um die gewünschte Fehlerprüfung festzulegen.

## **Als Text gespeicherte Zahlen**

Gelegentlich werden Zahlen formatiert und in Zellen als Text gespeichert. Dies kann Probleme bei Berechnungen verursachen oder irreführende Sortierreihenfolgen erzeugen. Zahlen, die als Text formatiert sind, sind in der Zelle linksbündig anstelle von rechtsbündig. Wenn eine Formel, die eine mathematische Operation mit Zellen durchführen sollte, kein Ergebnis zurückgibt, überprüfen Sie die Ausrichtung in den Zellen, auf die sich die Formel bezieht - einige oder alle diese Zellen könnten als Text formatierte Zahlen sein.

Sie können die Fehlerprüfungsoptionen verwenden, um Zahlen, die als Text gespeichert sind, schnell in echte Zahlen umzuwandeln. In Microsoft Excel 2003:

1. Klicken Sie im Menü **Extras** auf **Optionen**.
1. Wählen Sie den Tab Fehlerüberprüfung aus.
   Die Option **Als Text gespeicherte Zahl** ist standardmäßig aktiviert.
1. Deaktivieren Sie es.

Der folgende Beispielcode zeigt, wie Sie die Option zur Fehlerprüfung von als Text gespeicherten Zahlen für ein Arbeitsblatt in der Vorlage XLS-Datei mithilfe der Aspose.Cells-APIs deaktivieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ErrorCheckingOptions-1.cs" >}}
