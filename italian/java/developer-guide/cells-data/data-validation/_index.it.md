---
title: Convalida dei dati
type: docs
weight: 70
url: /it/java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel fornisce alcune ottime funzionalità per filtrare automaticamente o convalidare i dati del foglio di lavoro.

[Convalida dei dati](/cells/it/java/data-validation/) è la capacità di impostare regole relative ai dati inseriti in un foglio di lavoro. Ad esempio, utilizzare la convalida per garantire che una colonna denominata DATA contenga solo date, o che un'altra colonna contenga solo numeri. È persino possibile garantire che una colonna denominata DATA contenga solo date entro un determinato intervallo. Con la convalida dei dati, è possibile controllare cosa viene inserito nelle celle del foglio di lavoro. Aspose.Cells supporta pienamente la convalida dei dati e le funzioni di autofiltro di Microsoft Excel. Questo articolo spiega come utilizzare le funzionalità in Microsoft Excel e come codificarle utilizzando Aspose.Cells.

{{% /alert %}} 
## **Tipi ed esecuzione della convalida dei dati**
Microsoft Excel supporta diversi tipi di convalida dei dati. Ogni tipo viene utilizzato per controllare quale tipo di dati viene inserito in una cella o in un intervallo di celle. Di seguito, frammenti di codice illustrano come convalidare che:

- [I numeri sono interi](/cells/it/java/data-validation/), cioè, che non hanno una parte decimale.
- I numeri decimali seguono la struttura corretta. L'esempio di codice definisce che un intervallo di celle dovrebbe avere due posizioni decimali.
- I valori sono limitati a un elenco di valori. La convalida della lista definisce un elenco separato di valori che possono essere applicati a una cella o a un intervallo di celle.
- Le date rientrano in un intervallo specifico.
- L'ora rientra in un intervallo specifico.
- Un testo rientra in una data lunghezza specifica di caratteri.
### **Convalida dei dati con Microsoft Excel**
Per creare convalide utilizzando Microsoft Excel:

1. In un foglio di lavoro, selezionare le celle a cui si desidera applicare la convalida.
1. Dal menu **Dati**, selezionare **Convalida**.
   Viene visualizzata la finestra di dialogo di convalida.
1. Fare clic sulla scheda **Impostazioni** e immettere le impostazioni come mostrato di seguito. 

   **Impostazioni di convalida dei dati** 

![todo:image_alt_text](data-validation_1.png)
### **Convalida dei dati con Aspose.Cells**
La convalida dei dati è una funzionalità potente per convalidare le informazioni inserite nei fogli di lavoro. Con la convalida dei dati, gli sviluppatori possono fornire agli utenti un elenco di scelte, limitare le voci di dati a un tipo o dimensione specifici, ecc.
In Aspose.Cells, ogni classe [Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) ha un oggetto [Convalida](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations) che rappresenta una raccolta di oggetti [Convalida](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). Per impostare la convalida, impostare alcune proprietà della classe [Convalida](https://reference.aspose.com/cells/java/com.aspose.cells/Validation):

- [Tipo](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): rappresenta il tipo di convalida, che può essere specificato utilizzando uno dei valori predefiniti nell'enumerazione [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType).
- [Operatore](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): rappresenta l'operatore da utilizzare nella convalida, che può essere specificato utilizzando uno dei valori predefiniti nell'enumerazione [OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType).
- [Formula1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): rappresenta il valore o l'espressione associata alla prima parte della convalida dei dati.
- [Formula2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): rappresenta il valore o l'espressione associata alla seconda parte della convalida dei dati.

Una volta configurate le proprietà dell'oggetto [Convalida](https://reference.aspose.com/cells/java/com.aspose.cells/Validation), gli sviluppatori possono utilizzare la struttura [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) per memorizzare informazioni sul intervallo di celle che verrà convalidato utilizzando la convalida creata.
#### **Tipi di Convalida dei Dati**
La convalida dei dati consente di integrare regole aziendali in ciascuna cella in modo che le voci non corrette generino messaggi di errore. Le regole aziendali sono le politiche e le procedure che regolano il funzionamento di un'azienda. Aspose.Cells supporta tutti i principali tipi di convalida dei dati.

L'enumerazione [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType) ha i seguenti membri:

|**Nome Membr***|**Descrizione**|
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Indica un valore di qualsiasi tipo.
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Indica il tipo di convalida per i numeri interi.
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Indica il tipo di convalida per i numeri decimali.
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Indica il tipo di convalida per elenco a discesa.
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Indica il tipo di convalida per le date.
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Indica il tipo di convalida per l'ora.
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Indica il tipo di convalida per la lunghezza del testo.
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Indica il tipo di convalida personalizzato.
#### **Esempio di programmazione: convalida dati numerici interi**
Con questo tipo di convalida, gli utenti possono inserire solo numeri interi entro un determinato intervallo nelle celle convalidate. Gli esempi di codice che seguono mostrano come implementare il tipo di convalida [WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER). L'esempio crea la stessa convalida dei dati utilizzando Aspose.Cells, che abbiamo creato utilizzando Microsoft Excel sopra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Esempio di programmazione: convalida dati decimali**
Con questo tipo di convalida, l'utente può inserire numeri decimali nelle celle convalidate. Nell'esempio, all'utente è vietato inserire solo valori decimali e l'area di convalida è A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Esempio di programmazione: convalida dati di elenco**
Questo tipo di convalida consente all'utente di inserire valori da un elenco a discesa. Fornisce un elenco: una serie di righe che contengono dati. Gli utenti possono selezionare solo valori dall'elenco. L'area di convalida è l'intervallo di celle A1:A5 nel primo foglio di lavoro.

È importante impostare la proprietà [Validation.setInCellDrown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) su **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Esempio di programmazione: convalida dati di data**
Con questo tipo di convalida, gli utenti inseriscono valori di data entro un intervallo specificato, o che soddisfano determinati criteri, nelle celle convalidate. Nell'esempio, all'utente è vietato inserire date comprese tra il 1970 e il 1999. Qui, l'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Esempi di programmazione: convalida dati di ora**
Con questo tipo di convalida, gli utenti possono inserire orari entro un intervallo specificato, o soddisfare alcuni criteri, nelle celle convalidate. Nell'esempio, all'utente è vietato inserire orari tra le 09:00 e le 11:30 del mattino. Qui, l'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Esempi di programmazione: convalida dati di lunghezza del testo**
Con questo tipo di convalida, gli utenti possono inserire valori di testo di una lunghezza specificata nelle celle convalidate. Nell'esempio, all'utente è vietato inserire valori di stringa con più di 5 caratteri. L'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Regole di convalida dei dati**
Quando le convalide dei dati sono implementate, è possibile controllare la convalida assegnando valori diversi alle celle. [Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) può essere utilizzato per ottenere il risultato della convalida. L'esempio seguente dimostra questa funzionalità con valori diversi. Il file di esempio può essere scaricato dal seguente link per il test:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Verifica se la convalida in una cella è una selezione a discesa**
Come abbiamo visto ci sono molti tipi di convalide che possono essere implementati all'interno di una cella. Se si desidera verificare se la convalida è una selezione a discesa o meno, [Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) può essere utilizzato per testare questo. Il seguente codice di esempio dimostra l'utilizzo di questa proprietà. Il file di esempio per il test può essere scaricato dal seguente link:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Aggiungi CellArea alla convalida esistente**
Potrebbero esserci casi in cui potresti voler aggiungere [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) a [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) esistenti. Quando si aggiunge [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) usando [Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells controlla tutte le aree esistenti per vedere se la nuova area esiste già. Se il file ha un gran numero di convalide, ciò influisce sulle prestazioni. Per ovviare a ciò, l'API fornisce il metodo [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)). Il parametro *checkIntersection* indica se controllare l'intersezione di un'area data con le aree di convalida esistenti. Impostarlo su **false** disabiliterà il controllo di altre aree. Il parametro *checkEdge* indica se controllare le aree applicate. Se la nuova area diventa l'area in alto a sinistra, le impostazioni interne vengono ricostruite. Se sei sicuro che la nuova area non sia l'area in alto a sinistra, puoi impostare questo parametro su **false**.

Lo snippet di codice seguente mostra l'uso del metodo [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) per aggiungere una nuova [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) a un [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) esistente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

I file excel sorgente e di output sono allegati a scopo informativo.

[File Sorgente](PivotTableHideAndSortSample.xlsx)

[File di Output](ValidationsSample_out.xlsx)


## **Argomenti avanzati**
- [Ottieni la Convalida Cellulare nei File ODS](/cells/it/java/get-cell-validation-in-ods-files/)
- [Ottieni la Convalida Applicata su una Cella](/cells/it/java/get-validation-applied-on-a-cell/)
- [Verifica che il Valore della Cella Soddisfi le Regole di Convalida dei Dati](/cells/it/java/verify-that-cell-value-satisfies-data-validation-rules/)
