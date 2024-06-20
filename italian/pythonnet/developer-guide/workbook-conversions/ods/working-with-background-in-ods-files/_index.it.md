---
title: Lavorare con lo sfondo nei file ODS
type: docs
weight: 150
url: /it/python-net/working-with-background-in-ods-files/
description: Come lavorare con lo sfondo nei file ODS con Aspose.Cells per Python via .NET API.
keywords: Python lavora con lo sfondo nei file ODS, Leggere le informazioni sullo sfondo dal file ODS Pyton via NET, Aggiungere uno sfondo colorato al file ODS usando Python via NET, Python via NET Aggiungi uno sfondo grafico al file ODS.
---

## **Sfondo nei file ODS**

Lo sfondo può essere aggiunto ai fogli dei file ODS. Lo sfondo può essere di colore o grafico. Lo sfondo non è visibile quando il file è aperto ma se il file viene stampato come PDF, lo sfondo è visibile nel PDF generato. Lo sfondo è anche visibile nella visualizzazione anteprima di stampa.

Aspose.Cells per Python via .NET fornisce la possibilità di leggere le informazioni sullo sfondo e aggiungere lo sfondo nei file ODS.

## **Leggi informazioni di sfondo dal file ODS**

Aspose.Cells per Python via .NET fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della classe [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) caricando il file ODS di origine e leggendo le informazioni sullo sfondo. Si prega di vedere l'output della console generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

### **Output della console**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Aggiungere uno sfondo colorato al file ODS**

Aspose.Cells per Python via .NET fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) per aggiungere uno sfondo colorato al file ODS. Si prega di vedere il file ODS di output generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

## **Aggiungere uno sfondo grafico al file ODS**

Aspose.Cells per Python via .NET fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/) per aggiungere uno sfondo grafico al file ODS. Si prega di vedere il file ODS di output generato dal codice per riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
