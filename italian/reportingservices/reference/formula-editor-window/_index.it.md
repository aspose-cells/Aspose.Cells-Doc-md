---
title: Finestra dell Editor di Formule
type: docs
weight: 20
url: /it/reportingservices/formula-editor-window/
---

{{% alert color="primary" %}} 

L'Editor di Formule consente di creare formule per un report.

{{% /alert %}} 

Per modificare una formula in una cella di Microsoft Excel:

1. In Microsoft Excel, seleziona una cella.
1. Apri il dialogo Modifica Formula cliccando su **Modifica Formula** sulla barra degli strumenti.
   ([Aggiunta di Formule dei Servizi di Reporting](/cells/it/reportingservices/adding-reporting-services-formulas/) illustra un esempio di modifica di una formula).
   Il dialogo è diviso in sezioni: l'area di modifica nella parte superiore e l'area della formula nella parte inferiore. Utilizza l'area della formula per popolare l'area di modifica.
1. Seleziona una categoria (utente, parametri, campi, ecc.) dall'elenco **Campi del Report** (l'elenco a sinistra).
1. Seleziona il tipo dall'elenco **Funzioni** (in mezzo).
1. Seleziona un'opzione dall'elenco **Operatori** (l'elenco a destra).
1. Fai clic su **Inserisci** per aggiungere l'espressione all'area di **Modifica**.
1. Fai clic su **Inserisci** quando l'espressione è completa.
   La formula viene inserita nella cella.

**Il dialogo Modifica Formula** 

![todo:image_alt_text](formula-editor-window_1.png)

Il dialogo Modifica Formula è diviso in sezioni, descritte di seguito.
#### **Area di Modifica**
Quest'area è dove puoi creare o modificare una formula. Crea una formula facendo doppio clic su uno dei componenti elencati negli elenchi **Campi del Report**, **Funzioni** o **Operatori**. Quando scegli un componente, viene anche inserita la sintassi richiesta. Puoi anche inserire manualmente una formula. 
#### **Area della Formula**
L'area della formula contiene tre sezioni, ciascuna elencante informazioni utilizzate per creare una formula.

- Campi del Report - l'elenco a sinistra elenca tutti i campi del database accessibili per il report. Elenca anche qualsiasi formula o gruppi già creati.
- Funzioni - la lista centrale contiene funzioni, procedure predefinite che restituiscono valori. Eseguono calcoli come MEDIA, SOMMA, CONTA, SEN, MAIUSCOLE e così via.
- Operatori - i “verbi d'azione” utilizzati nelle formule. Gli operatori descrivono un'operazione o un'azione da compiere tra due o più valori. Esempi di operatori: aggiungi, sottrai, minore di e maggiore di e così via.
#### **Controlli**
La finestra di dialogo ha diversi controlli:

|**Nome del Pulsante** |**Descrizione** |
| :- | :- |
|Undo |Annulla un'azione. |
|Paste |Incolla una stringa di caratteri composta dai componenti elencati nell'area della formula nell'area di modifica. |
|Insert |Prende il valore nell'area di modifica ed lo inserisce come formula in una cella. |
|Exit |Chiude l'Editor di Formule. |
{{% alert color="primary" %}} 

Argomenti correlati:

- [Elenco Formule](/cells/it/reportingservices/formula-list/) - un elenco di campi e operatori.

{{% /alert %}}
