---
title: Unisci più Cartelle di Lavoro in una Singola Cartella di Lavoro
linktitle: Unione Cartelle di Lavoro
type: docs
weight: 50
url: /it/java/combine-multiple-workbooks-into-a-single-workbook/
description: Unisci più workbook in workbook singoli utilizzando il codice Java e l API Aspose.Cells for Java.
keywords: unire più workbook in uno, unire più workbook in uno java, unire più workbook in uno con java, unire più workbook in un unico workbook con java, unire più workbook in un unico workbook java, codice java per unire più workbook in un unico workbook, come unire più workbook in un unico workbook con java, come unire più workbook in uno con java, unire più workbook in un unico con java, come fondere più workbook in uno con java, come fondere più workbook in uno java, come fondere più workbook in uno con java
---

{{% alert color="primary" %}}

A volte è necessario unire workbook con contenuti vari come immagini, grafici e dati in un unico workbook. Aspose.Cells supporta questa funzionalità. Questo articolo mostra come creare un'applicazione semplice per unire workbook con poche righe di codice usando Aspose.Cells.

{{% /alert %}}

## **Unione Workbook**

Il codice di esempio unisce due workbook in un unico workbook utilizzando l'Aspose.Cells for Java. Il codice carica i workbook di origine, utilizza il metodo [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine-com.aspose.cells.Workbook-) per combinarli e salva il workbook di output.

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

Il frammento di codice seguente mostra come combinare più fogli di lavoro in un unico foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CombineMultipleWorkbooks-CombineMultipleWorkbooks.java" >}}

## **Risorse aggiuntive**

{{% alert color="primary" %}}

Potresti trovare utile l'articolo [Combina più fogli di lavoro in un unico foglio di lavoro](/cells/it/java/combine-multiple-worksheets-into-a-single-worksheet/) per ulteriori informazioni.

{{% /alert %}}

## **Argomenti avanzati**
- [Unisci più fogli di lavoro in un unico foglio di lavoro](/cells/it/java/combine-multiple-worksheets-into-a-single-worksheet/)
- [Unire file](/cells/it/java/merge-files/)

{{< app/cells/assistant language="java" >}}
