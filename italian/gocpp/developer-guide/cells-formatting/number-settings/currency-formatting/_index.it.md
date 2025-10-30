---
title: Come Formattare un Numero come Valuta con Golang tramite C++
linktitle: Come formattare un numero come valuta
type: docs
weight: 10
url: /it/go-cpp/format-number-to-currency/
description: Questo articolo introdurrà come formattare numeri come valuta usando l API Aspose.Cells for C++.
keywords: formattare numero come valuta, impostazioni numero cella, formattare numero come valuta, impostazioni valuta, formato valuta.
---

## **Possibili Scenari di Utilizzo**
La formattazione dei numeri come valuta in Excel è importante per diversi motivi, in particolare quando si lavora con dati finanziari. Ecco perché la formattazione in valuta è vantaggiosa:

1. **Chiarisce i Valori Finanziari**: formattare un numero come valuta ne rende chiaro che il valore rappresenta denaro. Per esempio, invece di vedere 1000, che potrebbe significare qualsiasi cosa, $1.000 indica chiaramente un importo monetario.
1. **Include Simboli Valuta**: quando si trattano valute internazionali o multiple, formattare i numeri con il simbolo di valuta appropriato (ad esempio $, €, £) chiarisce il tipo di valuta utilizzata, riducendo le confusioni in report finanziari internazionali o transazioni.
1. **Migliora la Presentazione Professionale**: valori di valuta ben formattati appaiono rifiniti e professionali, il che è particolarmente importante per report, presentazioni e documenti aziendali. $10.000,00 sembra più credibile e organizzato rispetto a un semplice 10000.
1. **Migliora la Leggibilità**: la formattazione in valuta aggiunge virgole come separatori di migliaia e decimali, rendendo più facile leggere numeri grandi. Per esempio, 1000000 diventa $1.000.000,00, più leggibile e facilmente comprensibile a colpo d'occhio.
1. **Garantisce la Coerenza**: applicando una formattazione in valuta coerente, si assicura che tutti i valori monetari in un set di dati siano visualizzati nello stesso formato. Questa coerenza è importante per l'accuratezza finanziaria e per una comunicazione professionale, specialmente in grandi fogli di calcolo con molti numeri.
1. **Mostra Precisione**: la formattazione in valuta di solito include due decimali, rendendo facile vedere gli importi monetari esatti. Per esempio, $100,50 è chiaramente diverso da $100,00, importante in report finanziari dove la precisione conta.
1. **Semplifica i Calcoli Finanziari**: quando si eseguono calcoli finanziari (come sommare totali o mediare i costi), la formattazione in valuta aiuta Excel e gli utenti a capire che i dati sono in termini monetari. Aiuta Excel ad applicare la formattazione appropriata in formule e funzioni, assicurando che i risultati rimangano coerenti.
1. **Riduce l'Interpretazione Errata**: senza la formattazione in valuta, i numeri potrebbero essere interpretati come valori numerici generici piuttosto che come importi di denaro. Per esempio, 500 potrebbe essere scambiato per un conteggio di articoli o unità, mentre $500,00 rappresenta chiaramente un importo finanziario.
1. **Compatibile con le Funzionalità Contabili**: la formattazione in valuta si integra bene con le funzioni contabili di Excel, come i bilanci o i rapporti di flusso di cassa. Rende più facile usare i valori nei rendiconti finanziari dove il denaro è l'aspetto principale.
<br>
In sintesi, la formattazione dei numeri come valuta aiuta a distinguere i valori monetari da altri tipi di numeri, aumenta la chiarezza e rende più facile interpretare i dati, specialmente in contesti finanziari.

## **Come formattare un numero come valuta in Excel**
Per formattare i numeri come valuta in Excel, segui questi passaggi:

### **Utilizzo dell'opzione Formato Valuta**
1. Seleziona le celle che desideri formattare come valuta.
1. Vai alla scheda Home sulla barra multifunzione.
1. Nel gruppo Numero, clicca sulla freccia a discesa accanto alla casella di formato numero (questo potrebbe visualizzare "Generale" di default).
<br>
<img src="1.png" width=60% />
1. Seleziona Valuta dall'elenco.

### **Utilizzo della finestra di dialogo Formato celle**
1. Seleziona le celle che desideri formattare.
1. Fai clic con il tasto destro sulle celle selezionate e scegli Format Cells per aprire la finestra di dialogo Format Cells.
1. Nella scheda Numero, seleziona Valuta dall’elenco a sinistra.
<br>
<img src="2.png" width=60% />
1. Puoi personalizzare quanto segue: Decimali, Simbolo, Numeri negativi.
1. Fai clic su OK per applicare la formattazione.

## **Come formattare un numero come valuta in Aspose.Cells**

Per formattare i numeri come valuta nella libreria Aspose.Cells for C++ per lavorare con i file Excel, puoi applicare la formattazione valuta alle celle programmaticamente. Ecco come farlo usando C++ con Aspose.Cells:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CurrencyFormatting.go" >}}
