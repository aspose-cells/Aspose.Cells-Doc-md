---
title: Congela riquadri in Apache POI e Aspose.Cells
type: docs
weight: 80
url: /it/java/freeze-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Congelamento Riquadri**
Aspose.Cells offre un corso,[Cartella di lavoro](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)che rappresenta un file Excel Microsoft. La classe Workbook contiene un WorksheetCollection che consente l'accesso a ogni foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato da[Foglio di lavoro](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)classe. La classe Worksheet fornisce un'ampia gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per configurare i riquadri bloccati, chiama il metodo freezePanes della classe Worksheet. Il metodo FreezePanes accetta i seguenti parametri:

- **Riga**, l'indice di riga della cella da cui inizierà il blocco.
- **Colonna**, l'indice di colonna della cella da cui inizierà il blocco.
- **Righe congelate**, il numero di righe visibili nel riquadro superiore.
- **Colonne congelate**, il numero di colonne visibili nel riquadro sinistro

**Java**

{{< highlight "java" >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Blocca i riquadri**
sheet.createFreezePane è disponibile per ottenere la funzionalità FreezePane durante l'utilizzo di Apache POI SS - HSSF e XSSF

**Java**

{{< highlight "java" >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Blocca i riquadri](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
