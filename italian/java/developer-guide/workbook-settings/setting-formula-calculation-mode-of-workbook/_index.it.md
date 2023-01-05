---
title: Impostazione della modalità di calcolo della formula della cartella di lavoro
type: docs
weight: 130
url: /it/java/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel consente di impostare la modalità di calcolo delle formule, ovvero il modo in cui vengono calcolate le formule. Ci sono tre possibili valori:

- Automatico: ricalcola ogni volta che qualcosa viene modificato e ogni volta che viene aperta una cartella di lavoro.
- Automatico ad eccezione delle tabelle di dati: ricalcola ogni volta che qualcosa viene modificato, ma tralasciando le tabelle di dati.
- Manuale: ricalcola solo quando l'utente lo richiede esplicitamente premendo F9 o CTRL+ALT+F9 o quando la cartella di lavoro viene salvata.

{{% /alert %}}

Per impostare la modalità di calcolo della formula in Microsoft Excel:

1.  Selezionare**Formule** e poi**Opzioni di calcolo**.
1. Seleziona una delle opzioni.

 Aspose.Cells permette anche di impostare il**Modalità di calcolo della formula** usando il[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) proprietà. Puoi assegnargli il[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType)enumerazione che ha uno dei seguenti valori:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

Il codice di esempio seguente crea innanzitutto una cartella di lavoro, quindi imposta la modalità di calcolo della formula su**Manuale** e salva la cartella di lavoro come file Excel di output su disco.

**Il file di output. Notare la modalità di calcolo della formula.**

![cose da fare:immagine_alt_testo](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
