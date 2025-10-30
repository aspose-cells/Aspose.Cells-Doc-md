---
title: Converti dati numerici testuali in numeri
type: docs
weight: 900
url: /it/nodejs-cpp/convert-text-numeric-data-to-number/
description: Impara come convertire i numeri memorizzati come testo in Excel in numeri usando l API Aspose.Cells for Node.js via C++.
keywords: excel converti testo in numero, codice Node js per convertire testo in numero in Excel, converti dati numerici come testo in numero in Excel, converti dati numerici come testo in numero in codice Node js, converti testo numerico in numero, codice Node js per convertire testo numerico in numero, converti testo numerico in numero con Node js, converti testo numerico in numero in Excel con codice Node js, converti testo numerico in numero in Excel con codice Node js, converti stringa numerica in numero in Excel con codice Node js, converti dati numerici come testo in numero in Node js, converti stringa numerica in numero in Node js
---

## **Possibili Scenari di Utilizzo**
A volte, vuoi convertire dati numerici inseriti come testo in numeri. Puoi inserire numeri come testo in Microsoft Excel mettendo un apostrofo prima di un numero, ad esempio **'12345**. Excel tratta quindi il numero come una stringa. Aspose.Cells for Node.js via C++ ti consente di convertire stringhe in numeri.


## Come Convertire i numeri memorizzati come testo in numeri in Excel
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

## Come convertire numeri memorizzati come testo in numeri usando Aspose.Cells for Node.js via C++
Aspose.Cells for Node.js via C++ fornisce il metodo [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--) che può essere usato per convertire tutti i dati numerici come stringa o testo in numeri.

La seguente immagine mostra numeri di stringa nelle celle **A1:A17**. I numeri di stringa sono allineati a sinistra.
<br>
<img src="5.png" width=70% />

Questi numeri di stringa sono stati convertiti in numeri utilizzando [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--) nella schermata seguente. Come puoi vedere, ora sono allineati a destra.
<br>
<img src="6.png" width=70% />

## Codice Node.js per convertire dati numerici come stringa in numeri effettivi

Il seguente codice di esempio illustra come convertire tutti i dati numerici di stringa in numeri effettivi in tutte le schede.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-ConvertTextNumericDatatoNumber.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
