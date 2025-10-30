---
title: Creazione dei subtotali
type: docs
weight: 800
url: /it/nodejs-cpp/creating-subtotals/
description: Impara come creare subtotali per valori ripetitivi in un foglio di calcolo usando l API Aspose.Cells for Node.js via C++.
keywords: Applica subtotali, Imposta subtotali, Aggiungi subtotali, Crea subtotali, Come aggiungere subtotali a un foglio di lavoro 
---

{{% alert color="primary" %}}

Puoi creare automaticamente subtotali per valori ripetitivi in un foglio di calcolo. Aspose.Cells for Node.js via C++ fornisce funzioni API che ti aiutano ad aggiungere subtotali ai fogli di calcolo in modo programmato.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per aggiungere subtotali in Microsoft Excel:

1. Crea una semplice lista di dati nel primo foglio di lavoro del documento (come mostrato nella figura qui sotto) e salva il file come Book1.xls.
1. Seleziona una qualsiasi cella all'interno della tua lista.
1. Dal menu **Dati**, seleziona **Subtotali**. Verrà visualizzata la finestra di dialogo Subtotali. Definisci quale funzione utilizzare e dove inserire i subtotali.

## **Usando l'API Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che permette l'accesso a ogni foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe fornisce una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro e di altri oggetti. Ogni foglio di lavoro è composto da una raccolta di [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Per aggiungere subtotali a un foglio di lavoro, utilizza il metodo [**subtotal**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) della classe [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Fornisci valori di parametro al metodo per specificare come il totale parziale deve essere calcolato e posizionato.

 Nei seguenti esempi, abbiamo aggiunto subtotali al primo foglio di lavoro del [file modello](book1.xlsx) usando l'API Aspose.Cells for Node.js via C++. Quando il codice viene eseguito, viene creato un foglio di lavoro con subtotali.

Gli snippet di codice che seguono mostrano come aggiungere subtotali a un foglio di lavoro con Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CreatingSubtotals-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
