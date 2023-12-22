---
title: Precedenti e dipendenti
type: docs
weight: 100
url: /it/cpp/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Fogli di lavoro finanziari complessi, soprattutto quelli sviluppati in collaborazione, possono nascondere gli errori più imbarazzanti. Controllare l'accuratezza delle formule e trovare l'origine di un errore può essere difficile quando la formula utilizza celle precedenti e celle dipendenti.

{{% /alert %}} 
##  **introduzione**
- **Celle precedenti** sono celle a cui fa riferimento una formula in un'altra cella. Ad esempio, se la cella D10 contiene la formula =B5, la cella B5 è un precedente della cella D10.
- **Celle dipendenti** contengono formule che si riferiscono ad altre celle. Ad esempio, se la cella D10 contiene la formula =B5, la cella D10 dipende dalla cella B5.

Per rendere il foglio di calcolo facile da leggere, potresti voler mostrare chiaramente quali celle di un foglio di calcolo vengono utilizzate in una formula. Allo stesso modo, potresti voler estrarre le celle dipendenti di altre celle.

Aspose.Cells permette di tracciare le celle e scoprire quali sono collegate.
##  **Tracciamento precedente e dipendente Cells: Microsoft Excel**
Le formule possono cambiare in base alle modifiche apportate da un cliente. Ad esempio, se la cella C1 dipende da C3 e C4 che contengono una formula e C1 viene modificata (quindi la formula viene sovrascritta), C3 e C4, o altre celle, devono essere modificate per bilanciare il foglio di calcolo in base alle regole aziendali.

Allo stesso modo, supponiamo che C1 contenga la formula "=(B1*22)/(M2*N32)". Voglio trovare le celle da cui dipende C1, ovvero le celle precedenti B1, M2 e N32.

Potrebbe essere necessario tracciare la dipendenza di una particolare cella da altre celle. Se le regole aziendali sono incorporate nelle formule, vorremmo scoprire la dipendenza ed eseguire alcune regole basate su di essa. Allo stesso modo, se il valore di una particolare cella viene modificato, quali celle del foglio di lavoro saranno interessate da tale modifica?

Microsoft Excel consente agli utenti di risalire a precedenti e dipendenti.

1.  Sul**Visualizza barra degli strumenti**, seleziona **Controllo formula**
1. Traccia precedenti:
 1. Seleziona la cella che contiene la formula per la quale desideri trovare le celle precedenti.
 1. Per visualizzare una freccia tracciante su ciascuna cella che fornisce direttamente i dati alla cella attiva, fare clic su**Tracciare i precedenti** sul**Controllo delle formule** barra degli strumenti.
1. Tracciare le formule che fanno riferimento a una cella particolare (dipendenti)
 1. Seleziona la cella per la quale desideri identificare le celle dipendenti.
1. Per visualizzare una freccia di tracciamento su ciascuna cella che dipende dalla cella attiva, fare clic su Traccia dipendenti sulla barra degli strumenti Controllo formula.
##  **Tracciamento Precedenti e Dipendenti Cells: Aspose.Cells**
###  **Tracciare i precedenti**
Aspose.Cells semplifica il recupero delle celle precedenti. Non solo può recuperare celle che forniscono dati a formule precedenti semplici, ma anche trovare celle che forniscono dati a formule precedenti complesse con intervalli denominati.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents-new.cpp" >}}
###  **Tracciamento dei dipendenti**
Aspose.Cells ti consente di ottenere celle dipendenti nei fogli di calcolo. Aspose.Cells non solo può recuperare celle che forniscono dati relativi a una formula semplice, ma anche trovare celle che forniscono dati a dipendenti di formule complesse con intervalli denominati.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents-new.cpp" >}}
