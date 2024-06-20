---
title: Öffentliche API Änderungen in Aspose.Cells 8.7.2
type: docs
weight: 250
url: /de/net/public-api-changes-in-aspose-cells-8-7-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.7.1 auf 8.7.2, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Erweiterte den Standardberechnungs-Engine**
Aspose.Cells-APIs verfügen über eine leistungsstarke Berechnungs-Engine, die fast alle Funktionen von Microsoft Excel berechnen kann. Darüber hinaus ermöglichen die Aspose.Cells-APIs nun die Erweiterung der Standardberechnungs-Engine, um individuelle Berechnungsanforderungen jeder Anwendung zu erfüllen.

Folgende APIs wurden mit der Veröffentlichung von Aspose.Cells for .NET 8.7.2 hinzugefügt.

1. AbstractCalculationEngine Klasse
1. CalculationData Klasse
1. CalculationOptions.CustomEngine Eigenschaft

{{% alert color="primary" %}} 

Die oben genannten APIs ermöglichen die Implementierung eines benutzerdefinierten Berechnungsmoduls für alle Funktionen (einschließlich der nativen Funktionen von Excel) mit mehr Flexibilität.

{{% /alert %}} {{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel zu [Implementieren eines benutzerdefinierten Berechnungsmechanismus](/cells/de/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Hinzugefügter überladener Indexer für TextBoxCollection**
Aspose.Cells for .NET 8.7.2 hat den überladenen Indexer für die TextBoxCollection-Klasse freigegeben, um auf die Instanz von TextBox anhand ihres Namens als Zeichenfolge zuzugreifen.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel zu [Zugreifen auf die TextBox über ihren Namen](/cells/de/net/access-the-text-box-by-the-name/)

{{% /alert %}} 

Das einfache Anwendungsszenario sieht wie folgt aus.

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


### **Hinzugefügtes OnAfterColumnFilter-Ereignis für GridWeb**
Aspose.Cells.GridWeb für .NET 8.7.2 hat das OnAfterColumnFilter-Ereignis freigelegt, das als Rückrufmechanismus für den Filtermechanismus dient, der über die Aspose.Cells.GridWeb-Benutzeroberfläche durchgeführt wurde. Wie der Name schon sagt, wird das Ereignis ausgelöst, nachdem der Spaltenfilter angewendet wurde, und kann verwendet werden, um die Filterinformationen wie den Spaltenindex, auf den der Filter angewendet wurde, und den ausgewählten Filterwert zu erhalten.

Das einfache Anwendungsszenario sieht wie folgt aus.

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
