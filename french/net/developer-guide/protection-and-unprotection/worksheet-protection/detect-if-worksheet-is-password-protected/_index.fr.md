---
title: Détecter si la feuille de calcul est protégée par un mot de passe
type: docs
weight: 360
url: /fr/net/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

Il est possible de protéger séparément les classeurs et les feuilles de calcul. Par exemple, une feuille de calcul peut contenir une ou plusieurs feuilles de calcul protégées par un mot de passe, mais la feuille de calcul elle-même peut être protégée ou non. Aspose.Cells Les API fournissent les moyens de détecter si une feuille de calcul donnée est protégée par mot de passe ou non. Cet article montre l'utilisation de Aspose.Cells for .NET API pour obtenir le même résultat.

{{% /alert %}}

 Aspose.Cells for .NET 8.7.0 a exposé le[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) propriété pour détecter si une feuille de calcul est protégée par un mot de passe ou non. Type booléen[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) retours de propriété**vrai** si[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) est protégé par un mot de passe et**faux** si non.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
