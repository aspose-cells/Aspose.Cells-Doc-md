---
title: Esporta Membri in Excel di Umbraco
type: docs
weight: 10
url: /it/net/umbraco-export-members-to-excel/
---

## **Introduzione**

Esporta Membri in Excel è un Add-on per Umbraco che consente di esportare i membri dal CMS di Umbraco a un Excel e un OpenDocument Spreadsheet utilizzando [Aspose.Cells] (https://products.aspose.com/cells/net/). Compare un nuovo nodo intitolato **Esporta Membri in Excel** sotto l'albero dei membri nel backend di Umbraco dopo l'installazione, dove è possibile semplicemente selezionare i membri da esportare e il formato di output per ottenere i membri nel formato documento di output selezionato.

### **Caratteristiche del Modulo**

Questa versione iniziale dell'Add-on ha le seguenti funzionalità:

- Esporta i membri in documenti Microsoft Excel (.xls, .xlsx e .xlsb)
- Esporta i membri in documento di testo delimitato da tabulazioni (.txt)
- Esporta i membri in CSV (delimitato da virgole) (*.csv)
- Esporta i membri in OpenDocument Spreadsheet (*.ods)
- Opzione per selezionare il formato di output desiderato prima dell'esportazione
- Opzione per esportare tutti o selezionare membri nel formato del documento di output selezionato.
- Funziona con tutte le versioni .NET a partire da .NET 2.0.
- Il documento esportato viene automaticamente inviato al browser per il download.
- Selezionato una copia del documento esportato viene salvata nella cartella App_Data/AsposeMemberExport sul server per un uso successivo.
- Compatibile con un'ampia gamma di versioni di Umbraco **4.5**+ **inclusa la Versione 6 e 7.**

## **Requisiti di sistema e piattaforme supportate**

### **Requisiti di sistema**

Per configurare questo modulo è necessario soddisfare i seguenti requisiti:

- Umbraco 6.0 +

Non esitate a contattarci se desiderate installare questo modulo su altre versioni di Umbraco.

### **Piattaforme Supportate**

Il modulo è supportato su tutte le versioni di

- Umbraco in esecuzione su ASP.NET 4.0

## **Download**

È possibile scaricare l'Add-on Esporta Membri in Excel da uno dei seguenti luoghi

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Umbraco_Member_Export_To_Excel_1.0)

## **Installazione**

Una volta scaricato, seguire questi passaggi per installare questo pacchetto nel sito web Umbraco:

1. Accedere alla sezione **Sviluppatore** di Umbraco, ad esempio `http://www.myblog.com/umbraco/`
1. Dall'albero, espandere la cartella **Pacchetti**.
1. Da qui ci sono due modi per installare un pacchetto: selezionare **Installa pacchetto locale** o cercare il **Repository dei Pacchetti Umbraco.**
1. Se si installa un **pacchetto locale**, non decomprimere il pacchetto ma caricare il file zip in Umbraco.
1. Seguire le istruzioni a schermo.

**Nota:** Potresti ricevere un errore di 'Superamento della lunghezza della richiesta massima' durante l'installazione. Puoi risolvere facilmente questo problema aggiornando il valore 'maxRequestLength' nel file web.config di Umbraco.

{{< highlight java >}}

  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" /> 

{{< /highlight >}}

## **Utilizzo**

Dopo aver installato il macro, è davvero semplice iniziare a usarlo sul tuo sito web:

1. Assicurati di aver effettuato l'accesso alla sezione **Sviluppatore** di Umbraco, ad esempio `http://www.myblog.com/umbraco/`
1. Fare clic su **Membri** nell'elenco delle sezioni in basso a sinistra dello schermo.
1. Alla fine dell'albero, vedrai un nodo intitolato **Esporta membri in Excel** clicca su di esso per avviare l'add-on Esporta in Excel.
1. Seleziona il formato del documento di output desiderato e seleziona i membri da esportare. Se desideri esportare tutti i membri, lascia la selezione dei membri o clicca sulla casella di controllo nella riga dell'intestazione.
1. Fare clic sul pulsante **Esporta** in basso e ti verrà richiesto di scaricare il file esportato.

## **Demo video**

Si prega di controllare [il video](https://www.youtube.com/watch?v=6PxZFvjWr2Y) di seguito per vedere il modulo in azione.

## **Supporto, Estendi e Contribuisci**

### **Supporto**

Fin dai primi giorni di Aspose, sapevamo che fornire ai nostri clienti solo buoni prodotti non sarebbe stato sufficiente. Dovevamo anche offrire un buon servizio. Siamo anche sviluppatori e comprendiamo quanto sia frustrante quando un problema tecnico o una stranezza nel software ti impedisce di fare ciò che devi fare. Siamo qui per risolvere i problemi, non per crearli.

Ecco perché offriamo un supporto gratuito. Chiunque utilizzi il nostro prodotto, che li abbia acquistati o li stia usando in valutazione, merita la nostra piena attenzione e rispetto.

È possibile registrare eventuali problemi o suggerimenti relativi ai moduli Aspose.Words .NET per Umbraco utilizzando una delle seguenti piattaforme

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Estensione e Contribuzione**

Esporta membri in Excel è un add-on open source e il suo codice sorgente è disponibile sui principali siti di codifica sociale elencati di seguito. Gli sviluppatori sono incoraggiati a scaricare il codice sorgente ed estendere la funzionalità secondo le proprie esigenze.

#### **Codice Sorgente**

Puoi ottenere l'ultimo codice sorgente da uno dei seguenti siti

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.UmbracoMemberExportToExcel)

#### **Come configurare il codice sorgente**

Devi avere quanto segue installato per aprire ed estendere il codice sorgente

- Visual Studio 2010 o superiore

Seguire questi semplici passaggi per iniziare

1. Scarica/Clona il codice sorgente.
1. Apri Visual Studio 2010 e scegli **File** > **Apri Progetto**
1. Passa al codice sorgente più recente che hai scaricato e apri **ad es. Aspose.UmbracoMemberExportToExcel.sln**
