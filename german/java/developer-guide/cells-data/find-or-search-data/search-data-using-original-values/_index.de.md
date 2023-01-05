---
title: Suchen Sie Daten mit Originalwerten
type: docs
weight: 540
url: /de/java/search-data-using-original-values/
---
{{% alert color="primary" %}} 

 Manchmal ist der Wert der Daten verborgen, weil sie auf irgendeine Weise formatiert sind. Angenommen, Zelle D4 hat die Formel =Sum(A1:A2) und ihr Wert ist 20, aber formatiert als ---, dann ist der Wert 20 ausgeblendet und kann nicht mit den Microsoft-Excel-Suchoptionen gefunden werden. Sie können es jedoch mit Aspose.Cells finden[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **Suchen Sie Daten mit Originalwerten**
 Der folgende Beispielcode veranschaulicht den obigen Punkt. Es findet Zelle D4, die nicht mit Microsoft Excel-Suchoptionen gefunden werden kann, aber Aspose.Cells kann sie mit finden[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). Bitte lesen Sie die Kommentare im Code für weitere Informationen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
