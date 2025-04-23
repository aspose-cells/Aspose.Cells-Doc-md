---
title: Cerca dati utilizzando valori originali
type: docs
weight: 380
url: /it/net/search-data-using-original-values/
description: Scopri come cercare dati utilizzando valori originali tramite l API Aspose.Cells for .NET.
keywords: Cerca dati utilizzando valori originali, Trova dati utilizzando valori originali, Cerca dati per valori originali, Trova dati per valori originali
---

{{% alert color="primary" %}}

A volte il valore dei dati è nascosto perché è formattato in qualche modo. Ad esempio, supponiamo che la cella D4 abbia la formula =Somma(A1:A2) e il suo valore sia 20 ma è formattato come ---, quindi il valore 20 è nascosto e non può essere trovato utilizzando le opzioni di ricerca di Microsoft Excel. Tuttavia, puoi trovarlo utilizzando Aspose.Cells utilizzando [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

Il seguente codice di esempio illustra il punto sopra. Trova la cella D4 che non può essere trovata utilizzando le opzioni di ricerca di Microsoft Excel ma Aspose.Cells può trovarla utilizzando [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype). Si prega di leggere i commenti all'interno del codice per ulteriori informazioni.

## Codice C# per cercare dati utilizzando valori originali

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## Output della console generato dall'esempio di codice

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
