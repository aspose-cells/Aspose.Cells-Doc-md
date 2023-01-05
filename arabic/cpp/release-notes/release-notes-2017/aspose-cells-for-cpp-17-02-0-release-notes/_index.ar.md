---
title: Aspose.Cells لـ CPP 17.02.0 ملاحظات الإصدار
type: docs
weight: 30
url: /ar/cpp/aspose-cells-for-cpp-17-02-0-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells لـ CPP 17.02.0](https://downloads.aspose.com/cells/cpp/new-releases/aspose.cells-for-c---17.02.0/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSCPP-41|حساب الصيغ في جداول بيانات Excel|ميزة جديدة|
|CELLSCPP-42|تحسين الأداء في قراءة XLSX ملفات|تحسين|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for C++. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يضيف طريقة IWorkbook :: CalculateFormula ()**
أضاف الإصدار الأخير 17.02.0 من Aspose.Cells لـ CPP API طريقة IWorkbook :: CalculateFormula (). يساعد المطورين على حساب نتيجة الصيغ وتخزينها في الخلية المناسبة من ورقة العمل. يمكن للمطورين أيضًا حساب الصيغ المخصصة.

يوضح مثال التعليمات البرمجية هذا كيفية حساب الصيغ في Excel:

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
#### **يضيف طريقة IWorkbook :: CalculateFormula (bool ignoreError)**
يمكن للمطورين حساب الصيغ بطرق مختلفة. تسمح طريقة IWorkbook :: CalculateFormula (bool ignoreError) للمطورين بحساب نتيجة الصيغ بالإضافة إلى إخفاء الخطأ في حساب الصيغ. يمكن أن يحدث خطأ بسبب الوظيفة غير المدعومة والروابط الخارجية وما إلى ذلك.



يوضح مثال التعليمات البرمجية هذا كيفية حساب الصيغ وتجاهل الأخطاء في Excel:

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
#### **يضيف طريقة IWorkbook :: CalculateFormula (intrusive_ptr <Aspose :: Cells :: ICalculationOptions> options)**
يقوم بحساب الصيغ في المصنف.
#### **يضيف طريقة IWorkbook :: CalculateFormula (bool ignoreError، intrusive_ptr <Aspose :: Cells :: ICustomFunction> customFunction)**
Aspose.Cells لـ CPP API يوفر واجهة ICustomFunction. يمكن للمطورين استدعاء أسلوب IWorkbook.CalculateFormula (false، ICustomFunction) لاستدعاء تنفيذ طريقة ICustomFunction.CalculateCustomFunction (). يسمح أسلوب ICustomFunction.CalculateCustomFunction () بمعالجة قيم الإرجاع للوظائف المخصصة. في مثال الكود أدناه ، يقوم تنفيذ واجهة ICustomFunction بتقييم وإرجاع قيم وظيفتين مخصصتين ، مثل MySampleFunc () و YourSampleFunc (). توجد هذه الوظائف المخصصة داخل الخلايا A1 و A2 على التوالي. يقوم بطباعة قيم A1 و A2 على وحدة تحكم ، والتي هي في الواقع القيم التي تم إرجاعها بواسطة ICustomFunction.CalculateCustomFunction ().


يوضح مثال التعليمات البرمجية هذا كيفية حساب الصيغ وتجاهل الأخطاء ومعالجة قيم الإرجاع للوظائف المخصصة في Excel:

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

#### **يضيف طريقة IWorksheet :: CalculateFormula (intrusive_ptr <Aspose :: Cells :: System :: String> الصيغة)**
تسمح طريقة IWorksheet :: CalculateFormula (intrusive_ptr <Aspose :: Cells :: System :: String>) للمطورين بحساب نتائج الصيغة مباشرة دون إضافتها إلى ورقة عمل. قيم الخلايا المستخدمة في الصيغة موجودة بالفعل في ورقة عمل ويحتاج المطورون فقط إلى العثور على نتيجة هذه القيم بناءً على بعض صيغة Excel Microsoft دون إضافة الصيغة في ورقة العمل.

يوضح مثال التعليمات البرمجية هذا كيفية حساب الصيغ مباشرة دون إضافتها إلى ورقة عمل في Excel:

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

#### **إضافة صيغة IWorksheet :: CalculateFormula (intrusive_ptr <Aspose :: Cells :: System :: String> الصيغة ، intrusive_ptr <Aspose :: Cells :: ICalculationOptions> opts)**
يحسب صيغة بطريقة أكثر مرونة.
#### **يضيف IWorksheet :: CalculateFormula (bool recursive، bool ignoreError، intrusive_ptr <Aspose :: Cells :: ICustomFunction> customFunction)**
يقوم بحساب جميع الصيغ في ورقة العمل.
#### **يضيف خيارات IWorksheet :: CalculateFormula (intrusive_ptr <Aspose :: Cells :: ICalculationOptions> خيارات ، طريقة منطقية متكررة)**
يقوم بحساب جميع الصيغ في ورقة العمل.
#### **يضيف طريقة ICell :: Calculate (intrusive_ptr <Aspose :: Cells :: ICalculationOptions> options)**
تحسب صيغة الخلية في ورقة العمل.
#### **يضيف طريقة ICell :: Calculate (bool ignoreError، intrusive_ptr <Aspose :: Cells :: ICustomFunction> customFunction)**
تحسب صيغة الخلية في ورقة العمل.
### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

1. [إضافة الصيغ وحساب النتائج](/cells/ar/cpp/ways-to-calculate-formulas#waystocalculateformulas-addingformulas&calculatingresults)
1. [الحساب المباشر للصيغة](/cells/ar/cpp/ways-to-calculate-formulas#waystocalculateformulas-directcalculationofformula)
1. [حساب الصيغ مرة واحدة فقط](/cells/ar/cpp/ways-to-calculate-formulas#waystocalculateformulas-calculatingformulasonceonly)
1. [استخدام ميزة ICustomFunction](/cells/ar/cpp/using-icustomfunction-feature#usingicustomfunctionfeature-usingicustomfunctionfeature) 


