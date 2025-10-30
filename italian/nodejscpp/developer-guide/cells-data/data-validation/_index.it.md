---  
title: Convalida dei dati
type: docs  
weight: 90  
url: /it/nodejs-cpp/data-validation/  
description: Impara come aggiungere la validazione dei dati tramite l API Aspose.Cells for Node.js via C++.  
keywords: Aggiungi Validazione Dati Node.js via C++, ottieni Valore di Validazione Node.js via C++, aggiungi Validazione Numero Intero Node.js via C++, aggiungi Validazione Lista Node.js via C++, aggiungi Validazione Data Node.js via C++, aggiungi Validazione Ora Node.js via C++, aggiungi Lunghezza del Testo Validazione Node.js via C++, aggiungi CellArea alla Validazione esistente Node.js via C++, verifica se la validazione in una cella è un menu a tendina Node.js via C++, aggiungi Validazione Personalizzata Node.js via C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel offre alcune buone funzioni per filtrare automaticamente o validare i dati del foglio di lavoro. Aspose.Cells supporta pienamente le funzioni di validazione dei dati e AutoFilter di Microsoft Excel. Questo articolo spiega come usare queste funzioni in Excel e come programmarle utilizzando Aspose.Cells for Node.js via C++.  
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

### **Validazione Dati con Aspose.Cells for Node.js via C++**  

La convalida dei dati è una funzionalità potente per convalidare le informazioni inserite nei fogli di lavoro. Con la convalida dei dati, gli sviluppatori possono fornire agli utenti un elenco di scelte, limitare le voci di dati a un tipo o dimensione specifici, ecc.  
In Aspose.Cells for Node.js via C++, ogni classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) ha un metodo [**getValidations()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getValidations--) che rappresenta una collezione di oggetti [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation). Per configurare la validazione, impostare alcune proprietà della classe [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) come segue:  

- Tipo – rappresenta il tipo di validazione, che può essere specificato usando uno dei valori predefiniti nell'enumerazione [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype).  
- Operatore – rappresenta l'operatore da usare nella validazione, che può essere specificato usando uno dei valori predefiniti nell'enumerazione [**OperatorType**](https://reference.aspose.com/cells/nodejs-cpp/operatortype).  
- Formula1: rappresenta il valore o l'espressione associata alla prima parte della convalida dei dati.  
- Formula2: rappresenta il valore o l'espressione associata alla seconda parte della convalida dei dati.  

Quando le proprietà dell'oggetto [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) sono state configurate, gli sviluppatori possono usare la struttura [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) per memorizzare informazioni sull'intervallo di celle che verrà convalidato usando la validazione creata.  

#### **Tipi di Convalida dei Dati**  

L'enumerazione [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) ha i seguenti membri:  

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

Con questo tipo di convalida, gli utenti possono inserire solo numeri interi all’interno di un intervallo specificato nelle celle convalidates. Gli esempi di codice che seguono mostrano come implementare il tipo di convalida NumberIntero. L’esempio crea la stessa convalida dei dati usando Aspose.Cells for Node.js via C++ che abbiamo creato in Microsoft Excel sopra.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-WholeNumber.js" >}}


##### **Convalida dei dati della lista**  

Questo tipo di convalida consente all'utente di inserire valori da un elenco a discesa. Fornisce un elenco: una serie di righe che contengono dati. Nell'esempio, viene aggiunta un secondo foglio di lavoro per contenere la fonte dell'elenco. Gli utenti possono selezionare solo valori dall'elenco. L'area di convalida è l'intervallo di celle A1:A5 nel primo foglio di lavoro.  

È importante qui impostare la proprietà [**Validation.setInCellDropDown(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#setInCellDropDown-boolean-) su **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ListData.js" >}}


##### **Convalida dei dati della data**  

Con questo tipo di convalida, gli utenti inseriscono valori di data entro un intervallo specificato, o che soddisfano determinati criteri, nelle celle convalidate. Nell'esempio, all'utente è vietato inserire date comprese tra il 1970 e il 1999. Qui, l'area di convalida è la cella B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DateData.js" >}}

##### **Convalida dei dati dell'ora**  

Con questo tipo di convalida, gli utenti possono inserire orari entro un intervallo specificato, o soddisfare alcuni criteri, nelle celle convalidate. Nell'esempio, all'utente è vietato inserire orari tra le 09:00 e le 11:30 del mattino. Qui, l'area di convalida è la cella B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TimeData.js" >}}


##### **Convalida della lunghezza del testo**  

Con questo tipo di convalida, gli utenti possono inserire valori di testo di una lunghezza specificata nelle celle convalidate. Nell'esempio, all'utente è vietato inserire valori di stringa con più di 5 caratteri. L'area di convalida è la cella B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TextLengthData.js" >}}


### **Regole di convalida dei dati**  

Quando le validazioni dei dati vengono implementate, è possibile verificarle assegnando valori diversi nelle celle. [**Cell.getValidationValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) può essere usato per ottenere il risultato della validazione. Il seguente esempio dimostra questa funzione con valori diversi. Il file di esempio può essere scaricato dal link sottostante per testare:  

[sampleDataValidationRules.xlsx](77496339.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DataValidationRules.js" >}}


## **Verifica se la convalida nella cella è a discesa**  

Come abbiamo visto, ci sono molti tipi di validazioni che possono essere implementate all’interno di una cella. Se vuoi verificare se la validazione è un menu a tendina o meno, puoi usare il metodo [**Validation.getInCellDropDown()**](https://reference.aspose.com/cells/nodejs-cpp/validation/#getInCellDropDown--) per testare questa proprietà. Un esempio di codice che dimostra l’uso di questa proprietà può essere scaricato dal link:  

[sampleValidation.xlsx](79527947.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-CheckValidationIsDropDown.js" >}}


## **Aggiungi CellArea alla convalida esistente**  

Potrebbero esserci casi in cui vuoi aggiungere [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) a un [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) esistente. Quando aggiungi [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) usando [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-), Aspose.Cells verifica tutte le aree esistenti per vedere se l'area nuova è già presente. Se il file ha molte validazioni, questo comporta un impatto sulle prestazioni. Per ovviare a questo, l’API fornisce il metodo [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-). Il parametro *checkIntersection* indica se verificare l’intersezione di un'area data con le aree di validazione esistenti. Impostarlo su **false** disabiliterà il controllo di altre aree. Il parametro *checkEdge* indica se verificare le aree applicate. Se la nuova area diventa l’area in alto a sinistra, le impostazioni interne vengono ricostruite. Se sei sicuro che la nuova area non sia quella in alto a sinistra, puoi impostare questo parametro su **false**.  

Il seguente esempio di codice dimostra l’uso del metodo [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-) per aggiungere una nuova [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) a un [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) esistente.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-AddCellAreaToExistingValidation.js" >}}

I file excel sorgente e di output sono allegati a scopo informativo.  

[File di origine](96928093.xlsx)  

[File di output](96928220.xlsx)  

## **Argomenti avanzati**  
- [Ottieni la Convalida Cellulare nei File ODS](/cells/it/nodejs-cpp/get-cell-validation-in-ods-files/)  
- [Ottieni la Convalida Applicata su una Cella](/cells/it/nodejs-cpp/get-validation-applied-on-a-cell/)  
- [Verifica che il Valore della Cella Soddisfi le Regole di Convalida dei Dati](/cells/it/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
