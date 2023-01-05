---
title: Arbeiten mit Validierungen in Spalten
type: docs
weight: 80
url: /de/net/working-with-validations-in-columns/
---
{{% alert color="primary" %}} 

 In einem unserer vorherigen Themen haben wir über Validierungen gesprochen, aber das war im Zusammenhang mit[Validierungen in Arbeitsblättern](/cells/de/net/working-with-validations-in-worksheets/) (Entwickler können sich auf dieses Thema beziehen, um allgemeine Informationen zu Validierung und Validierungsmodi zu erhalten). In diesem Thema erläutern wir Validierungen in Bezug auf Spalten. Mit dieser Funktion können Entwickler eine Validierungsregel auf jede Spalte des Arbeitsblatts anwenden. Lassen Sie es uns im Detail besprechen.

{{% /alert %}} 
## **Spaltenvalidierung hinzufügen**
Führen Sie die folgenden Schritte aus, um einer Spalte eine beliebige Validierung hinzuzufügen:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
- **Addieren** ein Gewünschtes**Validierung** zu irgendeiner Spalte

**WICHTIG:**Weitere Informationen zu den Validierungsarten (oder Validierungsmodi wie z**Erforderliche Validierung**, **Validierung regulärer Ausdrücke** und**Benutzerdefinierte Validierung** ) und Umsetzung**Benutzerdefinierte Validierung** , bitte beziehen Sie sich auf[Arbeiten mit Validierungen in Arbeitsblättern.](/cells/de/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Zugriff auf die Spaltenvalidierung**
Um auf eine bestimmte Spaltenvalidierung zuzugreifen, führen Sie bitte die folgenden Schritte aus:

-  Greifen Sie auf eine gewünschte zu**Arbeitsblatt**
-  Greifen Sie auf eine bestimmte Spalte zu**Validierung** in dem**Arbeitsblatt**
-  Bearbeiten**Validierung** Attribute ggf



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Entfernen der Spaltenvalidierung**
Führen Sie die folgenden Schritte aus, um eine bestimmte Spaltenvalidierung aus dem Arbeitsblatt zu entfernen:

-  Greifen Sie auf eine gewünschte zu**Arbeitsblatt**
-  Entfernen Sie eine bestimmte Spalte**Validierung** von dem**Arbeitsblatt**



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
