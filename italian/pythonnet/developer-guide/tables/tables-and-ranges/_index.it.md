---
title: Tabelle e intervalli
type: docs
weight: 50
url: /it/python-net/tables-and-ranges/
---

## **Introduzione**

A volte si crea una tabella in Microsoft Excel e non si desidera continuare a lavorare con la funzionalità di tabella che la accompagna. Piuttosto, si desidera qualcosa che assomigli a una tabella. Per mantenere i dati in una tabella senza perdere la formattazione, convertire la tabella in un intervallo regolare di dati.
Aspose.Cells per Python via .NET supporta questa funzione di Microsoft Excel per tabelle e oggetti elenco.

## **Utilizzando Microsoft Excel**

Utilizzare la funzionalità **Converti in Intervallo** per convertire rapidamente una tabella in un intervallo senza perdere la formattazione. In Microsoft Excel 2007/2010:

1. Fare clic ovunque nella tabella per garantire che la cella attiva sia in una colonna della tabella.
1. Sulla scheda **Design**, nel gruppo **Strumenti**, fare clic su **Converti in intervallo**.

## **Usando Aspose.Cells per Python via .NET**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRange-1.py" >}}

{{% alert color="primary" %}}

Le funzionalità della tabella non sono più disponibili dopo che la tabella è stata convertita in un intervallo. Ad esempio, le intestazioni di riga non includono più le frecce di ordinamento e filtro, e i riferimenti strutturati (riferimenti che usano i nomi delle tabelle) usati nelle formule diventano riferimenti di celle regolari.

{{% /alert %}}

## **Converti Tabella in Intervallo con Opzioni**

Aspose.Cells per Python via .NET fornisce opzioni aggiuntive durante la conversione di una tabella in intervallo tramite la classe [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions). La classe [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) fornisce la proprietà [**last_row**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions/last_row/) che permette di impostare l’indice finale della riga della tabella. La formattazione della tabella sarà mantenuta fino all’indice di riga specificato e il resto della formattazione verrà rimosso.

Il codice di esempio qui sotto dimostra l'uso della classe [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRangeWithOptions-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
