---
title: Creare una Tabella
type: docs
weight: 40
url: /it/java/creating-a-list-object/
---

{{% alert color="primary" %}}

Uno dei vantaggi dei fogli di calcolo è che consentono di creare diversi tipi di elenchi, ad esempio elenchi telefonici, elenchi delle attività, elenchi di transazioni, attivi o passivi. Diversi utenti possono lavorare insieme per utilizzare, creare e mantenere vari elenchi.

Aspose.Cells supporta la creazione e la gestione di elenchi.

{{% /alert %}}

## **Vantaggi di una tabella**

Ci sono diversi vantaggi quando si converte un elenco di dati in un vero oggetto lista:

- Nuove righe e colonne vengono automaticamente incluse.
- Una riga di totale in fondo al tuo elenco può essere facilmente aggiunta per visualizzare SOMMA, MEDIA, CONTEGGIO, ecc.
- Le colonne aggiunte a destra vengono automaticamente incorporate nell'oggetto Elenco.
- I grafici basati su righe e colonne verranno espansi automaticamente.
- I nomi definiti assegnati a righe e colonne verranno espansi automaticamente.
- L'elenco è protetto dalla cancellazione accidentale di righe e colonne.

## **Creazione di una tabella utilizzando Microsoft Excel**

**Selezione dell'intervallo di dati per la creazione di un oggetto lista** 

![todo:image_alt_text](creating-a-list-object_1.png)

Questo visualizza il dialogo Crea elenco.

**Dialogo Crea elenco** 

![todo:image_alt_text](creating-a-list-object_2.png)

Implementare l'oggetto Lista e specificare la Riga Totale (Selezionare **Dati**, quindi **Lista**, seguito da **Riga Totale**).

**Creazione di un oggetto Lista** 

![todo:image_alt_text](creating-a-list-object_3.png)

## **Creare una tabella utilizzando Aspose.Cells API**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una raccolta di [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) che consente l'accesso a ciascun foglio di calcolo in un file di Excel.

Un foglio di calcolo è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire un foglio di calcolo. Per creare un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) in un foglio di calcolo, utilizzare la proprietà di raccolta [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) della classe FoglioCalcolo. Ogni [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) è, infatti, un oggetto della classe [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection), che fornisce ulteriormente il metodo add per aggiungere un oggetto Lista e specificare un intervallo di celle per l'elenco.

Secondo l'intervallo specificato di celle, l'oggetto Lista viene creato nel foglio di calcolo da Aspose.Cells. Utilizzare gli attributi (ad esempio, MostraTotali, ColonneElenco ecc.) della classe [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) per controllare l'elenco.

Nell'esempio riportato di seguito, abbiamo creato lo stesso [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) utilizzando l'API di Aspose.Cells come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
