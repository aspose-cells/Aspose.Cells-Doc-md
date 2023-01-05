---
title: Imposta i titoli di stampa
type: docs
weight: 30
url: /it/net/set-print-titles/
---
## **Aspose.Cells - Imposta Titoli Stampa**
Aspose.Cells consente di designare le intestazioni di riga e colonna da ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, usa il[Impostazione della pagina](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)proprietà PrintTitleColumns e PrintTitleRows della classe.

Le righe o le colonne che verranno ripetute vengono definite passando i loro numeri di riga o colonna. Ad esempio, le righe sono definite come $1:$2 e le colonne sono definite come $A:$B.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scaricamento**Imposta i titoli di stampa** formare uno dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Impostazione delle opzioni di stampa](/cells/it/net/setting-print-options/).

{{% /alert %}}
