---
title: Accedere e aggiornare le porzioni di testo arricchito della cella
linktitle: Formattazione del testo arricchito
type: docs
weight: 40
url: /it/python-net/access-and-update-the-portions-of-rich-text-of-cell/
description: Scopri come accedere e aggiornare le porzioni di testo arricchito della cella tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Accesso e aggiornamento testo arricchito della cella in Python, Ottenere testo arricchito della cella in Python, Modificare testo arricchito della cella in Python, Accesso testo arricchito della cella in Python, Aggiornamento testo arricchito della cella in Python, Cambiare testo arricchito della cella in Python.
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET consente di accedere e aggiornare le porzioni di testo arricchito della cella. A questo scopo, è possibile utilizzare i metodi [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) e [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list). Questi metodi restituiranno e accetteranno l'array di oggetti [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) che è possibile utilizzare per accedere e aggiornare varie proprietà del carattere come nome del font, colore del font, grassetto, ecc.

{{% /alert %}}

## **Accedere e aggiornare le porzioni di testo arricchito della cella**

Il codice seguente dimostra l'uso dei metodi [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) e [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) utilizzando il [file excel di origine](5112369.xlsx) che è possibile scaricare dal link fornito. Il file excel di origine ha un testo arricchito nella cella A1. Ha 3 porzioni e ciascuna porzione ha un carattere diverso. Il seguente snippet di codice accede a queste porzioni e aggiorna la prima porzione con un nuovo nome di font. Infine, salva il workbook come [file di output excel](5112366.xlsx). Quando lo apri, troverai che il font della prima porzione del testo è stato cambiato in **"Arial"**.

### Codice C# per accedere e aggiornare le porzioni di testo arricchito della cella

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-UpdateRichTextCells-1.py" >}}

### Uscita della console generata dal codice di esempio

Ecco l'output della console del codice di esempio utilizzando il [file excel di origine](5112369.xlsx).

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
