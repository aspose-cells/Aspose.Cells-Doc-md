---
title: Licence
type: docs
weight: 21
url: /fr/python-net/licensing/
---
{{% alert color="primary" %}}

 Vous pouvez facilement télécharger une version d'évaluation de Aspose.Cells Python via .Net à partir de son[page de téléchargement](https://pypi.org/project/aspose-cells-python/) Pypi repos. La version d'évaluation fournit absolument les mêmes fonctionnalités que la version sous licence du composant. De plus, la version d'évaluation devient simplement sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour appliquer la licence.

{{% /alert %}}

## **Limites de la version d'évaluation**

La version d'évaluation de Aspose.Cells Python via le produit .Net (sans licence spécifiée) fournit toutes les fonctionnalités du produit, mais elle est limitée à l'ouverture de 100 fichiers dans un programme et d'une feuille de calcul supplémentaire avec filigrane d'évaluation.

Les limites sont indiquées ci-dessous :

- **Nombre de fichiers ouverts** (Aspose.Cells Python via .Net)
 Lors de l'exécution de votre programme, vous ne pouvez ouvrir que 100 fichiers Excel en utilisant Aspose.Cells Python via la bibliothèque .Net. Si votre application dépasse ce nombre, une exception sera levée.


De plus, une feuille de calcul avec un filigrane d'évaluation s'affichera toujours comme feuille de calcul active dans le fichier Excel généré en utilisant Aspose.Cells Python via la bibliothèque. Uniquement dans la version sous licence, vous pouvez définir la feuille de calcul active sur d'autres feuilles de calcul. Dans la sortie PDF ou le fichier image par Aspose.Cells Python via, un filigrane d'évaluation serait collé en haut du document/image.

{{% alert color="primary" %}}

 Si vous souhaitez tester Aspose.Cells Python via sans limitations de version d'évaluation, vous pouvez également demander un[Permis temporaire de 30 jours](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Application d'une licence au Aspose.Cells Python via le composant**

La licence est un fichier XML en texte brut qui contient des détails tels que le nom du produit, le nombre de développeurs auxquels il est licencié, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, ne modifiez donc pas le fichier. Même l'ajout par inadvertance d'un saut de ligne supplémentaire dans le fichier l'invalidera. Vous devez définir une licence avant d'utiliser Aspose.Cells Python via si vous souhaitez éviter sa limitation d'évaluation. Il n'est nécessaire de définir une licence qu'une seule fois par application (ou processus). La licence peut être chargée à partir d'un fichier.

Aspose.Cells Python via tente de trouver la licence dans des emplacements de chemin explicites.

Il existe deux méthodes courantes pour appliquer une licence à partir d'un fichier.

### **Application d'une licence à partir du disque**

Le moyen le plus simple de définir une licence consiste à placer le fichier de licence dans le chemin explicite.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

license = License();
 //For Windows
license.set_license("D:\Aspose.Cells.lic");
 //For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

Lorsque vous appelez le poste_méthode de licence, le nom de la licence doit être le même que celui de votre nom de fichier de licence. Par exemple, vous pouvez modifier le nom du fichier de licence en **Aspose.Cells.lic.xml**. Ensuite, dans votre code, vous devez utiliser le nom de licence modifié (**Aspose.Cells.lic.xml**) pour l'ensemble_méthode de licence.

{{% /alert %}}


