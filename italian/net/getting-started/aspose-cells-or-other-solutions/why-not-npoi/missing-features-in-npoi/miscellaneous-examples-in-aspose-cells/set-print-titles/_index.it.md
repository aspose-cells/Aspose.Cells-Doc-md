---
title: Impostare titoli di stampa
type: docs
weight: 30
url: /it/net/set-print-titles/
---

## **Aspose.Cells - Impostare titoli di stampa**
Aspose.Cells consente di designare intestazioni di righe e colonne da ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, utilizzare le proprietà PrintTitleColumns e PrintTitleRows della classe [PageSetup](https://reference.aspose.com/cells/net/aspose.cells/pagesetup).

Le righe o le colonne che verranno ripetute sono definite passando il loro numero di riga o colonna. Ad esempio, le righe sono definite come $1:$2 e le colonne sono definite come $A:$B.

**C#**

{{< highlight cs >}}

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
Scarica **Imposta titoli di stampa** da uno dei siti di codice sociale qui sotto:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Per maggiori dettagli, visita [Impostazione delle opzioni di stampa](/cells/it/net/setting-print-options/).

{{% /alert %}}
