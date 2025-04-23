---
title: Formattare intervalli con C++
linktitle: Formato intervalli
type: docs
weight: 105
url: /it/cpp/how-to-format-a-range/
description: Impara come formattare intervalli in Excel usando Aspose.Cells con C++. Applica stili, caratteri e colori agli intervalli di celle programmaticamente.
---

## **Possibili Scenari di Utilizzo**
Quando hai bisogno di applicare uno stile a un intervallo, puoi utilizzare la formattazione dell'intervallo.

## **Come formattare un intervallo in Excel**

Per formattare un intervallo di celle in Excel, puoi utilizzare le opzioni di formattazione integrate fornite da Excel. Ecco come puoi formattare direttamente un intervallo di celle in Excel:

1. Apri Excel e apri il foglio di lavoro che contiene l'intervallo che desideri formattare.

2. Seleziona l'intervallo di celle che desideri formattare. Puoi fare clic e trascinare per selezionare l'intervallo, oppure puoi utilizzare scorciatoie da tastiera come Maiusc + frecce per estendere la selezione.

3. Una volta selezionato l'intervallo, fai clic con il pulsante destro del mouse sull'intervallo selezionato e scegli "Formatta celle" dal menu contestuale. In alternativa, puoi andare alla scheda Home nella barra dei menu di Excel, fare clic sulla voce "Formato" nel gruppo "Celle" e selezionare "Formatta celle".

4. La finestra di dialogo "Formatta celle" apparirà. Qui puoi scegliere varie opzioni di formattazione da applicare all'intervallo selezionato. Ad esempio, puoi cambiare lo stile del carattere, la dimensione del carattere, il colore del carattere, il formato numero, i bordi, il colore di sfondo, ecc. Esplora le diverse schede nella finestra di dialogo per accedere a varie opzioni di formattazione.

5. Dopo aver apportato le modifiche di formattazione desiderate, fai clic sul pulsante "OK" per applicare la formattazione all'intervallo selezionato.

## **Come formattare un intervallo usando C++**

Per formattare un intervallo usando Aspose.Cells, puoi usare i seguenti metodi:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/range/setstyle/)

## **Codice di Esempio**
In questo esempio, creiamo un workbook Excel, aggiungiamo alcuni dati di esempio, accediamo al primo foglio di lavoro e definiamo due intervalli ("A1:C3" e "A4:C5"). Poi, creiamo nuovi stili, impostiamo varie opzioni di formattazione (ad esempio colore del carattere, grassetto) e applichiamo lo stile all'intervallo. Infine, salviamo il workbook in un nuovo file.
<br>
![todo:image_alt_text](format-range.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range = worksheet.GetCells().CreateRange(u"A1:C3");
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFont(true);
    range.ApplyStyle(style, flag);

    Range range2 = worksheet.GetCells().CreateRange(u"A4:C5");
    Style style2 = workbook.CreateStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    range2.SetStyle(style2);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
