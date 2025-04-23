---
title: Lavorare con lo sfondo nei file ODS
type: docs
weight: 170
url: /it/java/working-with-background-in-ods-files/
---

## **Sfondo nei file ODS**

Lo sfondo può essere aggiunto ai fogli nei file ODS. Lo sfondo può essere un colore di sfondo o uno sfondo grafico. Lo sfondo non è visibile quando il file è aperto, ma se il file è stampato come PDF, lo sfondo è visibile nel PDF generato. Lo sfondo è visibile anche nella finestra di anteprima di stampa.

Aspose.Cells fornisce la possibilità di leggere le informazioni di sfondo e aggiungere uno sfondo nei file ODS.

## **Leggere le informazioni di sfondo dal file OSD**

Aspose.Cells fornisce la classe [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della classe [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) caricando il file ODS di origine (GraphicBackground.ods) e leggendo le informazioni di sfondo. Si prega di consultare l'output della console generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Output della console**

{{< highlight java >}}

Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER

{{< /highlight >}}

## **Aggiungere uno sfondo colorato al file ODS**

Aspose.Cells fornisce la classe [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color) per aggiungere uno sfondo colorato al file ODS. Si prega di consultare il file ODS di output (ColoredBackground.ods) generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Aggiungere uno sfondo grafico al file ODS**

Aspose.Cells fornisce la classe [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData) per aggiungere uno sfondo grafico al file ODS. Si prega di consultare il file ODS di output (GraphicBackground.ods) generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
{{< app/cells/assistant language="java" >}}
