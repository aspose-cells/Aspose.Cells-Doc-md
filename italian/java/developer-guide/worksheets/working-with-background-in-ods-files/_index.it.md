---
title: Lavorare con lo sfondo nei file ODS
type: docs
weight: 170
url: /it/java/working-with-background-in-ods-files/
---
## **Sfondo nei file ODS**

Lo sfondo può essere aggiunto ai fogli nei file ODS. Lo sfondo può essere uno sfondo a colori o uno sfondo grafico. Lo sfondo non è visibile quando il file è aperto ma se il file viene stampato come PDF, lo sfondo è visibile nel PDF generato. Lo sfondo è visibile anche nella finestra di dialogo dell'anteprima di stampa.

Aspose.Cells offre la possibilità di leggere le informazioni di background e aggiungere background nei file ODS.

## **Leggi le informazioni di base dal file OSD**

Aspose.Cells fornisce il[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)classe per gestire lo sfondo nei file ODS. L'esempio di codice seguente illustra l'utilizzo di[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)classe caricando il file[fonte ODS](GraphicBackground.ods)file e leggendo le informazioni di base. Si prega di consultare l'output della console generato dal codice per riferimento.

### **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Uscita console**

Tipo di sfondo: GRAFICO

Posizione dello sfondo: CENTER_CENTER

## **Aggiungi sfondo colorato al file ODS**

Aspose.Cells fornisce il[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)classe per gestire lo sfondo nei file ODS. L'esempio di codice seguente illustra l'utilizzo di[**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color)proprietà per aggiungere uno sfondo colorato al file ODS. Si prega di consultare il[uscita ODS](ColoredBackground.ods)file generato dal codice per riferimento.

### **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Aggiungi sfondo grafico al file ODS**

Aspose.Cells fornisce il[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)classe per gestire lo sfondo nei file ODS. L'esempio di codice seguente illustra l'utilizzo di[**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData)proprietà per aggiungere uno sfondo grafico al file ODS. Si prega di consultare il[uscita ODS](GraphicBackground.ods)file generato dal codice per riferimento.

### **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
