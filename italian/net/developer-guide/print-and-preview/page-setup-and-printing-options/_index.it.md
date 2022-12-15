---
title: Impostazioni di pagina e opzioni di stampa
type: docs
weight: 60
url: /it/net/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

A volte, gli sviluppatori devono configurare l'impostazione della pagina e le impostazioni di stampa per controllare il processo di stampa. L'impostazione della pagina e le impostazioni di stampa offrono varie opzioni e sono completamente supportate in Aspose.Cells.

Questo articolo illustra come creare un'applicazione console in Visual Studio.Net e applicare le opzioni di configurazione e stampa della pagina a un foglio di lavoro con poche semplici righe di codice usando l'API Aspose.Cells.

{{% /alert %}}

## **Utilizzo delle impostazioni di pagina e stampa**

Per questo esempio, abbiamo creato una cartella di lavoro in Microsoft Excel e utilizzato Aspose.Cells per impostare l'impostazione della pagina e le opzioni di stampa.

### **Utilizzo di Aspose.Cells per impostare le opzioni di impostazione della pagina**

Per prima cosa crea un semplice foglio di lavoro in Microsoft Excel. Quindi applica le opzioni di impostazione della pagina. L'esecuzione del codice modifica le opzioni di Imposta pagina come nello screenshot qui sotto.

|**File di uscita.**|
|:- |
|![cose da fare:immagine_alt_testo](page-setup-and-printing-options_1.png)|

1. Crea un foglio di lavoro con alcuni dati in Microsoft Excel:
 1. Apri una nuova cartella di lavoro in Microsoft Excel.
 1. Aggiungi alcuni dati.
1. Imposta le opzioni di impostazione della pagina:
 Applicare le opzioni di impostazione della pagina al file. Di seguito è riportato uno screenshot delle opzioni predefinite, prima che vengano applicate le nuove opzioni.

|**Opzioni di impostazione della pagina predefinita.**|
|:- |
|![cose da fare:immagine_alt_testo](page-setup-and-printing-options_2.png)|

1. Scarica e installa Aspose.Cells:
   1. [Scarica](https://downloads.aspose.com/cells/net) Aspose.Cells per .Net.
 1. Installalo sul tuo computer di sviluppo.
Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e si limita a inserire filigrane nei documenti prodotti.
1. Crea un progetto:
 1. Avviare Visual Studio. Rete.
 1. Creare una nuova applicazione console.
 Questo esempio mostrerà un'applicazione console C#, ma puoi usare anche VB.NET.
1. Aggiungi riferimenti:
 1. Questo esempio usa Aspose.Cells quindi aggiungi un riferimento a quel componente al progetto. Per esempio:
 …\Programmi\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Scrivi l'applicazione che richiama l'API:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **Impostazione delle opzioni di stampa**

Le impostazioni di impostazione della pagina forniscono anche diverse opzioni di stampa (chiamate anche opzioni del foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro. Consentono agli utenti di:

- Selezionare un'area di stampa specifica di un foglio di lavoro.
- Stampa titoli.
- Stampa griglia.
- Stampa le intestazioni di riga/colonna.
- Ottieni una bozza di qualità.
- Stampa commenti.
- Stampa gli errori della cella.
- Definire l'ordine delle pagine.

L'esempio che segue applica le opzioni di stampa al file creato nell'esempio precedente (PageSetup.xls). Lo screenshot seguente mostra le opzioni di stampa predefinite prima che vengano applicate le nuove opzioni.

|**Documento di input**|
|:- |
|![cose da fare:immagine_alt_testo](page-setup-and-printing-options_3.png)|
L'esecuzione del codice modifica le opzioni di stampa.

|**File di uscita**|
|:- |
|![cose da fare:immagine_alt_testo](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
