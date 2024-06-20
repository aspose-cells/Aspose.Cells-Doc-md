---
title: Arbeiten mit Validierungen in Spalten
type: docs
weight: 80
url: /de/net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop, Validierung, Validierungen
description: Dieser Artikel führt ein, wie man Validierungen in Spalten in GridDesktop verwendet.
---

{{% alert color="primary" %}} 

In einem unserer früheren Themen haben wir über Validierungen diskutiert, jedoch im Zusammenhang mit [Validierungen in Arbeitsblättern](/cells/de/net/working-with-validations-in-worksheets/) (für allgemeine Informationen über Validierung und Validierungsmodi können Entwickler auf dieses Thema verweisen). In diesem Thema werden wir Validierungen im Hinblick auf Spalten erläutern. Mit dieser Funktion können Entwickler eine Validierungsregel auf eine beliebige Spalte des Arbeitsblatts anwenden. Lassen Sie uns das im Detail besprechen.

{{% /alert %}} 
## **Spaltenvalidierung hinzufügen**
Um eine beliebige Art von Validierung zu einer Spalte hinzuzufügen, befolgen Sie bitte die folgenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Fügen Sie einer beliebigen Spalte eine gewünschte **Validierung** hinzu

**WICHTIG:** Für weitere Informationen über die Arten der Validierung (oder Validierungsmodi wie **Erforderliche Validierung**, **Reguläre Ausdrucksvalidierung** und **Benutzerdefinierte Validierung**) und die Implementierung von **Benutzerdefinierter Validierung** lesen Sie bitte [Arbeiten mit Validierungen in Arbeitsblättern.](/cells/de/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Auf Spaltenvalidierung zugreifen**
Um eine spezifische Spaltenvalidierung zu verwenden, folgen Sie bitte den folgenden Schritten:

- Öffnen Sie ein gewünschtes **Arbeitsblatt**
- Greifen Sie auf eine spezifische **Validierung** in der **Arbeitsblatt** zu
- Bearbeiten Sie die Attribute der **Validierung**, wenn gewünscht



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Spaltenvalidierung entfernen**
Um die Validierung einer bestimmten Spalte aus dem Arbeitsblatt zu entfernen, befolgen Sie bitte die folgenden Schritte:

- Öffnen Sie ein gewünschtes **Arbeitsblatt**
- Entfernen Sie eine bestimmte Spalten-**Validierung** aus dem **Arbeitsblatt**



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
