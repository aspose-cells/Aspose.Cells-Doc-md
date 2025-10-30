---
title: Precedenti e Dipendenti
type: docs
weight: 100
url: /it/cpp/precedents-and-dependents/
---

{{% alert color="primary" %}} 

I fogli di lavoro finanziari complessi, specialmente quelli sviluppati in collaborazione, possono nascondere errori imbarazzanti. Verificare la precisione delle formule e trovare la fonte di un errore può essere difficile quando la formula utilizza celle precedenti e dipendenti.

{{% /alert %}} 
## **Introduzione**
- **Celle Precedenti** sono celle a cui una formula in un'altra cella fa riferimento. Ad esempio, se la cella D10 contiene la formula =B5, la cella B5 è precedente alla cella D10.
- Le **Celle Dipendenti** contengono formule che fanno riferimento ad altre celle. Ad esempio, se la cella D10 contiene la formula =B5, la cella D10 dipende dalla cella B5.

Per rendere il foglio di calcolo facile da leggere, potresti voler mostrare chiaramente quali celle del foglio di calcolo sono utilizzate in una formula. Allo stesso modo, potresti voler estrarre le celle dipendenti da altre celle.

Aspose.Cells ti consente di tracciare le celle e scoprire quali sono collegate.
## **Il Tracciamento delle Celle Precedenti e Dipendenti: Microsoft Excel**
Le formule possono cambiare in base alle modifiche apportate da un cliente. Ad esempio, se la cella C1 dipende da C3 e C4 contenenti una formula, e la cella C1 viene modificata (in modo che la formula venga sovrascritta), C3 e C4, o altre celle, devono cambiare per bilanciare il foglio di calcolo in base alle regole aziendali.

Allo stesso modo, supponiamo che la cella C1 contenga la formula "=(B1*22)/(M2*N32)". Voglio trovare le celle di cui C1 dipende, cioè le celle precedenti B1, M2 e N32.

Potresti aver bisogno di tracciare la dipendenza di una particolare cella verso altre celle. Se le regole aziendali sono incorporate nelle formule, vorremmo scoprire la dipendenza ed eseguire alcune regole in base ad essa. Allo stesso modo, se il valore di una particolare cella viene modificato, quali celle nel foglio di calcolo sono influenzate da tale modificare?

Microsoft Excel consente agli utenti di tracciare le celle precedenti e dipendenti.

1. Sulla **Barra degli Strumenti Visualizza**, seleziona **Auditing Formule**
1. Tracciare Precedenti:
   1. Seleziona la cella che contiene la formula per la quale desideri trovare le celle precedenti.
   1. Per visualizzare una freccia tracciante su ciascuna cella che fornisce direttamente dati alla cella attiva, fare clic su **Traccia Precedenti** sulla barra degli strumenti **Auditing delle Formule**.
1. Traccia delle formule che fanno riferimento a una particolare cella (dipendenti)
   1. Selezionare la cella per la quale si desidera identificare le celle dipendenti.
   1. Per visualizzare una freccia tracciante su ciascuna cella che dipende dalla cella attiva, fare clic su Traccia Dipendenti sulla barra degli strumenti dell'Auditing delle Formule.
## **Tracciamento delle Celle Precedenti e Dipendenti: Aspose.Cells**
### **Tracciamento dei Precedenti**
Aspose.Cells rende facile ottenere le celle precedenti. Non solo può recuperare le celle che forniscono dati alle precedenti formule semplici, ma può anche trovare le celle che forniscono dati alle precedenti formule complesse con intervalli denominati.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingPrecedents-new.cpp" >}}
### **Tracciamento dei Dipendenti**
Aspose.Cells consente di ottenere le celle dipendenti nei fogli di calcolo. Aspose.Cells può non solo recuperare le celle che forniscono dati relativi a una formula semplice, ma può anche trovare le celle che forniscono dati ai dipendenti formule complesse con intervalli denominati.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-TracingDependents-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
