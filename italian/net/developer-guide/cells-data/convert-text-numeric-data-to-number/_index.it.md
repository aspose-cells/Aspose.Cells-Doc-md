---
title: Converti dati numerici di testo in numeri
type: docs
weight: 900
url: /it/net/convert-text-numeric-data-to-number/
description: Scopri come convertire i numeri memorizzati come testo in Excel in numeri utilizzando Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
{{% alert color="primary" %}}

 A volte, vuoi convertire i dati numerici inseriti come testo in numeri. È possibile inserire numeri come testo in Microsoft Excel inserendo un apostrofo prima di un numero, ad esempio**'12345**. Excel quindi tratta il numero come una stringa. Aspose.Cells consente di convertire le stringhe in numeri.

{{% /alert %}}

Aspose.Cells fornisce il[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)metodo che può essere utilizzato per convertire tutti i dati numerici stringa o testo in numeri.

 Lo screenshot seguente mostra i numeri di stringa nelle celle**A1:A17**. I numeri delle stringhe sono allineati a sinistra.

|**File di input: numeri inseriti come stringhe di testo**|
|:- |
|![cose da fare:immagine_alt_testo](convert-text-numeric-data-to-number_1.png)|

Questi numeri di stringa sono stati convertiti in numeri utilizzando[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)nello screenshot seguente. Come puoi vedere, ora sono allineati a destra.

|**File di output: le stringhe sono state convertite in numeri**|
|:- |
|![cose da fare:immagine_alt_testo](convert-text-numeric-data-to-number_2.png)|

## C# codice per convertire i dati numerici stringa in numeri effettivi

Il seguente codice di esempio illustra come convertire tutti i dati numerici stringa in numeri effettivi in tutti i fogli di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
