---
title: Schattierung auf abwechselnden Zeilen und Spalten mit bedingter Formatierung anwenden
linktitle: Schattierung auf abwechselnden Zeilen und Spalten mit bedingter Formatierung anwenden
description: Wie man die Aspose.Cells Bibliothek in Node.js via C++ verwendet, um Bedingte Formatierungs Schatten für abwechselnde Zeilen und Spalten anzuwenden. Durch Anpassen dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Bedingte Formatierung, Schatten, Node.js via C++, abwechselnde Zeilen, abwechselnde Spalten
type: docs
weight: 30
url: /de/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells APIs bieten die Möglichkeit, Bedingte Formatierungsregeln für das [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Objekt hinzuzufügen und zu manipulieren. Diese Regeln können auf vielfältige Weise angepasst werden, um die gewünschte Formatierung basierend auf Bedingungen oder Regeln zu erhalten. Dieser Artikel demonstriert die Verwendung der APIs Aspose.Cells for Node.js via C++, um Schattierungen auf abwechselnde Zeilen & Spalten mit Hilfe von Bedingter Formatierung und den integrierten Funktionen von Excel anzuwenden.

{{% /alert %}}

Dieser Artikel verwendet integrierte Funktionen von Excel wie ROW, COLUMN & MOD. Hier sind einige Details zu diesen Funktionen, um das Code-Snippet, das im Folgenden bereitgestellt wird, besser zu verstehen.

- **ROW()** Funktion gibt die Zeilennummer eines Zellbezugs zurück. Wenn der Referenzparameter weggelassen wird, wird angenommen, dass sich die Referenz auf die Zellenadresse bezieht, in die die ROW-Funktion eingegeben wurde.
- **COLUMN()** Funktion gibt die Spaltennummer eines Zellbezugs zurück. Wenn der Referenzparameter weggelassen wird, wird angenommen, dass sich die Referenz auf die Zellenadresse bezieht, in die die COLUMN-Funktion eingegeben wurde.
- Die **MOD()**-Funktion gibt den Rest nach der Division einer Zahl durch einen Divisor zurück, wobei der erste Parameter der numerische Wert ist, von dem Sie den Rest finden möchten, und der zweite Parameter die Zahl ist, durch die die Nummernparameter dividiert werden. Wenn der Divisor 0 ist, wird der Fehler #DIV/0! zurückgegeben.

Beginnen wir mit dem Schreiben von Code, um dieses Ziel mithilfe der API Aspose.Cells for Node.js via C++ zu erreichen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyShadingToAlternateRowsAndColumns.js" >}}


Die folgende Momentaufnahme zeigt die resultierende Tabelle, die in der Excel-Anwendung geladen wird.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Um die Schattierung auf alternative Spalten anzuwenden, müssen Sie lediglich die Formel **=MOD(ZEILE(),2)=0** durch **=MOD(SPALTE(),2)=0** ersetzen, d.h. anstatt den Zeilenindex zu erhalten, ändern Sie die Formel, um den Spaltenindex abzurufen.  
Die resultierende Tabelle wird in diesem Fall folgendermaßen aussehen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="nodejs-cpp" >}}
