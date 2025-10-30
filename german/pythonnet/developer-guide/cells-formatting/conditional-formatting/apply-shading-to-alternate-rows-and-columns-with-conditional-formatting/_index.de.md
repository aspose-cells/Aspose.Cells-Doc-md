---
title: Schattierung auf abwechselnden Zeilen und Spalten mit bedingter Formatierung anwenden
description: Wie man die Aspose.Cells Bibliothek in Python benutzt, um Schatten bei bedingter Formatierung für wechselnde Zeilen und Spalten anzuwenden. Durch die Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie die Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Bedingte Formatierung, Python Alternierende Zeilen, Alternierende Spalten, Schatten
type: docs
weight: 30
url: /de/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET APIs bieten die Möglichkeit, bedingte Formatierungsregeln für das [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) Objekt hinzuzufügen und zu bearbeiten. Diese Regeln können auf vielerlei Weise angepasst werden, um die gewünschte Formatierung anhand von Bedingungen oder Regeln zu erzielen. Dieser Artikel zeigt die Verwendung der Aspose.Cells für Python via .NET APIs, um mit Hilfe von bedingten Formatierungsregeln und integrierten Excel-Funktionen Schattierungen auf alternierende Zeilen & Spalten anzuwenden.

{{% /alert %}}

Dieser Artikel verwendet integrierte Funktionen von Excel wie ROW, COLUMN & MOD. Hier sind einige Details zu diesen Funktionen, um das Code-Snippet, das im Folgenden bereitgestellt wird, besser zu verstehen.

- Die **ROW()**-Funktion gibt die Zeilennummer einer Zellreferenz zurück. Wenn der Referenzparameter ausgelassen wird, nimmt die Funktion an, dass die Referenz die Zelladresse ist, in die die ROW-Funktion eingegeben wurde.
- Die **COLUMN()**-Funktion gibt die Spaltennummer einer Zellreferenz zurück. Wenn der Referenzparameter ausgelassen wird, nimmt die Funktion an, dass die Referenz die Zelladresse ist, in die die COLUMN-Funktion eingegeben wurde.
- Die **MOD()**-Funktion gibt den Rest nach der Division einer Zahl durch einen Divisor zurück, wobei der erste Parameter der numerische Wert ist, von dem Sie den Rest finden möchten, und der zweite Parameter die Zahl ist, durch die die Nummernparameter dividiert werden. Wenn der Divisor 0 ist, wird der Fehler #DIV/0! zurückgegeben.

Lassen Sie uns mit der Programmierung beginnen, um dieses Ziel mithilfe der Aspose.Cells für Python via .NET API zu erreichen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyShadingToAlternateRowsColumns-1.py" >}}

Die folgende Momentaufnahme zeigt die resultierende Tabelle, die in der Excel-Anwendung geladen wird.

|![todo:image_alt_text](1.png)|
| :- |

Um die Schattierung auf alternative Spalten anzuwenden, müssen Sie lediglich die Formel **=MOD(ZEILE(),2)=0** durch **=MOD(SPALTE(),2)=0** ersetzen, d.h. anstatt den Zeilenindex zu erhalten, ändern Sie die Formel, um den Spaltenindex abzurufen. 
Die resultierende Tabelle wird in diesem Fall folgendermaßen aussehen.

|![todo:image_alt_text](2.png)|
| :- |

{{< app/cells/assistant language="python-net" >}}
