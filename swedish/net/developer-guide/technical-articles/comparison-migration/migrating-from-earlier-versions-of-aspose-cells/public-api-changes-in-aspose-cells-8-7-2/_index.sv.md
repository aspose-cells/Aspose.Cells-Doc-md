---
title: Offentliga API-ändringar i Aspose.Cells 8.7.2
type: docs
weight: 250
url: /sv/net/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.7.1 till 8.7.2 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Utökade standardberäkningsmotorn**
Aspose.Cells API:er har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-funktioner. Dessutom tillåter Aspose.Cells API:erna nu att utöka standardberäkningsmotorn för att möta anpassade beräkningskrav för alla applikationer.

Följande API:er har lagts till med utgåvan av Aspose.Cells för .NET 8.7.2.

1. AbstractCalculationEngine Class
1. CalculationData Class
1. CalculationOptions.CustomEngine Property

{{% alert color="primary" %}} 

Ovan nämnda API:er gör det möjligt att implementera anpassade beräkningsmotorer för alla funktioner (inklusive Excels inbyggda funktioner) med mer flexibilitet.

{{% /alert %}} {{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Implementering av Custom Calculation Engine](/cells/sv/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 public class MyEngine : AbstractCalculationEngine

{

    public override void Calculate(CalculationData data)

    {

        string funcName = data.FunctionName.ToUpper();

        if ("MYFUNC".Equals(funcName))

        {

            //do calculation for MYFUNC here

            int count = data.ParamCount;

            object res = null;

            for (int i = 0; i < count; i++)

            {

                object pv = data.GetParamValue(i);

                if (pv is ReferredArea)

                {

                    ReferredArea ra = (ReferredArea)pv;

                    pv = ra.GetValue(0, 0);

                }

                //process the parameter here

                //res = ...;

            }

            data.CalculatedValue = res;

        }

    }

}

{{< /highlight >}}


### **Lade till Overloaded Indexer för TextBoxCollection**
Aspose.Cells för .NET 8.7.2 har avslöjat den överbelastade indexeringen för TextBoxCollection-klassen för att komma åt instansen av TextBox med dess namn som sträng.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Åtkomst till textrutan via dess namn](/cells/sv/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

Enkelt användningsscenario ser ut som följer.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.Worksheets[0];

//Add a TextBox to the collection

int idx = sheet.TextBoxes.Add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.TextBoxes[idx];

//Set the name for the TextBox

box.Name = "MyTextBox";

//Access the same TextBox via its name

box = sheet.TextBoxes["MyTextBox"];

{{< /highlight >}}


### **Lade till OnAfterColumnFilter Event för GridWeb**
Aspose.Cells.GridWeb för .NET 8.7.2 har avslöjat händelsen OnAfterColumnFilter som fungerar som återuppringning till filtreringsmekanismen som görs via Aspose.Cells.GridWeb UI. Som namnet antyder utlöses händelsen efter att kolumnfiltreringen har tillämpats och kan användas för att få filtreringsinformation som kolumnindex på vilket filter som användes och valt filtervärde.

Enkelt användningsscenario ser ut som följer.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Glöm inte att registrera evenemanget till GridWeb control<acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
