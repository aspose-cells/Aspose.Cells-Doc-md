---
title: Opzioni di Impostazione Pagina e di Stampa
type: docs
weight: 60
url: /it/python-net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

A volte, gli sviluppatori devono configurare l’impostazione della pagina e le opzioni di stampa per controllare il processo di stampa. Le impostazioni di pagina e di stampa offrono varie opzioni e sono pienamente supportate in Aspose.Cells per Python via .NET.

Questo articolo mostra come creare un’applicazione console in Visual Studio.Net, e applicare le impostazioni di pagina e le opzioni di stampa a un foglio di lavoro con alcune semplici righe di codice usando l'API Aspose.Cells per Python via .NET.

{{% /alert %}}

## **Lavorare con Impostazioni Pagina e di Stampa**

Per questo esempio, abbiamo creato un workbook in Microsoft Excel e usato Aspose.Cells per Python via .NET per impostare le opzioni di impostazione della pagina e di stampa.

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


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPageSetup-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPrintingOptions-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
