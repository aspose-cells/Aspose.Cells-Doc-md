---
title: Wenden Sie Schattierung auf abwechselnde Zeilen und Spalten mit bedingter Formatierung an
type: docs
weight: 10
url: /de/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells APIs bieten die Möglichkeit, bedingte Formatierungsregeln hinzuzufügen und zu manipulieren[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Objekt. Diese Regeln können auf verschiedene Weise angepasst werden, um die gewünschte Formatierung basierend auf Bedingungen oder Regeln zu erhalten. Dieser Artikel demonstriert die Verwendung von Aspose.Cells for Java API zum Anwenden von Schattierungen auf abwechselnde Zeilen und Spalten mithilfe von Regeln für die bedingte Formatierung und den integrierten Funktionen von Excel.

{{% /alert %}} 
## **Wenden Sie mithilfe der bedingten Formatierung eine Schattierung auf abwechselnde Zeilen und Spalten an**
Dieser Artikel nutzt die integrierten Funktionen von Excel wie ROW, COLUMN & MOD. Hier sind kleine Details dieser Funktionen zum besseren Verständnis des Code-Snippets, das im Voraus bereitgestellt wird.

- **DIE ZEILE()** Funktion gibt die Zeilennummer eines Zellbezugs zurück. Wenn die Referenz weggelassen wird, wird davon ausgegangen, dass die Referenz die Zellenadresse ist, in die die ROW-Funktion eingegeben wurde.
- **SÄULE()**Funktion gibt die Spaltennummer eines Zellbezugs zurück. Wenn die Referenz weggelassen wird, wird davon ausgegangen, dass die Referenz die Zellenadresse ist, in die die COLUMN-Funktion eingegeben wurde.
- **MOD()** Die Funktion gibt den Rest zurück, nachdem eine Zahl durch einen Divisor geteilt wurde, wobei der erste Parameter der Funktion der numerische Wert ist, dessen Rest Sie finden möchten, und der zweite Parameter die Zahl ist, die zum Teilen in den Zahlenparameter verwendet wird. Wenn der Divisor 0 ist, wird #DIV/0 zurückgegeben! Error.

Beginnen wir mit dem Schreiben von Code, um das Ziel mit Hilfe von Aspose.Cells for Java API zu erreichen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



Der folgende Schnappschuss zeigt die resultierende Tabelle, die in die Excel-Anwendung geladen wurde.

![todo: Bild_alt_Text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

 Um die Schattierung auf alternative Spalten anzuwenden, müssen Sie lediglich die Formel ändern**=MOD(ZEILE(),2)=0** wie**=MOD(SPALTE(),2)=0** , das ist; Anstatt den Zeilenindex abzurufen, ändern Sie die Formel, um den Spaltenindex abzurufen.
Die resultierende Tabelle sieht in diesem Fall wie in der folgenden Abbildung aus.

![todo: Bild_alt_Text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
