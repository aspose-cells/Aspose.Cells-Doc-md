---
title: Gestion des images dans une feuille de calcul
type: docs
weight: 100
url: /fr/net/aspose-cells-griddesktop/manage-pictures-in-a-worksheet/
keywords: GridDesktop, image, images
description: Cet article présente comment travailler avec une image dans une feuille de calcul dans GridDesktop.
---

{{% alert color="primary" %}} 

La plupart des gens pensent qu'une image peut expliquer les choses mieux que des mots. C'est pourquoi Aspose.Cells.GridDesktop prend en charge l'ajout d'images dans les feuilles de calcul pour exécuter cette croyance des gens. Dans ce sujet, nous discuterons de l'ajout et de la manipulation d'images dans les feuilles de calcul.

{{% /alert %}} 
## **Ajout d'images**
Pour ajouter un hyperlien à une cellule à l'aide d'Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Ajoutez une **Image** à la feuille de calcul en spécifiant le chemin du fichier de l'image et le nom de la cellule où l'image sera insérée

La collection **Pictures** de l'objet **Worksheet** fournit une méthode **Add** surchargée. Les développeurs peuvent utiliser n'importe quelle version surchargée de la méthode **Add** selon leurs besoins spécifiques. En utilisant ces versions surchargées de la méthode **Add**, il est possible d'ajouter une image à partir d'un fichier, d'un flux ou d'un objet **Image**.

Voici le code d'exemple pour ajouter des images dans des feuilles de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Accéder aux images**
Pour accéder et modifier une image existante dans la feuille de calcul, les développeurs peuvent accéder à l'image depuis la collection **Pictures** de la **Worksheet** en spécifiant la cellule (en utilisant le nom de la cellule ou son emplacement en termes de numéro de ligne et de colonne) dans laquelle l'image est insérée. Une fois l'image est accédée, les développeurs peuvent modifier son Image à l'exécution.

Voici le code d'exemple pour accéder et modifier les images dans une feuille de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Suppression d'images**
Pour supprimer une image existante, les développeurs peuvent simplement accéder à une feuille de calcul souhaitée, puis **Supprimer** l'image de la collection **Pictures** de la **Worksheet** en spécifiant la cellule (en utilisant son nom ou son numéro de ligne et de colonne) qui contient l'image.

Dans le code ci-dessous, il est montré comment supprimer des images de la feuille de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
