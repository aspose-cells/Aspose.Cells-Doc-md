---
title: Imposta i titoli di stampa in xlsx4j
type: docs
weight: 40
url: /it/java/set-print-titles-in-xlsx4j/
---

## **Aspose.Cells - Impostare titoli di stampa**
Aspose.Cells ti consente di designare righe e colonne di intestazione da ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, utilizza le proprietà setPrintTitleColumns e setPrintTitleRows della classe [PageSetup](/java/PageSetup).

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Impostazione delle opzioni di stampa](/cells/it/java/page-setup-features/#setting-print-options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
