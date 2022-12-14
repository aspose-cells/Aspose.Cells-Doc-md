---
title: Vérifier le mot de passe utilisé pour protéger la feuille de calcul
type: docs
weight: 370
url: /fr/net/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells Les API ont amélioré la[**protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) classe en introduisant quelques propriétés et méthodes utiles. Une telle méthode est la[**Vérifier le mot de passe**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) qui permet de spécifier un mot de passe comme instance de*chaîne de caractères* et vérifie si le même mot de passe a été utilisé pour protéger le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

 La[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) la méthode renvoie**vrai**si le mot de passe spécifié correspond au mot de passe utilisé pour protéger la feuille de calcul donnée et**faux** si le mot de passe spécifié ne correspond pas. Le morceau de code suivant utilise le[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) méthode en collaboration avec[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)propriété pour détecter la protection par mot de passe et vérifie le mot de passe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
