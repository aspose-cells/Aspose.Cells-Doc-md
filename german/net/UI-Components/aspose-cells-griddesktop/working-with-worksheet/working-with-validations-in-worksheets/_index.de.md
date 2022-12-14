---
title: Arbeiten mit Validierungen in Arbeitsblättern
type: docs
weight: 70
url: /de/net/working-with-validations-in-worksheets/
---
{{% alert color="primary" %}} 

Aspose.Cells. GridDesktop unterstützt auch das Hinzufügen von Validierungen (oder Validierungsregeln) zu den Zellen eines Arbeitsblatts. Durch das Anwenden von Validierungsregeln auf Zellen können Entwickler Benutzer daran hindern, Daten in einem bestimmten Format in Grid einzugeben. Verschiedene Validierungsmodi werden von Aspose.Cells.GridDesktop unterstützt. In diesem Thema werden wir nicht nur über diese Validierungsmodi diskutieren, sondern auch die Manipulation dieser Validierungen erklären.

{{% /alert %}} 
## **Validierungsmodi**
Es gibt drei Validierungsmodi, die von Aspose.Cells.GridDesktop wie folgt unterstützt werden:

- Ist erforderlich Validierungsmodus
- Validierungsmodus für reguläre Ausdrücke
- Benutzerdefinierter Validierungsmodus
### **Ist erforderlich Validierungsmodus**
 In diesem Validierungsmodus sind Benutzer darauf beschränkt, Werte in bestimmte Zellen einzugeben. Einmal**Erforderliche Validierung** auf eine Arbeitsblattzelle angewendet wird, muss ein Benutzer einen Wert in diese Zelle eingeben.
### **Validierungsmodus für reguläre Ausdrücke**
 In diesem Modus werden Einschränkungen auf Arbeitsblattzellen angewendet, damit die Benutzer Daten in Zellen in einem bestimmten Format übermitteln können. Das Muster des Datenformats wird in Form von a bereitgestellt**Regulären Ausdruck**.
### **Benutzerdefinierter Validierungsmodus**
 Benutzen**Benutzerdefinierte Validierung** , Entwickler müssen die Schnittstelle Aspose.Cells.GridDesktop.ICustomValidation implementieren. Die Schnittstelle bietet a**Bestätigen** Methode. Diese Methode gibt true zurück, wenn die Daten gültig sind, andernfalls gibt sie false zurück.
## **Arbeiten mit Validierungen in Aspose.Cells.GridDesktop**
### **Validierung hinzufügen**
Führen Sie die folgenden Schritte aus, um einer Arbeitsblattzelle eine beliebige Art von Validierung hinzuzufügen:

-  Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrer hinzu**Bilden**
-  Greifen Sie beliebig zu**Arbeitsblatt**
-  Fügen Sie der eine gewünschte Validierung hinzu**Validierungen** Sammlung der**Arbeitsblatt** um anzugeben, welche Validierung auf welche Zelle angewendet wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

 In der obigen Abbildung haben wir auch die Validierungsregeln vor Zellen erwähnt, in denen diese Validierungsregeln angewendet werden. Wenn ein ungültiger Wert (der gemäß der für diese Zelle definierten Validierungsregel nicht gültig ist) eingegeben wird, a**Nachrichtenbox** angezeigt, um den Benutzer über den ungültigen Eintrag zu informieren.

{{% /alert %}} 
### **Implementieren von ICustomValidation**
 Im obigen Code-Snippet haben wir eine benutzerdefinierte Validierung hinzugefügt**A8**Zelle, aber wir haben diese benutzerdefinierte Validierung noch nicht implementiert. Wie wir am Anfang dieses Themas erklärt haben, müssen wir implementieren, um eine benutzerdefinierte Validierung anzuwenden**ICustomValidation** Schnittstelle. Versuchen wir also, eine zu implementierende Klasse zu erstellen**ICustomValidation** Schnittstelle.

Im unten angegebenen Code-Snippet haben wir eine benutzerdefinierte Validierung implementiert, um die folgenden Prüfungen durchzuführen:

- Überprüfen Sie, ob die Adresse der Zelle korrekt ist, in der die Validierung hinzugefügt wird
- Überprüfen Sie, ob der Datentyp des Zellenwerts doppelt ist
- Überprüfen Sie, ob der Wert der Zelle größer als 100 ist



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Zugriff auf Validierung**
Nachdem einer bestimmten Arbeitsblattzelle eine Validierung hinzugefügt wurde, müssen Entwickler möglicherweise zur Laufzeit auf die Attribute einer bestimmten Validierung zugreifen und diese ändern. Aspose.Cells.GridDesktop hat es Entwicklern also leicht gemacht, diese Aufgabe zu erfüllen.

Um auf eine bestimmte Validierung zuzugreifen, führen Sie bitte die folgenden Schritte aus:

-  Greifen Sie auf eine gewünschte zu**Arbeitsblatt**
-  Greifen Sie auf eine bestimmte zu**Validierung**im Arbeitsblatt durch Angabe des Zellennamens, auf den die Validierung angewendet wurde
-  Bearbeiten**Validierung** Attribute ggf



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**Validierungen** Sammlung hat zwei Indexer. Ein Indexer (der im Beispiel unten verwendet wird) ermöglicht den Zugriff auf a**Validierung** Objekt, indem er einen Zellennamen als Index verwendet, während der andere Indexer zwei Parameter (d. h. Zeilen- und Spaltennummern) verwendet, um dieselbe Aufgabe auszuführen.

{{% /alert %}} 
### **Validierung entfernen**
Um eine bestimmte Validierung aus dem Arbeitsblatt zu entfernen, führen Sie bitte die folgenden Schritte aus:

-  Greifen Sie auf eine gewünschte zu**Arbeitsblatt**
-  Entfernen Sie eine bestimmte**Validierung** von dem**Arbeitsblatt** durch Angabe des Zellennamens, auf den die Validierung angewendet wurde



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
