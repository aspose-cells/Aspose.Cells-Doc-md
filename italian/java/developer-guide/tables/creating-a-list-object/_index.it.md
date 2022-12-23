---
title: Creazione di una tabella
type: docs
weight: 40
url: /it/java/creating-a-list-object/
---
{{% alert color="primary" %}}

Uno dei vantaggi dei fogli di calcolo è che consentono di creare diversi tipi di elenchi, ad esempio elenchi telefonici, elenchi di attività, elenchi di transazioni, attività o passività. Diversi utenti possono lavorare insieme per utilizzare, creare e mantenere vari elenchi.

Aspose.Cells supporta la creazione e la gestione di Liste.

{{% /alert %}}

## **Vantaggi di un tavolo**

Ci sono alcuni vantaggi quando si converte un elenco di dati in un vero oggetto elenco:

- Nuove righe e colonne vengono incluse automaticamente.
- È possibile aggiungere facilmente una riga totale in fondo all'elenco per visualizzare SUM, AVERAGE, COUNT, ecc.
- Le colonne aggiunte a destra vengono incorporate automaticamente nell'oggetto List.
- I grafici basati su righe e colonne verranno espansi automaticamente.
- Gli intervalli denominati assegnati a righe e colonne verranno espansi automaticamente.
- L'elenco è protetto dall'eliminazione accidentale di righe e colonne.

## **Creazione di una tabella utilizzando Microsoft Excel**

**Selezione dell'intervallo di dati per la creazione di un oggetto elenco** 

![cose da fare:immagine_alt_testo](creating-a-list-object_1.png)

Viene visualizzata la finestra di dialogo Crea elenco.

**Finestra di dialogo Crea elenco** 

![cose da fare:immagine_alt_testo](creating-a-list-object_2.png)

 Implementando l'oggetto List e specificando Total Row (Select**Dati** , poi**Elenco** , seguito da**Riga totale**).

**Creazione di un oggetto Elenco** 

![cose da fare:immagine_alt_testo](creating-a-list-object_3.png)

## **Creazione di una tabella utilizzando Using Aspose.Cells API**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per creare un[**ElencoOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) in un foglio di lavoro, usa[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) proprietà collection della classe Worksheet. A testa[**ElencoOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) è, infatti, un oggetto del[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)class, che fornisce inoltre il metodo add per aggiungere un oggetto List e specificare un intervallo di celle per l'elenco.

In base all'intervallo di celle specificato, l'oggetto List viene creato nel foglio di lavoro da Aspose.Cells. Utilizzare gli attributi (ad esempio, ShowTotals, ListColumns ecc.) del[**ElencoOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)class per controllare l'elenco.

 Nell'esempio fornito di seguito, abbiamo creato lo stesso[**ElencoOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)utilizzando Aspose.Cells API come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
