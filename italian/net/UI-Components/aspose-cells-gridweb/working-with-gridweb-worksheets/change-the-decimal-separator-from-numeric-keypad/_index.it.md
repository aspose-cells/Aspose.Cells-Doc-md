---
title: Modificare il separatore decimale dal tastierino numerico
type: docs
weight: 150
url: /it/net/change-the-decimal-separator-from-numeric-keypad/
---
## **Possibili scenari di utilizzo**
Per impostazione predefinita, Aspose.Cells.GridWeb visualizza i dati numerici in base alle impostazioni locali/regionali sulla macchina. È possibile modificare il separatore decimale dal tastierino numerico a livello di codice utilizzando Aspose.Cells.GridWeb API. Pertanto, quando un file viene importato nella matrice GridWeb o si immettono alcuni dati numerici (dal tastierino numerico) in una nuova cella del foglio di lavoro, dovrebbe avere il decimale desiderato separatore impostato visivamente.
## **Modificare il separatore decimale dal tastierino numerico**
Usando il**GridWorksheetCollection.NumberDecimalSeparator**proprietà, è possibile modificare il separatore decimale dal tastierino numerico a livello di codice. Si prega di vedere gli screenshot che mostrano come funziona

![cose da fare:immagine_alt_testo](change-the-decimal-separator-from-numeric-keypad_1.png)

![cose da fare:immagine_alt_testo](change-the-decimal-separator-from-numeric-keypad_2.png)
## **Codice d'esempio**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

Tieni presente che la modifica del separatore decimale è solo per l'esperienza visiva degli utenti in GridWeb. Quando modifichi e salvi la cartella di lavoro, memorizzerà comunque i valori numerici (nel foglio di calcolo) in base al separatore decimale locale/regionale.

{{% /alert %}}
