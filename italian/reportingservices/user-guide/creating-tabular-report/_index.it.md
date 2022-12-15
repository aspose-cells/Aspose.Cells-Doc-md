---
title: Creazione di report tabulari
type: docs
weight: 70
url: /it/reportingservices/creating-tabular-report/
---
{{% alert color="primary" %}} 

Una tabella in un modello di report Aspose.Cells è costituita da un'intestazione, righe di dati della tabella, gruppi di righe e piè di pagina. Di seguito è mostrata una tabella di esempio.

**Una tabella di esempio** 

![cose da fare:immagine_alt_testo](creating-tabular-report_1.png)
#### **Intestazione tabella**
L'intestazione della tabella normalmente contiene il titolo di ogni colonna della tabella e altri elementi di testo come testo statico, parametri del report, variabili globali del report e così via. L'intestazione della tabella è facoltativa. Se si utilizza un'intestazione, il tag dell'intestazione deve essere posizionato a sinistra della prima colonna di dati della tabella per indicare che la riga è un'intestazione.
#### **Riga dati tabella**
Una riga di dati della tabella è una riga di celle che contengono marcatori intelligenti. Una tabella può contenere solo una singola riga di dati.
#### **Gruppo di righe**
Il gruppo di righe segue da vicino la riga di dati della tabella e comprende due parti: tag di gruppo e riga di dati di gruppo.

Il tag di gruppo deve essere posizionato a sinistra della prima colonna di dati della tabella per indicare che la riga è la riga di dati del gruppo di righe. Il formato del tag di gruppo è ##group{GroupColumn}, ad esempio ##group{SalesOrderNumber} dove SalesOrderNumber è uno dei nomi di colonna del set di dati. Una tabella può contenere solo un gruppo di righe, ma un gruppo di righe può contenere più di una riga di dati di gruppo. Il tag di gruppo può essere posizionato solo nella prima riga di dati, come mostrato nell'esempio precedente.

Il tag di gruppo viene rimosso dal file Microsoft Excel di output al momento del rendering. I gruppi di righe sono facoltativi.
#### **Piè di pagina**
 I piè di pagina vengono dopo il gruppo di righe e comprendono tre parti: tag del piè di pagina, riga di dati del piè di pagina e area di testo del piè di pagina.

Il tag del piè di pagina deve essere posizionato a sinistra della prima colonna della colonna dei dati della tabella che indica che la riga è il piè di pagina della tabella. Una tabella può contenere più di una riga di dati a piè di pagina e ogni riga a piè di pagina deve essere contrassegnata da un tag piè di pagina.

L'area di testo del piè di pagina può contenere testo statico, parametri del report e variabili globali del report, come mostrato nell'esempio precedente.

Il tag piè di pagina viene rimosso dal file Microsoft Excel di output al momento del rendering. I piè di pagina sono facoltativi.

L'output del modello di esempio è mostrato di seguito.

**Modello di esempio** 

![cose da fare:immagine_alt_testo](creating-tabular-report_2.png)

{{% /alert %}} 
###### **Questa sezione include i seguenti argomenti:**
- [Preparazione per la creazione di report tabella](/cells/it/reportingservices/preparing-for-creating-table-report/)
- [Aggiunta di informazioni di base per Table](/cells/it/reportingservices/adding-base-information-for-table/)
- [Aggiunta di formule di Reporting Services](/cells/it/reportingservices/adding-reporting-services-formulas/)
- [Aggiunta di un gruppo di tabelle](/cells/it/reportingservices/adding-table-group/)
- [Aggiunta di piè di pagina alla tabella](/cells/it/reportingservices/adding-table-footers/)
- [Aggiunta di parametri di report al report](/cells/it/reportingservices/adding-report-parameters-to-report/)
- [Aggiunta di variabili globali di Reporting Services al report](/cells/it/reportingservices/adding-reporting-services-global-variables-to-report/)
- [Impostazione degli attributi del report](/cells/it/reportingservices/setting-report-attributes/)
- [Modifica degli attributi del rapporto](/cells/it/reportingservices/modifying-report-attributes/)
