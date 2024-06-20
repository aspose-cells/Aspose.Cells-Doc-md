---
title: Vérifier si le projet VBA est protégé
type: docs
weight: 80
url: /fr/java/find-out-if-vba-project-is-protected/
---

## **Scénarios d'utilisation possibles**
Vous pouvez savoir si le projet VBA (Visual Basic Applications) de votre fichier Excel est protégé ou non avec Aspose.Cells en utilisant la méthode [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)
## **Code d'exemple**
Le code d'exemple suivant crée un classeur, puis vérifie si son projet VBA est protégé ou non. Ensuite, il protège le projet VBA et vérifie à nouveau s'il est protégé ou non. Veuillez consulter sa sortie console pour référence. Avant la protection, [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) renvoie **false** mais après la protection, il renvoie **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Sortie console**
Il s'agit de la sortie console du code d'exemple ci-dessus pour référence.

{{< highlight java >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
