---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /it/net/aspose-cells-net-for-php/
---

## **Iniziare**

### **Introduzione**

### **Requisiti di sistema e piattaforme supportate**

#### **Requisiti di sistema**

**Ecco i requisiti di sistema per utilizzare Aspose.Cells .NET per PHP:**

- IIS con PHP e PHP Manager installato.
- Aspose.Total APIs.
- Il file dll e tlb di interoperabilità di Aspose.Cells.

#### **Piattaforme Supportate**

**Di seguito sono indicate le piattaforme supportate:**

- PHP 5.3 o successivo
- Sistema operativo Windows

### **Scarica e Configura**

#### **Scarica le librerie necessarie**

Scarica le librerie necessarie indicate di seguito. Queste sono necessarie per eseguire gli esempi Aspose.Cells Java in PHP.

- [Scarica i file Aspose.Cells for .NET (DLL o MSI) dalla sezione download](https://downloads.aspose.com/cells/net)
- [Scarica il file Aspose.Cells for .NET dll di interoperabilità](https://downloads.aspose.com/cells/net)

Se si scarica la versione MSI, troverai Aspose.Cells.dll nella posizione di installazione predefinita, che si trova nella cartella C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0.
Tuttavia, nel caso tu abbia scaricato la versione DLL, puoi estrarla e poi copiare Aspose.Cells.dll dalla cartella .NET 2.0 nella cartella c:\temp per una maggiore facilità d'uso.
Analogamente, estrai il file zip interop e copia Aspose.Inteop.dll in c:\temp.

#### **Scarica esempi dai siti di codice sociale**

Le versioni in esecuzione degli esempi disponibili per il download sono disponibili sui siti di codici sociali di seguito menzionati:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Examples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Come configurare il codice sorgente su Windows Platform**

Si prega di seguire questi semplici passaggi per aprire ed estendere il codice sorgente durante l'uso:

##### **1. Registra entrambi i file dll e interop.dll ad es. Aspose.Cells.dll e Aspose.Cells.Interop.dll.**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Abilita le estensioni COM e DOTNET in PHP.**

In IIS apri PHP Manager e poi clicca su 'Abilita per Disabilitare e Estensioni'. Trova php_com_dotnet.dll e assicurati che sia abilitato.

##### **3. Configura gli Esempi di Aspose.Cells .NET per PHP**

###### **Metodo 1**

Clona gli Esempi in PHP da [github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
e esegui il seguente comando

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **Metodo 2**

Nel file composer.json del tuo progetto PHP aggiungi le seguenti righe

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

e esegui il comando di installazione

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **Supporta Estendi e Contribuisci**

#### **Supporto**

Fin dai primi giorni di Aspose, sapevamo che fornire ai nostri clienti solo buoni prodotti non sarebbe stato sufficiente. Dovevamo anche offrire un buon servizio. Siamo anche sviluppatori e comprendiamo quanto sia frustrante quando un problema tecnico o una stranezza nel software ti impedisce di fare ciò che devi fare. Siamo qui per risolvere i problemi, non per crearli.

Ecco perché offriamo un supporto gratuito. Chiunque utilizzi il nostro prodotto, che li abbia acquistati o li stia usando in valutazione, merita la nostra piena attenzione e rispetto.

Puoi segnalare eventuali problemi o suggerimenti relativi ad Aspose.Cells .NET per PHP utilizzando una delle seguenti piattaforme:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Estensione e Contribuzione**

Aspose.Cells .NET per PHP è open source e il suo codice sorgente è disponibile sui principali siti di codice sociale elencati di seguito. Si incoraggia gli sviluppatori a scaricare il codice sorgente e contribuire suggerendo o aggiungendo nuove funzionalità o migliorando quelle esistenti, in modo che anche altri possano beneficiarne.

#### **Codice Sorgente**

Puoi ottenere l'ultimo codice sorgente da uno dei seguenti siti

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Esempi di codice di esempio**

Questa sezione include i seguenti argomenti

- [Guida per programmatori PHP](/cells/it/net/php-programmers-guide/)
  - [Lavorare con i file in PHP](/cells/it/net/working-with-files-in-php/)
    - [Funzionalità di gestione dei file in PHP](/cells/it/net/file-handling-features-in-php/)
      - [Apertura dei file in PHP](/cells/it/net/opening-files-in-php/)
      - [Salvataggio dei file in PHP](/cells/it/net/saving-files-in-php/)
    - [Funzionalità di utilità in PHP](/cells/it/net/utility-features-in-php/)
      - [Crittografare i File in PHP](/cells/it/net/encrypting-files-in-php/)
      - [Conversione da Excel a PDF in PHP](/cells/it/net/excel-to-pdf-conversion-in-php/)
      - [Gestione delle proprietà del documento in PHP](/cells/it/net/managing-document-properties-in-php/)
      - [Conversione del foglio di lavoro in immagine in PHP](/cells/it/net/worksheet-to-image-conversion-in-php/)
  - [Lavorare con formule in PHP](/cells/it/net/working-with-formulas-in-php/)
    - [Calcolo delle formule in PHP](/cells/it/net/calculating-formulas-in-php/)
  - [Lavorare con i fogli di lavoro in PHP](/cells/it/net/working-with-worksheets-in-php/)
    - [Funzionalità di gestione in PHP](/cells/it/net/management-features-in-php/)
      - [Gestione dei fogli di lavoro in PHP](/cells/it/net/managing-worksheets-in-php/)
        - [Aggiungi fogli di lavoro a un file Excel esistente in PHP](/cells/it/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Aggiungi fogli di lavoro a un nuovo file Excel in PHP](/cells/it/net/add-worksheets-to-new-excel-file-in-php/)
        - [Rimozione dei fogli di lavoro utilizzando l'indice del foglio in PHP](/cells/it/net/removing-worksheets-using-sheet-index-in-php/)
        - [Rimozione dei fogli di lavoro utilizzando il nome del foglio in PHP](/cells/it/net/removing-worksheets-using-sheet-name-in-php/)
