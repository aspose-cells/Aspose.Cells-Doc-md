---
title: Tabelle e intervalli
type: docs
weight: 30
url: /it/cpp/tables-and-ranges/
---
## **introduzione**
volte crei una tabella in Microsoft Excel e non vuoi continuare a lavorare con la funzionalità della tabella che ne deriva. Invece, vuoi qualcosa che assomigli a un tavolo. Per mantenere i dati in una tabella senza perdere la formattazione, convertire la tabella in un normale intervallo di dati. Aspose.Cells supporta questa funzionalità di Microsoft Excel per tabelle e oggetti elenco.
## **Utilizzando Microsoft Excel**
 Utilizzare il**Converti in intervallo** funzionalità per convertire rapidamente una tabella in un intervallo senza perdere la formattazione. In Microsoft Excel 2007/2010:

1. Fare clic in un punto qualsiasi della tabella per assicurarsi che la cella attiva sia in una colonna della tabella.
1.  Sul**Disegno** scheda, nel**Strumenti** gruppo, fare clic**Converti in intervallo**.

{{% alert color="primary" %}} 

Le funzionalità della tabella non sono più disponibili dopo che la tabella è stata convertita in un intervallo. Ad esempio, le intestazioni di riga non includono più le frecce di ordinamento e filtro e i riferimenti strutturati (riferimenti che utilizzano nomi di tabella) utilizzati nelle formule si trasformano in normali riferimenti di cella.

{{% /alert %}} 
## **Utilizzando Aspose.Cells**
Il seguente frammento di codice illustra la stessa funzionalità utilizzando Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange.cpp" >}}
