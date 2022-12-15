---
title: Accedi e aggiorna le porzioni di Rich Text di Cell
linktitle: Ricco testo di formattazione
type: docs
weight: 40
url: /it/net/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}}

 Aspose.Cells consente di accedere e aggiornare le porzioni del rich text della cella. A tale scopo, puoi utilizzare[**Cell.GetCaratteri()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) e[**Cell.ImpostaCaratteri()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metodi. Questi metodi restituiranno e accetteranno l'array di[**Impostazione carattere**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)oggetti che puoi utilizzare per accedere e aggiornare varie proprietà del carattere come nome del carattere, colore del carattere, grassetto, ecc.

{{% /alert %}}

## **Accedi e aggiorna le porzioni di Rich Text di Cell**

 Il codice seguente illustra l'utilizzo di[**Cell.GetCaratteri()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) e[**Cell.ImpostaCaratteri()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metodo utilizzando il[file excel di origine](5112369.xlsx)che puoi scaricare dal link fornito. Il file excel di origine ha un rich text nella cella A1. Ha 3 porzioni e ogni porzione ha un carattere diverso. Il seguente frammento di codice accede a queste parti e aggiorna la prima parte con un nuovo nome di carattere. Infine, salva la cartella di lavoro come[file excel di output](5112366.xlsx) . Quando lo aprirai, scoprirai che il carattere della prima parte del testo è cambiato in**"Arial"**.

### Codice C# per accedere e aggiornare le porzioni di Rich Text di Cell

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Output della console generato dal codice di esempio

 Ecco l'output della console del codice di esempio precedente utilizzando il file[file excel di origine](5112369.xlsx).

{{< highlight "java" >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

