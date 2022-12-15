---
title: Überprüfen Sie das zu ändernde Passwort mit Aspose.Cells
type: docs
weight: 2400
url: /de/net/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Manchmal müssen Sie überprüfen, ob das angegebene Passwort mit dem übereinstimmt**Zu änderndes Passwort** programmatisch. Aspose.Cells stellt die Methode WorkbookSettings.WriteProtection.ValidatePassword() bereit, mit der Sie überprüfen können, ob das angegebene zu ändernde Passwort korrekt ist oder nicht.

{{% /alert %}}

## **Aktivieren Sie das zu ändernde Passwort in Microsoft Excel**

Sie können zuweisen**Passwort zum Öffnen** und**Zu änderndes Passwort** beim Erstellen Ihrer Arbeitsmappen in Microsoft Excel. Bitte sehen Sie sich diesen Screenshot an, der die Schnittstelle Microsoft zeigt, die Excel bereitstellt, um diese Passwörter anzugeben.

|![todo: Bild_alt_Text](check-password-to-modify-using-aspose-cells_1.png)|
|:- |

## **Überprüfen Sie das zu ändernde Passwort mit Aspose.Cells**

 Die folgenden Beispielcodes laden die[Quelle Excel](5112232.xlsx) Datei. Es hat ein Passwort zum Öffnen als 1234 und ein Passwort zum Ändern als 5678. Der Code prüft zuerst, ob 567 das richtige Passwort zum Ändern ist, und gibt falsch zurück, und dann prüft er, ob 5678 das zu ändernde Passwort ist, und es gibt wahr zurück.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Konsolenausgabe**

 Hier ist die Konsolenausgabe des obigen Beispielcodes nach dem Laden der[Quelle Excel](5112232.xlsx) Datei.

{{< highlight "java" >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
