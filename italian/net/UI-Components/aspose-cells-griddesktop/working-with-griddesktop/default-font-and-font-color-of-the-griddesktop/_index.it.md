---
title: Carattere predefinito e colore del carattere del GridDesktop
type: docs
weight: 70
url: /it/net/default-font-and-font-color-of-the-griddesktop/
---
## **Possibili scenari di utilizzo**
A volte, vuoi cambiare il carattere predefinito e il colore del carattere di GridDesktop. Si prega di utilizzare le seguenti due proprietà per questo scopo. È possibile accedere a queste proprietà in fase di progettazione o in fase di runtime a seconda delle esigenze.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Cambia il carattere predefinito e il colore del carattere in fase di progettazione**
Lo screenshot seguente mostra come modificare il carattere predefinito e il colore del carattere di GridDesktop in fase di progettazione.

![cose da fare:immagine_alt_testo](default-font-and-font-color-of-the-griddesktop_1.png)
## **Cambia il carattere predefinito e il colore del carattere in fase di esecuzione**
Il codice di esempio seguente spiega come modificare il carattere predefinito e il colore del carattere di GridDesktop in fase di esecuzione.

{{< highlight "java" >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}
