---
title: Accedi e modifica i valori Cell
type: docs
weight: 20
url: /it/net/access-and-modify-cell-values/
---
{{% alert color="primary" %}} 

[Accedi al foglio di lavoro Cells](/cells/it/net/access-worksheet-cells/) discusso l'accesso alle celle. Questo argomento estende tale discussione per mostrare come accedere e modificare i valori delle celle utilizzando Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Accesso e modifica del valore di un Cell**
### **Valori stringa**
 Prima di accedere e modificare il valore di una cella, è necessario sapere come accedere alle celle. Per dettagli sui diversi approcci per l'accesso alle celle, fare riferimento a[Accedi al foglio di lavoro Cells](/cells/it/net/access-worksheet-cells/).

Ogni cella ha una proprietà denominata StringValue. Una volta effettuato l'accesso a una cella, gli sviluppatori possono utilizzare la proprietà StringValue per accedere al valore della stringa della cella. Per modificare i valori delle celle, viene fornito un metodo speciale PutValue, che può essere utilizzato per aggiornare il valore della stringa della cella.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Tutti i tipi di valori**
Il metodo PutValue dell'oggetto di una cella dispone di 8 sovraccarichi che possono essere utilizzati per modificare qualsiasi tipo di valore (booleano, int, double, DateTime e stringa) in una cella.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



Esiste anche una versione sovraccaricata del metodo PutValue che può accettare qualsiasi tipo di valore in formato stringa e convertirlo automaticamente in un tipo di dati appropriato. Per realizzarlo, passa il valore booleano true a un altro parametro del metodo PutValue come mostrato di seguito nell'esempio.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
