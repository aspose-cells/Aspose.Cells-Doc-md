---
title: Verwenden Sie die Optionen zur Fehlerprüfung
type: docs
weight: 140
url: /de/net/use-error-checking-options/
---
{{% alert color="primary" %}}

Microsoft Mit Excel können Benutzer Optionen und Regeln für die Fehlerprüfung definieren. Benutzer sehen beim Erstellen von Formeln häufig Fehlerprüfungen. Ein kleines Dreieck in der oberen rechten Ecke einer Zelle hebt hervor, wenn ein Problem mit einer Zelle vorliegt. Excel stellt Informationen bereit, die Benutzern helfen, allgemeine Probleme zu beheben.

{{% /alert %}}

## **Arten von Fehlern**

Fehler, die dazu führen, dass die Formel kein Ergebnis zurückgeben kann – wie z. B. das Teilen einer Zahl durch Null – erfordern sofortige Aufmerksamkeit, und in der Zelle wird ein Fehlerwert angezeigt. Ein Klick auf das grüne Dreieck zeigt ein Ausrufezeichen, ein Klick darauf öffnet eine Liste mit Optionen.

Der Fehler kann mit den Optionen behoben oder ignoriert werden. Das Ignorieren eines Fehlers bedeutet, dass dieser Fehler bei weiteren Fehlerprüfungen nicht angezeigt wird.

Aspose.Cells bietet Optionen zur Fehlerprüfung. Das[**ErrorCheckOption**](https://reference.aspose.com/cells/net/aspose.cells/errorcheckoption) Die Klasse verwaltet verschiedene Arten von Fehlerprüfungen, z. B. als Text gespeicherte Zahlen, Formelberechnungsfehler und Validierungsfehler. Verwenden Sie die[**ErrorCheckType**](https://reference.aspose.com/cells/net/aspose.cells/errorchecktype)Enumeration, um die gewünschte Fehlerprüfung einzustellen.

## **Als Text gespeicherte Zahlen**

Gelegentlich können Zahlen formatiert und in Zellen als Text gespeichert werden. Dies kann zu Berechnungsproblemen oder verwirrenden Sortierreihenfolgen führen. Als Text formatierte Zahlen werden in der Zelle linksbündig statt rechtsbündig ausgerichtet. Wenn eine Formel, die eine mathematische Operation an Zellen ausführen soll, keinen Wert zurückgibt, überprüfen Sie die Ausrichtung in den Zellen, auf die sich die Formel bezieht – einige oder alle dieser Zellen könnten Zahlen sein, die als Text formatiert sind.

Sie können die Fehlerprüfungsoptionen verwenden, um als Text gespeicherte Zahlen schnell in reelle Zahlen umzuwandeln. In Microsoft Excel 2003:

1.  Auf der**Werkzeug** Menü, klicken**Optionen**.
1. Wählen Sie die Registerkarte Fehlerprüfung.
   **Nummer als Text gespeichert** Option ist standardmäßig aktiviert.
1. Deaktivieren Sie es.

Der folgende Beispielcode zeigt, wie die als Textfehlerprüfungsoption für ein Arbeitsblatt in der Vorlagen-XLS-Datei gespeicherten Zahlen mithilfe der Aspose.Cells-APIs deaktiviert werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ErrorCheckingOptions-1.cs" >}}
