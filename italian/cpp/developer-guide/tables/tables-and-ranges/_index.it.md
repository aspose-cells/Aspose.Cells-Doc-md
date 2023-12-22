---
title: Tabelle e intervalli
type: docs
weight: 30
url: /it/cpp/tables-and-ranges/
---
##  **introduzione**
volte crei una tabella in Microsoft Excel e non vuoi continuare a lavorare con la funzionalità della tabella fornita. Invece, vuoi qualcosa che assomigli a un tavolo. Per mantenere i dati in una tabella senza perdere la formattazione, converti la tabella in un intervallo di dati regolare. Aspose.Cells supporta questa funzionalità di Microsoft Excel per tabelle ed oggetti elenco.
##  **Utilizzando Microsoft Excel**
 Usa il**Converti in intervallo** funzionalità per convertire rapidamente una tabella in un intervallo senza perdere la formattazione. Nel Microsoft Excel 2007/2010:

1. Fai clic in un punto qualsiasi della tabella per assicurarti che la cella attiva si trovi in una colonna della tabella.
1.  Sul**Progetto** scheda, nel**Utensili** gruppo, fare clic su *Converti in intervallo**.

{{% alert color="primary" %}} 

Le funzionalità della tabella non sono più disponibili dopo che la tabella è stata convertita in un intervallo. Ad esempio, le intestazioni delle righe non includono più le frecce di ordinamento e filtro e i riferimenti strutturati (riferimenti che utilizzano nomi di tabella) utilizzati nelle formule si trasformano in riferimenti di cella regolari.

{{% /alert %}} 
##  **Utilizzando Aspose.Cells**
Il seguente frammento di codice dimostra la stessa funzionalità utilizzando Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
