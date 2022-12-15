---
title: Convalida dei dati
type: docs
weight: 70
url: /it/java/data-validation/
---
{{% alert color="primary" %}} 

Microsoft Excel offre alcune buone funzionalità per filtrare automaticamente o convalidare i dati del foglio di lavoro.

[Convalida dei dati](/cells/it/java/data-validation/)è la capacità di impostare regole relative ai dati inseriti in un foglio di lavoro. Ad esempio, utilizzare la convalida per garantire che una colonna etichettata DATE contenga solo date o che un'altra colonna contenga solo numeri. Potresti persino assicurarti che una colonna etichettata DATE contenga solo date all'interno di un determinato intervallo. Con la convalida dei dati, puoi controllare cosa viene inserito nelle celle del foglio di lavoro. Aspose.Cells supporta completamente le funzionalità di convalida dei dati e filtro automatico di Microsoft Excel. Questo articolo spiega come utilizzare le funzionalità in Microsoft Excel e come codificarle utilizzando Aspose.Cells.

{{% /alert %}} 
## **Tipi di convalida dei dati ed esecuzione**
Microsoft Excel supporta diversi tipi di convalida dei dati. Ogni tipo viene utilizzato per controllare quale tipo di dati viene immesso in una cella o in un intervallo di celle. Di seguito, frammenti di codice illustrano come convalidarlo:

- [I numeri sono interi](/cells/it/java/data-validation/), cioè che non hanno una parte decimale.
- [I numeri decimali seguono la struttura corretta](/cells/it/java/data-validation/)L'esempio di codice definisce che un intervallo di celle deve avere due spazi decimali.
- [I valori sono limitati a un elenco di valori](/cells/it/java/data-validation/). La convalida dell'elenco definisce un elenco separato di valori che possono essere applicati a una cella o a un intervallo di celle.
- [Le date rientrano in un intervallo specifico](/cells/it/java/data-validation/).
- [Il tempo è all'interno di un intervallo specifico](/cells/it/java/data-validation/).
- [Un testo si trova all'interno di una determinata lunghezza di caratteri](/cells/it/java/data-validation/).
### **Convalida dei dati con Microsoft Excel**
Per creare convalide utilizzando Microsoft Excel:

1. In un foglio di lavoro selezionare le celle a cui si desidera applicare la convalida.
1. Dal**Dati**menù, selezionare**Convalida**.
 Viene visualizzata la finestra di dialogo di convalida.
1. Clicca il**Impostazioni**scheda e immettere le impostazioni come mostrato di seguito.

   **Impostazioni di convalida dei dati** 

![cose da fare:immagine_alt_testo](data-validation_1.png)
### **Convalida dati con Aspose.Cells**
La convalida dei dati è una potente funzionalità per la convalida delle informazioni inserite nei fogli di lavoro. Con la convalida dei dati, gli sviluppatori possono fornire agli utenti un elenco di scelte, limitare l'immissione dei dati a un tipo o dimensione specifica, ecc.
 In Aspose.Cells, ciascuno[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)la classe ha a[Convalide](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)oggetto che rappresenta una raccolta di[Convalida](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)oggetti. Per impostare la convalida, imposta alcuni dei[Convalida](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)proprietà della classe:

- [Tipo](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): rappresenta il tipo di convalida, che può essere specificato utilizzando uno dei valori predefiniti in[Tipo di convalida](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)enumerazione.
- [Operatore](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): rappresenta l'operatore da utilizzare nella validazione, che può essere specificato utilizzando uno dei valori predefiniti nel file[OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)enumerazione.
- [Formula 1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): rappresenta il valore o l'espressione associata alla prima parte della convalida dei dati.
- [Formula2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): rappresenta il valore o l'espressione associata alla seconda parte della convalida dei dati.

Quando il[Convalida](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)le proprietà dell'oggetto sono state configurate, gli sviluppatori possono utilizzare il[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)struttura per memorizzare le informazioni sull'intervallo di celle che verranno convalidate utilizzando la convalida creata.
#### **Tipi di convalida dei dati**
La convalida dei dati consente di creare regole aziendali in ogni cella in modo che le voci errate generino messaggi di errore. Le regole aziendali sono le politiche e le procedure che governano il modo in cui opera un'azienda. Aspose.Cells supporta tutti i tipi importanti di convalida dei dati.

Il[Tipo di convalida](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)enumerazione ha i seguenti membri:

|**Nome del membro**|**Descrizione**|
|:- |:- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Indica un valore di qualsiasi tipo.|
|[NUMERO INTERO](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Indica il tipo di convalida per i numeri interi.|
|[DECIMALE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Indica il tipo di convalida per i numeri decimali.|
|[ELENCO](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Indica il tipo di convalida per l'elenco a discesa.|
|[DATA](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Indica il tipo di convalida per le date.|
|[VOLTA](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Denota il tipo di convalida per Time.|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Indica il tipo di convalida per la lunghezza del testo.|
|[COSTUME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Indica il tipo di convalida personalizzato.|
#### **Esempio di programmazione: convalida dei dati con numeri interi**
Con questo tipo di convalida, gli utenti possono inserire solo numeri interi all'interno di un intervallo specificato nelle celle convalidate. Gli esempi di codice che seguono mostrano come implementare il[NUMERO INTERO](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)tipo di convalida. L'esempio crea la stessa convalida dei dati utilizzando Aspose.Cells che abbiamo creato utilizzando Microsoft Excel sopra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Esempio di programmazione: convalida dei dati decimali**
Con questo tipo di convalida, l'utente può inserire numeri decimali nelle celle convalidate. Nell'esempio, l'utente può inserire solo valori decimali e l'area di convalida è A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Esempio di programmazione: convalida dei dati dell'elenco**
Questo tipo di convalida consente all'utente di immettere valori da un elenco a discesa. Fornisce un elenco: una serie di righe che contengono dati. Gli utenti possono solo selezionare i valori dall'elenco. L'area di convalida è l'intervallo di celle A1:A5 nel primo foglio di lavoro.

Qui è importante impostare il file[Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) proprietà a**VERO**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Esempio di programmazione: convalida dei dati della data**
Con questo tipo di convalida, gli utenti immettono valori di data all'interno di un intervallo specificato o che soddisfano criteri specifici nelle celle convalidate. Nell'esempio, l'utente è limitato a inserire date comprese tra il 1970 e il 1999. Qui, l'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Esempi di programmazione: convalida dei dati temporali**
Con questo tipo di convalida, gli utenti possono inserire orari all'interno di un intervallo specificato o che soddisfano alcuni criteri nelle celle convalidate. Nell'esempio, l'utente è limitato a inserire gli orari tra le 09:00 e le 11:30. Qui, l'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Esempi di programmazione: convalida dei dati di lunghezza del testo**
Con questo tipo di convalida, gli utenti possono inserire valori di testo di una lunghezza specificata nelle celle convalidate. Nell'esempio, l'utente è limitato a immettere valori di stringa con non più di 5 caratteri. L'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Regole di convalida dei dati**
 Quando vengono implementate le convalide dei dati, la convalida può essere verificata assegnando valori diversi nelle celle.[Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) può essere utilizzato per recuperare il risultato della convalida. L'esempio seguente mostra questa funzionalità con valori diversi. Il file di esempio può essere scaricato dal seguente link per il test:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Controlla se la convalida in una cella è a discesa**
 Come abbiamo visto ci sono molti tipi di validazioni che possono essere implementate all'interno di una cella. Se vuoi verificare se la convalida è a discesa o meno,[Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) proprietà può essere utilizzata per testare questo. Il seguente codice di esempio illustra l'utilizzo di questa proprietà. Il file di esempio per il test può essere scaricato dal seguente link:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Aggiungi CellArea alla convalida esistente**
Potrebbero esserci casi in cui potresti voler aggiungere[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)all'esistente[Convalida](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). Quando aggiungi[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)utilizzando[Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells controlla tutte le aree esistenti per vedere se la nuova area esiste già. Se il file ha un numero elevato di convalide, ciò subisce un calo delle prestazioni. Per ovviare a questo, l'API fornisce il[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) metodo. Il*checkIntersezione*parametro indica se controllare l'intersezione di una determinata area con le aree di validazione esistenti. Impostandolo su**falso**disabiliterà il controllo di altre aree. Il*checkEdge*parametro indica se controllare le aree applicate. Se la nuova area diventa l'area in alto a sinistra, le impostazioni interne vengono ricostruite. Se sei sicuro che la nuova area non sia l'area in alto a sinistra, puoi impostare questo parametro come**falso**.

Il seguente frammento di codice illustra l'uso di[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) metodo per aggiungere new[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)all'esistente[Convalida](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

I file excel di origine e di output sono allegati per riferimento.

[File sorgente](PivotTableHideAndSortSample.xlsx)

[File di uscita](ValidationsSample_out.xlsx)


## **Argomenti avanzati**
- [Ottieni la convalida Cell nei file ODS](/cells/it/java/get-cell-validation-in-ods-files/)
- [Ottieni la convalida applicata su uno Cell](/cells/it/java/get-validation-applied-on-a-cell/)
- [Verificare che il valore Cell soddisfi le regole di convalida dei dati](/cells/it/java/verify-that-cell-value-satisfies-data-validation-rules/)
