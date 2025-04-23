---
title: Schattierung auf abwechselnden Zeilen und Spalten mit bedingter Formatierung anwenden
description: Wie man die Aspose.Cells Bibliothek in C# verwendet, um bedingte Formatierungsschatten für abwechselnde Zeilen und Spalten anzuwenden. Durch Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Bedingte Formatierung, C#, Abwechselnde Zeilen, Abwechselnde Spalten, Schatten
type: docs
weight: 30
url: /de/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells-APIs bieten die Möglichkeit, bedingte Formatierungsregeln für das [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Objekt hinzuzufügen und zu manipulieren. Diese Regeln können auf verschiedene Weise angepasst werden, um basierend auf Bedingungen oder Regeln die gewünschte Formatierung zu erhalten. Dieser Artikel wird die Verwendung von Aspose.Cells for .NET-APIs demonstrieren, um mit Hilfe von bedingten Formatierungsregeln und den integrierten Funktionen von Excel Schattierungen auf abwechselnde Zeilen und Spalten anzuwenden.

{{% /alert %}}

Dieser Artikel verwendet integrierte Funktionen von Excel wie ROW, COLUMN & MOD. Hier sind einige Details zu diesen Funktionen, um das Code-Snippet, das im Folgenden bereitgestellt wird, besser zu verstehen.

- Die **ROW()**-Funktion gibt die Zeilennummer einer Zellreferenz zurück. Wenn der Referenzparameter ausgelassen wird, nimmt die Funktion an, dass die Referenz die Zelladresse ist, in die die ROW-Funktion eingegeben wurde.
- Die **COLUMN()**-Funktion gibt die Spaltennummer einer Zellreferenz zurück. Wenn der Referenzparameter ausgelassen wird, nimmt die Funktion an, dass die Referenz die Zelladresse ist, in die die COLUMN-Funktion eingegeben wurde.
- Die **MOD()**-Funktion gibt den Rest nach der Division einer Zahl durch einen Divisor zurück, wobei der erste Parameter der numerische Wert ist, von dem Sie den Rest finden möchten, und der zweite Parameter die Zahl ist, durch die die Nummernparameter dividiert werden. Wenn der Divisor 0 ist, wird der Fehler #DIV/0! zurückgegeben.

Lassen Sie uns damit beginnen, etwas Code zu schreiben, um dieses Ziel mit Hilfe der Aspose.Cells for .NET-API zu erreichen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

Die folgende Momentaufnahme zeigt die resultierende Tabelle, die in der Excel-Anwendung geladen wird.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Um die Schattierung auf alternative Spalten anzuwenden, müssen Sie lediglich die Formel **=MOD(ZEILE(),2)=0** durch **=MOD(SPALTE(),2)=0** ersetzen, d.h. anstatt den Zeilenindex zu erhalten, ändern Sie die Formel, um den Spaltenindex abzurufen. 
Die resultierende Tabelle wird in diesem Fall folgendermaßen aussehen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="csharp" >}}
