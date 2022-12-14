---
title: Specifica il numero massimo di righe della formula condivisa
type: docs
weight: 40
url: /it/java/specify-maximum-rows-of-shared-formula/
---
## **Possibili scenari di utilizzo**

Le righe massime predefinite della formula condivisa sono 64. Potrebbe essere qualsiasi numero, ad esempio potrebbe essere 1000. Le prestazioni della formula condivisa cambiano con un diverso numero di righe. Pertanto, Aspose.Cells fornisce il[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)proprietà che può essere utilizzata per specificare il numero massimo di righe della formula condivisa. La formula condivisa verrà suddivisa in diverse formule condivise se le righe totali della formula condivisa sono maggiori di essa, come mostrato nello screenshot seguente.

![cose da fare:immagine_alt_testo](specify-maximum-rows-of-shared-formula_1.png)

## **Specifica il numero massimo di righe della formula condivisa**

Il codice di esempio seguente illustra l'utilizzo di[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)proprietà. Imposta il numero massimo di righe della formula condivisa su 5 e aggiunge la formula condivisa nella cella D1 per 100 righe e salva in[file Excel di output](61767869.xlsx). Se estrai il contenuto del file Excel di output e controlli il file*foglio1.xml*, vedrai la formula condivisa divisa dopo ogni 5 righe come evidenziato nello screenshot qui sopra.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
