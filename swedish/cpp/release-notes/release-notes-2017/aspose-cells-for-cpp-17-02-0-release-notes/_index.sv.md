---
title: Aspose.Cells för CPP 17.02.0 Release Notes
type: docs
weight: 30
url: /sv/cpp/aspose-cells-for-cpp-17-02-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för CPP 17.02.0](https://downloads.aspose.com/cells/cpp/new-releases/aspose.cells-for-c---17.02.0/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSCPP-41|Beräkna formler i Excel-kalkylblad|Ny funktion|
|CELLSCPP-42|Förbättrad prestanda vid läsning av XLSX-filer|Förbättring|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, omdöpta, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells för C++. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Lägger till metoden IWorkbook::CalculateFormula().**
Den senaste versionen 17.02.0 av Aspose.Cells för CPP API har lagt till metoden IWorkbook::CalculateFormula(). Det hjälper utvecklare att beräkna resultatet av formler och lagra i lämplig cell i ett kalkylblad. Utvecklare kan också beräkna de anpassade formlerna.

Detta kodexempel visar hur man beräknar formlerna i ett Excel:

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
#### **Lägger till metoden IWorkbook::CalculateFormula(bool ignoreError).**
Utvecklare kan beräkna formler på olika sätt. IWorkbook::CalculateFormula(bool ignoreError)-metoden tillåter utvecklare att beräkna resultatet av formler samt döljer felet i beräkningsformler. Ett fel kan uppstå på grund av att funktionen inte stöds, externa länkar etc.



Detta kodexempel visar hur man beräknar formlerna och ignorerar fel i en Excel:

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
#### **Lägger till metoden IWorkbook::CalculateFormula(intrusive_ptr<Aspose::Cells::ICalculationOptions> options)**
Den beräknar formler i arbetsboken.
#### **Lägger till metoden IWorkbook::CalculateFormula(bool ignoreError,intrusive_ptr<Aspose::Cells::ICustomFunction> customFunction)**
 Aspose.Cells för CPP API erbjuder ICustomFunction-gränssnitt. Utvecklare kan anropa metoden IWorkbook.CalculateFormula(false, ICustomFunction) för att anropa implementeringen av metoden ICustomFunction.CalculateCustomFunction(). Metoden ICustomFunction.CalculateCustomFunction() gör det möjligt att manipulera returvärdena för anpassade funktioner. I kodexemplet nedan utvärderar och returnerar implementeringen av ICustomFunction-gränssnittet värdena för två anpassade funktioner, dvs MySampleFunc() och YourSampleFunc(). Dessa anpassade funktioner finns inuti cellerna A1 respektive A2. Den skriver ut värdena för A1 och A2 på en konsol, som faktiskt är de värden som returneras av ICustomFunction.CalculateCustomFunction().


Detta kodexempel visar hur man beräknar formlerna, ignorerar fel och manipulerar returvärdena för anpassade funktioner i en Excel:

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

#### **Lägger till metoden IWorksheet::CalculateFormula(intrusive_ptr<Aspose::Cells::System::String> formula)**
Metoden IWorksheet::CalculateFormula(intrusive_ptr<Aspose::Cells::System::String> formula) tillåter utvecklare att beräkna formelresultaten direkt utan att lägga till dem i ett kalkylblad. Värdena för celler som används i formeln finns redan i ett kalkylblad och utvecklare behöver bara hitta resultatet av dessa värden baserat på någon Microsoft Excel-formel utan att lägga till formeln i ett kalkylblad.

Detta kodexempel visar hur man beräknar formlerna direkt utan att lägga till dem i ett kalkylblad i en Excel:

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

#### **Lägger till IWorksheet::CalculateFormula(intrusive_ptr<Aspose::Cells::System::String> formula, intrusive_ptr<Aspose::Cells::ICalculationOptions> opts) metod**
Den beräknar en formel på ett mer flexibelt sätt.
#### **Lägger till IWorksheet::CalculateFormula(bool rekursiv, bool ignoreError, intrusive_ptr<Aspose::Cells::ICustomFunction> customFunction) metod**
Den beräknar alla formler i kalkylbladet.
#### **Lägger till IWorksheet::CalculateFormula(intrusive_ptr<Aspose::Cells::ICalculationOptions> optioner, bool rekursiv) metod**
Den beräknar alla formler i kalkylbladet.
#### **Lägger till metoden ICell::Calculate(intrusive_ptr<Aspose::Cells::ICalculationOptions> options)**
Den beräknar formeln för cellen i kalkylbladet.
#### **Lägger till metoden ICell::Calculate(bool ignoreError , intrusive_ptr<Aspose::Cells::ICustomFunction> customFunction)**
Den beräknar formeln för cellen i kalkylbladet.
### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

1. [Lägga till formler och beräkna resultat](/cells/sv/cpp/ways-to-calculate-formulas#waystocalculateformulas-addingformulas&calculatingresults)
1. [Direkt beräkning av formel](/cells/sv/cpp/ways-to-calculate-formulas#waystocalculateformulas-directcalculationofformula)
1. [Beräknar formler endast en gång](/cells/sv/cpp/ways-to-calculate-formulas#waystocalculateformulas-calculatingformulasonceonly)
1. [Använder ICustomFunction-funktionen](/cells/sv/cpp/using-icustomfunction-feature#usingicustomfunctionfeature-usingicustomfunctionfeature) 


