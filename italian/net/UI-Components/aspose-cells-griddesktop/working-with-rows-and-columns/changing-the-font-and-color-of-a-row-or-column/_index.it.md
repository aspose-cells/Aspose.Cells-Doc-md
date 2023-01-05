---
title: Modifica del carattere e del colore di una riga o di una colonna
type: docs
weight: 110
url: /it/net/changing-the-font-and-color-of-a-row-or-column/
---
{{% alert color="primary" %}} 

In questo argomento, discuteremo della modifica del carattere e del colore del carattere di righe e colonne di un foglio di lavoro. Questo è un livello base di funzionalità di formattazione offerto da Aspose.Cells.GridDesktop che consente agli sviluppatori di personalizzare la visualizzazione dei loro fogli di lavoro per renderli più presentabili.

{{% /alert %}} 
## **Modifica del carattere e del colore di una colonna**
Per modificare il carattere e il colore di una colonna utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Accedi a**Colonna** il cui carattere e colore devono essere modificati
-  Crea un file personalizzato**Font**
-  Impostare il**Font** del**Colonna** a quello personalizzato
-  Finalmente, set**Colore del carattere** del**Colonna** a qualsiasi desiderato**Colore**



{{< highlight "csharp" >}}

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
## **Modifica del carattere e del colore di una riga**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Accedi a**Riga** il cui carattere e colore devono essere modificati
-  Crea un file personalizzato**Font**
-  Impostare il**Font** del**Riga** a quello personalizzato
-  Finalmente, set**Colore del carattere** del**Riga** a qualsiasi desiderato**Colore**



{{< highlight "csharp" >}}

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
