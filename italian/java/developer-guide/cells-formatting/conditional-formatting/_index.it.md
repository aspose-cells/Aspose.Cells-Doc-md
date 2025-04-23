---
title: Formattazione condizionale
type: docs
weight: 120
url: /it/java/conditional-formatting/
---

{{% alert color="primary" %}} 

La formattazione condizionale è una funzione avanzata di Microsoft Excel che consente di applicare formati a una cella o a un intervallo di celle e di far sì che tale formattazione cambi a seconda del valore della cella o del valore di una formula. Ad esempio, è possibile far sì che una cella appaia in grassetto solo quando il valore della cella è superiore a 500. Quando il valore della cella soddisfa la condizione, il formato specificato viene applicato alla cella. Se il valore della cella non soddisfa la condizione, viene utilizzata la formattazione predefinita. In Microsoft Excel, selezionare **Formato**, quindi **Formattazione condizionale** per aprire il riquadro della formattazione condizionale.

**Formattazione condizionale in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_1.png)

Aspose.Cells supporta l'applicazione della formattazione condizionale alle celle in fase di esecuzione. In questo articolo viene spiegato come.

{{% /alert %}} 
## **Applicare la formattazione condizionale**
Aspose.Cells supporta la formattazione condizionale in due modi:

- [Utilizzo di un foglio di calcolo del designer](/cells/it/java/conditional-formatting/).
- [Creazione della formattazione condizionale in fase di esecuzione](/cells/it/java/conditional-formatting/).
### **Utilizzo del foglio di calcolo del designer**
Gli sviluppatori possono creare un foglio di calcolo del designer che contiene la formattazione condizionale in Microsoft Excel e quindi aprire quel foglio di calcolo con Aspose.Cells. Aspose.Cells carica e salva il foglio di calcolo del designer, mantenendo qualsiasi impostazione di formattazione condizionale. Per saperne di più sui fogli di calcolo del designer, leggere [Cos'è un foglio di calcolo del designer](/cells/it/java/what-is-a-designer-spreadsheet/).
## **Applicare la formattazione condizionale in fase di esecuzione**
Aspose.Cells supporta l'applicazione della formattazione condizionale in fase di esecuzione.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
### **Imposta Carattere**
**Impostazione dei caratteri in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
### **Imposta Bordo**
**Impostazione dei bordi in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
### **Imposta Schema**
**Impostazione di un modello di cella in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **Argomenti avanzati**
- [Aggiungi Impostazioni Icona Condizionale con il Testo della Cella](/cells/it/java/add-conditional-icons-set-with-the-cell-text/)
- [Aggiunta di Formattazioni Condizionali a Scala a 2 Colori e Scala a 3 Colori](/cells/it/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Applica la formattazione condizionale nei fogli di lavoro](/cells/it/java/apply-conditional-formatting-in-worksheets/)
- [Applica sfumature a righe e colonne alternative con la formattazione condizionale](/cells/it/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)

{{< app/cells/assistant language="java" >}}
