---
title: Vérifiez le mot de passe utilisé pour protéger la feuille de calcul
type: docs
weight: 370
url: /fr/net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Les API Aspose.Cells ont amélioré la classe [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) en introduisant certaines propriétés et méthodes utiles. Une telle méthode est la [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) qui permet de spécifier un mot de passe en tant qu'instance de *chaîne* et de vérifier si le même mot de passe a été utilisé pour protéger le [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

La méthode [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) renvoie **true** si le mot de passe spécifié correspond au mot de passe utilisé pour protéger la feuille de calcul donnée et **false** si le mot de passe spécifié ne correspond pas. Le code suivant utilise la méthode [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) en conjonction avec la propriété [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) pour détecter la protection par mot de passe et vérifie le mot de passe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
