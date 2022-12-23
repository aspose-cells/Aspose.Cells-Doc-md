---
title: Finestra dell'editor di formule
type: docs
weight: 20
url: /it/reportingservices/formula-editor-window/
---
{{% alert color="primary" %}} 

L'editor di formule consente di creare formule per un report.

{{% /alert %}} 

Per modificare una formula in una cella Excel Microsoft:

1. In Microsoft Excel selezionare una cella.
1.  Aprire la finestra di dialogo Modifica formula facendo clic**Modifica Formula** sulla barra degli strumenti.
   ([Aggiunta di formule di Reporting Services](/cells/it/reportingservices/adding-reporting-services-formulas/) illustra un esempio che modifica una formula.)
 La finestra di dialogo è divisa in sezioni: l'area di modifica in alto e l'area delle formule in basso. Utilizzare l'area della formula per popolare l'area di modifica.
1.  Selezionare una categoria (utente, parametri, campi ecc.) dal**Campi del rapporto** list (l'elenco a sinistra).
1.  Seleziona il tipo da**Funzioni** elenco (al centro).
1.  Seleziona un'opzione da**Operatori** lista (la lista a destra).
1.  Clic**Inserire**per aggiungere l'espressione a**Modificare** la zona.
1.  Clic**Inserire** quando l'espressione è completa.
 La formula viene inserita nella cella.

**La finestra di dialogo Modifica formula** 

![cose da fare:immagine_alt_testo](formula-editor-window_1.png)

La finestra di dialogo Modifica formula è suddivisa in sezioni, descritte di seguito.
#### **Modifica zona**
 Questa è l'area in cui crei o modifichi una formula. Creare una formula facendo doppio clic su uno dei componenti elencati nel file**Campi del rapporto**, **Funzioni** o**Operatori** elenchi. Quando si sceglie un componente, viene inserita anche la sintassi richiesta. Puoi anche inserire manualmente una formula.
#### **Zona Formula**
L'area della formula contiene tre sezioni, ciascuna delle quali elenca le informazioni utilizzate per creare una formula.

- Campi del rapporto: l'elenco a sinistra elenca tutti i campi del database accessibili per il rapporto. Elenca anche eventuali formule o gruppi già creati.
- Funzioni: l'elenco centrale contiene funzioni, procedure predefinite che restituiscono valori. Eseguono calcoli come MEDIA, SOMMA, CONTEGGIO, SIN, MAIUSCOLO e così via.
- Operatori - i "verbi di azione" usati nelle formule. Gli operatori descrivono un'operazione o un'azione da eseguire tra due o più valori. Esempi di operatori: addizione, sottrazione, minore di e maggiore di ecc.
#### **Controlli**
La finestra di dialogo ha diversi controlli:

|**Nome pulsante** |**Descrizione** |
|:- |:- |
| Annullare| Annulla un'azione.|
| Impasto| Incolla nell'area di modifica una stringa di caratteri costituita dai componenti elencati nell'area della formula.|
| Inserire| Prende il valore nell'area di modifica e lo inserisce come formula in una cella.|
| Uscita| Chiude l'editor di formule.|
{{% alert color="primary" %}} 

Argomenti correlati:

- [Elenco delle formule](/cells/it/reportingservices/formula-list/) - un elenco di campi e operatori.

{{% /alert %}}
