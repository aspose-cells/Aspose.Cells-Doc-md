---
title: Aspose.Cells .NET per PHP
type: docs
weight: 40
url: /it/net/aspose-cells-net-for-php/
---
## **Iniziare**

### **introduzione**

### **Requisiti di sistema e piattaforme supportate**

#### **Requisiti di sistema**

**Di seguito sono riportati i requisiti di sistema per utilizzare Aspose.Cells .NET per PHP:**

- IIS con PHP e PHP Manager installati.
- Aspose.Total API.
- Aspose.Cells il file Interop dll e tlb.

#### **Piattaforme supportate**

**Di seguito le piattaforme supportate:**

- PHP 5.3 o superiore
- Windows OS

### **Scarica e configura**

#### **Scarica le librerie richieste**

Scarica le librerie richieste menzionate di seguito. Questi sono i requisiti per l'esecuzione di Aspose.Cells Java per esempi PHP.

- [Scarica i file Aspose.Cells for .NET (DLL o MSI) dalla sezione download](https://downloads.aspose.com/cells/net)
- [Scarica Aspose.Cells for .NET interoperabilità dll](https://downloads.aspose.com/cells/net)

Se scarichi la versione MSI, troverai Aspose.Cells.dll nella posizione di installazione che è la cartella C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 per impostazione predefinita.
Tuttavia, se hai scaricato la versione DLL, puoi estrarla e quindi copiare Aspose.Cells.dll dalla cartella .NET 2.0 nella cartella c:\temp per facilità d'uso.
Allo stesso modo estrarre il file zip di interoperabilità e copiare Aspose.Inteop.dll in c:\temp

#### **Scarica esempi dai siti di codifica sociale**

Le seguenti versioni di esempi in esecuzione sono disponibili per il download sui siti di social coding sotto indicati:

-----

##### **Git Hub**

- **Aspose.Cells .NET per esempi PHP**

  - [Aspose.Cells .NET per PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Come configurare il codice sorgente sulla piattaforma Windows**

Si prega di seguire questi semplici passaggi per aprire ed estendere il codice sorgente durante l'utilizzo:

##### **1. Registrare entrambi i file dll e interop.dll, ad esempio Aspose.Cells.dll e Aspose.Cells.Interop.dll.**

{{< highlight "java" >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Abilita le estensioni COM e DOTNET in PHP.**

In IIS apri PHP Manager e fai clic su "Abilita per disabilitare ed estensione". Trova php_com_dotnet.dll e assicurati che sia abilitato.

##### **3. Configurare Aspose.Cells .NET per esempi PHP**

###### **Metodo 1**

 Clona esempi PHP da[github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
ed eseguire il seguente comando

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

###### **Metodo 2**

Nel file composer.json del tuo progetto PHP aggiungi le seguenti righe

{{< highlight "java" >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

ed eseguire il comando install

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

 Per leggere la visita del compositore<https://getcomposer.org/>

### **Supporto Estendi e contribuisci**

#### **Supporto**

Fin dai primi giorni di Aspose, sapevamo che solo dare ai nostri clienti buoni prodotti non sarebbe bastato. Avevamo anche bisogno di fornire un buon servizio. Siamo sviluppatori noi stessi e comprendiamo quanto sia frustrante quando un problema tecnico o una stranezza nel software ti impedisce di fare ciò che devi fare. Siamo qui per risolvere i problemi, non per crearli.

Per questo offriamo assistenza gratuita. Chiunque utilizzi il nostro prodotto, sia che lo abbia acquistato o che stia utilizzando una valutazione, merita la nostra piena attenzione e rispetto.

Puoi registrare eventuali problemi o suggerimenti relativi a Aspose.Cells .NET per PHP utilizzando una delle seguenti piattaforme:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Estendi e contribuisci**

Aspose.Cells .NET per PHP è open source e il suo codice sorgente è disponibile sui principali siti Web di social coding elencati di seguito. Gli sviluppatori sono incoraggiati a scaricare il codice sorgente ea contribuire suggerendo o aggiungendo nuove funzionalità o migliorando quelle esistenti, in modo che anche altri possano trarne vantaggio.

#### **Codice sorgente**

È possibile ottenere il codice sorgente più recente da una delle seguenti posizioni

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Esempi di codice di esempio**

Questa sezione include i seguenti argomenti

- [Guida per programmatori PHP](/cells/it/net/php-programmers-guide/)
  - [Lavorare con i file in PHP](/cells/it/net/working-with-files-in-php/)
    - [Funzionalità di gestione dei file in PHP](/cells/it/net/file-handling-features-in-php/)
      - [Apertura di file in PHP](/cells/it/net/opening-files-in-php/)
      - [Salvataggio di file in PHP](/cells/it/net/saving-files-in-php/)
    - [Funzionalità di utilità in PHP](/cells/it/net/utility-features-in-php/)
      - [Crittografia dei file in PHP](/cells/it/net/encrypting-files-in-php/)
      - [Conversione da Excel a PDF in PHP](/cells/it/net/excel-to-pdf-conversion-in-php/)
      - [Gestione delle proprietà del documento in PHP](/cells/it/net/managing-document-properties-in-php/)
      - [Conversione da foglio di lavoro a immagine in PHP](/cells/it/net/worksheet-to-image-conversion-in-php/)
  - [Lavorare con le formule in PHP](/cells/it/net/working-with-formulas-in-php/)
    - [Calcolo di formule in PHP](/cells/it/net/calculating-formulas-in-php/)
  - [Lavorare con i fogli di lavoro in PHP](/cells/it/net/working-with-worksheets-in-php/)
    - [Funzionalità di gestione in PHP](/cells/it/net/management-features-in-php/)
      - [Gestione dei fogli di lavoro in PHP](/cells/it/net/managing-worksheets-in-php/)
        - [Aggiungi fogli di lavoro al file Excel esistente in PHP](/cells/it/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Aggiungi fogli di lavoro al nuovo file Excel in PHP](/cells/it/net/add-worksheets-to-new-excel-file-in-php/)
        - [Rimozione di fogli di lavoro utilizzando l'indice dei fogli in PHP](/cells/it/net/removing-worksheets-using-sheet-index-in-php/)
        - [Rimozione di fogli di lavoro utilizzando il nome del foglio in PHP](/cells/it/net/removing-worksheets-using-sheet-name-in-php/)
