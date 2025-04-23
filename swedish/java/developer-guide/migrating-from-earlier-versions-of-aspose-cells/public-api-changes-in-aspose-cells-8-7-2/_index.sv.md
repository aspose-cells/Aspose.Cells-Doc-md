---
title: Förändringar i offentligt API i Aspose.Cells 8.7.2
type: docs
weight: 260
url: /sv/java/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Det här dokumentet beskriver förändringarna i Aspose.Cells API från version 8.7.1 till 8.7.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda & borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Förlängd standardberäkningsmotor**
Aspose.Cells API:er har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-funktioner. Dessutom tillåter nu Aspose.Cells API:er att förlänga standardberäkningsmotorn för att möta anpassade beräkningskrav för vilken applikation som helst.

Följande API:er har lagts till med släppet av Aspose.Cells for Java 8.7.2.

1. Klassens AbstractCalculationEngine
1. Klassen CalculationData
1. Egenskapen CalculationOptions.CustomEngine

{{% alert color="primary" %}} 

Ovanstående API:er tillåter att implementera anpassad beräkningsmotor för alla funktioner (inklusive Excels inbyggda funktioner) med mer flexibilitet.

{{% /alert %}} {{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Implementera Anpassad Beräkningsmotor](/cells/sv/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 public class CustomEngine extends AbstractCalculationEngine

{

	public void calculate(CalculationData data)

        {

		if(data.getFunctionName().toUpperCase().equals("SUM")==true)

                {

                    double val = (double)data.getCalculatedValue();

                    val = val + 30;

                    data.setCalculatedValue(val);

                }

        }

}

{{< /highlight >}}
### **Tillagt Överbelastad Indexer för TextBoxCollection**
Aspose.Cells for Java 8.7.2 har exponerat den överbelastade indexer för klassen TextBoxCollection för att kunna komma åt instansen av TextBox med dess namn som Sträng.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Tillgång till TextBox via dess Namn](/cells/sv/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

Enkelt användningsscenarie ser ut som följande. 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access the first Worksheet from the collection

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a TextBox to the collection

int idx = sheet.getTextBoxes().add(10, 10, 10, 10);

//Access the TextBox using its index

TextBox box = sheet.getTextBoxes().get(idx);

//Set the name for the TextBox

box.setName("MyTextBox");

//Access the same TextBox via its name

box = sheet.getTextBoxes().get("MyTextBox");

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
