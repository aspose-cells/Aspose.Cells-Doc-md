---
title: Applicare la formattazione condizionale avanzata
description: Come utilizzare la libreria Aspose.Cells in C# per applicare la formattazione condizionale avanzata. Regolando questi criteri, si ha più controllo su come appaiono e appaiono le celle.
keywords: Aspose.Cells, Formattazione condizionale avanzata, C#, Condizionale, Formattazione
type: docs
weight: 70
url: /it/net/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 e versioni successive (2010/2013/2016) fornisce alcune funzionalità avanzate per la formattazione condizionale. Ad esempio, consente di applicare sfumature di celle, bordi, icone colorate, frecce, bandiere e formattazione del testo, ecc. che è diventata piuttosto sofisticata.

{{% /alert %}} 
## **Applicare la formattazione condizionale avanzata ai file Microsoft Excel**
La formattazione condizionale può:

- Aggiungere barre di dati sfumate per migliorare graficamente i numeri sottostanti incorporando un semplice grafico a barre nelle celle.
- Sfumare automaticamente le celle con scale di colori in base alla loro relazione con i valori in altre celle nel range. Le impostazioni predefinite sfumano il valore più basso in rosso fino al valore più alto in verde.
- Usare set di icone in modo simile alle scale di colori, ma anziché sfumare le celle aggiunge piccole icone, come frecce e semafori, alle celle.

Aspose.Cells supporta pienamente la formattazione condizionale fornita da Microsoft Excel 2007 e versioni successive in formato XLSX sulle celle in fase di esecuzione. Questo esempio dimostra un esercizio per tipi avanzati di formattazione condizionale, tra cui IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom e altre regole con diversi insiemi di attributi.

- [**Adding Color Scale Conditional Formattings**](/cells/it/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/it/net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/it/net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/it/net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/it/net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/it/net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/it/net/how-to-add-top10-conditional-formatting/)


### **Calcola il colore scelto da Microsoft Excel per la formattazione condizionale delle scale di colore**
Aspose.Cells ti permette di calcolare il colore selezionato da Microsoft Excel quando viene utilizzata la formattazione condizionale delle scale di colore in un file modello. Vedere il codice di esempio di seguito per imparare come calcolare il colore selezionato da Microsoft Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
