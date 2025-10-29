---  
title: Découvrez si le projet VBA est protégé avec Golang via C++  
linktitle: Vérifier si le projet VBA est protégé  
type: docs  
weight: 20  
url: /fr/go-cpp/find-out-if-vba-project-is-protected/  
description: Vérifiez si le projet VBA d un fichier Excel est protégé en utilisant Aspose.Cells avec Golang via C++.  
---  

## **Vérifiez si le projet VBA est protégé en C++**

Vous pouvez déterminer si le projet VBA (Visual Basic Applications) de votre fichier Excel est protégé ou non avec Aspose.Cells en utilisant la propriété [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/).

## **Code d'exemple**

Le code exemple suivant crée un classeur puis vérifie si son projet VBA est protégé ou non. Ensuite, il protège le projet VBA et vérifie de nouveau. Veuillez consulter la sortie de la console pour référence. Avant la protection, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/) retourne **faux**, mais après, il retourne **vrai**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindOutIfVbaProjectIsProtected.go" >}}
## **Sortie console**

Il s'agit de la sortie console du code d'exemple ci-dessus pour référence.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
