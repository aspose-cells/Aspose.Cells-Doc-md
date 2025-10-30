---
title: Precedenti e Dipendenti con Node.js via C++
linktitle: Precedenti e Dipendenti
type: docs
weight: 230
url: /it/nodejs-cpp/precedents-and-dependents/
description: Impara a tracciare le celle precedent e dipendente nei fogli di calcolo utilizzando Aspose.Cells for Node.js via C++. Comprendi come identificare le celle collegate in fogli di calcolo finanziari complessi.
---

{{% alert color="primary" %}} 

I fogli di lavoro finanziari complessi, specialmente quelli sviluppati in collaborazione, possono nascondere errori imbarazzanti. Verificare la precisione delle formule e trovare la fonte di un errore può essere difficile quando la formula utilizza celle precedenti e dipendenti.

{{% /alert %}} 
## **Introduzione**
- Le **celle precedenti** sono celle a cui si fa riferimento in una formula in un'altra cella. Ad esempio, se la cella D10 contiene la formula =B5, la cella B5 è una cella precedente rispetto alla cella D10.
- **Celle dipendenti** contengono formule che si riferiscono ad altre celle. Ad esempio, se la cella D10 contiene la formula =B5, la cella D10 dipende dalla cella B5.

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
   1. Per visualizzare una freccia traccia a ciascuna cella che dipende dalla cella attiva, clicca su **Traccia Dipendenti** sulla barra degli strumenti di auditing delle formule.
## **Tracciamento delle Celle Precedenti e Dipendenti: Aspose.Cells**
### **Tracciamento dei Precedenti**
Aspose.Cells rende facile ottenere le celle precedenti. Non solo può recuperare le celle che forniscono dati alle precedenti formule semplici, ma può anche trovare le celle che forniscono dati alle precedenti formule complesse con intervalli denominati.

Nell'esempio sottostante viene utilizzato un file excel modello, Book1.xls. Il foglio di calcolo contiene dati e formule nel primo Foglio di lavoro.

Aspose.Cells fornisce il metodo [Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--) della classe [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) usato per tracciare i precedenti di una cella. Ritorna una collezione di aree riferite. Come mostrato sopra, in Book1.xls, la cella B7 contiene una formula "=SUM(A1:A3)". Pertanto, le celle A1:A3 sono le precedenti della cella B7. Il seguente esempio dimostra la funzione di tracciamento dei precedenti usando il file modello Book1.xls.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B4");
// Check if the cell object is not null before proceeding
if (cell) 
{
const ret = cell.getPrecedents();
if (!ret.isNull() && ret.getCount() > 0)
{
const area = ret.get(0);
console.log(area.getSheetName());
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));
}
else
{
console.error("No precedents found for the cell.");
}
} 
else 
{
console.error("Cell B4 is null.");
}
```
### **Tracciamento dei Dipendenti**
Aspose.Cells permette di ottenere le celle dipendenti nei fogli di calcolo. Aspose.Cells non solo può recuperare le celle che forniscono dati riguardo a una formula semplice ma anche trovare le celle che forniscono dati ai dipendenti di formule complesse con intervalli nominati.

Aspose.Cells fornisce il metodo [Cell.getDependents(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-) della classe [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) usato per tracciare i dipendenti di una cella. Ad esempio, in Book1.xlsx ci sono formule: "=A1+20" e "=A1+30" nelle celle B2 e C2 rispettivamente. Il seguente esempio mostra come tracciare i dipendenti della cella A1 usando il file modello Book1.xlsx.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B2");
// Ensure dependents is an array
const dependents = cell.getDependents(true);

if (Array.isArray(dependents)) 
{
for (const c of dependents) 
{
console.log(c.getName());
}
} 
else 
{
console.error("Dependents is not an array");
}
```
### **Tracciamento delle celle precedenti e dipendenti secondo la catena di calcolo**
Le API sopra per il tracciamento di precedenti e dipendenti sono basate sull'espressione della formula stessa. Forniscono semplicemente un modo comodo per gli utenti di tracciare le interdipendenze di alcune formule. Se ci sono molte formule nel workbook e l'utente ha bisogno di tracciare precedenti e dipendenti per ogni cella, questo porterà a scarse prestazioni. Per tale situazione, l'utente dovrebbe considerare l'uso di [Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--) e [Cell.getDependentsInCalculation(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-) metodi. Questi due metodi tracciano le dipendenze secondo la catena di calcolo. Quindi, per usarli, prima bisogna attivare la catena di calcolo tramite [FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--). Poi, si deve eseguire il calcolo completo del Workbook tramite [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--). Dopo ciò, si può tracciare i precedenti o i dipendenti per tutte le celle necessarie.

Per alcune formule, i precedenti risultanti possono differire tra getPrecedents e getPrecedentsInCalculation, e i dipendenti risultanti possono differire tra getDependents e getDependentsInCalculation. Ad esempio, se la formula di A1 è "=IF(TRUE,B2,C3)", getPrecedents fornirà B2 e C3 come precedenti di A1. Di conseguenza, B2 e C3 avranno entrambi A1 come dipendente quando si controlla con getDependents. Tuttavia, per il calcolo di questa formula, è ovvio che solo B2 può influenzare il risultato calcolato. Pertanto, getPrecedentsInCalculation non fornirà C3 per A1, e getDependentsInCalculation non fornirà A1 per C3. A volte gli utenti potrebbero avere solo l'esigenza di tracciare le interdipendenze che effettivamente influenzano il risultato calcolato delle formule in base ai dati attuali del Workbook, allora devono usare invece getDependentsInCalculation/getPrecedentsInCalculation.

Il seguente esempio dimostra come tracciare i precedenti e i dipendenti secondo la catena di calcolo per le celle:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
cells.get("A1").setFormula("=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2");
cells.get("A2").setFormula("=IF(TRUE,B2,B1)");
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);
workbook.calculateFormula();

let en = cells.get("B1").getDependentsInCalculation(false);
console.log("B1's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}


en = cells.get("B2").getDependentsInCalculation(false);
console.log("B2's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}

en = cells.get("A1").getPrecedentsInCalculation();
console.log("A1's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}


en = cells.get("A2").getPrecedentsInCalculation();
console.log("A2's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
