---
title: Vérifiez le mot de passe utilisé pour protéger la feuille de calcul
type: docs
weight: 290
url: /fr/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Les API Aspose.Cells ont amélioré la classe [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) en introduisant quelques propriétés et méthodes utiles. L'une de ces méthodes est [**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) qui permet de spécifier un mot de passe en tant qu'instance de String et de vérifier si le même mot de passe a été utilisé pour protéger la feuille de calcul.

{{% /alert %}}

## **Vérifier le mot de passe utilisé pour protéger la feuille de calcul**

La méthode [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) renvoie **vrai** si le mot de passe spécifié correspond au mot de passe utilisé pour protéger la feuille de calcul donnée, **faux** si le mot de passe spécifié ne correspond pas. Le morceau de code suivant utilise la méthode [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) en conjonction avec la propriété [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) pour détecter la protection par mot de passe, et vérifie le mot de passe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
