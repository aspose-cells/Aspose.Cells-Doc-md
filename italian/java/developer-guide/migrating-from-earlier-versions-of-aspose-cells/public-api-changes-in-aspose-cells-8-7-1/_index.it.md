---
title: Pubblico API Modifiche Aspose.Cells 8.7.1
type: docs
weight: 250
url: /it/java/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.7.0 alla 8.7.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Aggiunta proprietà LookInType.ORIGINAL_VALUES**
 Aspose.Cells le API supportano già il[Trova o cerca dati](/cells/it/java/find-or-search-data/)funzione per fogli di calcolo per trovare un particolare contenuto nel valore e nella formula della cella. Tuttavia, a questa funzionalità mancava l'aspetto della formattazione applicata alla cella che potrebbe modificare l'aspetto e il valore dei contenuti, rendendo di conseguenza il testo non ricercabile utilizzando il valore originale. Con questa versione delle API Aspose.Cells, è stata esposta al pubblico un'altra costante dal nome LookInType.ORIGINAL_VALUES API che consente di superare la situazione discussa sopra.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Cerca i dati utilizzando i valori originali](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add 10 in cell A1 and A2

worksheet.getCells().get("A1").putValue(10);

worksheet.getCells().get("A2").putValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.getCells().get("D4");

Style style = cell.getStyle();

style.setCustom("---");

cell.setStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formated as ---

cell.setFormula("=Sum(A1:A2)");

//Calculate the workbook

workbook.calculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.setLookInType(LookInType.ORIGINAL_VALUES);

options.setLookAtType(LookAtType.ENTIRE_CONTENT);

Cell foundCell = null;

Object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.getCells().find(obj, foundCell, options);

//Print the found cell

System.out.println(foundCell);

{{< /highlight >}}
