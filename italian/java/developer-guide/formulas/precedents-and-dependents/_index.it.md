---
title: Precedenti e dipendenti
type: docs
weight: 230
url: /it/java/precedents-and-dependents/
---
{{% alert color="primary" %}} 

Fogli di lavoro finanziari complessi, specialmente quelli sviluppati in collaborazione, possono nascondere gli errori più imbarazzanti. Controllare l'accuratezza delle formule e trovare l'origine di un errore può essere difficile quando la formula utilizza celle precedenti e celle dipendenti.

{{% /alert %}} 
## **introduzione**
- **Cellule precedenti** sono celle a cui fa riferimento una formula in un altro Cell. Ad esempio, se la cella D10 contiene la formula =B5, la cella B5 è precedente alla cella D10.
- **Cellule dipendenti** contengono formule che fanno riferimento ad altre celle. Ad esempio, se la cella D10 contiene la formula =B5, la cella D10 dipende dalla cella B5.

Per rendere il foglio di calcolo facile da leggere, potresti voler mostrare chiaramente quali celle di un foglio di calcolo vengono utilizzate in una formula. Allo stesso modo, potresti voler estrarre le celle dipendenti di altre celle.

Aspose.Cells permette di rintracciare le celle e scoprire quali sono collegate.
## **Tracing precedente e dipendente Cells: Microsoft Excel**
Le formule possono cambiare in base alle modifiche apportate da un cliente. Ad esempio, se la cella C1 dipende da C3 e C4 che contengono una formula e C1 viene modificata (quindi la formula viene sovrascritta), C3 e C4 o altre celle devono essere modificate per bilanciare il foglio di calcolo in base alle regole aziendali.

Allo stesso modo, supponiamo che C1 contenga la formula "=(B1*22)/(M2*N32)". Voglio trovare le celle da cui dipende C1, cioè le celle precedenti B1, M2 e N32.

Potrebbe essere necessario tracciare la dipendenza di una particolare cella da altre celle. Se le regole aziendali sono incorporate nelle formule, vorremmo scoprire la dipendenza ed eseguire alcune regole basate su di essa. Allo stesso modo, se il valore di una particolare cella viene modificato, quali celle nel foglio di lavoro sono interessate da tale modifica?

Microsoft Excel consente agli utenti di tracciare precedenti e dipendenti.

1.  Sul**Visualizza la barra degli strumenti** , Selezionare**Controllo delle formule**. Verrà visualizzata la finestra di dialogo Formula Auditing.
1. Traccia precedenti:
1. Seleziona la cella che contiene la formula per la quale desideri trovare le celle precedenti.
 1. Per visualizzare una freccia tracciante su ciascuna cella che fornisce dati direttamente alla cella attiva, fare clic su**Traccia i precedenti** sul**Controllo delle formule** barra degli strumenti.
1. Traccia formule che fanno riferimento a una particolare cella (dipendenti)
 1. Selezionare la cella per la quale si desidera identificare le celle dipendenti.
 1. Per visualizzare una freccia tracciante su ciascuna cella che dipende dalla cella attiva, fare clic su Trace Dependents sulla barra degli strumenti Formula Auditing.
## **Tracing precedente e dipendente Cells: Aspose.Cells**
### **Rintracciare i precedenti**
Aspose.Cells rende facile ottenere celle precedenti. Non solo può recuperare celle che forniscono dati a precedenti di formule semplici, ma anche trovare celle che forniscono dati a precedenti di formule complesse con intervalli denominati.

Nell'esempio seguente viene utilizzato un file Excel modello, Book1.xls. Il foglio di calcolo contiene dati e formule nel primo foglio di lavoro.

 Aspose.Cells fornisce il[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) classe'[Ottieni precedenti](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedents() ) metodo utilizzato per tracciare i precedenti di una cella. Restituisce un[ReferredAreaCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredAreaCollection). Come puoi vedere sopra, in Book1.xls, la cella B7 contiene una formula "=SUM(A1:A3)". Quindi le celle A1:A3 sono le celle precedenti alla cella B7. L'esempio seguente mostra la funzione di traccia dei precedenti utilizzando il file modello Book1.xls.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingPrecedents.java" >}}
### **Tracciamento dei dipendenti**
Aspose.Cells ti consente di ottenere celle dipendenti nei fogli di calcolo. Aspose.Cells non solo può recuperare celle che forniscono dati relativi a una formula semplice, ma anche trovare celle che forniscono dati a dipendenti di una formula complessa con intervalli denominati.

 Aspose.Cells fornisce il[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) classe'[GetDependents](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependents(boolean)metodo utilizzato per tracciare i dipendenti di una cella. Ad esempio, in Book1.xlsx sono presenti le formule: "=A1+20" e "=A1+30" rispettivamente nelle celle B2 e C2. L'esempio seguente mostra come tracciare i dipendenti per la cella A1 utilizzando il file modello Book1.xlsx.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependents.java" >}}
### **Tracing delle celle precedenti e dipendenti secondo la catena di calcolo**
 Sopra apis di tracciare precedenti e dipendenti sono secondo l'espressione della formula stessa. Forniscono semplicemente un modo conveniente per l'utente di tracciare le interdipendenze per alcune formule. Se nella cartella di lavoro è presente una grande quantità di formule e l'utente deve tracciare precedenti e dipendenti per ogni cella, daranno prestazioni scadenti. Per tale situazione, l'utente dovrebbe considerare di utilizzare[GetPrecedentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getPrecedentsInCalculation() /) e[GetDependentsInCalculation](https://reference.aspose.com/cells/java/com.aspose.cells/Cell#getDependentsInCalculation(boolean) /) metodi. Questi due metodi tracciano le dipendenze in base alla catena di calcolo. Quindi, per usarli, devi prima abilitare la catena di calcolo di[Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/java/com.aspose.cells/FormulaSettings#EnableCalculationChain) . Quindi dovresti eseguire il calcolo completo per la cartella di lavoro di[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)). Successivamente, puoi rintracciare precedenti o dipendenti per tutte quelle celle di cui hai bisogno.

Per alcune formule, i precedenti risultanti potrebbero essere diversi per GetPrecedents e GetPrecedentsInCalculation e i dipendenti risultanti potrebbero essere diversi per GetDependents e GetDependentsInCalculation. Ad esempio, se la formula della cella A1 è "=IF(TRUE,B2,C3)", GetPrecedents fornirà B2 e C3 come precedente di A1. Di conseguenza, B2 e C3 hanno entrambi l'A1 dipendente durante il controllo tramite GetDependents. Tuttavia, per il calcolo di questa formula, è ovvio che solo B2 può influenzare il risultato calcolato. Quindi GetPrecedentsInCalculation non fornirà C3 per A1 e GetDependentsInCalculation non fornirà A1 per C3. A volte l'utente può avere solo il requisito di tracciare quelle interdipendenze che influiscono effettivamente sul risultato calcolato delle formule basate sui dati correnti della cartella di lavoro, quindi devono anche utilizzare GetDependentsInCalculation/GetPrecedentsInCalculation invece di GetDependents/GetPrecedents.

L'esempio seguente mostra come tracciare i precedenti e i dipendenti in base alla catena di calcolo per le celle:


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-TracingDependenciesInCalculation.java" >}}
