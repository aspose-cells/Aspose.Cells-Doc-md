---
title: Impostazione Formula Condivisa
type: docs
weight: 10
url: /it/net/setting-shared-formula/
---

{{% alert color="primary" %}}

Se desideri aggiungere una funzione nel foglio di lavoro che effettuerà alcuni calcoli, questo articolo spiega come raggiungere questo obiettivo utilizzando Aspose.Cells.

{{% /alert %}}

## Impostazione Formula Condivisa utilizzando Aspose.Cells

Supponiamo di avere un foglio di lavoro pieno di dati nel formato che assomiglia al seguente foglio di lavoro di esempio.

|**File di input con una colonna di dati**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Desideri aggiungere una funzione in B2 che calcolerà l'IVA per la prima riga di dati. L'IVA è del **9%**. La formula che calcola l'IVA è: **"=A2*0.09"**. Questo articolo spiega come applicare questa formula con Aspose.Cells.

Aspose.Cells consente di specificare una formula utilizzando la proprietà [**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula). Ci sono due opzioni per aggiungere formule alle altre celle (B3, B4, B5, e così via) nella colonna.

Puoi fare quello che hai fatto per la prima cella, impostando effettivamente la formula per ogni cella, aggiornando di conseguenza il riferimento della cella (A3*0,09, A4*0,09, A5*0,09 e così via). Questo richiede che i riferimenti delle celle per ciascuna riga siano aggiornati. Richiede anche ad Aspose.Cells di elaborare singolarmente ogni formula, il che può essere temporaneo per fogli di calcolo di grandi dimensioni e formule complesse. Aggiunge anche righe di codice aggiuntive anche se i cicli possono ridurle in qualche modo.

Un altro approccio è utilizzare una **formula condivisa**. Con una formula condivisa, le formule vengono aggiornate automaticamente per i riferimenti alle celle in ogni riga in modo che l'imposta venga calcolata correttamente. Il metodo [**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index) è più efficiente del primo metodo.

L'esempio seguente mostra come utilizzarla.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
