---
title: Modifiche all API pubblica in Aspose.Cells 8.7.1
type: docs
weight: 250
url: /it/java/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.7.0 a 8.7.1 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Proprietà LookInType.ORIGINAL_VALUES aggiunta**
Le API di Aspose.Cells supportano già la funzionalità [Trova o Cerca Dati](/cells/it/java/find-or-search-data/) per i fogli di calcolo al fine di individuare alcuni contenuti particolari nel valore della cella e nella formula. Tuttavia, questa funzionalità mancava dell'aspetto della formattazione applicata alla cella che può modificare l'aspetto così come il valore dei contenuti, rendendo di conseguenza il testo non cercabile utilizzando il valore originale. Con questa versione delle API Aspose.Cells, una nuova costante dal nome LookInType.ORIGINAL_VALUES è stata esposta all'API pubblica, che consente di superare la situazione discussa in precedenza. 

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Ricerca Dati Utilizzando Valori Originali](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

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
