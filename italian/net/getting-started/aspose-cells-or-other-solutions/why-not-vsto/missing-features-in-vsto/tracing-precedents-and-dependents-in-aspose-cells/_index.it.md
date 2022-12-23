---
title: Rintracciare precedenti e dipendenti in Aspose.Cells
type: docs
weight: 130
url: /it/net/tracing-precedents-and-dependents-in-aspose-cells/
---
{{% alert color="primary" %}} 

Fogli di lavoro finanziari complessi, specialmente quelli sviluppati in collaborazione, possono nascondere gli errori più imbarazzanti. Controllare l'accuratezza delle formule e trovare l'origine di un errore può essere difficile quando la formula utilizza celle precedenti e celle dipendenti.

- **Cellule precedenti** sono celle a cui fa riferimento una formula in un altro Cell. Ad esempio, se la cella D10 contiene la formula =B5, la cella B5 è precedente alla cella D10.
- **Cellule dipendenti** contengono formule che fanno riferimento ad altre celle. Ad esempio, se la cella D10 contiene la formula =B5, la cella D10 dipende dalla cella B5.

Per rendere il foglio di calcolo facile da leggere, potresti voler mostrare chiaramente quali celle di un foglio di calcolo vengono utilizzate in una formula. Allo stesso modo, potresti voler estrarre le celle dipendenti di altre celle.

Aspose.Cells permette di rintracciare le celle e scoprire quali sono collegate.

{{% /alert %}} 
## **Tracing precedente e dipendente Cells: Microsoft Excel**
Le formule possono cambiare in base alle modifiche apportate da un cliente. Ad esempio, se la cella C1 dipende da C3 e C4 che contengono una formula e C1 viene modificata (quindi la formula viene sovrascritta), C3 e C4 o altre celle devono essere modificate per bilanciare il foglio di calcolo in base alle regole aziendali.

Allo stesso modo, supponiamo che C1 contenga la formula "=(B1*22)/(M2*N32)". Voglio trovare le celle da cui dipende C1, cioè le celle precedenti B1, M2 e N32.

Potrebbe essere necessario tracciare la dipendenza di una particolare cella da altre celle. Se le regole aziendali sono incorporate nelle formule, vorremmo scoprire la dipendenza ed eseguire alcune regole basate su di essa. Allo stesso modo, se il valore di una particolare cella viene modificato, quali celle nel foglio di lavoro sono interessate da tale modifica?

Microsoft Excel consente agli utenti di rintracciare precedenti e dipendenti.

1.  Sul**Visualizza la barra degli strumenti** , Selezionare**Controllo delle formule**.
 Viene visualizzata la finestra di dialogo Controllo formula.
   **La finestra di dialogo Controllo formule** 

![cose da fare:immagine_alt_testo](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Traccia precedenti:
1. Seleziona la cella che contiene la formula per la quale desideri trovare le celle precedenti.
 1. Per visualizzare una freccia tracciante su ciascuna cella che fornisce dati direttamente alla cella attiva, fare clic su**Traccia i precedenti** sul**Controllo delle formule** barra degli strumenti.
1. Traccia formule che fanno riferimento a una particolare cella (dipendenti)
 1. Selezionare la cella per la quale si desidera identificare le celle dipendenti.
 1. Per visualizzare una freccia tracciante su ciascuna cella che dipende dalla cella attiva, fare clic su Trace Dependents sulla barra degli strumenti Formula Auditing.
## **Tracing precedente e dipendente Cells: Aspose.Cells**
### **Rintracciare i precedenti**
Aspose.Cells rende facile ottenere celle precedenti. Non solo può recuperare celle che forniscono dati a precedenti di una formula semplice, ma anche trovare celle che forniscono dati a precedenti di una formula complessa con intervalli denominati.

Nell'esempio seguente viene utilizzato un file Excel modello, Book1.xls. Il foglio di calcolo contiene dati e formule nel primo foglio di lavoro.

**Il foglio di calcolo di input** 

![cose da fare:immagine_alt_testo](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells fornisce il metodo GetPrecedents della classe Cell utilizzato per tracciare i precedenti di una cella. Restituisce una ReferredAreaCollection. Come puoi vedere sopra, in Book1.xls, la cella B7 contiene una formula "=SUM(A1:A3)". Quindi le celle A1:A3 sono le celle precedenti alla cella B7. L'esempio seguente mostra la funzione di traccia dei precedenti utilizzando il file modello Book1.xls.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("book1.xls");

Cells cells = workbook.Worksheets[0].Cells;

Aspose.Cells.Cell cell = cells["B7"];

//Tracing precedents of the cell B7.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.GetPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.Count; m++)

  {

    ReferredArea area = ret[m];

    StringBuilder stringBuilder = new StringBuilder();

    if (area.IsExternalLink)

    {

        stringBuilder.Append("[");

        stringBuilder.Append(area.ExternalFileName);

        stringBuilder.Append("]");

     }

     stringBuilder.Append(area.SheetName);

     stringBuilder.Append("!");

     stringBuilder.Append(CellsHelper.CellIndexToName(area.StartRow, area.StartColumn));

     if (area.IsArea)

      {

          stringBuilder.Append(":");

          stringBuilder.Append(CellsHelper.CellIndexToName(area.EndRow, area.EndColumn));

      }


      Console.WriteLine(stringBuilder.ToString());

   }

}



{{< /highlight >}}
### **Tracciamento dei dipendenti**
Aspose.Cells ti consente di ottenere celle dipendenti nei fogli di calcolo. Aspose.Cells non solo può recuperare celle che forniscono dati relativi a una formula semplice, ma anche trovare celle che forniscono dati a dipendenti di una formula complessa con intervalli denominati.

Aspose.Cells fornisce il metodo GetDependents della classe Cell utilizzato per tracciare i dipendenti di una cella. Ad esempio, in Book1.xlsx sono presenti le formule: "=A1+20" e "=A1+30" rispettivamente nelle celle B2 e C2. L'esempio seguente mostra come tracciare i dipendenti per la cella A1 utilizzando il file modello Book1.xlsx.

**C#**

{{< highlight "csharp" >}}

 string path = "Book1.xlsx";

Workbook workbook = new Workbook(path);

Worksheet worksheet = workbook.Worksheets[0];

var c = worksheet.Cells["A1"];

var dependents = c.GetDependents(true);

foreach (var dependent in dependents)

{

     Debug.WriteLine(string.Format("{0} ---- {1} : {2}", dependent.Worksheet.Name, dependent.Name, dependent.Value));

}

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

