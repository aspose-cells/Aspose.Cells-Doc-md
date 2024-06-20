---
title: Specificare il Numero Massimo di Righe della Formula Condivisa
type: docs
weight: 40
url: /it/net/specify-maximum-rows-of-shared-formula/
---

## **Possibili Scenari di Utilizzo**

Il numero massimo predefinito di righe della formula condivisa è 64. Potrebbe essere qualsiasi numero, ad esempio potrebbe essere 1000. Le prestazioni della formula condivisa cambiano con un numero diverso di righe. Pertanto, Aspose.Cells fornisce la proprietà [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) che può essere utilizzata per specificare il numero massimo di righe della formula condivisa. La formula condivisa sarà divisa in più formule condivise se il numero totale di righe della formula condivisa è maggiore di esso come mostrato nello screenshot seguente.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Specificare il numero massimo di righe della formula condivisa**

Il seguente codice di esempio spiega l'uso della proprietà [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula). Imposta il numero massimo di righe della formula condivisa a 5 e aggiunge la formula condivisa nella cella D1 per 100 righe e salva nel file Excel di output (61767856.xlsx). Se si estraggono i contenuti del file Excel di output e si controlla il *sheet1.xml*, si vedrà la divisione della formula condivisa dopo ogni 5 righe come evidenziato nello screenshot sopra.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
