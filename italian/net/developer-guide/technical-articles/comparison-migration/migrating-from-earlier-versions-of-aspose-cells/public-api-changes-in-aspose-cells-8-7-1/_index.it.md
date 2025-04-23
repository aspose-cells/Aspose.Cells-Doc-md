---
title: Modifiche all API pubblica in Aspose.Cells 8.7.1
type: docs
weight: 240
url: /it/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.7.0 a 8.7.1 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà aggiunta LookInType.OriginalValues**
Le API di Aspose.Cells supportano già la funzione [Trova o Cerca Dati](/cells/it/net/find-or-search-data/) per fogli elettronici al fine di trovare un particolare contenuto nella cella, che si tratti di valore o formula. Tuttavia, questa funzionalità mancava dell'aspetto della formattazione applicata alla cella che potrebbe modificare l'aspetto così come il valore dei contenuti, rendendo di conseguenza il testo non ricercabile utilizzando il valore originale. Con questo rilascio delle API di Aspose.Cells, un'altra costante denominata LookInType.OriginalValues è stata esposta all'API pubblica che consente di superare la situazione come discusso precedentemente.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzione, consulta l'articolo dettagliato su [Cerca Dati Utilizzando i Valori Originali](/cells/it/net/search-data-using-original-values/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 in cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formatted as ---

cell.Formula = "=Sum(A1:A2)";

//Calculate the workbook

workbook.CalculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.LookInType = LookInType.OriginalValues;

options.LookAtType = LookAtType.EntireContent;

Cell foundCell = null;

object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.Cells.Find(obj, foundCell, options);

//Print the found cell

Console.WriteLine(foundCell);

{{< /highlight >}}


### **Aggiunto evento OnBeforeColumnFilter per GridWeb**
Aspose.Cells.GridWeb per .NET 8.7.1 ha esposto l'evento OnBeforeColumnFilter che funge da callback per il meccanismo di filtraggio effettuato tramite l'interfaccia utente di GridWeb. Come suggerisce il nome, l'evento viene attivato prima dell'applicazione del filtraggio delle colonne e può essere utilizzato per ottenere le informazioni di filtraggio come l'indice della colonna e il valore su cui applicare il filtro.

Lo scenario di utilizzo semplice appare come segue.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
