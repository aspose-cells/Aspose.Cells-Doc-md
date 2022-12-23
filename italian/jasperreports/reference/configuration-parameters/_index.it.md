---
title: Parametri di configurazione
type: docs
weight: 10
url: /it/jasperreports/configuration-parameters/
---
{{% alert color="primary" %}} 

 La tabella seguente elenca i parametri di configurazione.

{{% /alert %}} 

|**Nome del parametro** |**Descrizione** |
|:- |:- |
| FORMAT_TIPO| Può essere impostato su "EXCEL97TO2003" o "EXCEL2007" per generare file in formato Microsoft Excel 79 0 2003 o Excel 2007.|
|È_UNO_PAGINA_PER_ FOGLIO| Un valore booleano che specifica se ogni pagina del report deve essere scritta in un foglio di lavoro XLS diverso.|
|È_RIMUOVERE_VUOTO_SPAZIO_ TRA_RIGHE| Un valore booleano che specifica se gli spazi vuoti che possono apparire tra le righe devono essere rimossi o meno.|
|È_RIMUOVERE_VUOTO_SPAZIO_ TRA_COLONNE|Un valore booleano che specifica se gli spazi vuoti che possono apparire tra le colonne devono essere rimossi o meno.|
|È_BIANCA_ PAGINA_SFONDO| Un valore booleano che specifica se lo sfondo della pagina deve essere bianco o il colore di sfondo predefinito XLS. Il colore di sfondo XLS può variare a seconda delle proprietà del visualizzatore XLS o della combinazione di colori del sistema operativo.|
|È_RILEVA_ TIPO_CELLA| Flag utilizzato per indicare se l'esportatore deve prendere in considerazione il tipo di espressioni del campo di testo originale e impostare i tipi di celle ei valori di conseguenza.|
| SCHEDA_NOMI|Un array di stringhe che rappresentano nomi di fogli personalizzati. Questo è utile se utilizzato con l'IS_UNO_PAGINA_PER_ Parametro FOGLIO.|
|È_FONT_TAGLIA_AGGIUSTARE_ ABILITATO| Flag per la riduzione della dimensione del carattere in modo che il testo rientri nell'altezza della cella specificata.|
|MASSIMO_RIGHE_ PER_FOGLIO|Un valore intero che specifica il numero massimo di righe che possono essere visualizzate in un foglio. Quando impostato, viene creato un nuovo foglio per la visualizzazione delle righe rimanenti. Valori negativi o zero significano che non è stato impostato alcun limite.|
|È_IGNORARE_ GRAFICA| Contrassegno per ignorare elementi grafici ed esportare solo elementi di testo.|
|È_CROLLO_ ROW_SPAN| Contrassegna per la compressione dell'intervallo di righe ed evita di unire le celle tra le righe.|
|È_IGNORARE_ CELL_BORDER| Flag per ignorare il bordo della cella.|
|È_USO_ GRAFICO_EXCEL| Flag per l'utilizzo di grafici modificabili in formato Excel Microsoft anziché immagini statiche. Il valore predefinito è vero.|

