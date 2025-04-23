---  
title: Cerca dati utilizzando valori originali
type: docs  
weight: 380  
url: /it/nodejs-cpp/search-data-using-original-values/  
description: Impara come cercare dati usando valori originali tramite l’API Aspose.Cells for Node.js via C++.  
keywords: Ricerca dati usando valori originali Node.js tramite C++, Trova dati usando valori originali Node.js tramite C++, Ricerca dati tramite valori originali Node.js tramite C++, Trova dati tramite valori originali Node.js tramite C++  
---  

{{% alert color="primary" %}}  

A volte il valore dei dati è nascosto perché è formattato in qualche modo. Ad esempio, supponiamo che la cella D4 abbia la formula =Somma(A1:A2) e il suo valore sia 20 ma è formattato come ---, quindi il valore 20 è nascosto e non può essere trovato utilizzando le opzioni di ricerca di Microsoft Excel. Tuttavia, puoi trovarlo utilizzando Aspose.Cells utilizzando [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype)  

{{% /alert %}}  

Il seguente codice di esempio illustra il punto sopra. Trova la cella D4 che non può essere trovata utilizzando le opzioni di ricerca di Microsoft Excel ma Aspose.Cells può trovarla utilizzando [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype). Si prega di leggere i commenti all'interno del codice per ulteriori informazioni.  

## Codice Node.js per cercare dati usando valori originali  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchDataUsingOriginalValues.js" >}}


## Output della console generato dall'esempio di codice  

Ecco l'output della console del codice di esempio sopra.  

{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}  

