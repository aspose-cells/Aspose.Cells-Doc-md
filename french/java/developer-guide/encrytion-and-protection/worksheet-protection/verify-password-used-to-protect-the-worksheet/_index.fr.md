---
title: Vérifier le mot de passe utilisé pour protéger la feuille de calcul
type: docs
weight: 290
url: /fr/java/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells Les API ont amélioré la[**protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) classe en introduisant quelques propriétés et méthodes utiles. Une telle méthode est la[**vérifier le mot de passe**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)qui permet de spécifier un mot de passe en tant qu'instance de String et vérifie si le même mot de passe a été utilisé pour protéger la feuille de travail.

{{% /alert %}}

## **Vérifier le mot de passe utilisé pour protéger la feuille de calcul**

 La[**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) ) la méthode renvoie**vrai** si le mot de passe spécifié correspond au mot de passe utilisé pour protéger la feuille de calcul donnée,**faux** si le mot de passe spécifié ne correspond pas. Le morceau de code suivant utilise le[**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) ) méthode en conjonction avec[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)propriété pour détecter la protection par mot de passe et vérifie le mot de passe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
