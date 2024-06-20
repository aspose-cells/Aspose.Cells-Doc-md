---
title: Accesso e Modifica del Valore della Cella
type: docs
weight: 20
url: /it/net/aspose-cells-gridweb/access-and-modify-cell-value/
keywords: GridWeb, valore della cella, modifica, valore
description: Questo articolo introduce come ottenere e modificare il valore della cella in GridWeb.
---

{{% alert color="primary" %}} 

[Accesso alle celle del foglio di lavoro](/cells/it/net/aspose-cells-gridweb/access-worksheet-cells/) discute l'accesso alle celle. Questo argomento estende quella discussione per mostrare come accedere e modificare i valori delle celle utilizzando l'API Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Accesso e modifica del valore di una cella**
### **Valori stringa**
Prima di accedere e modificare il valore di una cella, è necessario sapere come accedere alle celle. Per ulteriori dettagli sui diversi approcci per accedere alle celle, fare riferimento all'articolo [Accesso alle celle del foglio di lavoro](/cells/it/net/aspose-cells-gridweb/access-worksheet-cells/).

Ogni cella ha una proprietà chiamata StringValue. Una volta che una cella viene acceduta, gli sviluppatori possono utilizzare la proprietà StringValue per accedere al valore di stringa delle celle. Per modificare i valori delle celle è fornito un metodo speciale PutValue, che può essere utilizzato per aggiornare il valore di stringa della cella.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Tutti i tipi di valori**
Il metodo PutValue di un oggetto cella ha a disposizione 8 sovraccarichi che possono essere utilizzati per modificare qualsiasi tipo di valore (Boolean, int, double, DateTime e stringa) in una cella.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



C'è anche una versione sovraccaricata del metodo PutValue che può prendere qualsiasi tipo di valore in formato stringa e convertirlo automaticamente in un tipo di dati appropriato. Per farlo accadere, passare il valore Booleano true a un altro parametro del metodo PutValue come mostrato di seguito nell'esempio.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
