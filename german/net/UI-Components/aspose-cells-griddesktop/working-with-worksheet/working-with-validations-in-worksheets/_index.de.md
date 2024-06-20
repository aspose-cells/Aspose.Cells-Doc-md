---
title: Arbeiten mit Validierungen in Arbeitsblättern
type: docs
weight: 70
url: /de/net/aspose-cells-griddesktop/work-with-validations-in-worksheets/
keywords: GridDesktop,validations,validation
description: Dieser Artikel stellt vor, wie man mit Validierungen in GridDesktop arbeitet.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop unterstützt auch das Hinzufügen von Validierungen (oder Validierungsregeln) zu den Zellen eines Arbeitsblatts. Durch das Anwenden von Validierungsregeln auf Zellen können Entwickler Benutzer daran hindern, Daten in einem bestimmten Format in das Grid einzugeben. Unterschiedliche Validierungsmodi werden von Aspose.Cells.GridDesktop unterstützt. In diesem Thema werden wir nicht nur über diese Validierungsmethoden sprechen, sondern auch die Manipulation dieser Validierungen erläutern.

{{% /alert %}} 
## **Validierungsmodi**
Es gibt drei Validierungsmodi, die von Aspose.Cells.GridDesktop unterstützt werden, wie folgt:

- Ist erforderlicher Validierungsmodus
- Validierungsmodus für reguläre Ausdrücke
- Benutzerdefinierter Validierungsmodus
### **Ist erforderlicher Validierungsmodus**
In diesem Validierungsmodus ist es Benutzern untersagt, Werte in spezifische Zellen einzugeben. Sobald die **Ist erforderliche Validierung** auf eine Arbeitsblattzelle angewendet wird, muss der Benutzer einen Wert in diese Zelle eingeben.
### **Validierungsmodus für reguläre Ausdrücke**
In diesem Modus werden Beschränkungen für Arbeitsblattzellen festgelegt, damit Benutzer Daten in einem bestimmten Format in die Zellen eingeben können. Das Datenformatmuster wird in Form eines **Regulären Ausdrucks** bereitgestellt.
### **Benutzerdefinierter Validierungsmodus**
Um die **Benutzerdefinierte Validierung** zu verwenden, müssen Entwickler die Aspose.Cells.GridDesktop.ICustomValidation-Schnittstelle implementieren. Die Schnittstelle bietet eine **Validate**-Methode. Diese Methode gibt true zurück, wenn die Daten gültig sind, andernfalls false.
## **Arbeiten mit Validierungen in Aspose.Cells.GridDesktop**
### **Validierung hinzufügen**
Um eine beliebige Art von Validierung zu einer Arbeitsblattzelle hinzuzufügen, befolgen Sie bitte die untenstehenden Schritte:

- Fügen Sie das Steuerelement Aspose.Cells.GridDesktop zu Ihrem **Formular** hinzu
- Greifen Sie auf jedes gewünschte **Arbeitsblatt** zu
- Fügen Sie eine gewünschte Validierung der **Validations**-Sammlung des **Arbeitsblatts** hinzu, um zu spezifizieren, welche Validierung auf welche Zelle angewendet wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

In der obigen Abbildung haben wir auch die Validierungsregeln vor den Zellen erwähnt, auf die diese Validierungsregeln angewendet werden. Wenn ein ungültiger Wert (der gemäß der für diese Zelle definierten Validierungsregel nicht gültig ist) eingegeben wird, erscheint eine **MessageBox**, um den Benutzer über den ungültigen Eintrag zu informieren.

{{% /alert %}} 
### **Implementierung von ICustomValidation**
Im obigen Code-Ausschnitt haben wir eine benutzerdefinierte Validierung in **A8**-Zelle hinzugefügt, aber wir haben diese benutzerdefinierte Validierung noch nicht implementiert. Wie wir am Anfang dieses Themas erklärt haben, müssen wir die **ICustomValidation**-Schnittstelle implementieren, um benutzerdefinierte Validierung anzuwenden. Also, lassen Sie uns versuchen, eine Klasse zu erstellen, um die **ICustomValidation**-Schnittstelle zu implementieren.

Im untenstehenden Code-Ausschnitt haben wir eine benutzerdefinierte Validierung implementiert, um die folgenden Überprüfungen durchzuführen:

- Überprüfen Sie, ob die Adresse der Zelle korrekt ist, in der die Validierung hinzugefügt wurde
- Überprüfen Sie, ob der Datentyp des Zellenwerts double ist
- Überprüfen Sie, ob der Wert der Zelle größer als 100 ist



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Zugriff auf Validierung**
Sobald eine Validierung einer bestimmten Arbeitsblattzelle hinzugefügt wurde, kann es erforderlich sein, dass Entwickler die Attribute einer bestimmten Validierung zur Laufzeit zugreifen und ändern müssen. So hat es Aspose.Cells.GridDesktop Entwicklern einfach gemacht, diese Aufgabe zu erledigen.

Um auf eine bestimmte Validierung zuzugreifen, befolgen Sie bitte die folgenden Schritte:

- Öffnen Sie ein gewünschtes **Arbeitsblatt**
- Zugriff auf eine bestimmte **Validierung** im Arbeitsblatt, indem Sie den Zellnamen angeben, auf den die Validierung angewendet wurde
- Bearbeiten Sie die Attribute der **Validierung**, wenn gewünscht



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

Die **Validierungen**-Sammlung hat zwei Indizierungen. Ein Indexer (der im folgenden Beispiel verwendet wird) ermöglicht den Zugriff auf ein **Validierungs**-Objekt, indem er einen Zellnamen als Index verwendet, während der andere Indexer zwei Parameter (das sind Zeilen- und Spaltennummern) verwendet, um die gleiche Aufgabe auszuführen.

{{% /alert %}} 
### **Validierung entfernen**
Um eine bestimmte Validierung aus dem Arbeitsblatt zu entfernen, befolgen Sie bitte die folgenden Schritte:

- Öffnen Sie ein gewünschtes **Arbeitsblatt**
- Entfernen Sie eine bestimmte **Validierung** aus dem **Arbeitsblatt**, indem Sie den Zellnamen angeben, auf den die Validierung angewendet wurde



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
