---
title: Converti dati numerici di testo in numeri
type: docs
weight: 150
url: /it/java/convert-text-numeric-data-to-number/
description: Scopri come convertire i numeri memorizzati come testo in numeri utilizzando l'API Aspose.Cells for Java.
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
{{% alert color="primary" %}}

 A volte, vuoi convertire i dati numerici inseriti come testo in numeri. È possibile inserire numeri come testo in Microsoft Excel, ad esempio inserendo un apostrofo prima di un numero**'12345**. Excel quindi tratta il numero come una stringa. Aspose.Cells consente di convertire le stringhe in numeri.

{{% /alert %}}

Aspose.Cells for Java API fornisce il[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) che può essere utilizzato per convertire tutti i dati numerici stringa o testo in numeri.

 Lo screenshot seguente mostra i numeri di stringa nelle celle**A1:A17**. I numeri delle stringhe sono allineati a sinistra.

**File di input: numeri inseriti come stringhe di testo** 

![cose da fare:immagine_alt_testo](convert-text-numeric-data-to-number_1.png)

Questi numeri di stringa sono stati convertiti in numeri utilizzando[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) nello screenshot seguente. Come puoi vedere, ora sono allineati a destra.

**File di output: le stringhe sono state convertite in numeri** 

![cose da fare:immagine_alt_testo](convert-text-numeric-data-to-number_2.png)

Il seguente codice di esempio illustra come convertire tutti i dati numerici stringa in numeri effettivi in tutti i fogli di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
