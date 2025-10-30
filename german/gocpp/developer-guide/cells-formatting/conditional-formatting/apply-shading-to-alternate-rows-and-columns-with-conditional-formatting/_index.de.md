---
title: Schattierung abwechselnder Zeilen und Spalten mit bedingter Formatierung mit Golang über C++
linktitle: Schattierung abwechselnder Zeilen und Spalten anwenden
description: So verwenden Sie die Aspose.Cells Bibliothek in C++, um Schatten für abwechselnde Zeilen und Spalten mit bedingter Formatierung anzuwenden. Durch die Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Bedingte Formatierung, C++, Abwechselnde Zeilen, Abwechselnde Spalten, Schatten
type: docs
weight: 30
url: /de/go-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Die Aspose.Cells-APIs bieten die Möglichkeit, bedingte Formatierungsregeln für das [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/)-Objekt hinzuzufügen und zu manipulieren. Diese Regeln können auf vielfältige Weise angepasst werden, um das gewünschte Format basierend auf Bedingungen oder Regeln zu erzielen. Dieser Artikel zeigt die Verwendung der APIs mit der Nummer Aspose.Cells for C++, um Schattierungen für abwechselnde Zeilen & Spalten mithilfe bedingter Formatierungsregeln und Excel-Funktionen anzuwenden.

{{% /alert %}}

Dieser Artikel verwendet integrierte Funktionen von Excel wie ROW, COLUMN & MOD. Hier sind einige Details zu diesen Funktionen, um das Code-Snippet, das im Folgenden bereitgestellt wird, besser zu verstehen.

- Die **ROW()**-Funktion gibt die Zeilennummer einer Zellreferenz zurück. Wenn der Referenzparameter ausgelassen wird, nimmt die Funktion an, dass die Referenz die Zelladresse ist, in die die ROW-Funktion eingegeben wurde.
- Die **COLUMN()**-Funktion gibt die Spaltennummer einer Zellreferenz zurück. Wenn der Referenzparameter ausgelassen wird, nimmt die Funktion an, dass die Referenz die Zelladresse ist, in die die COLUMN-Funktion eingegeben wurde.
- Die **MOD()**-Funktion gibt den Rest nach der Division einer Zahl durch einen Divisor zurück, wobei der erste Parameter der numerische Wert ist, von dem Sie den Rest finden möchten, und der zweite Parameter die Zahl ist, durch die die Nummernparameter dividiert werden. Wenn der Divisor 0 ist, wird der Fehler #DIV/0! zurückgegeben.

Lassen Sie uns mit der Verwendung der API Aspose.Cells for C++ beginnen, um dieses Ziel zu erreichen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyShadingToAlternateRowsAndColumnsWithConditionalFormatting.go" >}}
Die folgende Momentaufnahme zeigt die resultierende Tabelle, die in der Excel-Anwendung geladen wird.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Um die Schattierung auf alternative Spalten anzuwenden, müssen Sie lediglich die Formel **=MOD(ZEILE(),2)=0** durch **=MOD(SPALTE(),2)=0** ersetzen, d.h. anstatt den Zeilenindex zu erhalten, ändern Sie die Formel, um den Spaltenindex abzurufen. 
Die resultierende Tabelle wird in diesem Fall folgendermaßen aussehen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
