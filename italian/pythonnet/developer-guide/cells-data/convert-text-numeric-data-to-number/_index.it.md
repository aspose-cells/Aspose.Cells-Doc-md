---
title: Converti dati numerici testuali in numeri
type: docs
weight: 900
url: /it/python-net/convert-text-numeric-data-to-number/
description: Scopri come convertire i numeri memorizzati come testo in Excel in numeri utilizzando l API Aspose.Cells for Python via .NET.
keywords: python excel converti testo in numero, python excel converti testo in numero, python excel converti dati numerici testuali in numero, python excel converti dati numerici testuali in numero, python excel converti testo numerico in numero, python excel converti testo numerico in numero, excel converti testo numerico in numero con python, converti testo numerico in numero in excel con python, converti testo numerico in numero in excel con libreria python, converti stringa numerica in numero in excel con libreria python excel, python excel converti dati numerici testuali in numero, python excel converti stringa numerica in numero.
---

## **Possibili Scenari di Utilizzo**
A volte vuoi convertire dati numerici testuali in numeri. Puoi inserire numeri come testo in Microsoft Excel mettendo un'apostrofo prima di un numero, ad esempio **'12345**. Excel tratta quindi il numero come una stringa. Aspose.Cells for Python via .NET ti consente di convertire le stringhe in numeri.


## **Come convertire i numeri memorizzati come testo in numeri in Excel**
Puoi convertire i numeri memorizzati come testo in numeri seguendo alcuni semplici passaggi.
1. Seleziona una singola cella o un intervallo di celle che ha un indicatore di errore nell'angolo in alto a sinistra.
1. Accanto alla cella o all'intervallo di celle selezionato, fai clic sul pulsante di errore che appare. Nel menu, fai clic su Converti in numero. 
<br>
<img src="4.png" width=70% />
1. Se il pulsante di avviso non è disponibile, seleziona una colonna con questo problema. Se non vuoi convertire l'intera colonna, puoi selezionare una o più celle invece. Assicurati solo che le celle che selezioni siano nella stessa colonna, altrimenti questo processo non funzionerà. Il pulsante Testo in colonne viene generalmente utilizzato per dividere una colonna, ma può anche essere utilizzato per convertire una singola colonna di testo in numeri. Sulla scheda Dati, fai clic su Testo in colonne.
<br>
<img src="1.png" width=70% />
1. Fai clic sul pulsante Fine nella finestra di dialogo.
<br>
<img src="2.png" width=70% />
1. I numeri memorizzati come testo vengono trasformati in numeri.
<br>
<img src="3.png" width=70% />

## **Come convertire i numeri memorizzati come testo in numeri utilizzando la libreria Aspose.Cells for Python Excel**
Aspose.Cells for Python via .NET fornisce il metodo [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) che può essere utilizzato per convertire tutti i dati numerici di stringhe o testo in numeri.

La seguente immagine mostra numeri di stringa nelle celle **A1:A17**. I numeri di stringa sono allineati a sinistra.
<br>
<img src="5.png" width=70% />

Questi numeri di stringa sono stati convertiti in numeri utilizzando [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) nella schermata seguente. Come puoi vedere, ora sono allineati a destra.
<br>
<img src="6.png" width=70% />

## **Codice Python per convertire dati numerici di stringa in numeri effettivi**

Il seguente codice di esempio illustra come convertire tutti i dati numerici di stringa in numeri effettivi in tutte le schede.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.py" >}}
