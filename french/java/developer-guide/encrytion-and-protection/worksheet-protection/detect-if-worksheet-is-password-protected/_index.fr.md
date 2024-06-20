---
title: Détecter si la feuille de calcul est protégée par mot de passe
type: docs
weight: 280
url: /fr/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Il est possible de protéger les classeurs et les feuilles de calcul séparément. Par exemple, une feuille de calcul peut contenir une ou plusieurs feuilles de calcul protégées par mot de passe, cependant, la feuille de calcul elle-même peut être protégée ou non. Les API Aspose.Cells fournissent les moyens de détecter si une feuille de calcul donnée est protégée par mot de passe ou non. Cet article démontre l'utilisation de l'API Aspose.Cells for Java pour atteindre le même objectif.

{{% /alert %}}

## **Détecter si la feuille de calcul est protégée par mot de passe**

Aspose.Cells for Java 8.7.0 a exposé la propriété [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) pour détecter si une feuille de calcul est protégée par mot de passe ou non. Le champ de type booléen [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) renvoie **vrai** si [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) est protégé par mot de passe et **faux** sinon.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
