---
title: Cambia il separatore decimale dal tastierino numerico
type: docs
weight: 150
url: /it/net/aspose-cells-gridweb/change-the-decimal-separator-from-numeric-keypad/
keywords: GridWeb, decimale, separatore decimale
description: Questo articolo introduce come cambiare il separatore decimale in GridWeb.
---

## **Possibili Scenari di Utilizzo**
Per impostazione predefinita, Aspose.Cells.GridWeb visualizza i dati numerici in base alle impostazioni locali/regionali sulla macchina. È possibile cambiare il separatore decimale dal tastierino numerico programmaticamente utilizzando l'API di Aspose.Cells.GridWeb. Quindi, quando un file viene importato nella matrice GridWeb o si inseriscono dei dati numerici (dall'alfabeto numerico) in una nuova cella del foglio di lavoro, dovrebbe visualizzare il separatore decimale desiderato. 
## **Cambia il separatore decimale dal tastierino numerico**
Utilizzando la proprietà **GridWorksheetCollection.NumberDecimalSeparator**, è possibile cambiare il separatore decimale dal tastierino numerico programmaticamente. Si prega di vedere gli screenshot che mostrano come funziona

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Si noti che il cambio del separatore decimale è solo per l'esperienza visiva degli utenti in GridWeb. Quando si modifica e si salva il proprio foglio di lavoro, i valori numerici vengono comunque memorizzati (nel foglio di calcolo) in base al separatore decimale locale/regionale.

{{% /alert %}}
