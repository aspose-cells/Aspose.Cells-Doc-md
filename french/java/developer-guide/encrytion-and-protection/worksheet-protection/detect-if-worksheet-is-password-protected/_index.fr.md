---
title: Détecter si la feuille de calcul est protégée par un mot de passe
type: docs
weight: 280
url: /fr/java/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

Il est possible de protéger séparément les classeurs et les feuilles de calcul. Par exemple, une feuille de calcul peut contenir une ou plusieurs feuilles de calcul protégées par un mot de passe, mais la feuille de calcul elle-même peut être protégée ou non. Aspose.Cells Les API fournissent les moyens de détecter si une feuille de calcul donnée est protégée par mot de passe ou non. Cet article montre l'utilisation de Aspose.Cells for Java API pour obtenir le même résultat.

{{% /alert %}}

## **Détecter si la feuille de calcul est protégée par un mot de passe**

Aspose.Cells for Java 8.7.0 a exposé le[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) propriété pour détecter si une feuille de calcul est protégée par un mot de passe ou non. Type booléen[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) retours de champ**vrai** si[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) est protégé par un mot de passe et**faux** si non.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
