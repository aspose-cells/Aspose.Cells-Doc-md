---
title: Détecter si la feuille de calcul est protégée par mot de passe
type: docs
weight: 360
url: /fr/python-net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Il est possible de protéger séparément les classeurs et les feuilles de calcul. Par exemple, une feuille de calcul peut contenir une ou plusieurs feuilles protégées par mot de passe, toutefois, le classeur lui-même peut ou non être protégé. Les API Aspose.Cells pour Python via .NET permettent de détecter si une feuille est protégée par mot de passe ou non. Cet article montre comment utiliser l'API Aspose.Cells pour Python via .NET pour faire cela.

{{% /alert %}}

Aspose.Cells pour Python via .NET a exposé la propriété [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) pour détecter si une feuille de calcul est protégée par mot de passe ou non. La propriété booléenne [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) retourne **true** si [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) est protégé par mot de passe et **false** sinon.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckIfPasswordProtected.py" >}}

