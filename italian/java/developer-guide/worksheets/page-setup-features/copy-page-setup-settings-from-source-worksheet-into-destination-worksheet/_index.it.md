---
title: Copia le impostazioni di configurazione pagina dal foglio di lavoro di origine nel foglio di lavoro di destinazione
type: docs
weight: 10
url: /it/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
---

## **Possibili Scenari di Utilizzo**

Quando aggiungi un nuovo foglio a un workbook, contiene le impostazioni predefinite della configurazione di pagina. Ci possono essere momenti in cui è necessario trasferire le impostazioni ([**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)) da un foglio di lavoro a un altro foglio di lavoro. Questo documento spiega come copiare le impostazioni della configurazione di pagina da un foglio di lavoro a un altro utilizzando le API di Aspose.Cells.

## **Copia le impostazioni del layout pagina dal foglio di origine al foglio di destinazione**

Il seguente codice di esempio illustra come copiare le impostazioni della configurazione di pagina da un foglio di lavoro a un altro utilizzando il metodo [**PageSetup.Copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#copy(com.aspose.cells.PageSetup,%20com.aspose.cells.CopyOptions)). Si prega di consultare il seguente codice di esempio e il suo output sulla console per riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.java" >}}

## **Output della console**

{{< highlight java >}}

Before Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

Before Paper Size: PAPER_LETTER

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

{{< /highlight >}}
