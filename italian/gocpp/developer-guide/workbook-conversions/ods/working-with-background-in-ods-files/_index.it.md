---
title: Lavorare con lo sfondo nei file ODS con Golang tramite C++
linktitle: Lavorare con lo sfondo nei file ODS
type: docs
weight: 150
url: /it/go-cpp/working-with-background-in-ods-files/
description: Impara come gestire sfondi colorati e grafici nei file ODS utilizzando Aspose.Cells con Golang tramite C++.
---

## **Sfondo nei file ODS**

Lo sfondo può essere aggiunto ai fogli dei file ODS. Lo sfondo può essere di colore o grafico. Lo sfondo non è visibile quando il file è aperto ma se il file viene stampato come PDF, lo sfondo è visibile nel PDF generato. Lo sfondo è anche visibile nella visualizzazione anteprima di stampa.

Aspose.Cells fornisce la capacità di leggere le informazioni di sfondo e aggiungere lo sfondo nei file ODS.

## **Leggi informazioni di sfondo dal file ODS**

Aspose.Cells fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) per gestire lo sfondo nei file ODS. Il seguente esempio di codice mostra l'uso della classe [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) caricando il file [source ODS](90112030.ods) e leggendo le informazioni sullo sfondo. Consulta l'output della console generato dal codice come riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles.go" >}}
### **Output della console**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Aggiungere uno sfondo colorato al file ODS**

Aspose.Cells fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) per aggiungere uno sfondo colorato al file ODS. Consulta il file [output ODS](90112031.ods) generato dal codice come riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-1.go" >}}
## **Aggiungere uno sfondo grafico al file ODS**

Aspose.Cells fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/go-cpp/odspagebackground/getgraphicdata/) per aggiungere uno sfondo grafico al file ODS. Consulta il file [output ODS](90112030.ods) generato dal codice come riferimento.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-2.go" >}}
