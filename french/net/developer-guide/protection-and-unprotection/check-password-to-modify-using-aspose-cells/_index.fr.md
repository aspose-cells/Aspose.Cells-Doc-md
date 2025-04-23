---
title: Vérifiez le mot de passe pour modifier en utilisant Aspose.Cells
type: docs
weight: 2400
url: /fr/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Parfois, vous devez vérifier si le mot de passe donné correspond au **Mot de passe pour modifier** de manière programmatique. Aspose.Cells fournit la méthode WorkbookSettings.WriteProtection.ValidatePassword() qui vous permet de vérifier si le mot de passe pour modifier donné est correct ou non.

{{% /alert %}}

## **Vérifiez le mot de passe pour modifier dans Microsoft Excel**

Vous pouvez attribuer **Mot de passe pour ouvrir** et **Mot de passe pour modifier** lors de la création de vos classeurs dans Microsoft Excel. Veuillez consulter cette capture d'écran qui montre l'interface fournie par Microsoft Excel pour spécifier ces mots de passe.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Vérifier le mot de passe pour modifier à l'aide d'Aspose.Cells**

Les codes d'exemple suivants chargent le [fichier Excel source](5112232.xlsx). Il y a un Mot de passe pour ouvrir comme 1234 et un Mot de passe pour modifier comme 5678. Le code vérifie d'abord si 567 est le bon mot de passe pour modifier et il renvoie faux, puis il vérifie si 5678 est le mot de passe pour modifier et il renvoie vrai.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus après le chargement du [fichier Excel source](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
