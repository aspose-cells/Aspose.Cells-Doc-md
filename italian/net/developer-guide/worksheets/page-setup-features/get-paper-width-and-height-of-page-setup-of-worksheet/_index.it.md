---
title: Ottieni larghezza e altezza della carta della configurazione della pagina del foglio di lavoro
type: docs
weight: 50
url: /it/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Scoprirai in questo articolo come ottenere la larghezza e l altezza della carta della configurazione della pagina del foglio di lavoro di Excel utilizzando il codice C# in modo programmato con API o libreria .NET.
keywords: excel larghezza carta configurazione pagina c#, excel altezza carta configurazione pagina c#
---

## **Possibili Scenari di Utilizzo**

A volte è necessario conoscere la larghezza e l'altezza della dimensione della carta come è stata impostata nella configurazione della pagina del foglio di lavoro. Si prega di utilizzare le proprietà [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) e [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) a questo scopo.

## **Ottenere larghezza e altezza della pagina di configurazione del foglio di lavoro**

Il seguente codice di esempio spiega l'uso delle proprietà [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) e [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight). Prima cambia la dimensione della carta in *A2* e poi trova la larghezza e l'altezza della carta, quindi la cambia in *A3*, *A4*, *Letter* e trova rispettivamente la larghezza e l'altezza della carta.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **Output della console**

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
