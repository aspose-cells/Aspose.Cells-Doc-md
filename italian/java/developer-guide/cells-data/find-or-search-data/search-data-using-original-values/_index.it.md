---
title: Cerca i dati utilizzando i valori originali
type: docs
weight: 540
url: /it/java/search-data-using-original-values/
---
{{% alert color="primary" %}} 

 A volte il valore dei dati è nascosto perché è formattato in qualche modo. Ad esempio, supponiamo che la cella D4 abbia la formula =Somma(A1:A2) e il suo valore è 20 ma è formattato come ---, quindi il valore 20 è nascosto e non può essere trovato utilizzando le opzioni di ricerca di Excel Microsoft. Tuttavia, puoi trovarlo utilizzando Aspose.Cells utilizzando[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **Cerca i dati utilizzando i valori originali**
 Il seguente codice di esempio illustra il punto precedente. Trova la cella D4 che non può essere trovata utilizzando Microsoft Opzioni di ricerca di Excel ma Aspose.Cells può trovarla utilizzando[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES). Si prega di leggere i commenti all'interno del codice per ulteriori informazioni.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **Uscita console**
Ecco l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
