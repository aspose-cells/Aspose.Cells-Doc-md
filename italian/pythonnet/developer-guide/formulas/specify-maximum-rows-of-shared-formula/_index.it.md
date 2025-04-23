---
title: Specificare il Numero Massimo di Righe della Formula Condivisa
type: docs
weight: 40
url: /it/python-net/specify-maximum-rows-of-shared-formula/
---

## **Possibili Scenari di Utilizzo**

Il massimo predefinito di righe della formula condivisa è 64. Potrebbe essere qualsiasi numero ad esempio 1000. La performance della formula condivisa cambia con un numero diverso di righe. Pertanto, Aspose.Cells for Python via .NET fornisce la proprietà [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula) che può essere usata per specificare il massimo numero di righe della formula condivisa. La formula condivisa sarà suddivisa in diverse formule condivise se il numero totale di righe della formula condivisa è maggiore di questo, come mostrato nello screenshot seguente.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Specificare il numero massimo di righe della formula condivisa**

Il seguente codice di esempio spiega l'uso della proprietà [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula). Imposta il numero massimo di righe della formula condivisa a 5 e aggiunge la formula condivisa nella cella D1 per 100 righe e salva nel file Excel di output (61767856.xlsx). Se si estraggono i contenuti del file Excel di output e si controlla il *sheet1.xml*, si vedrà la divisione della formula condivisa dopo ogni 5 righe come evidenziato nello screenshot sopra.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SpecifyMaximumRowsOfSharedFormula.py" >}}

