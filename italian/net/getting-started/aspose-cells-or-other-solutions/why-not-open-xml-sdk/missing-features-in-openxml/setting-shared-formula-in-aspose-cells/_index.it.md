---
title: Impostare la Formula Condivisa in Aspose.Cells
type: docs
weight: 110
url: /it/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

Supponiamo di avere un foglio di lavoro riempito con dati.

Desideri aggiungere una funzione in B2 che calcolerà l'IVA per la prima riga di dati. L'IVA è del **9%**. La formula che calcola l'IVA è: **"=A2*0.09"**. Questo articolo spiega come applicare questa formula con Aspose.Cells.

{{% /alert %}} 

Aspose.Cells ti permette di specificare una formula utilizzando la proprietà Cell.Formula.

Ci sono due opzioni per aggiungere formule alle altre celle (B3, B4, B5 e così via) nella colonna.

Oppure fare ciò che hai fatto per la prima cella, impostando effettivamente la formula per ogni cella, aggiornando di conseguenza il riferimento della cella (A3*0.09, A4*0.09, A5*0.09 e così via). Questo richiede l'aggiornamento dei riferimenti di cella per ogni riga. Richiede anche che Aspose.Cells analizzi singolarmente ciascuna formula, il che può richiedere tempo per fogli di calcolo grandi e formule complesse. Aggiunge anche righe extra di codice anche se i cicli possono ridurle in qualche misura.

Un altro approccio è utilizzare una **formula condivisa**. Con una formula condivisa, le formule vengono aggiornate automaticamente per i riferimenti delle celle in ogni riga in modo che l'IVA sia calcolata correttamente. Il metodo Cell.SetSharedFormula è più efficiente del primo metodo.

L'esempio seguente mostra come utilizzarla.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Shared Formula.xlsx";

//Instantiate a Workbook from existing file

Workbook workbook = new Workbook(FileName);

//Get the cells collection in the first worksheet

Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

//Apply the shared formula in the range i.e.., B2:B14

cells["B2"].SetSharedFormula("=A2*0.09", 13, 1);

//Save the excel file

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Scarica Esempio in Esecuzione**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
