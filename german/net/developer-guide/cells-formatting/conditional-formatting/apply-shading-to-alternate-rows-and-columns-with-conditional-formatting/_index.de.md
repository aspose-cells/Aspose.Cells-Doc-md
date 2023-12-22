---
title: Wenden Sie Schattierungen auf alternative Zeilen und Spalten mit bedingter Formatierung an
description: So verwenden Sie die Aspose.Cells-Bibliothek in C#, um bedingte Formatierungsschatten für abwechselnde Zeilen und Spalten anzuwenden. Durch Anpassen dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und angezeigt werden.
keywords: Aspose.Cells, Conditional Formatting, C#, Alternate Rows, Alternate Columns, Shadows
type: docs
weight: 30
url: /de/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells APIs bieten die Möglichkeit, Regeln für die bedingte Formatierung hinzuzufügen und zu bearbeiten[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Objekt. Diese Regeln können auf verschiedene Arten angepasst werden, um basierend auf Bedingungen oder Regeln die gewünschte Formatierung zu erhalten. In diesem Artikel wird die Verwendung von Aspose.Cells for .NET-APIs zum Anwenden von Schattierungen auf alternative Zeilen und Spalten mithilfe von bedingten Formatierungsregeln und den integrierten Funktionen von Excel demonstriert.

{{% /alert %}}

In diesem Artikel werden die in Excel integrierten Funktionen wie ROW, COLUMN und MOD verwendet. Hier sind einige Details dieser Funktionen zum besseren Verständnis des weiter oben bereitgestellten Codeausschnitts.

- **ROW()** Die Funktion gibt die Zeilennummer einer Zellreferenz zurück. Wenn der Referenzparameter weggelassen wird, wird davon ausgegangen, dass es sich bei der Referenz um die Zellenadresse handelt, in die die ROW-Funktion eingegeben wurde.
- **COLUMN()**Die Funktion gibt die Spaltennummer einer Zellreferenz zurück. Wenn der Referenzparameter weggelassen wird, wird davon ausgegangen, dass es sich bei der Referenz um die Zellenadresse handelt, in die die COLUMN-Funktion eingegeben wurde.
- **MOD()** Die Funktion gibt den Rest zurück, nachdem eine Zahl durch einen Teiler geteilt wurde. Dabei ist der erste Parameter der Funktion der numerische Wert, dessen Rest Sie ermitteln möchten, und der zweite Parameter ist die Zahl, die zum Teilen durch den Zahlenparameter verwendet wird. Wenn der Divisor 0 ist, wird #DIV/0 zurückgegeben! Fehler.

Beginnen wir mit dem Schreiben von Code, um dieses Ziel mithilfe von Aspose.Cells for .NET API zu erreichen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

Der folgende Schnappschuss zeigt die resultierende Tabelle, die in die Excel-Anwendung geladen wurde.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

 Um die Schattierung auf alternative Spalten anzuwenden, müssen Sie lediglich die Formel ändern**=MOD(ROW(),2)=0** als *=MOD(COLUMN(),2)=0**, das heißt; Anstatt den Zeilenindex abzurufen, ändern Sie die Formel, um den Spaltenindex abzurufen.
Die resultierende Tabelle sieht in diesem Fall wie folgt aus.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
