---
title: Förändringar i offentligt API i Aspose.Cells 8.7.2
type: docs
weight: 250
url: /sv/net/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Det här dokumentet beskriver förändringarna i Aspose.Cells API från version 8.7.1 till 8.7.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda & borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Förlängd standardberäkningsmotor**
Aspose.Cells API:er har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-funktioner. Dessutom tillåter nu Aspose.Cells API:er att förlänga standardberäkningsmotorn för att möta anpassade beräkningskrav för vilken applikation som helst.

Följande API:er har lagts till med släppet av Aspose.Cells for .NET 8.7.2.

1. Klassens AbstractCalculationEngine
1. Klassen CalculationData
1. Egenskapen CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Ovanstående API:er tillåter att implementera anpassad beräkningsmotor för alla funktioner (inklusive Excels inbyggda funktioner) med mer flexibilitet.

{{% /alert %}} {{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska den detaljerade artikeln om [Implementering av anpassad beräkningsmotor](/cells/sv/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Tillagt Överbelastad Indexer för TextBoxCollection**
Aspose.Cells for .NET 8.7.2 har exponerat det överbelastade indexet för TextBoxCollection-klassen för att komma åt instansen av TextBox med dess namn som en sträng.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska den detaljerade artikeln om [Åtkomst av TextBox via dess namn](/cells/sv/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

Enkelt användningsscenarie ser ut som följande.

**C#**

{{< highlight csharp >}}

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


### **Tillagd OnAfterColumnFilter-händelse för GridWeb**
Aspose.Cells.GridWeb för .NET 8.7.2 har exponerat OnAfterColumnFilter-händelsen som fungerar som återuppringning till filtretmekanismen som utförs genom Aspose.Cells.GridWeb UI. Som namnet antyder aktiveras händelsen efter att kolumnfiltret har tillämpats och kan användas för att få information om filtreringen, såsom kolumnindex där filtret har tillämpats och valt filtervärde.

Enkelt användningsscenarie ser ut som följande.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_AfterColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnAfterColumnFilter="GridWeb1_AfterColumnFilter"/>

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
