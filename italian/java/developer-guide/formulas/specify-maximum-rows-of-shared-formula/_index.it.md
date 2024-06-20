---
title: Specificare il Numero Massimo di Righe della Formula Condivisa
type: docs
weight: 40
url: /it/java/specify-maximum-rows-of-shared-formula/
---

## **Possibili Scenari di Utilizzo**

Il numero massimo di righe predefinito della formula condivisa è 64. Potrebbe essere qualsiasi numero, ad esempio potrebbe essere 1000. Le prestazioni della formula condivisa cambiano con un diverso numero di righe. Pertanto, Aspose.Cells fornisce la proprietà [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) che può essere utilizzata per specificare il numero massimo di righe della formula condivisa. Se il totale delle righe della formula condivisa è maggiore, la formula condivisa verrà divisa in diverse formule condivise come mostrato nella seguente schermata.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Specificare il numero massimo di righe della formula condivisa**

Il seguente codice di esempio spiega l'uso della proprietà [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula). Imposta il numero massimo di righe della formula condivisa su 5 e aggiunge la formula condivisa nella cella D1 per 100 righe e salva il [file Excel di output](61767869.xlsx). Se si estrae il contenuto del file Excel di output e si controlla il *sheet1.xml*, si vedrà che la formula condivisa si suddivide dopo ogni 5 righe come evidenziato nella schermata sopra.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
