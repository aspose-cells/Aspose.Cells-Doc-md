---
title: Componente Canvas del Rapporto Ohal
type: docs
weight: 30
url: /it/net/ohal-report-canvas-component/
---

{{% alert color="primary" %}}

[Report PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**Uso di Aspose.Cells nel Componente Canvas del Rapporto**

Robert Chilvers, 17 marzo 2008

{{% /alert %}}

## **Sfondo del prodotto**

Il Componente Canvas del Rapporto consente all'utente di creare rapporti visuali basati su un set di dati pre-caricato. L'utente può aggiungere diversi componenti alla propria canvas, tra cui immagini, caselle di testo, grafici e tabelle, specificando quindi i dati e come devono essere aggregati. L'utente può quindi riorganizzare e ridimensionare gli oggetti per adattarli alla propria pagina. L'utente può specificare palette di colori e salvare modelli per un uso futuro. Aspose.Cells viene utilizzato per esportare tutti gli oggetti sulla canvas su Excel con i dati corretti. Il componente è scritto con VB.Net in Visual Studio 2008.

## **Scenario dei requisiti**

Abbiamo selezionato Aspose.Cells per le sue capacità di esportazione quasi complete di Microsoft Excel. È importante per noi la capacità di esportare grafici e tabelle, specialmente in Microsoft Excel 2007, cosa che mancava in altri componenti di terze parti.

## **Implementazione della soluzione**

Ogni oggetto sulla canvas del rapporto ha una funzione a cui viene passata un'istanza del foglio di calcolo di Aspose.Cells e aggiunge se stesso al foglio di calcolo. Quando l'utente richiede un'esportazione, il libro di lavoro e i fogli di lavoro vengono inizializzati e a ciascun oggetto sulla canvas del rapporto viene chiamata questa funzione.

## **Vantaggi**

Aspose.Cells ci ha permesso di costruire il libro di lavoro su Excel in modo del tutto indipendente da Excel e poi salvare il libro di lavoro nel formato selezionato dall'utente. Ciò ha risparmiato ore di debug dell'interazione quando si utilizza l'Excel interop e l'implementazione di diverse routine per il salvataggio in versioni diverse di Excel.

## **Implementazione Futura**

Abbiamo intenzione di utilizzare Aspose.Cells per tutti il caricamento e il salvataggio dei file di Excel. Ciò includerà il caricamento di modelli di dati e l'esportazione dei risultati.

## **Conclusioni**

{{% alert color="primary" %}}

Finora non abbiamo avuto problemi nell'utilizzo dei componenti Aspose.Cells e il componente dovrebbe risparmiarci tempo di sviluppo sia a breve che a lungo termine. Le richieste di supporto e vendita sono state risposte prontamente e in modo utile.

{{% /alert %}}
