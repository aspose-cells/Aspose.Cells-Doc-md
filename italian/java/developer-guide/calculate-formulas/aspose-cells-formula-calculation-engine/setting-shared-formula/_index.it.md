---
title: Impostazione della formula condivisa
type: docs
weight: 10
url: /it/java/setting-shared-formula/
---
{{% alert color="primary" %}} 

Supponiamo di avere un foglio di lavoro pieno di dati nel formato che assomiglia al seguente foglio di lavoro di esempio.

**File di input con una colonna o dati** 

![cose da fare:immagine_alt_testo](setting-shared-formula_1.png)

 Si desidera aggiungere una funzione in B2 che calcolerà l'imposta sulle vendite per la prima riga di dati. La tassa è**9%** . La formula che calcola l'imposta sulle vendite è:**"=A2*0.09"**. Questo articolo spiega come applicare questa formula con Aspose.Cells.

{{% /alert %}} 

 Aspose.Cells consente di specificare una formula utilizzando il[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) proprietà, nello specifico[Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) e[Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

Esistono due opzioni per aggiungere formule alle altre celle (B3, B4, B5 e così via) nella colonna.

fai quello che hai fatto per la prima cella, impostando effettivamente la formula per ogni cella, aggiornando di conseguenza il riferimento di cella (A3*0,09, A4*0.09, A5*0.09 e così via). Ciò richiede l'aggiornamento dei riferimenti di cella per ogni riga. Richiede inoltre Aspose.Cells per analizzare ogni formula individualmente, il che può richiedere molto tempo per fogli di calcolo di grandi dimensioni e formule complesse. Aggiunge anche ulteriori righe di codici sebbene i loop possano ridurli in qualche modo.

 Un altro approccio consiste nell'usare a**formula condivisa** . Con una formula condivisa, le formule vengono aggiornate automaticamente per i riferimenti di cella in ogni riga in modo che l'imposta venga calcolata correttamente. Il[Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)) è più efficiente del primo metodo.

L'esempio seguente mostra come usarlo. Lo screenshot qui sotto mostra il file di output.

**File di output: formula condivisa applicata** 

![cose da fare:immagine_alt_testo](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
