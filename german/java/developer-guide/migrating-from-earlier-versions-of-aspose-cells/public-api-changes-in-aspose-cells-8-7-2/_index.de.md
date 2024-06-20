---
title: Öffentliche API Änderungen in Aspose.Cells 8.7.2
type: docs
weight: 260
url: /de/java/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.7.1 auf 8.7.2, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Erweiterte den Standardberechnungs-Engine**
Aspose.Cells-APIs verfügen über eine leistungsstarke Berechnungs-Engine, die fast alle Funktionen von Microsoft Excel berechnen kann. Darüber hinaus ermöglichen die Aspose.Cells-APIs nun die Erweiterung der Standardberechnungs-Engine, um individuelle Berechnungsanforderungen jeder Anwendung zu erfüllen.

Mit der Version Aspose.Cells for Java 8.7.2 wurden folgende APIs hinzugefügt.

1. AbstractCalculationEngine Klasse
1. CalculationData Klasse
1. CalculationOptions.CustomEngine Eigenschaft

{{% alert color="primary" %}} 

Die oben genannten APIs ermöglichen die Implementierung eines benutzerdefinierten Berechnungsmoduls für alle Funktionen (einschließlich der nativen Funktionen von Excel) mit mehr Flexibilität.

{{% /alert %}} {{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel über die [Implementierung eines benutzerdefinierten Berechnungsmoduls](/cells/de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Hinzugefügter überladener Indexer für TextBoxCollection**
Aspose.Cells for Java 8.7.2 hat den überladenen Indexer für die TextBoxCollection-Klasse freigegeben, um auf die Instanz von TextBox mit ihrem Namen als String zuzugreifen.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel über [den Zugriff auf die TextBox über ihren Namen](/cells/de/java/access-the-text-box-by-the-name/)

{{% /alert %}} 

Das einfache Anwendungsszenario sieht wie folgt aus. 

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
