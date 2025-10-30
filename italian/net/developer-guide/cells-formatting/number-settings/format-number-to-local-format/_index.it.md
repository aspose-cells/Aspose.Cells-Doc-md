---
title: Come formattare un numero nel formato locale
type: docs
weight: 10
url: /it/net/how-to-format-number-to-local-language-format/
description: Questo articolo introdurrà come formattare un numero nel formato della lingua locale Aspose.Cells for .NET API.
keywords: Converti un numero in un formato linguistico locale, Trasforma un cifra nel formato linguistico locale, Cambia un numero nel suo formato linguistico locale corrispondente, Format a valore numerico nel formato linguistico locale, Esprimi un numero come formato linguistico locale, Formatta Numero al formato linguistico locale.
---

## **Possibili Scenari di Utilizzo**

Formattare i numeri ai formati locali in Excel è essenziale per garantire che i dati siano chiaramente compresi, accuratamente interpretati e presentati professionalmente in diverse regioni e culture.

1. **Adattamento culturale e regionale**: Diverse regioni utilizzano vari formati numerici per decimali, separatori delle migliaia, valute e date. 
1. **Professionalità e chiarezza**: Utilizzare formati locali migliora l'aspetto professionale dei tuoi fogli di calcolo. Dimostra attenzione ai dettagli e considerazione per il pubblico, fondamentale in rapporti, bilanci e dati condivisi con stakeholder.
1. **Coerenza nella visualizzazione dei dati**: La formattazione locale garantisce coerenza durante la collaborazione con team o clienti di diverse regioni. Previene errori derivanti da interpretazioni errate dei dati, come confondere i separatori decimali.
1. **Compatibilità con sistemi esterni**: Quando esporti dati in altri formati (ad esempio CSV), la formattazione locale aiuta a mantenere l'integrità dei dati.
1. **Accessibilità e facilità d'uso**: La formattazione locale rende i dati più accessibili agli utenti che non sono familiari con formati stranieri. Per esempio, visualizzare le date nel formato "GG/MM/AAAA" (comune nel Regno Unito) vs. "MM/GG/AAAA" (comune negli USA) evita confusione.
1. **Validazione e accuratezza dei dati**: Una formattazione errata può portare a errori di calcolo. Per esempio, se un numero viene interpretato erroneamente a causa di problemi con il separatore decimale, le formule possono produrre risultati sbagliati. Usare i formati locali assicura che i dati inseriti dagli utenti siano conformi agli standard regionali, riducendo il rischio di errori durante l'inserimento o l'analisi dei dati.

## **Come formattare un numero nel formato linguistico locale in Excel**

Per formattare i numeri nel formato linguistico locale in Excel, puoi utilizzare diverse funzionalità e funzioni integrate che si adattano alle impostazioni regionali. 

1. **Usa le impostazioni locali integrate di Excel**: Vai su File > Opzioni > Impostazioni regionali (o simile, a seconda della versione di Excel). Seleziona la lingua/regione desiderata (es. tedesco per i separatori decimali con virgola, inglese per i punti). I valori e le formule esistenti si convertiranno automaticamente nel nuovo formato.
1. **Usa la funzione TESTO per una formattazione locale personalizzata**: La funzione TESTO può forzare la formattazione dei numeri in base a pattern specifici della regione, utile per visualizzare numeri come numeri di telefono o valute senza modificare le impostazioni globali. Sintassi: =TESTO(valore, "codice_formato").
1. **Gestione programmatica (VBA/APIs)**: Per gli sviluppatori che usano VBA, puoi usare NumberFormat con le stringhe di formato in inglese americano (es. "#.##"). Excel si adatterà automaticamente alle impostazioni locali dell'utente. Evitare NumberFormatLocal a meno che non si necessiti esplicitamente di stringhe di formato specifiche della regione.
1. **Sovrascrivi i separatori di sistema per casi specifici**: Se la formattazione localizzata si comporta in modo inaspettato (ad esempio, a causa di aggiornamenti di Windows che influenzano i separatori), sovrascrivi manualmente i default: nelle opzioni di Excel, disattiva "Usa separatori di sistema" e definisci separatori decimali/migliaia personalizzati.
1. **Formatta i numeri usando formati personalizzati**: Fai clic destro sulla cella, seleziona 'Formato celle', quindi trova 'Numero'->'Personalizzato' e imposta il tipo di numero personalizzato desiderato. Prendendo come esempio la impostazione di formati numerici personalizzati in un ambiente cinese.
<br>
<img src="1.png" width=60% />


## **Come formattare un numero nel formato linguistico locale in Aspose.Cells for .NET**

Per formattare i numeri nel formato linguistico locale in Aspose.Cells for .NET, puoi utilizzare l'oggetto `Style` associato a una cella o a un intervallo di celle. L'oggetto `Style` ti permette di impostare varie opzioni di formattazione, incluso il formato numerico personalizzato. 

Ecco un esempio di base su come applicare un formato numerico nel linguaggio locale a una cella in Aspose.Cells for .NET:

1. **Riferisci a Aspose.Cells**: assicurati di aver incluso Aspose.Cells for .NET nel tuo progetto. Puoi ottenerlo da NuGet o dal sito di Aspose.

2. **Creare o aprire un workbook**: Inizia creando un nuovo workbook o aprendo uno esistente.

3. **Accedere alla cella desiderata**: Identifica e accedi alla cella o intervallo di celle da formattare.

4. **Applica formato numerico personalizzato**: Imposta il formato numerico dello stile della cella su un formato numerico in lingua cinese.

4. **Codice di esempio**: Ecco un esempio di codice che dimostra questi passaggi.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-FormatNumber-To-LocalLanguageFormat.cs" >}}

## **Sei output generato dal codice di esempio**
Ecco il risultato in PDF del codice di esempio sopra.
<br>
<img src="2.png" width=60% />

{{< app/cells/assistant language="csharp" >}}
