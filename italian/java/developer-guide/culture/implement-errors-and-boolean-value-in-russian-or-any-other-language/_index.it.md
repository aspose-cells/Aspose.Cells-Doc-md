---
title: Implementa errori e valore booleano in russo o in qualsiasi altra lingua
type: docs
weight: 30
url: /it/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Possibili scenari di utilizzo**
 Se si utilizza Microsoft Excel nella lingua o lingua russa o in qualsiasi altra lingua o lingua, visualizzerà errori e valori booleani in base a quella lingua o lingua. È possibile ottenere un comportamento simile utilizzando Aspose.Cells[Cartella di lavoro.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) metodo o proprietà. Dovrai sovrascrivere i seguenti metodi di[Impostazioni di globalizzazione](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)classe.

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Implementa errori e valore booleano in russo o in qualsiasi altra lingua**
 Il seguente codice di esempio illustra come implementare gli errori e il valore booleano in russo o in qualsiasi altra lingua. Si prega di controllare il file Excel di esempio utilizzato in questo codice e il suo PDF di output. Lo screenshot mostra la differenza tra[Esempio di file Excel](48496697.xlsx) e il[Uscita PDF](48496696.pdf) per un riferimento.

![cose da fare:immagine_alt_testo](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
