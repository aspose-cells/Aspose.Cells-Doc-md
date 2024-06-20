---
title: Modifica del carattere e del colore di una riga o colonna
type: docs
weight: 110
url: /it/net/aspose-cells-griddesktop/change-the-font-and-color-of-a-row-or-column/
keywords: GridDesktop, carattere, colore
description: Questo articolo introduce come cambiare il font e il colore in riga o colonna in GridDesktop.
---

{{% alert color="primary" %}} 

In questo argomento, discuteremo del cambiamento del font e del colore del font delle righe e delle colonne di un foglio di lavoro. Si tratta di una funzionalità di formattazione di base offerta da Aspose.Cells.GridDesktop che consente agli sviluppatori di personalizzare la visualizzazione dei propri fogli di lavoro per renderli più presentabili.

{{% /alert %}} 
## **Cambiare il Font e il Colore di una Colonna**
Per cambiare il font e il colore di una colonna usando Aspose.Cells.GridDesktop, seguire i passaggi seguenti:

- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Accedere a una **Colonna** di cui si desidera cambiare il font e il colore
- Creare un **Font** personalizzato
- Impostare il **Font** della **Colonna** su quello personalizzato
- Infine, impostare il **Colore del Font** della **Colonna** su un qualsiasi **Colore** desiderato



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first column of the worksheet

GridColumn column = sheet.Columns[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Bold);

//Setting the font of the column to the customized Font object

column.SetFont(font);

//Setting the font color of the column to Blue

column.SetFontColor(Color.Blue);

{{< /highlight >}}
## **Cambiare il Font & il Colore di una Riga**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Accedere a una **Riga** di cui si desidera cambiare il font e il colore
- Creare un **Font** personalizzato
- Impostare il **Font** della **Riga** su quello personalizzato
- Infine, impostare il **Colore del Font** della **Riga** su un qualsiasi **Colore** desiderato



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first row of the worksheet

GridRow row = sheet.Rows[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Underline);

//Setting the font of the column to the customized Font object

row.SetFont(font);

//Setting the font color of the column to Green

row.SetFontColor(Color.Green);

{{< /highlight >}}
