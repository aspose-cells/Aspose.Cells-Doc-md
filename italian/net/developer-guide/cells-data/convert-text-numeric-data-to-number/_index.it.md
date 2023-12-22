---
title: Converti dati numerici di testo in numeri
type: docs
weight: 900
url: /it/net/convert-text-numeric-data-to-number/
description: Scopri come convertire i numeri memorizzati come testo in Excel in numeri utilizzando Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
##  **Possibili scenari di utilizzo**
A volte è necessario convertire i dati numerici immessi come testo in numeri. È possibile inserire i numeri come testo in Excel Microsoft inserendo un apostrofo prima del numero, ad esempio *'12345**. Excel quindi tratta il numero come una stringa. Aspose.Cells consente di convertire stringhe in numeri.


##  Come convertire i numeri memorizzati come testo in numeri in Excel
Puoi convertire i numeri memorizzati come testo in numeri seguendo alcuni semplici passaggi.
1. Seleziona una singola cella o intervallo di celle che presenta un indicatore di errore nell'angolo in alto a sinistra.
1.  Accanto alla cella o all'intervallo di celle selezionato, fai clic sul pulsante di errore visualizzato. Nel menu, fare clic su Converti in numero.
<br>
<img src="4.png" width=70% />
1. Se il pulsante di avviso non è disponibile, seleziona una colonna con questo problema. Se non desideri convertire l'intera colonna, puoi invece selezionare una o più celle. Assicurati solo che le celle selezionate siano nella stessa colonna, altrimenti questo processo non funzionerà. Il pulsante Testo in colonne viene generalmente utilizzato per dividere una colonna, ma può anche essere utilizzato per convertire una singola colonna di testo in numeri. Nella scheda Dati fare clic su Testo in colonne.
<br>
<img src="1.png" width=70% />
1. Fare clic sul pulsante Fine nella finestra popup.
<br>
<img src="2.png" width=70% />
1. I numeri memorizzati come testo vengono trasformati in numeri.
<br>
<img src="3.png" width=70% />

## Come convertire i numeri memorizzati come testo in numeri utilizzando Aspose.Cells for .NET
Aspose.Cells fornisce il[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)metodo che può essere utilizzato per convertire tutti i dati numerici di tipo stringa o testo in numeri.

La schermata seguente mostra i numeri di stringa nelle celle *A1:A17**. I numeri delle stringhe sono allineati a sinistra.
<br>
<img src="5.png" width=70% />

 Questi numeri di stringa sono stati convertiti in numeri utilizzando[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)nella schermata seguente. Come puoi vedere, ora sono allineati a destra.
<br>
<img src="6.png" width=70% />

##  C# codice per convertire i dati numerici della stringa in numeri effettivi

Nell'esempio di codice seguente viene illustrato come convertire tutti i dati numerici di stringa in numeri effettivi in tutti i fogli di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
