---
title: Parametri di configurazione
type: docs
weight: 10
url: /it/jasperreports/configuration-parameters/
---

{{% alert color="primary" %}} 

La seguente tabella elenca i parametri di configurazione. 

{{% /alert %}} 

|**Nome del parametro** |**Descrizione** |
| :- | :- |
|FORMAT_TYPE |Può essere impostato su "EXCEL97TO2003" o "EXCEL2007" per generare file di formato Microsoft Excel 97-2003 o Excel 2007.
|IS_ONE_PAGE_PER_SHEET |Un valore booleano che specifica se ogni pagina del report deve essere scritta su un foglio di lavoro XLS separato.
|IS_REMOVE_EMPTY_SPACE_BETWEEN_ROWS |Un valore booleano che specifica se gli spazi vuoti che possono apparire tra le righe devono essere rimossi o meno.
|IS_REMOVE_EMPTY_SPACE_BETWEEN_COLUMNS |Un valore booleano che specifica se gli spazi vuoti che possono apparire tra le colonne devono essere rimossi o meno.
|IS_WHITE_PAGE_BACKGROUND |Un valore booleano che specifica se lo sfondo della pagina dovrebbe essere bianco o il colore di sfondo XLS predefinito. Il colore di sfondo XLS può variare a seconda delle proprietà del visualizzatore XLS o dello schema di colore del sistema operativo.
|IS_DETECT_CELL_TYPE |Flag utilizzato per indicare se l'esportatore dovrebbe tener conto del tipo di espressioni del campo di testo originale e impostare i tipi di cella e i valori di conseguenza.
|SHEET_NAMES |Un array di stringhe che rappresentano nomi di fogli personalizzati. È utile quando usato con il parametro IS_ONE_PAGE_PER_SHEET.
|IS_FONT_SIZE_FIX_ENABLED |Flag per ridurre le dimensioni del carattere in modo che il testo si adatti all'altezza della cella specificata.
|MAXIMUM_ROWS_PER_SHEET |Un valore intero che specifica il numero massimo di righe consentite da mostrare in un foglio. Quando impostato, viene creato un nuovo foglio per mostrare le righe rimanenti. Valori negativi o zero significano che non è stato impostato alcun limite.
|IS_IGNORE_GRAPHICS |Flag per ignorare gli elementi grafici ed esportare solo gli elementi di testo.
|IS_COLLAPSE_ROW_SPAN |Flag per collassare la distanza tra le righe ed evitare la fusione delle celle tra le righe.
|IS_IGNORE_CELL_BORDER |Flag per ignorare il bordo della cella.
|IS_USE_EXCEL_CHART |Flag per utilizzare un grafico modificabile nel formato Microsoft Excel anziché immagini statiche. Il valore predefinito è true.

