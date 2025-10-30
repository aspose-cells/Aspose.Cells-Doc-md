---
title: Come ruotare il testo della cella con C++
linktitle: Come ruotare il testo della cella
type: docs
weight: 80
url: /it/cpp/how-to-rotate-text-of-cell/
description: Codice C++ per ruotare il testo della cella con API Aspose.Cells for C++
keywords: ruota testo di una cella in C++, programma C++ per ruotare il testo di una cella nel workbook, impostare programmativamente l angolo di rotazione della cella nel workbook, come ruotare il testo di una cella in Excel con C++
---

## **Ruotare il testo della cella in Aspose.Cells**

Aspose.Cells è un potente componente C++ che permette agli sviluppatori di lavorare con i fogli Excel programmativamente. Una delle funzionalità offerte da Aspose.Cells è la possibilità di ruotare le celle, consentendo di personalizzare l'orientamento del testo e migliorare la presentazione visiva dei dati. In questo documento, esploreremo come ruotare le celle usando Aspose.Cells.

## **Come ruotare il testo della cella in Excel**
Per ruotare una cella in Excel, è possibile utilizzare i seguenti passaggi:
1. Apri Excel e seleziona la cella o l'intervallo di celle che desideri ruotare.
1. Fai clic con il pulsante destro del mouse sulla cella (o le celle) selezionata(e) e scegli "Formato celle" dal menu contestuale. In alternativa, puoi andare alla scheda "Home" nel nastro di Excel, fare clic sulla visualizzazione a discesa "Formato" nel gruppo "Celle" e selezionare "Formato celle".
1. Nella finestra di dialogo "Formato celle", passa alla scheda "Allineamento".
1. Nella sezione "Orientamento", vedrai le opzioni per ruotare il testo. Puoi inserire direttamente l'angolo di rotazione desiderato in gradi nella casella "Gradi". I valori positivi ruotano il testo in senso antiorario e i valori negativi lo ruotano in senso orario.
<br>
![todo:image_alt_text](alignment.png)
1. Una volta selezionata la rotazione desiderata, fai clic su "OK" per applicare le modifiche. La/e cella/e selezionata/e verranno ora ruotate in base all'angolo di rotazione o orientamento scelto.

## **Come ruotare il testo della cella utilizzando l'API di Aspose.Cells**

La proprietà [**Style.GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) rende comodo ruotare le celle. Per ruotare le celle in Aspose.Cells, è necessario seguire questi passaggi:
1. Carica il documento di lavoro di Excel
<br>
Prima di tutto, è necessario caricare il workbook di Excel utilizzando Aspose.Cells. Puoi utilizzare la classe Workbook per aprire un file Excel esistente o crearne uno nuovo. 

1. Accedere al foglio di lavoro
<br>
Una volta caricato il workbook, è necessario accedere al foglio di lavoro in cui si desidera ruotare le celle. Puoi accedere al foglio di lavoro tramite l'indice o il nome. 

1. Ruotare il testo della cella
<br>
Ora che hai accesso al foglio di lavoro, puoi ruotare le celle modificando l'oggetto Style delle celle desiderate. L'oggetto Style ti consente di impostare diverse opzioni di formattazione, inclusa la rotazione. 

1. Salvare il workbook
<br>
Dopo aver ruotato le celle, puoi salvare il workbook modificato su un file o un flusso utilizzando il metodo Save.

## **Codice di esempio C++**

Si prega di consultare il codice seguente, crea un oggetto workbook e imposta diversi angoli di rotazione per diverse celle. La schermata mostra il risultato dopo l'esecuzione del codice di esempio.
<br>
<img src="rotation.png" width=80% />

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Row index of the cell
    int row = 0;
    // Column index of the cell
    int column = 0;

    // Get cell A1 and set its value
    Cell a1 = worksheet.GetCells().Get(row, column);
    a1.PutValue(u"a1 rotate text");
    Style a1Style = a1.GetStyle();

    // Set the rotation angle in degrees
    a1Style.SetRotationAngle(45);
    a1.SetStyle(a1Style);

    // Set column index to 1 for cell B1
    column = 1;
    Cell b1 = worksheet.GetCells().Get(row, column);
    b1.PutValue(u"b1 rotate text");
    Style b1Style = b1.GetStyle();

    // Set the rotation angle in degrees
    b1Style.SetRotationAngle(255);
    b1.SetStyle(b1Style);

    // Set column index to 2 for cell C1
    column = 2;
    Cell c1 = worksheet.GetCells().Get(row, column);
    c1.PutValue(u"c1 rotate text");
    Style c1Style = c1.GetStyle();

    // Set the rotation angle in degrees
    c1Style.SetRotationAngle(-90);
    c1.SetStyle(c1Style);

    // Set column index to 3 for cell D1
    column = 3;
    Cell d1 = worksheet.GetCells().Get(row, column);
    d1.PutValue(u"d1 rotate text");
    Style d1Style = d1.GetStyle();

    // Set the rotation angle in degrees
    d1Style.SetRotationAngle(-90);
    d1.SetStyle(d1Style);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
