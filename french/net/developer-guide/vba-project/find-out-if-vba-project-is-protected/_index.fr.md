---
title: Vérifier si le projet VBA est protégé
type: docs
weight: 20
url: /fr/net/find-out-if-vba-project-is-protected/
---

## **Savoir si le projet VBA est protégé en C#**

Vous pouvez voir si le projet VBA (Applications Visual Basic) de votre fichier Excel est protégé ou non avec Aspose.Cells en utilisant la propriété [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected).

## **Code d'exemple**

Le code d'exemple suivant crée un classeur et vérifie ensuite si son projet VBA est protégé ou non. Ensuite, il protège le projet VBA et vérifie à nouveau si son projet VBA est protégé ou non. Veuillez consulter la sortie console pour référence. Avant la protection, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) retourne **false** mais après la protection, il retourne **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **Sortie console**

Il s'agit de la sortie console du code d'exemple ci-dessus pour référence.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
