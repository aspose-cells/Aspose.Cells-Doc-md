---
title: Impostazione della formula condivisa
type: docs
weight: 10
url: /it/net/setting-shared-formula/
---
{{% alert color="primary" %}}

Se vuoi aggiungere una funzione nel foglio di lavoro che eseguirà alcuni calcoli. Questo articolo spiega come eseguire questa attività utilizzando Aspose.Cells.

{{% /alert %}}

## Impostazione della formula condivisa utilizzando Aspose.Cells

Supponiamo di avere un foglio di lavoro pieno di dati nel formato che assomiglia al seguente foglio di lavoro di esempio.

|**File di input con una colonna o dati**|
|:- |
|![cose da fare:immagine_alt_testo](setting-shared-formula_1.png)|

 Si desidera aggiungere una funzione in B2 che calcolerà l'imposta sulle vendite per la prima riga di dati. La tassa è**9%** La formula che calcola l'imposta sulle vendite è:**"=A2*0.09"**. Questo articolo spiega come applicare questa formula con Aspose.Cells.

 Aspose.Cells consente di specificare una formula utilizzando il[**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)proprietà. Esistono due opzioni per aggiungere formule alle altre celle (B3, B4, B5 e così via) nella colonna.

O fai quello che hai fatto per la prima cella, impostando effettivamente la formula per ogni cella, aggiornando di conseguenza il riferimento di cella (A3*0,09, A4*0.09, A5*0.09 e così via). Ciò richiede l'aggiornamento dei riferimenti di cella per ogni riga. Richiede inoltre Aspose.Cells per analizzare ogni formula individualmente, il che può richiedere molto tempo per fogli di calcolo di grandi dimensioni e formule complesse. Aggiunge anche ulteriori righe di codici sebbene i loop possano ridurli in qualche modo.

 Un altro approccio consiste nell'usare a**formula condivisa** Con una formula condivisa, le formule vengono aggiornate automaticamente per i riferimenti di cella in ogni riga in modo che l'imposta venga calcolata correttamente. Il[**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index)metodo è più efficiente del primo metodo.

L'esempio seguente mostra come usarlo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
