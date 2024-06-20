---
title: Daten mithilfe der Originalwerte suchen
type: docs
weight: 540
url: /de/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

Manchmal ist der Wert der Daten verborgen, weil sie auf bestimmte Weise formatiert sind. Nehmen wir zum Beispiel an, dass die Zelle D4 die Formel =Sum(A1:A2) hat und ihr Wert 20 ist, aber sie ist als --- formatiert, dann ist der Wert 20 verborgen und kann nicht mit den Suchoptionen von Microsoft Excel gefunden werden. Sie können ihn jedoch mit Aspose.Cells unter Verwendung von [LookInType.ORIGINAL_VALUES] (https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES) finden.

{{% /alert %}} 
## **Daten mithilfe der Originalwerte suchen**
Der folgende Beispielcode veranschaulicht den obigen Punkt. Er findet die Zelle D4, die mit den Suchoptionen von Microsoft Excel nicht gefunden werden kann, aber Aspose.Cells kann sie mit [LookInType.ORIGINAL_VALUES] (https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES) finden. Bitte lesen Sie die Kommentare innerhalb des Codes für weitere Informationen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
