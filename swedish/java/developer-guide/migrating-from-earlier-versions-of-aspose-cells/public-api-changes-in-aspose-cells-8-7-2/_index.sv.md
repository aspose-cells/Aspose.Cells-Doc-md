---
title: Offentlig API Ändringar i Aspose.Cells 8.7.2
type: docs
weight: 260
url: /sv/java/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.7.1 till 8.7.2 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Utökade standardberäkningsmotorn**
Aspose.Cells API:er har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel-funktioner. Dessutom tillåter API:erna Aspose.Cells nu att utöka standardberäkningsmotorn för att möta anpassade beräkningskrav för alla applikationer.

Följande API:er har lagts till med utgåvan av Aspose.Cells for Java 8.7.2.

1. AbstractCalculationEngine Class
1. CalculationData Class
1. CalculationOptions.CustomEngine Property

{{% alert color="primary" %}} 

Ovan nämnda API:er gör det möjligt att implementera anpassade beräkningsmotorer för alla funktioner (inklusive Excels inbyggda funktioner) med mer flexibilitet.

{{% /alert %}} {{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Implementering av Custom Calculation Engine](/cells/sv/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

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
### **Lade till Overloaded Indexer för TextBoxCollection**
Aspose.Cells for Java 8.7.2 har exponerat den överbelastade indexeraren för klassen TextBoxCollection för att komma åt instansen av TextBox med dess namn som String.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Åtkomst till textrutan via dess namn](/cells/sv/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

 Enkelt användningsscenario ser ut som följer.

**Java**

{{< highlight "csharp" >}}

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
