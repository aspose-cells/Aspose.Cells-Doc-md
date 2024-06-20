---
title: Creazione di un report tabellare
type: docs
weight: 70
url: /it/reportingservices/creating-tabular-report/
---

{{% alert color="primary" %}} 

Una tabella in un modello di report Aspose.Cells è composta da un'intestazione, righe di dati della tabella, gruppi di righe e piè di pagina. Di seguito è mostrato un esempio di tabella.

**Un esempio di tabella** 

![todo:image_alt_text](creating-tabular-report_1.png)
#### **Intestazione della tabella**
L'intestazione della tabella contiene normalmente il titolo di ciascuna colonna della tabella e altri elementi testuali come testo statico, parametri del report, variabili globali del report e così via. L'intestazione della tabella è facoltativa. Se si utilizza un'intestazione, il tag dell'intestazione deve essere posto a sinistra della prima colonna dei dati della tabella per indicare che la riga è un'intestazione.
#### **Riga dei dati della tabella**
Una riga dei dati di una tabella è una riga di celle che contengono marker intelligenti. Una tabella può contenere solo una singola riga di dati.
#### **Gruppo di righe**
Il gruppo di righe segue strettamente la riga dei dati della tabella e comprende due parti: tag del gruppo e riga di dati del gruppo. 

Il tag del gruppo deve essere posizionato a sinistra della prima colonna dei dati della tabella per indicare che la riga è la riga di dati del gruppo. Il formato del tag del gruppo è ##group{NomeColonnaGruppo}, ad esempio ##group{NumeroOrdineVendita} dove NumeroOrdineVendita è uno dei nomi delle colonne del set di dati. Una tabella può contenere solo un gruppo di righe, ma un gruppo di righe può contenere più di una riga di dati del gruppo. Il tag del gruppo può essere posizionato solo nella prima riga di dati, come mostrato nell'esempio sopra.

Il tag del gruppo viene rimosso dal file di output di Microsoft Excel al momento del rendering. I gruppi di righe sono facoltativi.
#### **Piè di pagina**
I piè di pagina vengono dopo il gruppo di righe e includono tre parti: tag del piè di pagina, riga di dati del piè di pagina e area di testo del piè di pagina. 

Il tag del piè di pagina dovrebbe essere posizionato a sinistra della prima colonna della colonna dati della tabella che indica che la riga è il piè di pagina della tabella. Una tabella può contenere più di una riga di dati del piè di pagina e ogni riga del piè di pagina deve essere contrassegnata da un tag del piè di pagina. 

L'area di testo del piè di pagina può contenere testo statico, parametri del report e variabili globali del report, come mostrato nell'esempio sopra.

Il tag del piè di pagina viene rimosso dal file di output di Microsoft Excel al momento del rendering. I piè di pagina sono facoltativi.

L'output del modello di esempio è mostrato di seguito.

**Modello di esempio** 

![todo:image_alt_text](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Questa sezione include i seguenti argomenti:** 
- [Preparazione per la creazione di un report tabellare](/cells/it/reportingservices/preparing-for-creating-table-report/)
- [Aggiunta delle informazioni di base per la tabella](/cells/it/reportingservices/adding-base-information-for-table/)
- [Aggiunta delle formule dei servizi di report](/cells/it/reportingservices/adding-reporting-services-formulas/)
- [Aggiunta del gruppo di tabelle](/cells/it/reportingservices/adding-table-group/)
- [Aggiunta dei piè di pagina della tabella](/cells/it/reportingservices/adding-table-footers/)
- [Aggiunta dei parametri del report al report](/cells/it/reportingservices/adding-report-parameters-to-report/)
- [Aggiunta delle variabili globali dei servizi di report al report](/cells/it/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Impostazione degli attributi del report](/cells/it/reportingservices/setting-report-attributes/)
- [Modifica degli attributi del report](/cells/it/reportingservices/modifying-report-attributes/)
