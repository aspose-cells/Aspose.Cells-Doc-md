---
title: Cerca i dati utilizzando i valori originali
type: docs
weight: 380
url: /it/net/search-data-using-original-values/
---
{{% alert color="primary" %}}

 A volte il valore dei dati è nascosto perché è formattato in qualche modo. Ad esempio, supponiamo che la cella D4 abbia la formula =Somma(A1:A2) e il suo valore è 20 ma è formattato come ---, quindi il valore 20 è nascosto e non può essere trovato utilizzando le opzioni di ricerca di Excel Microsoft. Tuttavia, puoi trovarlo utilizzando Aspose.Cells utilizzando[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

 Il seguente codice di esempio illustra il punto precedente. Trova la cella D4 che non può essere trovata utilizzando Microsoft Opzioni di ricerca di Excel ma Aspose.Cells può trovarla utilizzando[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Si prega di leggere i commenti all'interno del codice per ulteriori informazioni.

## C# codice per cercare i dati utilizzando i valori originali

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Output della console generato dal codice di esempio

Ecco l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
