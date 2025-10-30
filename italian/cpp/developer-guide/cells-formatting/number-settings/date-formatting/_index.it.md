---
title: Come formattare un numero come data con C++
linktitle: Come formattare un numero come data
type: docs
weight: 10
url: /it/cpp/format-number-to-date/
description: Questo articolo introdurrà come formattare un numero come data usando l’API Aspose.Cells for C++.
keywords: formatta il numero come data, impostazioni del numero della cella, formatta il numero come data, impostazioni della data, formato della data.
---

## **Possibili Scenari di Utilizzo**
Formattare numeri come date in Excel (o qualsiasi software di fogli di calcolo) è importante per vari motivi, soprattutto quando si lavora con dati che includono informazioni di tempo o pianificazione. Ecco perché è vantaggioso formattare i numeri come date:

1. **Interpretazione corretta dei valori di data**: In Excel, le date vengono memorizzate come numeri seriali (ad esempio, 1 rappresenta il 1° gennaio 1900 e 44210 rappresenta il 6 settembre 2021). Se questi numeri non sono formattati come date, gli utenti potrebbero vedere numeri senza senso anziché date riconoscibili. La formattazione corretta consente a Excel di visualizzarle come date effettive (ad esempio, 09/06/2021 invece di 44210).
2. **Semplifica i calcoli relativi al tempo**: Excel può eseguire molti calcoli usando le date, come calcolare il numero di giorni tra due date, aggiungere o sottrarre giorni o determinare il giorno della settimana. Se i numeri non sono formattati come date, Excel non potrà eseguire efficacemente queste operazioni. Ad esempio, se vuoi sapere quanti giorni ci sono tra 09/01/2023 e 10/01/2023, Excel può calcolarlo facilmente se i numeri sono in formato data.
3. **Garantisce coerenza**: Quando tutti i valori relativi alle date sono formattati correttamente, si garantisce che tutte le date appaiano in uno stile uniforme e leggibile. Questa coerenza è importante in rapporti aziendali, programmi di progetto e database dove la coerenza delle date è cruciale. Le regioni diverse utilizzano formati di data differenti (ad esempio MM/GG/AAAA negli Stati Uniti vs. GG/MM/AAAA in molti altri paesi), quindi la formattazione aiuta a garantire che le date siano interpretate correttamente.
4. **Migliora la leggibilità**: Le date presentate in un formato standard (ad esempio 01/01/2024) sono più facili da leggere rispetto ai numeri seriali grezzi come 45000. La formattazione corretta della data rende il tuo foglio di calcolo più intuitivo e previene confusioni. Questo è particolarmente importante in scenari quali pianificazione, timeline, organizzazione di eventi o dati storici.
5. **Aiuta nell’ordinamento e nel filtro**: Quando le date sono formattate correttamente, Excel le riconosce come date vere e proprie, rendendo più semplice ordinare o filtrare i dati in ordine cronologico. Ad esempio, puoi ordinare un elenco di eventi per data o filtrare un intervallo di dati per mostrare solo record compresi tra due date specifiche. Senza una corretta formattazione della data, l’ordinamento potrebbe avvenire in base al numero grezzo anziché alle date effettive.
6. **Abilita l’uso delle funzioni di data**: Excel offre una vasta gamma di potenti funzioni di data, come: TODAY(), DATEDIF(), WORKDAY(), YEAR(), MONTH(), DAY(). Queste funzioni richiedono che le date siano formattate correttamente per calcoli accurati.
7. **Supporta la visualizzazione (grafici/timeline)**: Le date formattate correttamente possono essere utilizzate per creare grafici e diagrammi in cui il tempo è un asse chiave. Ad esempio, in un grafico a timeline, Excel ha bisogno di date in un formato riconosciuto per tracciare gli eventi con precisione nel tempo. Numeri mal formattati o non formattati possono risultare in grafici incongruenti o che riflettono informazioni errate.
8. **Prevenirne la disinterpretazione**: I numeri grezzi possono essere facilmente fraintesi. Ad esempio, 44210 potrebbe essere letto come un valore numerico generale, ma se formattato come data, è chiaro che rappresenta il 6 settembre 2021. Le date formattate correttamente aiutano a evitare fraintendimenti sui dati.
9. ** Facilita l’inserimento dei dati**: Quando le celle sono formattate come date, agli utenti viene richiesto di inserire i dati in un formato di data valido, il che previene errori di inserimento e garantisce che i valori di data siano catturati correttamente.
10. **Fondamentale per la pianificazione e il tracciamento**: In qualsiasi situazione che coinvolga la pianificazione, il monitoraggio o le scadenze (come la gestione di progetti, previsioni finanziarie o rapporti sensibili al tempo), la formattazione dei numeri come date è fondamentale per accuratezza e comprensione. Consente una migliore pianificazione ed esecuzione.

## **Come formattare un numero come data in Excel**
Per formattare un numero come data in Excel, segui questi passaggi:

### **Utilizzando la barra multifunzione (scheda Home)**
1. Seleziona le celle contenenti i numeri che desideri formattare come date.
2. Vai alla scheda Home nella barra multifunzione.
3. Nel gruppo Numero, clicca sulla freccia a discesa della casella di formattazione del numero (che può mostrare "Generale" o "Numero" di default).
4. Scegli Data breve o Data estesa dal menu a discesa. Data breve: visualizza la data in un formato compatto, ad esempio MM/GG/AAAA (formato statunitense) o GG/MM/AAAA (formato internazionale). Data estesa: visualizza la data in un formato più descrittivo, ad esempio lunedì, 1 gennaio 2024.
<br>
<img src="1.png" width=60% />

### **Utilizzo della finestra di dialogo Formato celle**
1. Seleziona le celle che desideri formattare.
2. Fai clic con il pulsante destro sulle celle selezionate e scegli Format Cells, oppure premi Ctrl + 1 (Windows) o Cmd + 1 (Mac).
3. Nella finestra di dialogo Formato celle, vai alla scheda Numero.
4. Dalla lista a sinistra, seleziona Data.
5. Scegli il formato data desiderato dall'elenco a destra (ad esempio, GG/MM/AAAA, MM/GG/AAAA, o formati personalizzati).
<br>
<img src="2.png" width=60% />
6. Clicca su OK per applicare il formato data.

## **Come formattare un numero come data in Aspose.Cells**

Per formattare numeri come data nella libreria Aspose.Cells for C++ per lavorare con file Excel, puoi applicare programmaticamente il formato data alle celle. Ecco come farlo usando C++ con Aspose.Cells:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell where you want to apply the date format
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Set a numeric value that represents a date (e.g., 44210 represents 09/06/2021 in Excel)
    a1.PutValue(44210);

    // Create a style object to apply the date format
    Style a1Style = a1.GetStyle();

    // "14" represents a standard date format in Excel (MM/DD/YYYY)
    a1Style.SetNumber(14);

    // Apply the style to the cell
    a1.SetStyle(a1Style);

    // Access the cell where you want to apply the currency format
    Cell a2 = worksheet.GetCells().Get(u"A2");

    // Set a numeric value to the cell
    a2.PutValue(44210);

    // Create a style object to apply the date format
    Style a2Style = a2.GetStyle();

    // Custom format for YYYY-MM-DD
    a2Style.SetCustom(u"YYYY-MM-DD");

    // Apply the style to the cell
    a2.SetStyle(a2Style);

    // Save the workbook
    workbook.Save(u"DateFormatted.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
