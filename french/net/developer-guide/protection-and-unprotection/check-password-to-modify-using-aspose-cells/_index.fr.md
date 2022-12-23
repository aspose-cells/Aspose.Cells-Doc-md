---
title: Vérifiez le mot de passe à modifier en utilisant Aspose.Cells
type: docs
weight: 2400
url: /fr/net/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Parfois, vous devez vérifier si le mot de passe donné correspond au**Mot de passe à modifier** par programme. Aspose.Cells fournit la méthode WorkbookSettings.WriteProtection.ValidatePassword() que vous pouvez utiliser pour vérifier si le mot de passe donné à modifier est correct ou non.

{{% /alert %}}

## **Vérifier le mot de passe à modifier dans Microsoft Excel**

 Vous pouvez attribuer**Mot de passe pour ouvrir** et**Mot de passe à modifier** lors de la création de vos classeurs dans Microsoft Excel. Veuillez consulter cette capture d'écran qui montre l'interface Microsoft fournie par Excel pour spécifier ces mots de passe.

|![tâche : image_autre_texte](check-password-to-modify-using-aspose-cells_1.png)|
|:- |

## **Vérifiez le mot de passe à modifier en utilisant Aspose.Cells**

 Les exemples de codes suivants chargent le[source Excel](5112232.xlsx) dossier. Il a un mot de passe à ouvrir en tant que 1234 et un mot de passe à modifier en tant que 5678. Le code vérifie d'abord si 567 est le mot de passe correct à modifier et il renvoie faux, puis il vérifie si 5678 est le mot de passe à modifier et il renvoie vrai.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Sortie console**

 Voici la sortie de la console de l'exemple de code ci-dessus après le chargement du[source Excel](5112232.xlsx) dossier.

{{< highlight "java" >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
