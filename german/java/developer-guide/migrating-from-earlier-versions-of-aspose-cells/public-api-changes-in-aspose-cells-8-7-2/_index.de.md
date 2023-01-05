---
title: Öffentlich API Änderungen in Aspose.Cells 8.7.2
type: docs
weight: 260
url: /de/java/public-api-changes-in-aspose-cells-8-7-2/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.7.1 zu 8.7.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Standard-Berechnungsmodul erweitert**
Aspose.Cells APIs verfügen über eine leistungsstarke Berechnungs-Engine, die fast alle Microsoft Excel-Funktionen berechnen kann. Darüber hinaus ermöglichen die Aspose.Cells-APIs jetzt die Erweiterung des Standard-Berechnungsmoduls, um benutzerdefinierte Berechnungsanforderungen jeder Anwendung zu erfüllen.

Die folgenden APIs wurden mit der Veröffentlichung von Aspose.Cells for Java 8.7.2 hinzugefügt.

1. AbstractCalculationEngine-Klasse
1. CalculationData-Klasse
1. CalculationOptions.CustomEngine-Eigenschaft

{{% alert color="primary" %}} 

Die oben genannten APIs ermöglichen die Implementierung einer benutzerdefinierten Berechnungsmaschine für alle Funktionen (einschließlich der nativen Funktionen von Excel) mit mehr Flexibilität.

{{% /alert %}} {{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Implementieren einer benutzerdefinierten Berechnungs-Engine](/cells/de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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
### **Überladener Indexer für TextBoxCollection hinzugefügt**
Aspose.Cells for Java 8.7.2 hat den überladenen Indexer für die TextBoxCollection-Klasse verfügbar gemacht, um auf die Instanz von TextBox mit ihrem Namen als String zuzugreifen.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Zugriff auf die TextBox über ihren Namen](/cells/de/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

 Ein einfaches Nutzungsszenario sieht wie folgt aus.

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
