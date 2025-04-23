---
title: Congela la prima colonna(o) del foglio di lavoro di Excel
linktitle: Congelare le colonne
type: docs
weight: 190
url: /it/net/how-to-freeze-columns-of-excel-worksheet
description: In questo articolo, imparerai come congelare le colonne di sinistra dei fogli di lavoro di Excel in modo programmato utilizzando la libreria C# con API .NET.
keywords: Congela le colonne di sinistra, congela le prime colonne, blocca la/e colonna/e
---

## **Introduzione**

In questo articolo, impareremo come bloccare (freezare) colonne a sinistra. Quando hai una grande quantità di dati in una riga, e non riesci a vedere le colonne a sinistra quando scorri orizzontalmente, puoi bloccare e fissare la prima colonna in modo da poter vedere quella parte fissa anche quando si scorrono il resto dei dati. In questo modo, puoi vedere facilmente le intestazioni nelle colonne a sinistra.


## **Congela le colonne In Excel**

**![Congelare la/e colonna/e di sinistra in Excel](freeze-columns.png)**


1. Se vuoi congelare la/e colonna/e di sinistra, seleziona prima la colonna sotto la colonna che deve essere congelata
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Congela la prima colonna.
4. Se si scorre verso il basso, la prima colonna è sempre nella vista sinistra.

**![Colonna congelata](frozen-columns.png)**

Come si può vedere, la prima colonna è congelata, è sempre bloccata in alto nella vista quando si scorre orizzontalmente.

Le colonne fisse ti consentono di visualizzare i tuoi dati lunghi senza tenere traccia della prima colonna.




## **Congelare colonne con Aspose.Cells per .Net**
È semplice congelare la prima colonna(i) con Aspose.Cells per .Net. 
Si prega di utilizzare il metodo [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) per congelare la/e colonna/e alla colonna selezionata.
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.
2. Congelare la prima colonna con il metodo Worksheet.FreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

File Excel di esempio allegato (Freeze.xlsx).
{{< app/cells/assistant language="csharp" >}}
