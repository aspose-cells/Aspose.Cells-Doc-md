---
title: Cerca dati utilizzando valori originali
type: docs
weight: 540
url: /it/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

A volte il valore dei dati è nascosto perché è formattato in qualche modo. Per esempio, supponi che la cella D4 abbia la formula =Sum(A1:A2) e il suo valore sia 20 ma sia formattata come ---, allora il valore 20 è nascosto e non può essere trovato usando le opzioni di ricerca di Microsoft Excel. Tuttavia, puoi trovarlo usando Aspose.Cells usando [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES)

{{% /alert %}} 
## **Cerca dati usando valori originali**
Il codice di esempio seguente illustra il punto sopra. Trova la cella D4 che non può essere trovata usando le opzioni di ricerca di Microsoft Excel ma Aspose.Cells può trovarla usando [LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL-VALUES). Si prega di leggere i commenti all'interno del codice per ulteriori informazioni.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Output della console**
Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
