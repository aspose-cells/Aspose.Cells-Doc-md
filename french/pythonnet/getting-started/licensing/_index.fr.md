---
title: Licence
type: docs
weight: 21
url: /fr/python-net/licensing/
---

{{% alert color="primary" %}}

Vous pouvez facilement télécharger une version d'évaluation de Aspose.Cells Python via .Net depuis sa [page de téléchargement](https://pypi.org/project/aspose-cells-python/) @ Dépôts Pypi. La version d'évaluation fournit exactement les mêmes fonctionnalités que la version sous licence du composant. De plus, la version d'évaluation devient simplement sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour appliquer la licence.

{{% /alert %}}

## **Limitations de la version d'évaluation**

La version d'évaluation de la Aspose.Cells Python via .Net (sans licence spécifiée) offre toutes les fonctionnalités du produit, mais est limitée à l'ouverture de 100 fichiers dans un programme et à une feuille de calcul supplémentaire avec un filigrane d'évaluation.

Les limitations sont affichées ci-dessous :

- **Nombre de fichiers ouverts** (Aspose.Cells Python via .Net)
  Lorsque vous exécutez votre programme, vous ne pouvez ouvrir que 100 fichiers Excel en utilisant la bibliothèque Aspose.Cells Python via .Net. Si votre application dépasse ce nombre, une exception sera déclenchée.


De plus, une feuille de calcul avec un filigrane d'évaluation sera toujours affichée comme la feuille de calcul active dans le fichier Excel généré à l'aide de la bibliothèque Aspose.Cells Python via. Seule dans la version sous licence, vous pouvez définir la feuille de calcul active sur d'autres feuilles de calcul. Dans le fichier PDF ou l'image de sortie généré par Aspose.Cells Python via, un filigrane d'évaluation sera collé en haut du document/image.

{{% alert color="primary" %}}

Si vous souhaitez tester Aspose.Cells Python via sans limitation de la version d'évaluation, vous pouvez également demander une [licence temporaire de 30 jours](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Application d'une Licence dans le Composant Aspose.Cells Python via**

La licence est un fichier XML en texte clair qui contient des détails tels que le nom du produit, le nombre de développeurs auxquels il est autorisé, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, donc ne modifiez pas le fichier. Même l'ajout involontaire d'un saut de ligne supplémentaire dans le fichier l'invalidera. Vous devez définir une licence avant d'utiliser Aspose.Cells Python via si vous souhaitez éviter sa limitation d'évaluation. Il suffit de définir une licence une fois par application (ou processus). La licence peut être chargée à partir d'un fichier.

Aspose.Cells Python via tente de trouver la licence dans des emplacements de chemin explicites.

Il existe deux méthodes courantes pour appliquer une licence à partir d'un fichier.

### **Application d'une Licence à partir du Disque**

La manière la plus simple de définir une licence est de placer le fichier de licence dans le chemin explicite.

{{< highlight csharp >}}

# Instantiate an instance of license and set the license file through its path

license = License();
# For Windows
license.set_license("D:\Aspose.Cells.lic");
# For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

Lorsque vous appelez la méthode set_license, le nom de la licence doit être le même que celui de votre fichier de licence. Par exemple, vous pouvez changer le nom du fichier de licence en **Aspose.Cells.lic.xml**. Ensuite, dans votre code, vous devez utiliser le nom de licence modifié (**Aspose.Cells.lic.xml**) pour la méthode set_license.

{{% /alert %}}


{{< app/cells/assistant language="python-net" >}}
