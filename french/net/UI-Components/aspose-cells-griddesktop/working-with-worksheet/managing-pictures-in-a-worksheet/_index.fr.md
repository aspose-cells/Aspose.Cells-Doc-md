---
title: Gestion des images dans une feuille de calcul
type: docs
weight: 100
url: /fr/net/managing-pictures-in-a-worksheet/
---
{{% alert color="primary" %}} 

La plupart des gens croient qu'une image peut expliquer les choses mieux que des mots. C'est pourquoi Aspose.Cells.GridDesktop prend en charge l'ajout d'images aux feuilles de calcul pour exécuter cette croyance des gens. Dans cette rubrique, nous discuterons de l'ajout et de la manipulation d'images dans les feuilles de calcul.

{{% /alert %}} 
## **Ajout d'images**
Pour ajouter un lien hypertexte vers une cellule à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Ajouter**Photo** à la feuille de calcul en spécifiant le chemin du fichier de l'image et le nom de la cellule où l'image sera insérée

**Des photos** collecte dans le**Feuille de travail** l'objet fournit une surcharge**Ajouter** méthode. Les développeurs peuvent utiliser n'importe quelle version surchargée de**Ajouter** méthode en fonction de leurs besoins spécifiques. L'utilisation de ces versions surchargées de**Ajouter** méthode, il est possible d'ajouter une image à partir d'un fichier, d'un flux ou**Image** objet.

Vous trouverez ci-dessous l'exemple de code permettant d'ajouter des images dans des feuilles de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Accéder aux photos**
 Pour accéder à une image existante dans la feuille de calcul et la modifier, les développeurs peuvent accéder à l'image à partir du**Des photos** collecte de la**Feuille de travail** en spécifiant la cellule (en utilisant le nom de la cellule ou son emplacement en termes de numéro de ligne et de colonne) dans laquelle l'image est insérée. Une fois l'image accessible, les développeurs peuvent modifier son image au moment de l'exécution.

Vous trouverez ci-dessous l'exemple de code permettant d'accéder aux images d'une feuille de calcul et de les modifier.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Suppression d'images**
 Pour supprimer une image existante, les développeurs peuvent simplement accéder à une feuille de calcul souhaitée, puis**Supprimer** image de la**Des photos** collecte de la**Feuille de travail** en spécifiant la cellule (en utilisant son nom ou son numéro de ligne et de colonne) qui contient l'image.

Dans le code ci-dessous, il est montré comment supprimer des images de la feuille de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
