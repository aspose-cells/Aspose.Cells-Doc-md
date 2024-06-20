---
title: Détecter si la feuille de calcul est protégée par mot de passe
type: docs
weight: 360
url: /fr/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Il est possible de protéger les classeurs et les feuilles de calcul séparément. Par exemple, une feuille de calcul peut contenir une ou plusieurs feuilles protégées par mot de passe, cependant, la feuille de calcul elle-même peut être protégée ou non. Les API Aspose.Cells fournissent les moyens de détecter si une certaine feuille de calcul est protégée par mot de passe ou non. Cet article démontre l'utilisation de l'API Aspose.Cells for .NET pour atteindre le même objectif.

{{% /alert %}}

Aspose.Cells for .NET 8.7.0 a exposé la propriété [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) pour détecter si une feuille de calcul est protégée par mot de passe ou non. La propriété de type booléen [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) renvoie **true** si la [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) est protégée par mot de passe et **false** si ce n'est pas le cas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
