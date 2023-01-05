---
title: Wenden Sie bedingte Formatierung in Arbeitsblättern an
type: docs
weight: 130
url: /de/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Dieser Artikel soll ein detailliertes Verständnis dafür vermitteln, wie Sie einer Reihe von Zellen in einem Arbeitsblatt eine bedingte Formatierung hinzufügen.

Die bedingte Formatierung ist eine erweiterte Funktion in Microsoft Excel, mit der Sie Formate auf einen Bereich von Zellen anwenden und diese Formatierung abhängig vom Wert der Zelle oder dem Wert einer Formel ändern können. Beispielsweise kann der Hintergrund einer Zelle rot sein, um einen negativen Wert hervorzuheben, oder die Textfarbe könnte für einen positiven Wert grün sein. Wenn der Wert der Zelle die Formatbedingung erfüllt, wird das Format angewendet. Wenn der Wert der Zelle die Formatbedingung nicht erfüllt, wird die Standardformatierung der Zelle verwendet.

Es ist möglich, bedingte Formatierung mit Microsoft Office Automation anzuwenden, aber das hat seine Nachteile. Dafür gibt es mehrere Gründe und Probleme: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit. Der Hauptgrund für die Suche nach einer anderen Lösung ist, dass Microsoft selbst dringend von Office Automation für Softwarelösungen abrät.

Dieser Artikel zeigt, wie Sie eine Konsolenanwendung erstellen und Zellen mit ein paar einfachsten Codezeilen mit Aspose.Cells API bedingt formatieren.

{{% /alert %}}

## **Verwenden von Aspose.Cells zum Anwenden einer bedingten Formatierung basierend auf dem Wert von Cell**

1. **Laden Sie Aspose.Cells herunter und installieren Sie es**.
 1. Laden Sie Aspose.Cells for .NET herunter.
1. Installieren Sie es auf Ihrem Entwicklungscomputer.
Alle Aspose-Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein.
1. **Erstellen Sie ein Projekt**.
 Starten Sie Visual Studio.NET und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel erstellt eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden.
1. **Referenzen hinzufügen**.
 Fügen Sie Ihrem Projekt einen Verweis auf Aspose.Cells hinzu, z. B. einen Verweis auf ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. * Wenden Sie eine bedingte Formatierung basierend auf dem Zellenwert an.
 Nachfolgend finden Sie den Code, der zum Ausführen der Aufgabe verwendet wird. Ich wendet eine bedingte Formatierung auf eine Zelle an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle „A1“ im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die auf A1 angewendete bedingte Formatierung hängt vom Zellenwert ab. Wenn der Zellenwert von A1 zwischen 50 und 100 liegt, ist die Hintergrundfarbe aufgrund der angewendeten bedingten Formatierung rot.

## **Verwenden von Aspose.Cells zum Anwenden einer bedingten Formatierung basierend auf einer Formel**

1. Bedingte Formatierung je nach Formel anwenden (Code Snippet)
 Unten ist der Code, um die Aufgabe zu erfüllen. Es wendet die bedingte Formatierung auf B3 an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle „B3“ im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die angewendete bedingte Formatierung hängt von der Formel ab, die den Wert von „B3“ als Summe von B1 & B2 berechnet.
