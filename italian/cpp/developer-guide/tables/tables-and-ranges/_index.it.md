---
title: Tabelle e intervalli
type: docs
weight: 30
url: /it/cpp/tables-and-ranges/
---

## **Introduzione**
A volte crei una tabella in Microsoft Excel e non vuoi continuare a lavorare con la funzionalità tabella che la accompagna. Invece, desideri qualcosa che assomigli a una tabella. Per mantenere i dati in una tabella senza perdere la formattazione, converti la tabella in un intervallo regolare di dati. Aspose.Cells supporta questa funzione di Microsoft Excel per tabelle e oggetti elenco.
## **Utilizzando Microsoft Excel**
Utilizzare la funzionalità **Converti in Intervallo** per convertire rapidamente una tabella in un intervallo senza perdere la formattazione. In Microsoft Excel 2007/2010:

1. Fare clic ovunque nella tabella per garantire che la cella attiva sia in una colonna della tabella.
1. Sulla scheda **Design**, nel gruppo **Strumenti**, fare clic su **Converti in intervallo**.

{{% alert color="primary" %}} 

Le funzionalità della tabella non sono più disponibili dopo che la tabella è stata convertita in un intervallo. Ad esempio, le intestazioni di riga non includono più le frecce di ordinamento e filtro, e i riferimenti strutturati (riferimenti che usano i nomi delle tabelle) usati nelle formule diventano riferimenti di celle regolari.

{{% /alert %}} 
## **Usare Aspose.Cells**
Il seguente snippet di codice dimostra la stessa funzionalità utilizzando Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
