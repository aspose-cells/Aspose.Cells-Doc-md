---
title: Combinare più cartelle di lavoro in una singola cartella di lavoro con Golang tramite C++
linktitle: Unione Cartelle di Lavoro
type: docs
weight: 66
url: /it/go-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Impara come combinare più cartelle di lavoro in una singola cartella di lavoro usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

A volte, è necessario combinare workbook con contenuti vari come immagini, grafici e dati in un singolo workbook. Aspose.Cells supporta questa funzionalità. Questo esempio mostra come creare un'applicazione console in Visual Studio e combinare i workbook con alcune righe di codice semplici utilizzando Aspose.Cells.

{{% /alert %}}

## **Unione Cartelle di Lavoro con Immagini e Grafici**

Il codice di esempio unisce due cartelle di lavoro in una singola cartella di lavoro utilizzando Aspose.Cells. Il codice carica le cartelle di lavoro di origine, utilizza il metodo [**Workbook::Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) per combinarle e salva la cartella di lavoro di output.

### **Cartelle di Lavoro di Origine**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Cartelle di Lavoro di Output**

- [combined.xlsx](5473095.xlsx)

### **Screenshot**

Di seguito sono riportati gli screenshot delle cartelle di lavoro di origine e di output.

{{% alert color="primary" %}}

Puoi utilizzare qualsiasi cartella di lavoro di origine. Queste immagini sono solo a scopo illustrativo.

{{% /alert %}}

**Il primo foglio di lavoro della cartella di lavoro dei grafici - sovrapposto** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Secondo foglio di lavoro della cartella di lavoro dei grafici - linea** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Primo foglio di lavoro della cartella di immagini - immagine** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Tutti e tre i fogli di lavoro nel libro combinato - sovrapposti, linea, immagine** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeWorkbooks.go" >}}
## **Argomenti avanzati**
- [Unisci più fogli di lavoro in un'unica scheda](/cells/it/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Unire file](/cells/it/cpp/merge-files/)
