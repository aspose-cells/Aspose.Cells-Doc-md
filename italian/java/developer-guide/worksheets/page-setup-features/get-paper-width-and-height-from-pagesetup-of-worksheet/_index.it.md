---
title: Ottieni larghezza e altezza della carta da PageSetup di Foglio di Lavoro
type: docs
weight: 300
url: /it/java/get-paper-width-and-height-from-pagesetup-of-worksheet/
---

## **Possibili Scenari di Utilizzo**

A volte è necessario conoscere la larghezza e l'altezza del formato carta come è stato impostato nella configurazione pagina del foglio di lavoro. Si prega di utilizzare le proprietà [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperWidth) e [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperHeight) a questo scopo.

## **Ottieni larghezza e altezza carta dalle impostazioni pagina del foglio di lavoro**

Il codice di esempio seguente spiega l'uso delle proprietà [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperWidth) e [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperHeight). Prima cambia le dimensioni della carta in A2 e quindi trova la larghezza e l'altezza della carta, poi la cambia in A3, A4, Lettera e trova rispettivamente larghezza e altezza della carta.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-GetPaperWidthHeight-GetPaperWidthHeight.java" >}}

## **Output della console**

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11.0

{{< /highlight >}}
