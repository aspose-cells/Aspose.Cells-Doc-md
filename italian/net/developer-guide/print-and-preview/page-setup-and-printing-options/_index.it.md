---
title: Opzioni di Impostazione Pagina e di Stampa
type: docs
weight: 60
url: /it/net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

A volte, gli sviluppatori devono configurare l'impostazione della pagina e le impostazioni di stampa per controllare il processo di stampa. Le impostazioni di configurazione della pagina e di stampa offrono varie opzioni e sono completamente supportate in Aspose.Cells.

Questo articolo mostra come creare un'applicazione console in Visual Studio.Net e applicare impostazioni di impaginazione e stampa a un foglio di lavoro con poche righe di codice utilizzando l'API Aspose.Cells.

{{% /alert %}}

## **Lavorare con Impostazioni Pagina e di Stampa**

Per questo esempio, abbiamo creato un libro in Microsoft Excel e utilizzato Aspose.Cells per impostare le opzioni di impostazione pagina e di stampa.

### **Utilizzare Aspose.Cells per impostare le opzioni di impaginazione della pagina**

Prima creare un foglio di lavoro semplice in Microsoft Excel. Quindi applicare le opzioni dell'impostazione pagina ad esso. Eseguendo il codice cambia le opzioni dell'impostazione pagina come nello screenshot sottostante.

|**File di output.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Creare un foglio di lavoro con alcuni dati in Microsoft Excel:
   1. Apri un nuovo foglio di lavoro in Microsoft Excel.
   1. Aggiungi alcuni dati.
1. Imposta opzioni dell'impostazione pagina:
   Applicare le opzioni di impostazione pagina al file. Di seguito è riportata una schermata delle opzioni predefinite, prima che vengano applicate le nuove opzioni.

|**Opzioni di impaginazione predefinite.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Scarica e installa Aspose.Cells:
   1. [Scarica](https://downloads.aspose.com/cells/net) Aspose.Cells for .Net.
   1. Installalo sul tuo computer di sviluppo.
      Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. Crea un progetto:
   1. Avvia Visual Studio. Net.
   1. Crea una nuova applicazione console.
      Questo esempio mostrerà un'applicazione console C#, ma è possibile utilizzare anche VB.NET.
1. Aggiungi riferimenti:
   1. Questo esempio utilizza Aspose.Cells, quindi aggiungi un riferimento a quel componente al progetto. Ad esempio:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Scrivi l'applicazione che invoca l'API:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Impostazione delle opzioni di stampa**

Le impostazioni di impostazione pagina forniscono anche diverse opzioni di stampa (chiamate anche opzioni di foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro. Consentono agli utenti di:

- Selezionare un'area di stampa specifica di un foglio di lavoro.
- Stampare i titoli.
- Stampare le linee di griglia.
- Stampare gli intitoli di riga/colonna.
- Ottenere una qualità di bozza.
- Stampare commenti.
- Stampare errori di cella.
Definire l'ordinamento delle pagine.

L'esempio che segue applica le opzioni di stampa al file creato nell'esempio precedente (PageSetup.xls). La schermata di seguito mostra le opzioni di stampa predefinite prima che vengano applicate nuove opzioni.

|**Documento di input**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
Eseguendo il codice si modificano le opzioni di stampa.

|**File di output**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
