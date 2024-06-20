---
title: Impostare titoli di stampa
type: docs
weight: 10
url: /it/java/set-print-titles/
---

## **Aspose.Cells - Impostare titoli di stampa**
Aspose.Cells ti consente di designare intestazioni di riga e colonna da ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, utilizza le proprietà setPrintTitleColumns e setPrintTitleRows della classe [PageSetup](/java/pagesetup).

Le righe o le colonne che verranno ripetute sono definite passando il loro numero di riga o colonna. Ad esempio, le righe sono definite come $1:$2 e le colonne sono definite come $A:$B.

**Java**

{{< highlight java >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Impostazione delle opzioni di stampa](/cells/it/java/page-setup-features/#setting-print-options).

{{% /alert %}}
