---
title: Impostazione Formula Condivisa
type: docs
weight: 10
url: /it/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

Supponiamo di avere un foglio di lavoro pieno di dati nel formato che assomiglia al seguente foglio di lavoro di esempio.

**File di input con una colonna o dati** 

![todo:image_alt_text](setting-shared-formula_1.png)

Desideri aggiungere una funzione in B2 che calcolerà l'IVA per la prima riga di dati. L'IVA è del **9%**. La formula che calcola l'IVA è: **"=A2*0.09"**. Questo articolo spiega come applicare questa formula con Aspose.Cells.

{{% /alert %}} 

Aspose.Cells ti permette di specificare una formula utilizzando la proprietà [Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula), in particolare [Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) e [Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

Ci sono due opzioni per aggiungere formule alle altre celle (B3, B4, B5 e così via) nella colonna.

Puoi fare ciò che hai fatto per la prima cella, impostando efficacemente la formula per ogni cella, aggiornando di conseguenza il riferimento della cella (`A3*0.09`, `A4*0.09`, `A5*0.09` e così via). Ciò richiede che i riferimenti delle celle per ogni riga vengano aggiornati. Richiede anche che Aspose.Cells analizzi singolarmente ciascuna formula, il che può richiedere tempo per fogli di calcolo di grandi dimensioni e formule complesse. Aggiunge anche righe di codice aggiuntive, anche se i loop possono ridurle in qualche misura.

Un altro approccio è utilizzare una **formula condivisa**. Con una formula condivisa, le formule vengono aggiornate automaticamente per i riferimenti delle celle in ogni riga in modo che l'imposta venga calcolata correttamente. Il metodo [Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)) è più efficiente rispetto al primo metodo.

L'esempio seguente mostra come usarlo. Nella schermata sottostante viene mostrato il file di output.

**File di output: formula condivisa applicata** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
