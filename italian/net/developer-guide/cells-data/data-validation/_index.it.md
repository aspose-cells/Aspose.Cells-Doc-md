---
title: Convalida dei dati
type: docs
weight: 90
url: /it/net/data-validation/
---
{{% alert color="primary" %}}

Microsoft Excel fornisce alcune buone funzionalità per filtrare o convalidare automaticamente i dati del foglio di lavoro.Aspose.Cells supporta completamente Microsoft la convalida dei dati di Excel e le funzionalità di filtro automatico. Questo articolo spiega come utilizzare le funzionalità in Microsoft Excel e come codificarle utilizzando Aspose.Cells.

{{% /alert %}}

## **Tipi di convalida dei dati ed esecuzione**

La convalida dei dati è la capacità di impostare regole relative ai dati inseriti in un foglio di lavoro. Ad esempio, utilizzare la convalida per garantire che una colonna etichettata DATE contenga solo date o che un'altra colonna contenga solo numeri. Potresti persino assicurarti che una colonna etichettata DATE contenga solo date all'interno di un determinato intervallo. Con la convalida dei dati, puoi controllare cosa viene inserito nelle celle del foglio di lavoro.

Microsoft Excel supporta diversi tipi di convalida dei dati. Ogni tipo viene utilizzato per controllare quale tipo di dati viene immesso in una cella o in un intervallo di celle. Di seguito, frammenti di codice illustrano come convalidarlo:

- I numeri sono interi, cioè che non hanno la parte decimale.
- I numeri decimali seguono la struttura corretta. L'esempio di codice definisce che un intervallo di celle deve avere due spazi decimali.
- I valori sono limitati a un elenco di valori. La convalida dell'elenco definisce un elenco separato di valori che possono essere applicati a una cella o a un intervallo di celle.
- Le date rientrano in un intervallo specifico.
- Un tempo è all'interno di un intervallo specifico.
- Un testo si trova all'interno di una determinata lunghezza di caratteri.

### **Convalida dati con Microsoft Excel**

Per creare convalide utilizzando Microsoft Excel:

1. In un foglio di lavoro selezionare le celle a cui si desidera applicare la convalida.
1.  Dal**Dati** menù, selezionare**Convalida**. Verrà visualizzata la finestra di dialogo di convalida.
1.  Clicca il**Impostazioni** scheda e accedere alle impostazioni.

### **Convalida dati con Aspose.Cells**

La convalida dei dati è una potente funzionalità per la convalida delle informazioni inserite nei fogli di lavoro. Con la convalida dei dati, gli sviluppatori possono fornire agli utenti un elenco di scelte, limitare l'immissione dei dati a un tipo o dimensione specifica, ecc.
 In Aspose.Cells, ciascuno[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe ha a[**Convalide**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)proprietà che rappresenta una raccolta di[**Convalida**](https://reference.aspose.com/cells/net/aspose.cells/validation) oggetti. Per impostare la convalida, imposta alcuni dei[**Convalida**](https://reference.aspose.com/cells/net/aspose.cells/validation)class' proprietà come segue:

- Tipo: rappresenta il tipo di convalida, che può essere specificato utilizzando uno dei valori predefiniti in[**Tipo di convalida**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)enumerazione.
-  Operatore: rappresenta l'operatore da utilizzare nella convalida, che può essere specificato utilizzando uno dei valori predefiniti in[**OperatorType**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)enumerazione.
- Formula1: rappresenta il valore o l'espressione associata alla prima parte della convalida dei dati.
- Formula2: rappresenta il valore o l'espressione associata alla seconda parte della convalida dei dati.

 Quando il[**Convalida**](https://reference.aspose.com/cells/net/aspose.cells/validation) le proprietà dell'oggetto sono state configurate, gli sviluppatori possono utilizzare il[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)struttura per memorizzare le informazioni sull'intervallo di celle che verranno convalidate utilizzando la convalida creata.

#### **Tipi di convalida dei dati**

 Il[**Tipo di convalida**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)enumerazione ha i seguenti membri:

|**Nome del membro**|**Descrizione**|
|:- |:- |
|AnyValue|Indica un valore di qualsiasi tipo.|
|Numero intero|Indica il tipo di convalida per i numeri interi.|
|Decimale|Indica il tipo di convalida per i numeri decimali.|
|Elenco|Indica il tipo di convalida per l'elenco a discesa.|
|Data|Indica il tipo di convalida per le date.|
|Volta|Denota il tipo di convalida per l'ora.|
|Lunghezza testo|Indica il tipo di convalida per la lunghezza del testo.|
|Costume|Indica il tipo di convalida personalizzato.|

##### **Convalida dei dati con numeri interi**

Con questo tipo di convalida, gli utenti possono inserire solo numeri interi all'interno di un intervallo specificato nelle celle convalidate. Gli esempi di codice che seguono mostrano come implementare il tipo di convalida WholeNumber. L'esempio crea la stessa convalida dei dati utilizzando Aspose.Cells che abbiamo creato utilizzando Microsoft Excel sopra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **Convalida dei dati dell'elenco**

Questo tipo di convalida consente all'utente di immettere valori da un elenco a discesa. Fornisce un elenco: una serie di righe che contengono dati. Nell'esempio, viene aggiunto un secondo foglio di lavoro per contenere l'origine dell'elenco. Gli utenti possono solo selezionare i valori dall'elenco. L'area di convalida è l'intervallo di celle A1:A5 nel primo foglio di lavoro.

 Qui è importante impostare il file[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) proprietà a**VERO**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **Data Convalida dati**

Con questo tipo di convalida, gli utenti immettono valori di data all'interno di un intervallo specificato o che soddisfano criteri specifici nelle celle convalidate. Nell'esempio, l'utente è limitato a inserire date comprese tra il 1970 e il 1999. Qui, l'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **Convalida dei dati temporali**

Con questo tipo di convalida, gli utenti possono inserire orari all'interno di un intervallo specificato o che soddisfano alcuni criteri nelle celle convalidate. Nell'esempio, l'utente è limitato a inserire gli orari tra le 09:00 e le 11:30. Qui, l'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **Convalida dei dati sulla lunghezza del testo**

Con questo tipo di convalida, gli utenti possono inserire valori di testo di una lunghezza specificata nelle celle convalidate. Nell'esempio, l'utente è limitato a immettere valori di stringa con non più di 5 caratteri. L'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **Regole di convalida dei dati**

Quando vengono implementate le convalide dei dati, la convalida può essere verificata assegnando valori diversi nelle celle.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) può essere utilizzato per recuperare il risultato della convalida. L'esempio seguente mostra questa funzionalità con valori diversi. Il file di esempio può essere scaricato dal seguente link per il test:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **Controlla se la convalida nella cella è a discesa**

 Come abbiamo visto ci sono molti tipi di validazioni che possono essere implementate all'interno di una cella. Se vuoi verificare se la convalida è a discesa o meno,[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) proprietà può essere utilizzata per testare questo. Il codice di esempio seguente illustra l'utilizzo di questa proprietà. Un file di esempio per il test può essere scaricato dal seguente link:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **Aggiungi CellArea alla convalida esistente**

 Potrebbero esserci casi in cui potresti voler aggiungere[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)all'esistente[**Convalida**](https://reference.aspose.com/cells/net/aspose.cells/validation). Quando aggiungi[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) utilizzando[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells controlla tutte le aree esistenti per vedere se la nuova area esiste già. Se il file ha un numero elevato di convalide, ciò subisce un calo delle prestazioni. Per ovviare a questo, lo API mette a disposizione il[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) metodo. Il*checkIntersezione* parametro indica se controllare l'intersezione di una determinata area con le aree di validazione esistenti. Impostandolo su**falso** disabiliterà il controllo di altre aree. Il*checkEdge* parametro indica se controllare le aree applicate. Se la nuova area diventa l'area in alto a sinistra, le impostazioni interne vengono ricostruite. Se sei sicuro che la nuova area non sia l'area in alto a sinistra, puoi impostare questo parametro come**falso**.

Il seguente frammento di codice illustra l'uso di[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) metodo per aggiungere nuovo[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)all'esistente[**Convalida**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

I file excel di origine e di output sono allegati per riferimento.

[File sorgente](96928093.xlsx)

[File di uscita](96928220.xlsx)


## **Argomenti avanzati**
- [Ottieni la convalida Cell nei file ODS](/cells/it/net/get-cell-validation-in-ods-files/)
- [Ottieni la convalida applicata su uno Cell](/cells/it/net/get-validation-applied-on-a-cell/)
- [Verificare che il valore Cell soddisfi le regole di convalida dei dati](/cells/it/net/verify-that-cell-value-satisfies-data-validation-rules/)
