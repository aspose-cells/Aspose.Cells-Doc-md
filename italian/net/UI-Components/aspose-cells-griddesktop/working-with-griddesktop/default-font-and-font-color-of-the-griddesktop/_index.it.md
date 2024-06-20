---
title: Il carattere predefinito e il colore del carattere della GridDesktop
type: docs
weight: 70
url: /it/net/aspose-cells-griddesktop/default-font-and-font-color-of-the-griddesktop/
keywords: GridDesktop, carattere, colore
description: Questo articolo introduce il carattere predefinito e il colore del carattere nella GridDesktop.
---

## **Possibili Scenari di Utilizzo**
A volte, si desidera modificare il carattere predefinito e il colore del carattere della GridDesktop. Si prega di utilizzare le seguenti due proprietà a tale scopo. È possibile accedere a queste proprietà durante il Design Time o durante l'esecuzione a seconda delle esigenze.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Cambia il font predefinito e il colore del font in fase di progettazione**
La seguente schermata mostra come cambiare il font predefinito e il colore del font di GridDesktop in fase di progettazione.

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **Cambia il font predefinito e il colore del font in esecuzione**
Il seguente codice di esempio spiega come cambiare il font predefinito e il colore del font di GridDesktop in esecuzione.

{{< highlight java >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}
