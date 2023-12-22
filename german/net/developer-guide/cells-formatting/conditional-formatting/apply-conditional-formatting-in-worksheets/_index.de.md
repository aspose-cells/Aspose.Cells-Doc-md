---
title: Wenden Sie bedingte Formatierung in Arbeitsblättern an
description: So verwenden Sie die Bibliothek Aspose.Cells in C#, um bedingte Formatierung in Arbeitsblättern anzuwenden. Durch Anpassen dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und angezeigt werden.
keywords: Aspose.Cells, Conditional Formatting, C#, Worksheet, Formatting
type: docs
weight: 130
url: /de/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Dieser Artikel soll ein detailliertes Verständnis dafür vermitteln, wie man einer Reihe von Zellen in einem Arbeitsblatt eine bedingte Formatierung hinzufügt.

Die bedingte Formatierung ist eine erweiterte Funktion in Microsoft Excel, mit der Sie Formate auf einen Bereich von Zellen anwenden und diese Formatierung abhängig vom Wert der Zelle oder dem Wert einer Formel ändern können. Beispielsweise kann der Hintergrund einer Zelle rot sein, um einen negativen Wert hervorzuheben, oder die Textfarbe könnte grün sein, um einen positiven Wert hervorzuheben. Wenn der Wert der Zelle die Formatbedingung erfüllt, wird das Format angewendet. Wenn der Wert der Zelle die Formatbedingung nicht erfüllt, wird die Standardformatierung der Zelle verwendet.

Es ist möglich, bedingte Formatierung mit Microsoft Office Automation anzuwenden, aber das hat seine Nachteile. Es gibt mehrere Gründe und Probleme: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit. Der Hauptgrund für die Suche nach einer anderen Lösung ist, dass Microsoft selbst dringend von Office Automation für Softwarelösungen abrät.

In diesem Artikel wird gezeigt, wie Sie mit ein paar einfachen Codezeilen mithilfe von Aspose.Cells API eine Konsolenanwendung erstellen und bedingte Formatierung für Zellen hinzufügen.

{{% /alert %}}

##  **Verwenden von Aspose.Cells zum Anwenden einer bedingten Formatierung basierend auf dem Wert Cell**

1. *Laden Sie Aspose.Cells herunter und installieren Sie es**.
 1. Laden Sie Aspose.Cells for .NET herunter.
1. Installieren Sie es auf Ihrem Entwicklungscomputer.
 Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Auswertungsmodus ist zeitlich unbegrenzt und fügt lediglich Wasserzeichen in erstellte Dokumente ein.
1. *Erstellen Sie ein Projekt**.
 Starten Sie Visual Studio.NET und erstellen Sie eine neue Konsolenanwendung. In diesem Beispiel wird eine Konsolenanwendung C# erstellt, Sie können jedoch auch VB.NET verwenden.
1. *Referenzen hinzufügen**.
 Fügen Sie Ihrem Projekt einen Verweis auf Aspose.Cells hinzu, beispielsweise einen Verweis auf ….\Programme\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. *Wenden Sie eine bedingte Formatierung basierend auf dem Zellenwert an.
Unten finden Sie den Code, der zum Ausführen der Aufgabe verwendet wird. Ich wende bedingte Formatierung auf eine Zelle an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle „A1“ im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die auf A1 angewendete bedingte Formatierung hängt vom Zellenwert ab. Wenn der Zellenwert von A1 zwischen 50 und 100 liegt, ist die Hintergrundfarbe aufgrund der angewendeten bedingten Formatierung rot.

##  **Verwenden von Aspose.Cells zum Anwenden einer bedingten Formatierung basierend auf einer Formel**

1. Bedingte Formatierung abhängig von der Formel anwenden (Code-Snippet)
 Unten finden Sie den Code zum Ausführen der Aufgabe. Es wendet die bedingte Formatierung auf B3 an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

Wenn der obige Code ausgeführt wird, wird die bedingte Formatierung auf die Zelle „B3“ im ersten Arbeitsblatt der Ausgabedatei (output.xls) angewendet. Die angewendete bedingte Formatierung hängt von der Formel ab, die den Wert von „B3“ als Summe von B1 und B2 berechnet.
