---
title: Implementa la dimensione della carta personalizzata del foglio di lavoro per la resa
type: docs
weight: 70
url: /it/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: Questo articolo spiega come utilizzare il codice di esempio dell API C# o della libreria .NET per impostare la dimensione della carta personalizzata dei fogli di lavoro desiderati durante la resa del file Excel nel formato file PDF in modo programmato.
keywords: imposta dimensione carta personalizzata durante la resa excel in pdf c#
---

## **Possibili Scenari di Utilizzo**

Non c'è un'opzione diretta disponibile per creare dimensioni di carta personalizzate in MS Excel, tuttavia è possibile impostare la dimensione della carta personalizzata dei fogli di lavoro desiderati durante la resa del file Excel nel formato file PDF. Questo documento spiega come impostare una dimensione di carta personalizzata di un foglio di lavoro utilizzando le API di Aspose.Cells.

## **Implementare un formato carta personalizzato del foglio di lavoro per il rendering**

Aspose.Cells consente di implementare la dimensione della carta desiderata del foglio di lavoro. È possibile utilizzare il metodo [**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) della classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) per specificare una dimensione della pagina personalizzata. Il seguente codice di esempio illustra come specificare una dimensione di carta personalizzata per il primo foglio di lavoro nella cartella di lavoro. Si prega inoltre di consultare il [file PDF di output](45056028.pdf) generato con il seguente codice per un riferimento.

## **Screenshot**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
