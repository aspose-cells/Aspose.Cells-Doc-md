---
title: Convalida dei dati
type: docs
weight: 90
url: /it/net/data-validation/
description: Scopri come aggiungere la convalida dei dati tramite lo Aspose.Cells for .NET API.
keywords: Add Data Validation, Get Validation Value, Add Whole Number Data Validation, Add List Data Validation, Add Date Data Validation, Add Time Data Validation, Add Text Length Data Validation, Add CellArea to existing Validation, Check if validation in cell is dropdown, Add Custom Valication  
---
{{% alert color="primary" %}}

Microsoft Excel fornisce alcune buone funzionalità per filtrare o convalidare automaticamente i dati del foglio di lavoro. Aspose.Cells supporta completamente Microsoft la convalida dei dati di Excel e le funzionalità di filtro automatico. Questo articolo spiega come utilizzare le funzionalità in Microsoft Excel e come codificarle utilizzando Aspose.Cells.

{{% /alert %}}

##  **Tipi ed esecuzione di convalida dei dati**

La convalida dei dati è la capacità di impostare regole relative ai dati immessi in un foglio di lavoro. Ad esempio, utilizza la convalida per garantire che una colonna denominata DATA contenga solo date o che un'altra colonna contenga solo numeri. Potresti anche assicurarti che una colonna denominata DATE contenga solo date comprese in un determinato intervallo. Con la convalida dei dati, puoi controllare cosa viene inserito nelle celle del foglio di lavoro.

Microsoft Excel supporta diversi tipi di convalida dei dati. Ciascun tipo viene utilizzato per controllare il tipo di dati immessi in una cella o in un intervallo di celle. Di seguito, i frammenti di codice illustrano come convalidarlo:

- Numbers sono interi, cioè non hanno la parte decimale.
- numeri decimali seguono la struttura corretta. L'esempio di codice definisce che un intervallo di celle deve avere due spazi decimali.
- I valori sono limitati a un elenco di valori. La convalida dell'elenco definisce un elenco separato di valori che possono essere applicati a una cella o a un intervallo di celle.
- Le date rientrano in un intervallo specifico.
- Un'ora rientra in un intervallo specifico.
- Un testo rientra in una determinata lunghezza di caratteri.

###  **Convalida dati con Microsoft Excel**

Per creare convalide utilizzando Microsoft Excel:

1. In un foglio di lavoro seleziona le celle a cui desideri applicare la convalida.
1.  Dal**Dati** selezionare *Convalida**. Verrà visualizzata la finestra di dialogo di convalida.
1.  Clicca il**Impostazioni** scheda e accedere alle impostazioni.

###  **Convalida dati con Aspose.Cells**

La convalida dei dati è una potente funzionalità per convalidare le informazioni immesse nei fogli di lavoro. Con la convalida dei dati, gli sviluppatori possono fornire agli utenti un elenco di scelte, limitare le immissioni di dati a un tipo o dimensione specifica, ecc.
 Allo Aspose.Cells, ciascuno[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)la classe ha a[**Convalide**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations) proprietà che rappresenta una raccolta di[**Validazione**](https://reference.aspose.com/cells/net/aspose.cells/validation) oggetti. Per impostare la convalida, imposta alcuni dei file[**Validazione**](https://reference.aspose.com/cells/net/aspose.cells/validation)proprietà della classe come segue:

- Tipo: rappresenta il tipo di convalida, che può essere specificato utilizzando uno dei valori predefiniti nel file[**Tipo di convalida**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)enumerazione.
-  Operatore – rappresenta l'operatore da utilizzare nella validazione, che può essere specificato utilizzando uno dei valori predefiniti nel file[**OperatorType**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)enumerazione.
- Formula1 – rappresenta il valore o l'espressione associata alla prima parte della convalida dei dati.
- Formula2 – rappresenta il valore o l'espressione associata alla seconda parte della convalida dei dati.

 Quando il[**Validazione**](https://reference.aspose.com/cells/net/aspose.cells/validation) le proprietà dell'oggetto sono state configurate, gli sviluppatori possono utilizzare il file[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)struttura per memorizzare informazioni sull'intervallo di celle che verrà convalidato utilizzando la convalida creata.

####  **Tipi di convalida dei dati**

 IL[**Tipo di convalida**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)l'enumerazione ha i seguenti membri:

|**Nome del membro**|**Descrizione**|
| :- | :- |
|QualsiasiValore|Denota un valore di qualsiasi tipo.|
|Numero intero|Indica il tipo di convalida per i numeri interi.|
|Decimale|Indica il tipo di convalida per i numeri decimali.|
|Elenco|Indica il tipo di convalida per l'elenco a discesa.|
|Data|Indica il tipo di convalida per le date.|
|Tempo|Indica il tipo di convalida per il tempo.|
|Lunghezza del testo|Indica il tipo di convalida per la lunghezza del testo.|
|Costume|Indica il tipo di convalida personalizzata.|

#####  **Convalida dei dati di numeri interi**

Con questo tipo di convalida, gli utenti possono inserire nelle celle convalidate solo numeri interi entro un intervallo specificato. Gli esempi di codice seguenti mostrano come implementare il tipo di convalida WholeNumber. L'esempio crea la stessa convalida dei dati utilizzando Aspose.Cells che abbiamo creato utilizzando Microsoft Excel sopra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

#####  **Elenco convalida dati**

Questo tipo di convalida consente all'utente di immettere valori da un elenco a discesa. Fornisce un elenco: una serie di righe che contengono dati. Nell'esempio viene aggiunto un secondo foglio di lavoro per contenere l'origine dell'elenco. Gli utenti possono selezionare solo valori dall'elenco. L'area di convalida è l'intervallo di celle A1:A5 nel primo foglio di lavoro.

 È importante qui impostare il file[**Validazione.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)proprietà su *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

#####  **Data di convalida dei dati**

Con questo tipo di convalida, gli utenti inseriscono valori di data entro un intervallo specificato o che soddisfano criteri specifici nelle celle convalidate. Nell'esempio, l'utente è limitato a inserire date comprese tra il 1970 e il 1999. Qui l'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

#####  **Convalida dei dati temporali**

Con questo tipo di convalida, gli utenti possono inserire orari entro un intervallo specificato o che soddisfano alcuni criteri nelle celle convalidate. Nell'esempio, l'utente può inserire solo orari compresi tra le 09:00 e le 11:30. Qui, l'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

#####  **Convalida dei dati sulla lunghezza del testo**

Con questo tipo di convalida, gli utenti possono inserire valori di testo di una lunghezza specificata nelle celle convalidate. Nell'esempio, l'utente può immettere valori stringa con non più di 5 caratteri. L'area di convalida è la cella B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

###  **Regole di convalida dei dati**

 Quando vengono implementate le convalide dei dati, la convalida può essere verificata assegnando valori diversi nelle celle.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) può essere utilizzato per recuperare il risultato della convalida. L'esempio seguente illustra questa funzionalità con valori diversi. Il file di esempio può essere scaricato dal seguente collegamento per il test:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

##  **Controlla se la convalida nella cella è a discesa**

 Come abbiamo visto ci sono molti tipi di validazioni che possono essere implementate all'interno di una cella. Se vuoi verificare se la convalida è a discesa o meno,[**Validazione.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)La proprietà può essere utilizzata per testarlo. Il codice di esempio seguente illustra l'utilizzo di questa proprietà. Un file di esempio per il test può essere scaricato dal seguente collegamento:

[campioneValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

##  **Aggiungi CellArea alla convalida esistente**

 Potrebbero esserci casi in cui potresti voler aggiungere[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)all'esistere[**Validazione**](https://reference.aspose.com/cells/net/aspose.cells/validation). Quando aggiungi[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) utilizzando[**Validazione.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells controlla tutte le zone esistenti per vedere se la nuova zona esiste già. Se il file ha un numero elevato di convalide, ciò comporta un calo delle prestazioni. Per ovviare a ciò lo API mette a disposizione il[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) metodo. IL*checkIntersezione* Il parametro indica se verificare l'intersezione di una determinata area con aree di validazione esistenti. Impostandolo su**falso** disabiliterà il controllo di altre aree. IL*checkEdge*Il parametro indica se controllare le aree applicate. Se la nuova area diventa l'area in alto a sinistra, le impostazioni interne vengono ricostruite. Se sei sicuro che la nuova area non sia l'area in alto a sinistra, puoi impostare questo parametro come *false**.

Il seguente frammento di codice illustra l'uso di[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) metodo per aggiungerne di nuovi[**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)all'esistere[**Validazione**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

I file Excel di origine e di output sono allegati per riferimento.

[File sorgente](96928093.xlsx)

[File di uscita](96928220.xlsx)


##  **Argomenti avanzati**
- [Ottieni la convalida Cell nei file ODS](/cells/it/net/get-cell-validation-in-ods-files/)
- [Ottieni la convalida applicata al numero Cell](/cells/it/net/get-validation-applied-on-a-cell/)
- [Verificare che il valore Cell soddisfi le regole di convalida dei dati](/cells/it/net/verify-that-cell-value-satisfies-data-validation-rules/)
