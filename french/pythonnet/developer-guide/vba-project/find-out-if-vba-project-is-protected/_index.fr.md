---
title: Vérifier si le projet VBA est protégé
type: docs
weight: 20
url: /fr/python-net/find-out-if-vba-project-is-protected/
---

## **Découvrir si le projet VBA est protégé en Python**

Vous pouvez vérifier si le projet VBA (Visual Basic Applications) de votre fichier Excel est protégé ou non avec Aspose.Cells pour Python via .NET en utilisant la propriété [**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected).

## **Code d'exemple**

Le code d'exemple suivant crée un classeur et vérifie ensuite si son projet VBA est protégé ou non. Ensuite, il protège le projet VBA et vérifie à nouveau si son projet VBA est protégé ou non. Veuillez consulter la sortie console pour référence. Avant la protection, [**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected) retourne **false** mais après la protection, il retourne **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FindoutifVBAProjectisProtected.py" >}}

## **Sortie console**

Il s'agit de la sortie console du code d'exemple ci-dessus pour référence.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
