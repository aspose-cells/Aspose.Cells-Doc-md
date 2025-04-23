---
title: Convalida dei dati
type: docs
weight: 90
url: /it/net/data-validation/
description: Scopri come aggiungere la convalida dei dati tramite l API Aspose.Cells for .NET.
keywords: Aggiungi la convalida dei dati, ottieni il valore di convalida, aggiungi la convalida dei dati numerici interi, aggiungi la convalida dei dati di elenco, aggiungi la convalida dei dati della data, aggiungi la convalida dell orario, aggiungi la convalida della lunghezza del testo, aggiungi l area della cella alla convalida esistente, Controlla se la convalida nella cella è un menu a discesa, Aggiungi convalida personalizzata  
---

{{% alert color="primary" %}}

Microsoft Excel fornisce alcune buone funzioni per filtrare automaticamente o convalidare i dati del foglio di lavoro. Aspose.Cells supporta completamente le funzionalità di convalida dei dati e filtro automatico di Microsoft Excel. Questo articolo spiega come utilizzare le funzionalità in Microsoft Excel e come codificarle utilizzando Aspose.Cells.

{{% /alert %}}

## **Tipi ed esecuzione della convalida dei dati**

La convalida dei dati è la capacità di impostare regole relative ai dati inseriti in un foglio di lavoro. Ad esempio, utilizzare la convalida per garantire che una colonna denominata DATA contenga solo date, o che un'altra colonna contenga solo numeri. È possibile anche garantire che una colonna denominata DATA contenga solo date entro un determinato intervallo. Con la convalida dei dati è possibile controllare cosa viene inserito nelle celle del foglio di lavoro.

Microsoft Excel supporta diversi tipi di convalida dei dati. Ogni tipo viene utilizzato per controllare quale tipo di dati viene inserito in una cella o in un intervallo di celle. Di seguito, frammenti di codice illustrano come convalidare che:

- I numeri sono interi, cioè non hanno una parte decimale.
- I numeri decimali seguono la struttura corretta. L'esempio di codice definisce che un intervallo di celle dovrebbe avere due decimali.
- I valori sono limitati a un elenco di valori. La convalida dell'elenco definisce un elenco separato di valori che possono essere applicati a una cella o a un intervallo di celle.
- Le date rientrano in un intervallo specifico.
- Un'ora è all'interno di un intervallo specifico.
- Un testo è di una determinata lunghezza di caratteri.

### **Convalida dei dati con Microsoft Excel**

Per creare convalide utilizzando Microsoft Excel:

1. In un foglio di lavoro, selezionare le celle a cui si desidera applicare la convalida.
1. Dal menu **Dati**, seleziona **Convalida**. Verrà visualizzata la finestra di dialogo di convalida.
1. Fai clic sulla scheda **Impostazioni** e inserisci le impostazioni.

### **Convalida dei dati con Aspose.Cells**

La convalida dei dati è una funzionalità potente per convalidare le informazioni inserite nei fogli di lavoro. Con la convalida dei dati, gli sviluppatori possono fornire agli utenti un elenco di scelte, limitare le voci di dati a un tipo o dimensione specifici, ecc.
In Aspose.Cells, ogni classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ha una proprietà [**Validations**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations) che rappresenta una raccolta di oggetti [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation). Per impostare la convalida, impostare alcune delle proprietà della classe [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) come segue:

- Tipo: rappresenta il tipo di convalida, che può essere specificato utilizzando uno dei valori predefiniti nell'enumerazione [**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype).
- Operatore: rappresenta l'operatore da utilizzare nella convalida, che può essere specificato utilizzando uno dei valori predefiniti nell'enumerazione [**OperatorType**](https://reference.aspose.com/cells/net/aspose.cells/operatortype).
- Formula1: rappresenta il valore o l'espressione associata alla prima parte della convalida dei dati.
- Formula2: rappresenta il valore o l'espressione associata alla seconda parte della convalida dei dati.

Quando le proprietà dell'oggetto [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) sono state configurate, gli sviluppatori possono utilizzare la struttura [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) per memorizzare informazioni sull'intervallo di celle che verrà convalidato utilizzando la convalida creata.

#### **Tipi di Convalida dei Dati**

L'enumerazione [**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype) ha i seguenti membri:

|**Nome Membr***|**Descrizione**|
| :- | :- |
|AnyValue|Denota un valore di qualsiasi tipo.
|WholeNumber|Denota il tipo di convalida per i numeri interi.
|Decimal|Indica il tipo di convalida per i numeri decimali.|
|List|Indica il tipo di convalida per elenchi a discesa.|
|Date|Indica il tipo di convalida per le date.|
|Time|Indica il tipo di convalida per l'ora.|
|TextLength|Indica il tipo di convalida per la lunghezza del testo.|
|Custom|Indica il tipo di convalida personalizzato.|

##### **Convalida dei dati del numero intero**

Con questo tipo di convalida, gli utenti possono inserire solo numeri interi entro un intervallo specificato nelle celle convalidare. Gli esempi di codice seguenti mostrano come implementare il tipo di convalida del numero intero. L'esempio crea la stessa convalida dei dati utilizzando Aspose.Cells che abbiamo creato usando Microsoft Excel sopra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **Convalida dei dati della lista**

Questo tipo di convalida consente all'utente di inserire valori da un elenco a discesa. Fornisce un elenco: una serie di righe che contengono dati. Nell'esempio, viene aggiunta un secondo foglio di lavoro per contenere la fonte dell'elenco. Gli utenti possono selezionare solo valori dall'elenco. L'area di convalida è l'intervallo di celle A1:A5 nel primo foglio di lavoro.

È importante qui impostare la proprietà [**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) su **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **Convalida dei dati della data**

Con questo tipo di convalida, gli utenti inseriscono valori di data entro un intervallo specificato, o che soddisfano determinati criteri, nelle celle convalidate. Nell'esempio, all'utente è vietato inserire date comprese tra il 1970 e il 1999. Qui, l'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **Convalida dei dati dell'ora**

Con questo tipo di convalida, gli utenti possono inserire orari entro un intervallo specificato, o soddisfare alcuni criteri, nelle celle convalidate. Nell'esempio, all'utente è vietato inserire orari tra le 09:00 e le 11:30 del mattino. Qui, l'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **Convalida della lunghezza del testo**

Con questo tipo di convalida, gli utenti possono inserire valori di testo di una lunghezza specificata nelle celle convalidate. Nell'esempio, all'utente è vietato inserire valori di stringa con più di 5 caratteri. L'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **Regole di convalida dei dati**

Quando le convalide dei dati sono implementate, la convalida può essere verificata assegnando valori diversi nelle celle. [**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) può essere utilizzato per ottenere il risultato della convalida. L'esempio seguente illustra questa funzionalità con valori diversi. Il file di esempio può essere scaricato dal seguente link per il test:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **Verifica se la convalida nella cella è a discesa**

Come abbiamo visto, ci sono molti tipi di convalida che possono essere implementati all'interno di una cella. Se si desidera verificare se la convalida è a discesa o no, può essere utilizzata la proprietà [**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) per testare questo. Il codice di esempio seguente dimostra l'uso di questa proprietà. Un file di esempio per il testing può essere scaricato dal seguente link:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **Aggiungi CellArea alla convalida esistente**

Potrebbero esserci casi in cui si desidera aggiungere [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) a [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) esistenti. Quando si aggiunge [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) utilizzando [**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells controlla tutte le aree esistenti per vedere se la nuova area esiste già. Se il file contiene un gran numero di convalide, si verifica un calo delle prestazioni. Per superare questo problema, l'API fornisce il metodo [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1). Il parametro *checkIntersection* indica se verificare l'intersezione di una data area con le aree di convalida esistenti. Impostarlo su **false** disabilita la verifica delle altre aree. Il parametro *checkEdge* indica se verificare le aree applicate. Se la nuova area diventa l'area in alto a sinistra, le impostazioni interne vengono ricostruite. Se si è sicuri che la nuova area non sia l'area in alto a sinistra, è possibile impostare questo parametro su **false**.

Il seguente frammento di codice dimostra l'uso del metodo [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) per aggiungere nuove [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) alle [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) esistenti.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

I file excel sorgente e di output sono allegati a scopo informativo.

[File di origine](96928093.xlsx)

[File di output](96928220.xlsx)


## **Argomenti avanzati**
- [Ottieni la Convalida Cellulare nei File ODS](/cells/it/net/get-cell-validation-in-ods-files/)
- [Ottieni la Convalida Applicata su una Cella](/cells/it/net/get-validation-applied-on-a-cell/)
- [Verifica che il Valore della Cella Soddisfi le Regole di Convalida dei Dati](/cells/it/net/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="csharp" >}}
