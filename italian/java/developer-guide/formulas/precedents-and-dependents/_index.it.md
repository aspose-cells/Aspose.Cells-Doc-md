---
title: Precedenti e Dipendenti
type: docs
weight: 230
url: /it/java/precedents-and-dependents/
---

{{% alert color="primary" %}} 

I fogli di lavoro finanziari complessi, specialmente quelli sviluppati in collaborazione, possono nascondere errori imbarazzanti. Verificare la precisione delle formule e trovare la fonte di un errore può essere difficile quando la formula utilizza celle precedenti e dipendenti.

{{% /alert %}} 
## **Introduzione**
- Le **celle precedenti** sono celle a cui si fa riferimento in una formula in un'altra cella. Ad esempio, se la cella D10 contiene la formula =B5, la cella B5 è una cella precedente rispetto alla cella D10.
- Le **Celle Dipendenti** contengono formule che fanno riferimento ad altre celle. Ad esempio, se la cella D10 contiene la formula =B5, la cella D10 dipende dalla cella B5.

Per rendere il foglio di calcolo facile da leggere, potresti voler mostrare chiaramente quali celle del foglio di calcolo sono utilizzate in una formula. Allo stesso modo, potresti voler estrarre le celle dipendenti da altre celle.

Aspose.Cells ti consente di tracciare le celle e scoprire quali sono collegate.
## **Il Tracciamento delle Celle Precedenti e Dipendenti: Microsoft Excel**
Le formule possono cambiare in base alle modifiche apportate da un cliente. Ad esempio, se la cella C1 dipende da C3 e C4 contenenti una formula, e la cella C1 viene modificata (in modo che la formula venga sovrascritta), C3 e C4, o altre celle, devono cambiare per bilanciare il foglio di calcolo in base alle regole aziendali.

Allo stesso modo, supponiamo che la cella C1 contenga la formula "=(B1*22)/(M2*N32)". Voglio trovare le celle di cui C1 dipende, cioè le celle precedenti B1, M2 e N32.

Potresti aver bisogno di tracciare la dipendenza di una particolare cella verso altre celle. Se le regole aziendali sono incorporate nelle formule, vorremmo scoprire la dipendenza ed eseguire alcune regole in base ad essa. Allo stesso modo, se il valore di una particolare cella viene modificato, quali celle nel foglio di calcolo sono influenzate da tale modificare?

Microsoft Excel consente agli utenti di tracciare le celle precedenti e dipendenti.

1. Nella **Barra degli strumenti Vista**, seleziona **Verifica formule**. Verrà visualizzata la finestra di verifica delle formule.
1. Tracciare Precedenti:
   1. Seleziona la cella che contiene la formula per la quale desideri trovare le celle precedenti.
   1. Per visualizzare una freccia tracciante su ciascuna cella che fornisce direttamente dati alla cella attiva, fare clic su **Traccia Precedenti** sulla barra degli strumenti **Auditing delle Formule**.
1. Traccia delle formule che fanno riferimento a una particolare cella (dipendenti)
   1. Selezionare la cella per la quale si desidera identificare le celle dipendenti.
   1. Per visualizzare una freccia tracciante su ciascuna cella che dipende dalla cella attiva, fare clic su Traccia Dipendenti sulla barra degli strumenti dell'Auditing delle Formule.
## **Tracciamento delle Celle Precedenti e Dipendenti: Aspose.Cells**
### **Tracciamento dei Precedenti**
Aspose.Cells rende facile ottenere le celle precedenti. Non solo può recuperare le celle che forniscono dati alle precedenti formule semplici, ma può anche trovare le celle che forniscono dati alle precedenti formule complesse con intervalli denominati.

Nell'esempio sottostante viene utilizzato un file excel modello, Book1.xls. Il foglio di calcolo contiene dati e formule nel primo Foglio di lavoro.

Aspose.Cells fornisce il metodo [GetPrecedents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents--) della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell), utilizzato per tracciare i precedenti di una cella. Restituisce una [ReferredAreaCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection). Come si può vedere, in Book1.xls, la cella B7 contiene la formula "=SUM(A1:A3)". Quindi le celle A1:A3 sono le celle precedenti alla cella B7. L'esempio seguente mostra la funzionalità di tracciamento dei precedenti utilizzando il file modello Book1.xls.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **Tracciamento dei Dipendenti**
Aspose.Cells ti consente di ottenere le celle dipendenti nei fogli di calcolo. Aspose.Cells non solo può recuperare le celle che forniscono dati riguardanti una semplice formula, ma può anche trovare le celle che forniscono dati ai dipendenti di una formula complessa con nomi definiti.

Aspose.Cells fornisce il metodo [GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents(boolean)) della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell), utilizzato per tracciare i dipendenti di una cella. Ad esempio, in Book1.xlsx ci sono le formule: "=A1+20" e "=A1+30" nelle celle B2 e C2 rispettivamente. L'esempio seguente mostra come tracciare i dipendenti per la cella A1 utilizzando il file modello Book1.xlsx.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **Tracciamento delle celle precedenti e dipendenti secondo la catena di calcolo**
Le API sopra per il tracciamento dei precedenti e dei dipendenti si riferiscono all'espressione della formula stessa. Forniscono semplicemente un modo conveniente per tracciare le interdipendenze per poche formule. Se ci sono un gran numero di formule nel foglio di lavoro e l'utente ha bisogno di tracciare i precedenti e i dipendenti per ogni cella, forniranno prestazioni scadenti. In tal caso, l'utente dovrebbe considerare di utilizzare i metodi [GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation--) e [GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation(boolean)/). Questi due metodi tracciano le dipendenze secondo la catena di calcolo. Quindi, per usarli, è necessario abilitare prima la catena di calcolo con [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain). Quindi è necessario eseguire il calcolo completo per il foglio di lavoro con [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)). Dopo di che, è possibile tracciare i precedenti o i dipendenti per tutte quelle celle di cui si ha bisogno.

Per alcune formule, i precedenti risultanti possono essere diversi per GetPrecedents e GetPrecedentsInCalculation, e i dipendenti risultanti possono essere diversi per GetDependents e GetDependentsInCalculation. Ad esempio, se la formula della cella A1 è "=IF(TRUE,B2,C3)", GetPrecedents fornirà B2 e C3 come precedenti di A1. Di conseguenza, B2 e C3 entrambi hanno il dipendente A1 quando controllato da GetDependents. Tuttavia, per il calcolo di questa formula, è ovvio che solo B2 può influenzare il risultato calcolato. Quindi GetPrecedentsInCalculation non fornirà C3 per A1, e GetDependentsInCalculation non fornirà A1 per C3. A volte l'utente può avere solo il requisito di tracciare quelle interdipendenze che influenzano effettivamente il risultato calcolato delle formule in base ai dati attuali del foglio di calcolo, quindi devono anche utilizzare GetDependentsInCalculation/GetPrecedentsInCalculation invece di GetDependents/GetPrecedents.

L'esempio seguente mostra come tracciare i precedenti e i dipendenti secondo la catena di calcolo per le celle:


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
