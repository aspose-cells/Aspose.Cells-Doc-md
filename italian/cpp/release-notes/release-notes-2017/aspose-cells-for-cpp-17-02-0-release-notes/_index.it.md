---
title: Aspose.Cells per le note di rilascio di CPP 17.02.0
type: docs
weight: 30
url: /it/cpp/aspose-cells-for-cpp-17-02-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells per CPP 17.02.0](https://downloads.aspose.com/cells/cpp/new-releases/aspose.cells-for-c---17.02.0/).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSCPP-41|Calcola formule in fogli di calcolo Excel|Nuova caratteristica|
|CELLSCPP-42|Prestazioni migliorate nella lettura dei file XLSX|Miglioramento|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for C++. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge il metodo IWorkbook::CalculateFormula()**
La recente versione 17.02.0 di Aspose.Cells per CPP API ha aggiunto il metodo IWorkbook::CalculateFormula(). Aiuta gli sviluppatori a calcolare il risultato delle formule e memorizzarlo nella cella appropriata di un foglio di lavoro. Gli sviluppatori possono anche calcolare le formule personalizzate.

Questo esempio di codice mostra come calcolare le formule in un Excel:

{{< highlight "java" >}}

 	/*create a new workbook*/

	intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

	/*get the first worksheet*/

	intrusive_ptr<IWorksheetCollection> wsc = wb->GetIWorksheets();

	intrusive_ptr<IWorksheet> ws = wsc->GetObjectByIndex(0);

	/*get cells*/

	intrusive_ptr<ICells> cells = ws->GetICells();

	/*set value to cell(0,0) and cell(1,0)*/

	cells->GetObjectByIndex(0, 0)->PutValue(3);

	cells->GetObjectByIndex(1, 0)->PutValue(2);

	/*set formula*/

	cells->GetObjectByIndex(0, 1)->SetFormula(new String("=SUM(A1,A2)"));

	/*formula calculation*/

	wb->CalculateFormula();

	/*check result*/

	EXPECT_TRUE(5 == cells->GetObjectByIndex(new String("B1"))->GetIntValue());

	/*save this workbook to resultFile*/

	wb->Save(resultPath->StringAppend(new String("book5.xlsx")));

{{< /highlight >}}
#### **Aggiunge il metodo IWorkbook::CalculateFormula(bool ignoreError).**
Gli sviluppatori possono calcolare le formule in vari modi. Il metodo IWorkbook::CalculateFormula(bool ignoreError) consente agli sviluppatori di calcolare il risultato delle formule e nasconde l'errore nel calcolo delle formule. Può verificarsi un errore a causa della funzione non supportata, collegamenti esterni, ecc.



Questo esempio di codice mostra come calcolare le formule e ignorare gli errori in un Excel:

{{< highlight "java" >}}

 	/*create a new workbook*/

	intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

	/*get the first worksheet*/

	intrusive_ptr<IWorksheetCollection> wsc = wb->GetIWorksheets();

	intrusive_ptr<IWorksheet> ws = wsc->GetObjectByIndex(0);

	/*get cells*/

	intrusive_ptr<ICells> cells = ws->GetICells();

	/*set value to cell(0,0) and cell(1,0)*/

	cells->GetObjectByIndex(0, 0)->PutValue(3);

	cells->GetObjectByIndex(1, 0)->PutValue(2);

	/*set formula*/

	cells->GetObjectByIndex(0, 1)->SetFormula(new String("=SUM(A1,A2)"));

	/*formula calculation*/

	wb->CalculateFormula(true);

	/*check result*/

	EXPECT_TRUE(5 == cells->GetObjectByIndex(new String("B1"))->GetIntValue());

	/*save this workbook to resultFile*/

	wb->Save(resultPath->StringAppend(new String("book5.xlsx")));

{{< /highlight >}}
#### **Aggiunge il metodo IWorkbook::CalculateFormula(intrusive_ptr<Aspose::Cells::ICalculationOptions>)**
Calcola le formule nella cartella di lavoro.
#### **Aggiunge il metodo IWorkbook::CalculateFormula(bool ignoreError,intrusive_ptr<Aspose::Cells::ICustomFunction> customFunction)**
Aspose.Cells per CPP API offre l'interfaccia ICustomFunction. Gli sviluppatori possono chiamare il metodo IWorkbook.CalculateFormula(false, ICustomFunction) per richiamare l'implementazione del metodo ICustomFunction.CalculateCustomFunction(). Il metodo ICustomFunction.CalculateCustomFunction() consente di manipolare i valori di ritorno delle funzioni personalizzate. Nell'esempio di codice riportato di seguito, l'implementazione dell'interfaccia ICustomFunction valuta e restituisce i valori di due funzioni personalizzate, ovvero MySampleFunc() e YourSampleFunc(). Queste funzioni personalizzate si trovano rispettivamente all'interno delle celle A1 e A2. Stampa i valori di A1 e A2 su una console, che in realtà sono i valori restituiti da ICustomFunction.CalculateCustomFunction().


Questo esempio di codice mostra come calcolare le formule, ignorare gli errori e manipolare i valori restituiti delle funzioni personalizzate in un Excel:

{{< highlight "java" >}}

 //Implement ICustomFunction interface

class CustomFunction : public ICustomFunction

{

public:

    //Evalaute and return the values of your custom functions

    intrusive_ptr<Aspose::Cells::System::Object> 

        CalculateCustomFunction(

        intrusive_ptr<Aspose::Cells::System::String> functionName, 

        intrusive_ptr<Aspose::Cells::System::Collections::ArrayList> paramsList, 

        intrusive_ptr<Aspose::Cells::System::Collections::ArrayList> contextObjects)

    {

            if (functionName->Equals(new String("MySampleFunc")))

            {

                return new String("MY sample function was called successfully.");

            }



            if (functionName->Equals(new String("YourSampleFunc")))

            {

                return new String("YOUR sample function was called successfully.");

            }



            return NULL;

    }



};



//Call this function to run the code

void Run()

{

    //Create workbook

    intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();



    //Access first worksheet in the workbook

    intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);



    //Adding custom formulas to Cell A1 and A2

    ws->GetICells()->GetObjectByIndex(new String("A1"))->SetFormula(new String("=MySampleFunc()"));

    ws->GetICells()->GetObjectByIndex(new String("A2"))->SetFormula(new String("=YourSampleFunc()"));



    // Calcualting Formulas

    intrusive_ptr<CustomFunction> custFunc = new CustomFunction();

    wb->CalculateFormula(true, custFunc);



    //Print the value of cell A1 and A2 after the calculation of custom function implemented by us.

    intrusive_ptr<String> valA1 = ws->GetICells()->GetObjectByIndex(new String("A1"))->GetStringValue();

    intrusive_ptr<String> valA2 = ws->GetICells()->GetObjectByIndex(new String("A2"))->GetStringValue();



    //Print the values on console

    printf("Value of A1: %s\r\n", valA1->charValue());

    printf("Value of A2: %s\r\n", valA2->charValue());

}

{{< /highlight >}}

#### **Aggiunge il metodo IWorksheet::CalculateFormula(intrusive_ptr<Aspose::Cells::System::String> formula)**
Il metodo IWorksheet::CalculateFormula(intrusive_ptr<Aspose::Cells::System::String> formula) consente agli sviluppatori di calcolare direttamente i risultati della formula senza aggiungerli a un foglio di lavoro. I valori delle celle utilizzate nella formula esistono già in un foglio di lavoro e gli sviluppatori devono solo trovare il risultato di tali valori in base a una formula di Excel Microsoft senza aggiungere la formula in un foglio di lavoro.

Questo esempio di codice mostra come calcolare direttamente le formule senza aggiungerle in un foglio di lavoro in Excel:

{{< highlight "java" >}}

 //Create workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();



//Access first worksheet in the workbook

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);



//Put 20 in cell A1

intrusive_ptr<ICell> cellA1 = ws->GetICells()->GetObjectByIndex(new String("A1"));

cellA1->PutValue(20);



//Put 30 in cell A2

intrusive_ptr<ICell> cellA2 = ws->GetICells()->GetObjectByIndex(new String("A2"));

cellA2->PutValue(30);



//Calculate the Sum of A1 and A2

intrusive_ptr<Aspose::Cells::System::Object> results = ws->CalculateFormula(new String("=Sum(A1:A2)"));



//Print the output

printf("Value of A1: %s\r\n", cellA1->GetStringValue()->charValue());

printf("Value of A2: %s\r\n", cellA2->GetStringValue()->charValue());

printf("Result of Sum(A1:A2): %s\r\n", results->ToString()->charValue());

{{< /highlight >}}

#### **Aggiunge il metodo IWorksheet::CalculateFormula(intrusive_ptr<Aspose::Cells::System::String>, intrusive_ptr<Aspose::Cells::ICalculationOptions> opts)**
Calcola una formula in modo più flessibile.
#### **Aggiunge il metodo IWorksheet::CalculateFormula(bool recursive, bool ignoreError, intrusive_ptr<Aspose::Cells::ICustomFunction> customFunction)**
Calcola tutte le formule nel foglio di lavoro.
#### **Aggiunge il metodo IWorksheet::CalculateFormula(intrusive_ptr<Aspose::Cells::ICalculationOptions>, bool recursive)**
Calcola tutte le formule nel foglio di lavoro.
#### **Aggiunge il metodo ICell::Calculate(intrusive_ptr<Aspose::Cells::ICalculationOptions>)**
Calcola la formula della cella nel foglio di lavoro.
#### **Aggiunge il metodo ICell::Calculate(bool ignoreError , intrusive_ptr<Aspose::Cells::ICustomFunction> customFunction)**
Calcola la formula della cella nel foglio di lavoro.
### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

1. [Aggiunta di formule e calcolo dei risultati](/cells/it/cpp/ways-to-calculate-formulas#waystocalculateformulas-addingformulas&calculatingresults)
1. [Calcolo diretto della formula](/cells/it/cpp/ways-to-calculate-formulas#waystocalculateformulas-directcalculationofformula)
1. [Calcolo delle formule una sola volta](/cells/it/cpp/ways-to-calculate-formulas#waystocalculateformulas-calculatingformulasonceonly)
1. [Utilizzo della funzione ICustomFunction](/cells/it/cpp/using-icustomfunction-feature#usingicustomfunctionfeature-usingicustomfunctionfeature) 


