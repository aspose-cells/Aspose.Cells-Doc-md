---
title: Impostazione della modalità di calcolo delle formule di Workbook
type: docs
weight: 130
url: /it/java/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel consente di impostare la modalità di calcolo delle formule, cioè il modo in cui le formule vengono calcolate. Ci sono tre possibili valori:

- Automatico - ricalcola ogni volta che qualcosa viene modificato e ogni volta che viene aperto un workbook.
- Automatico tranne per le tabelle dati - ricalcola ogni volta che qualcosa viene modificato, ma tralasciando le tabelle dati.
- Manuale - ricalcola solo quando l'utente lo richiede esplicitamente premendo F9 o CTRL+ALT+F9, o quando il workbook viene salvato.

{{% /alert %}}

Per impostare la modalità di calcolo delle formule in Microsoft Excel:

1. Selezionare **Formule** e quindi **Opzioni di calcolo**.
1. Seleziona una delle opzioni.

Aspose.Cells ti permette anche di impostare la **Modalità di Calcolo della Formula** utilizzando la proprietà [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode). Puoi assegnarle l'enumerazione [**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType) che ha uno dei seguenti valori:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC-EXCEPT-TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

Il seguente codice di esempio crea prima un workbook, quindi imposta la modalità di calcolo della formula su **Manuale** e salva il workbook come file Excel di output su disco.

**Il file di output. Nota la modalità di calcolo della formula.**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
{{< app/cells/assistant language="java" >}}
