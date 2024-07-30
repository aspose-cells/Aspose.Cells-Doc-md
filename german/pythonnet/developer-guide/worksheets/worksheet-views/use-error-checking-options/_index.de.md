---
title: Verwenden von Fehlerüberprüfungsoptionen
type: docs
weight: 140
url: /de/python-net/use-error-checking-options/
description: In diesem Artikel finden Sie Beispielscode, der fehlerüberprüfende Optionen von Excel Arbeitsblättern, z.B. Zahlen als Text gespeichert, programmgesteuert mit der Aspose.Cells für Python via .NET API verwendet.
keywords: Python Excel Bibliothek, Zahlen als Text in Excel speichern, Umgang mit Fehlerprüfungsoptionen in Python.
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, Fehlerprüfoptionen und -regeln zu definieren. Benutzer sehen oft Fehlerprüfungen beim Erstellen von Formeln, ein kleines Dreieck in der oberen rechten Ecke einer Zelle markiert, wenn ein Problem mit einer Zelle vorliegt. Excel bietet Informationen, die den Benutzern helfen, häufige Probleme zu korrigieren.

{{% /alert %}}

## **Arten von Fehlern**

Fehler, die bedeuten, dass die Formel kein Ergebnis zurückgeben kann - wie beispielsweise die Division durch Null - erfordern sofortige Aufmerksamkeit, und ein Fehlerwert wird in der Zelle angezeigt. Durch Klicken auf das grüne Dreieck wird ein Ausrufezeichen angezeigt, und ein Klick darauf öffnet eine Liste von Optionen.

Der Fehler kann mithilfe der Optionen behoben oder ignoriert werden. Das Ignorieren eines Fehlers bedeutet, dass dieser bei weiteren Fehlerprüfungen nicht mehr angezeigt wird.

Aspose.Cells für Python via .NET bietet Funktionen zur Fehlerüberprüfung. Die [**ErrorCheckOption**](https://reference.aspose.com/cells/python-net/aspose.cells/errorcheckoption) Klasse verwaltet verschiedene Arten von Fehlerprüfungen, wie z.B. Zahlen als Text gespeichert, Formelberechnungsfehler und Validierungsfehler. Verwenden Sie die [**ErrorCheckType**](https://reference.aspose.com/cells/python-net/aspose.cells/errorchecktype) Aufzählung, um die gewünschte Fehlerprüfung einzurichten.

## **Als Text gespeicherte Zahlen**

Gelegentlich werden Zahlen formatiert und in Zellen als Text gespeichert. Dies kann Probleme bei Berechnungen verursachen oder irreführende Sortierreihenfolgen erzeugen. Zahlen, die als Text formatiert sind, sind in der Zelle linksbündig anstelle von rechtsbündig. Wenn eine Formel, die eine mathematische Operation mit Zellen durchführen sollte, kein Ergebnis zurückgibt, überprüfen Sie die Ausrichtung in den Zellen, auf die sich die Formel bezieht - einige oder alle diese Zellen könnten als Text formatierte Zahlen sein.

Sie können die Fehlerprüfungsoptionen verwenden, um Zahlen, die als Text gespeichert sind, schnell in echte Zahlen umzuwandeln. In Microsoft Excel 2003:

1. Klicken Sie im Menü **Extras** auf **Optionen**.
1. Wählen Sie den Fehlerüberprüfungs-Tab aus. Die Option **Zahl als Text gespeichert** ist standardmäßig aktiviert.
1. Deaktivieren Sie es.

Der folgende Beispielscode zeigt, wie die Fehlerüberprüfungsoption für Zahlen als Text für ein Arbeitsblatt in der XLS-Vorlagendatei mit den Aspose.Cells für Python via .NET APIs deaktiviert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ErrorCheckingOptions-1.py" >}}
