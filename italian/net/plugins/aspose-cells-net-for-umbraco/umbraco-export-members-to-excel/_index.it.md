---
title: Umbraco Esporta i membri in Excel
type: docs
weight: 10
url: /it/net/umbraco-export-members-to-excel/
---
## **introduzione**

 Esporta membri in Excel è un componente aggiuntivo per Umbraco che ti consente di esportare membri dal tuo CMS Umbraco a un foglio di calcolo Excel e OpenDocument utilizzando[Aspose.Cells](https://products.aspose.com/cells/net/) . Un nuovo nodo intitolato**Esporta membri in Excel**appare sotto l'albero dei membri nel back-end di Umbraco dopo l'installazione, dove puoi semplicemente selezionare i membri da esportare e il formato di output per ottenere i membri nel formato del documento di output selezionato.

### **Caratteristiche del modulo**

Questa versione iniziale del componente aggiuntivo ha le seguenti caratteristiche:

- Esporta membri in documenti Excel Microsoft (.xls, .xlsx e .xlsb)
- Esporta membri in un documento di testo delimitato da tabulazioni (.txt)
- Esporta membri in CSV (delimitato da virgole) (*.csv)
- Esporta membri in OpenDocument Spreadsheet (*.ods)
- Opzione per selezionare il formato di output desiderato prima dell'esportazione
- Opzione per esportare tutti o membri selezionati nel formato del documento di output selezionato.
- Funziona con tutte le versioni .NET a partire dalla .NET 2.0.
- Il documento esportato viene inviato automaticamente al browser per il download
- Se selezionato, una copia del documento esportato viene salvata nella cartella App_Data/AsposeMemberExport sul server per un uso successivo.
-  Compatibile con un'ampia gamma di versioni Umbraco**4.5**+ **comprese le versioni 6 e 7.**

## **Requisiti di sistema e piattaforme supportate**

### **Requisiti di sistema**

Per configurare questo modulo è necessario soddisfare i seguenti requisiti:

- Umbraco 6.0+

Non esitate a contattarci se desiderate installare questo modulo su altre versioni di Umbraco.

### **Piattaforme supportate**

Il modulo è supportato su tutte le versioni di

- Umbraco in esecuzione su ASP.NET 4.0

## **Download**

È possibile scaricare il componente aggiuntivo Esporta membri in Excel da uno dei seguenti percorsi

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Installazione**

Una volta scaricato, segui questi passaggi per installare questo pacchetto nel tuo sito Web Umbraco:

1.  Accedi all'Umbraco**Sviluppatore** sezione, ad esempio `http://www.myblog.com/umbraco/`
1.  Dall'albero, espandi il file**Pacchi** cartella.
1.  Da qui ci sono due modi per installare un pacchetto: select**Installa il pacchetto locale** oppure sfoglia il**Repository dei pacchetti Umbraco.**
1. Se installi**pacchetto locale**, non decomprimere il pacco ma caricare lo zip in Umbraco.
1. Segui le istruzioni sullo schermo.

**Nota:** È possibile che venga visualizzato un errore "Lunghezza massima richiesta superata" durante l'installazione. Puoi facilmente risolvere questo problema aggiornando il valore 'maxRequestLength' nel tuo file Umbraco web.config.

{{< highlight "java" >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **Usando**

Dopo aver installato la macro è davvero semplice iniziare a usarla sul tuo sito web:

1. Assicurati di aver effettuato l'accesso a Umbraco**Sviluppatore** sezione, ad esempio `http://www.myblog.com/umbraco/`
1.  Clic**Membri** nell'elenco delle sezioni in basso a sinistra dello schermo.
1.  Alla fine dell'albero, vedrai un nodo intitolato**Esporta membri in Excel** fare clic su di esso per avviare il componente aggiuntivo Esporta in Excel.
1. Selezionare il formato del documento di output desiderato e selezionare Membri da esportare. Se desideri esportare tutti i membri, lascia la selezione dei membri o fai clic sulla casella di controllo nella riga dell'intestazione.
1.  Clic**Esportare** pulsante in basso e ti verrà chiesto di scaricare il file esportato.

## **Dimostrazione video**

 si prega di controllare[il video](https://www.youtube.com/watch?v=6PxZFvjWr2Y) sotto per vedere il modulo in azione.

## **Supporto, estensione e contributo**

### **Supporto**

Fin dai primi giorni di Aspose, sapevamo che solo dare ai nostri clienti buoni prodotti non sarebbe bastato. Avevamo anche bisogno di fornire un buon servizio. Siamo sviluppatori noi stessi e comprendiamo quanto sia frustrante quando un problema tecnico o una stranezza nel software ti impedisce di fare ciò che devi fare. Siamo qui per risolvere i problemi, non per crearli.

Per questo offriamo assistenza gratuita. Chiunque utilizzi il nostro prodotto, sia che lo abbia acquistato o che stia utilizzando una valutazione, merita la nostra piena attenzione e rispetto.

Puoi registrare eventuali problemi o suggerimenti relativi a Aspose.Words .NET per i moduli Umbraco utilizzando una delle seguenti piattaforme

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Estendi e contribuisci**

Esporta membri in Excel è un componente aggiuntivo open source e il suo codice sorgente è disponibile sui principali siti Web di social coding elencati di seguito. Gli sviluppatori sono incoraggiati a scaricare il codice sorgente ed estendere la funzionalità secondo i propri requisiti.

#### **Codice sorgente**

È possibile ottenere il codice sorgente più recente da una delle seguenti posizioni

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **Come configurare il codice sorgente**

È necessario che sia installato quanto segue per aprire ed estendere il codice sorgente

- Visual Studio 2010 o versioni successive

Segui questi semplici passaggi per iniziare

1. Scarica/clona il codice sorgente.
1.  Apri Visual Studio 2010 e scegli**File** > **Progetto aperto**
1.  Sfoglia fino all'ultimo codice sorgente che hai scaricato e aperto**ad esempio Aspose.UmbracoMemberExportToExcel.sln**
