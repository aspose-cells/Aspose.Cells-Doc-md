---
title: Precedenti e Dipendenti
type: docs
weight: 230
url: /it/python-net/precedents-and-dependents/
---

{{% alert color="primary" %}} 

I fogli di lavoro finanziari complessi, specialmente quelli sviluppati in collaborazione, possono nascondere errori imbarazzanti. Verificare la precisione delle formule e trovare la fonte di un errore può essere difficile quando la formula utilizza celle precedenti e dipendenti.

{{% /alert %}} 
## **Introduzione**
- Le **celle precedenti** sono celle a cui si fa riferimento in una formula in un'altra cella. Ad esempio, se la cella D10 contiene la formula =B5, la cella B5 è una cella precedente rispetto alla cella D10.
- Le **Celle Dipendenti** contengono formule che fanno riferimento ad altre celle. Ad esempio, se la cella D10 contiene la formula =B5, la cella D10 dipende dalla cella B5.

Per rendere il foglio di calcolo facile da leggere, potresti voler mostrare chiaramente quali celle del foglio di calcolo sono utilizzate in una formula. Allo stesso modo, potresti voler estrarre le celle dipendenti da altre celle.

Aspose.Cells for Python via .NET permette di rintracciare le celle e scoprire quali sono collegate.
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
## **Tracciare celle precedent e dipendenti: Aspose.Cells for Python via .NET**
### **Tracciamento dei Precedenti**
Aspose.Cells for Python via .NET semplifica l'ottenimento delle celle precedent. Può recuperare le celle che forniscono dati ai precedenti di formule semplici o trovare celle che forniscono dati ai precedenti di formule complesse con intervalli denominati.

Nell'esempio sottostante viene utilizzato un file excel modello, Book1.xls. Il foglio di calcolo contiene dati e formule nel primo Foglio di lavoro.

Aspose.Cells for Python via .NET fornisce la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) e il metodo [**get_precedents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents/#) usati per tracciare i precedenti di una cella. Restituisce un [**ReferredAreaCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/referredareacollection). Come mostrato sopra, nel file Book1.xls, la cella B7 contiene la formula "=SUM(A1:A3)". Quindi, le celle A1:A3 sono i precedenti della cella B7. Il seguente esempio dimostra la funzione di tracciamento dei precedenti usando il file modello Book1.xls.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingPrecedents-1.py" >}}
### **Tracciamento dei Dipendenti**
Aspose.Cells for Python via .NET ti permette di ottenere le celle dipendenti nei fogli di calcolo. Aspose.Cells for Python via .NET non solo può recuperare le celle che forniscono dati riguardo a formule semplici, ma anche trovare celle che forniscono dati ai dipendenti di formule complesse con intervalli denominati.

Aspose.Cells for Python via .NET fornisce la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) e il metodo [**get_dependents**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents/#bool) usati per tracciare i dipendenti di una cella. Ad esempio, in Book1.xlsx ci sono formule: "=A1+20" e "=A1+30" rispettivamente nelle celle B2 e C2. Il seguente esempio dimostra come tracciare i dipendenti per la cella A1 usando il file modello Book1.xlsx.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependents-1.py" >}}

### **Tracciamento delle celle precedenti e dipendenti secondo la catena di calcolo**
Le API sopra per tracciare precedenti e dipendenti sono secondo l'espressione della formula stessa. Offrono semplicemente un modo conveniente per tracciare le interdipendenze di alcune formule. Se ci sono molte formule nel workbook e l'utente ha bisogno di tracciare precedenti e dipendenti per ogni cella, le prestazioni saranno scarse. Per tali situazioni, si consiglia di usare i metodi [**get_precedents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_precedents_in_calculation/#) e [**get_dependents_in_calculation**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_dependents_in_calculation/#bool). Questi due metodi tracciano le dipendenze secondo la catena di calcolo. Per usarli, prima bisogna abilitare la catena di calcolo tramite [**Workbook.settings.formula_settings.enable_calculation_chain**](https://reference.aspose.com/cells/python-net/aspose.cells/formulasettings/enable_calculation_chain/). Poi si esegue il calcolo completo del workbook tramite [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#). Successivamente, si può tracciare precedenti o dipendenti per tutte le celle necessarie.

Per alcune formule, i precedenti risultanti possono essere diversi per GetPrecedents e GetPrecedentsInCalculation, e i dipendenti risultanti possono essere diversi per GetDependents e GetDependentsInCalculation. Ad esempio, se la formula della cella A1 è "=IF(TRUE,B2,C3)", GetPrecedents fornirà B2 e C3 come precedenti di A1. Di conseguenza, B2 e C3 entrambi hanno il dipendente A1 quando controllato da GetDependents. Tuttavia, per il calcolo di questa formula, è ovvio che solo B2 può influenzare il risultato calcolato. Quindi GetPrecedentsInCalculation non fornirà C3 per A1, e GetDependentsInCalculation non fornirà A1 per C3. A volte l'utente può avere solo il requisito di tracciare quelle interdipendenze che influenzano effettivamente il risultato calcolato delle formule in base ai dati attuali del foglio di calcolo, quindi devono anche utilizzare GetDependentsInCalculation/GetPrecedentsInCalculation invece di GetDependents/GetPrecedents.

L'esempio seguente mostra come tracciare i precedenti e i dipendenti secondo la catena di calcolo per le celle:


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-TracingDependenciesInCalculation.py" >}}

{{< app/cells/assistant language="python-net" >}}
