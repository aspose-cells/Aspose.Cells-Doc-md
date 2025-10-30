---
title: Unisci più Cartelle di Lavoro in una Singola Cartella di Lavoro
linktitle: Unione Cartelle di Lavoro
type: docs
weight: 66
url: /it/python-net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

A volte, è necessario combinare diversi libri di lavoro con contenuti vari come immagini, grafici e dati in un unico documento. Aspose.Cells for Python via .NET supporta questa funzionalità. Questo articolo mostra come creare un'applicazione console in Visual Studio e combinare i libri di lavoro con poche righe di codice utilizzando Aspose.Cells for Python via .NET.

{{% /alert %}}

## **Unione Cartelle di Lavoro con Immagini e Grafici**

Il codice di esempio combina due cartelle di lavoro in una singola utilizzando Aspose.Cells per Python via .NET. Il codice carica le cartelle di lavoro di origine, utilizza il metodo [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) per combinarle e salva la cartella di lavoro di output.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CombineMultipleWorkbooksSingleWorkbook-1.py" >}}

## **Argomenti avanzati**
- [Unisci più fogli di lavoro in un'unica scheda](/cells/it/python-net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Unire file](/cells/it/python-net/merge-files/)

{{< app/cells/assistant language="python-net" >}}
