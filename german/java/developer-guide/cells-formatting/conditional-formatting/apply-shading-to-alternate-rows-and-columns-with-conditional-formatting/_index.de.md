---
title: Schattierung auf abwechselnden Zeilen und Spalten mit bedingter Formatierung anwenden
type: docs
weight: 10
url: /de/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells APIs bieten die Möglichkeit, bedingte Formatierungsregeln für das [Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) zu hinzuzufügen und zu manipulieren. Diese Regeln können in vielerlei Hinsicht angepasst werden, um die gewünschte Formatierung basierend auf Bedingungen oder Regeln zu erhalten. Dieser Artikel wird die Verwendung der Aspose.Cells for Java API zur Anwendung von Schattierung auf alternative Zeilen und Spalten mithilfe von bedingten Formatierungsregeln und den integrierten Funktionen von Excel zeigen.

{{% /alert %}} 
## **Anwendung von Schattierung auf alternative Zeilen & Spalten mithilfe bedingter Formatierung**
Dieser Artikel verwendet integrierte Funktionen von Excel wie ZEILE, SPALTE & REST. Hier sind einige Details dieser Funktionen zur besseren Verständnis des vorangehenden Codes.

- Die **ZEILE()**-Funktion gibt die Zeilennummer einer Zellreferenz zurück. Wenn die Referenz ausgelassen wird, nimmt sie an, dass die Referenz die Zelladresse ist, in die die ZEILE-Funktion eingegeben wurde.
- Die **SPALTE()**-Funktion gibt die Spaltennummer einer Zellreferenz zurück. Wenn die Referenz ausgelassen wird, nimmt sie an, dass die Referenz die Zelladresse ist, in die die SPALTE-Funktion eingegeben wurde.
- Die **MOD()**-Funktion gibt den Rest nach der Division einer Zahl durch einen Divisor zurück, wobei der erste Parameter der numerische Wert ist, von dem Sie den Rest finden möchten, und der zweite Parameter die Zahl ist, durch die die Nummernparameter dividiert werden. Wenn der Divisor 0 ist, wird der Fehler #DIV/0! zurückgegeben.

Lassen Sie uns einige Codezeilen schreiben, um das Ziel mithilfe der Aspose.Cells for Java API zu erreichen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



Die folgende Momentaufnahme zeigt die resultierende Tabelle, die in der Excel-Anwendung geladen wird.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

Um die Schattierung auf alternative Spalten anzuwenden, müssen Sie lediglich die Formel **=MOD(ZEILE(),2)=0** durch **=MOD(SPALTE(),2)=0** ersetzen, d.h. anstatt den Zeilenindex zu erhalten, ändern Sie die Formel, um den Spaltenindex abzurufen. 
Die resultierende Tabelle sieht in diesem Fall wie das folgende Bild aus.

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
