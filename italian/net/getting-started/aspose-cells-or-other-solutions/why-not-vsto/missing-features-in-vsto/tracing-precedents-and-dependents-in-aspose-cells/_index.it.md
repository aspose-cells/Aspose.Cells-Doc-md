---
title: Tracciare i precedenti e i dipendenti in Aspose.Cells
type: docs
weight: 130
url: /it/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

I fogli di lavoro finanziari complessi, specialmente quelli sviluppati in collaborazione, possono nascondere errori imbarazzanti. Verificare la precisione delle formule e trovare la fonte di un errore può essere difficile quando la formula utilizza celle precedenti e dipendenti.

- Le **celle precedenti** sono celle a cui si fa riferimento in una formula in un'altra cella. Ad esempio, se la cella D10 contiene la formula =B5, la cella B5 è una cella precedente rispetto alla cella D10.
- Le **celle dipendenti** contengono formule che si riferiscono ad altre celle. Ad esempio, se la cella D10 contiene la formula =B5, la cella D10 è dipendente dalla cella B5.

Per rendere il foglio di calcolo facile da leggere, potresti voler mostrare chiaramente quali celle del foglio di calcolo sono utilizzate in una formula. Allo stesso modo, potresti voler estrarre le celle dipendenti da altre celle.

Aspose.Cells ti consente di tracciare le celle e scoprire quali sono collegate.

{{% /alert %}} 
## **Il Tracciamento delle Celle Precedenti e Dipendenti: Microsoft Excel**
Le formule possono cambiare in base alle modifiche apportate da un cliente. Ad esempio, se la cella C1 dipende da C3 e C4 che contiene una formula, e C1 viene modificata (quindi la formula viene sovrascritta), anche C3 e C4, o altre celle, devono cambiare per bilanciare il foglio di calcolo in base alle regole aziendali.

Allo stesso modo, supponiamo che C1 contenga la formula "=(B1*22)/(M2*N32)". Voglio trovare le celle di cui C1 dipende, ovvero le celle precedenti B1, M2 e N32.

Potresti aver bisogno di tracciare la dipendenza di una particolare cella con altre celle. Se le regole aziendali sono incorporate nelle formule, vorremmo scoprire la dipendenza ed eseguire alcune regole in base ad essa. Allo stesso modo, se il valore di una particolare cella viene modificato, quali celle nel foglio di lavoro sono influenzate da tale modifica?

Microsoft Excel consente agli utenti di tracciare le celle precedenti e dipendenti.

1. Sulla **Barra degli strumenti Visualizzazione**, seleziona **Audit delle formule**.
   Viene visualizzata la finestra di Dialogo di Audit delle formule. 
   **La finestra di dialogo di Audit delle formule** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Tracciare Precedenti:
   1. Seleziona la cella che contiene la formula per la quale desideri trovare le celle precedenti.
   1. Per visualizzare una freccia tracciante su ciascuna cella che fornisce direttamente dati alla cella attiva, fare clic su **Traccia Precedenti** sulla barra degli strumenti **Auditing delle Formule**.
1. Traccia delle formule che fanno riferimento a una particolare cella (dipendenti)
   1. Selezionare la cella per la quale si desidera identificare le celle dipendenti.
   1. Per visualizzare una freccia tracciante su ciascuna cella che dipende dalla cella attiva, fare clic su Traccia Dipendenti sulla barra degli strumenti dell'Auditing delle Formule.
## **Tracciamento delle Celle Precedenti e Dipendenti: Aspose.Cells**
### **Tracciamento dei Precedenti**
Aspose.Cells rende facile ottenere le celle precedenti. Non solo può recuperare le celle che forniscono dati a precedenti formule semplici ma può anche trovare le celle che forniscono dati a precedenti formule complesse con nomi definiti.

Nell'esempio sottostante viene utilizzato un file excel modello, Book1.xls. Il foglio di calcolo contiene dati e formule nel primo Foglio di lavoro.

**Il foglio di calcolo di input** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells fornisce il metodo GetPrecedents della classe Cell utilizzato per tracciare i precedenti di una cella. Restituisce una ReferredAreaCollection. Come si può vedere sopra, nel file Book1.xls, la cella B7 contiene la formula =SUM(A1:A3). Quindi le celle A1:A3 sono le celle precedenti alla cella B7. L'esempio seguente dimostra la funzionalità del tracciamento dei precedenti utilizzando il file modello Book1.xls.

**C#**

{{< highlight csharp >}}

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
### **Tracciamento dei Dipendenti**
Aspose.Cells ti permette di ottenere le celle dipendenti nei fogli di calcolo. Aspose.Cells non solo può recuperare le celle che forniscono dati per una semplice formula ma può anche trovare le celle che forniscono dati per una complessa formula dipendente con nomi definiti.

Aspose.Cells fornisce il metodo GetDependents della classe Cell utilizzato per tracciare i dipendenti di una cella. Ad esempio, nel file Book1.xlsx ci sono formule: "=A1+20" e "=A1+30" nelle celle B2 e C2 rispettivamente. L'esempio seguente dimostra come tracciare i dipendenti per la cella A1 utilizzando il file modello Book1.xlsx.

**C#**

{{< highlight csharp >}}

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

