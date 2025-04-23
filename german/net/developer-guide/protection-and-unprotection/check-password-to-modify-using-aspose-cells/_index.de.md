---
title: Passwort zum Ändern mit Aspose.Cells überprüfen
type: docs
weight: 2400
url: /de/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Manchmal müssen Sie programmgesteuert überprüfen, ob das angegebene Passwort mit dem **Passwort zum Ändern** übereinstimmt. Aspose.Cells bietet die Methode WorkbookSettings.WriteProtection.ValidatePassword(), mit der Sie überprüfen können, ob das angegebene Passwort zum Ändern korrekt ist oder nicht.

{{% /alert %}}

## **Passwort zum Ändern in Microsoft Excel überprüfen**

Sie können beim Erstellen Ihrer Arbeitsbücher in Microsoft Excel **Passwort zum Öffnen** und **Passwort zum Ändern** zuweisen. Bitte sehen Sie sich diesen Screenshot an, der die Benutzeroberfläche zeigt, die Microsoft Excel zum Angeben dieser Passwörter bereitstellt.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Überprüfen Sie das Kennwort zur Änderung mit Aspose.Cells**

Die folgenden Beispielscodes laden die [Quell-Excel](5112232.xlsx)-Datei. Sie hat ein Passwort zum Öffnen als 1234 und ein Passwort zum Ändern als 5678. Der Code überprüft zunächst, ob 567 das richtige Passwort zum Ändern ist, und gibt false zurück, und dann überprüft er, ob 5678 das Passwort zum Ändern ist, und gibt true zurück.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielscodes nach dem Laden der [Quell-Excel](5112232.xlsx)-Datei.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
