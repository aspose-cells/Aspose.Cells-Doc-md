---
title: Impostazione Formula Condivisa
type: docs
weight: 10
url: /it/python-net/setting-shared-formula/
---

{{% alert color="primary" %}}

Se desideri aggiungere una funzione nel foglio di lavoro che esegua alcuni calcoli. Questo articolo spiega come ottenere questo risultato usando Aspose.Cells for Python via .NET.

{{% /alert %}}

## Impostare una formula condivisa usando Aspose.Cells for Python via .NET

Supponiamo di avere un foglio di lavoro pieno di dati nel formato che assomiglia al seguente foglio di lavoro di esempio.

|**File di input con una colonna di dati**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Vuoi aggiungere una funzione in B2 che calcoli l'imposta sulle vendite per la prima riga di dati. L'imposta è **9%**. La formula che calcola l'imposta sulle vendite è: **"=A2*0.09"**. Questo articolo spiega come applicare questa formula con Aspose.Cells for Python via .NET.

Aspose.Cells for Python via .NET ti consente di specificare una formula usando la proprietà [**Cell.formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula). Ci sono due opzioni per aggiungere formule alle altre celle (B3, B4, B5, ecc.) nella colonna.

Puoi fare ciò che hai fatto per la prima cella, impostando effettivamente la formula per ogni cella, aggiornando di conseguenza il riferimento della cella (A3*0.09, A4*0.09, A5*0.09 e così via). Ciò richiede di aggiornare i riferimenti di cella per ogni riga. Richiede anche che Aspose.Cells for Python via .NET analizzi ogni formula singolarmente, il che può richiedere molto tempo per fogli di calcolo di grandi dimensioni e formule complesse. Aggiunge anche linee di codice extra anche se i cicli possono ridurle in qualche modo.

Un altro approccio è utilizzare una **formula condivisa**. Con una formula condivisa, le formule vengono aggiornate automaticamente per i riferimenti alle celle in ogni riga in modo che l'imposta venga calcolata correttamente. Il metodo [**Cell.set_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_shared_formula) è più efficiente del primo metodo.

L'esempio seguente mostra come utilizzarla.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSharedFormula-1.py" >}}

