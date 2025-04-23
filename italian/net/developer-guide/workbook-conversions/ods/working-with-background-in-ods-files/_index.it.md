---
title: Lavorare con lo sfondo nei file ODS
type: docs
weight: 150
url: /it/net/working-with-background-in-ods-files/
---

## **Sfondo nei file ODS**

Lo sfondo può essere aggiunto ai fogli dei file ODS. Lo sfondo può essere di colore o grafico. Lo sfondo non è visibile quando il file è aperto ma se il file viene stampato come PDF, lo sfondo è visibile nel PDF generato. Lo sfondo è anche visibile nella visualizzazione anteprima di stampa.

Aspose.Cells fornisce la capacità di leggere le informazioni di sfondo e aggiungere lo sfondo nei file ODS.

## **Leggi informazioni di sfondo dal file ODS**

Aspose.Cells fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della classe [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) caricando il file ODS di origine e leggendo le informazioni di sfondo. Si prega di consultare l'output della Console generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **Output della console**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Aggiungere uno sfondo colorato al file ODS**

Aspose.Cells fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color) per aggiungere uno sfondo di colore al file ODS. Si prega di consultare il file ODS di output generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **Aggiungere uno sfondo grafico al file ODS**

Aspose.Cells fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata) per aggiungere uno sfondo grafico al file ODS. Si prega di consultare il file ODS di output generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
