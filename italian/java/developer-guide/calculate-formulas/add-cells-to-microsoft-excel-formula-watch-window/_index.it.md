---
title: Aggiungi celle alla finestra di monitoraggio delle formule di Microsoft Excel
type: docs
weight: 20
url: /it/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Possibili Scenari di Utilizzo**

La finestra di controllo di Microsoft Excel è uno strumento utile per controllare comodamente i valori delle celle e le formule in una finestra. Puoi aprire la *Watch Window* utilizzando Microsoft Excel cliccando su *Formule > Watch* *Window*. Ha il pulsante *Add Watch* che può essere usato per aggiungere le celle da ispezionare. Allo stesso modo, puoi utilizzare il metodo *[**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add-int-int-)* per aggiungere le celle alla *Watch Window* utilizzando l'API Aspose.Cells.

## **Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel**

Il seguente codice di esempio imposta la formula delle celle C1 e E1 e le aggiunge entrambe alla *Watch Window*. Quindi salva il workbook come [file Excel di output](67338509.xlsx). Se apri il file Excel di output e visualizzi la *Watch Window*, vedrai entrambe le celle come mostrato in questa schermata.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
{{< app/cells/assistant language="java" >}}
