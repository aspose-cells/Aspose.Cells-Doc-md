---
title: Découvrez si le projet VBA est protégé
type: docs
weight: 80
url: /fr/java/find-out-if-vba-project-is-protected/
---
## **Scénarios d'utilisation possibles**
 Vous pouvez savoir si le projet VBA (Visual Basic Applications) de votre fichier Excel est protégé ou non avec Aspose.Cells en utilisant[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)méthode
## **Exemple de code**
L'exemple de code suivant crée un classeur, puis vérifie si son projet VBA est protégé ou non. Ensuite, il protège le projet VBA et vérifie à nouveau si son projet VBA est protégé ou non. Veuillez consulter sa sortie console pour une référence. Avant protection,[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) Retour**faux** mais après protection, il revient**vrai**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Sortie console**
Il s'agit de la sortie console de l'exemple de code ci-dessus pour référence.

{{< highlight "java" >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
