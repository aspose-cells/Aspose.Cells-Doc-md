---
title: Licence
type: docs
weight: 50
url: /fr/python-java/licensing/
---

{{% alert color="primary" %}} 

Vous pouvez installer une version d'évaluation de **Aspose.Cells** pour Python via Java avec `pip install aspose-cells`. La version d'évaluation offre exactement les mêmes fonctionnalités que la version sous licence du produit. De plus, la version d'évaluation devient simplement une version sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour l'appliquer.

Une fois que vous êtes satisfait de votre évaluation d'**Aspose.Cells**, vous pouvez [acheter une licence](https://purchase.aspose.com) sur le site Web Aspose. Familiarisez-vous avec les différents types d'abonnements proposés. Si vous avez des questions, n'hésitez pas à contacter l'équipe de vente d'Aspose.

Chaque licence Aspose comprend un abonnement d'un an pour les mises à jour gratuites vers toutes les nouvelles versions ou correctifs qui sortent pendant cette période. Le support technique est gratuit et illimité et est fourni aussi bien aux utilisateurs titulaires d'une licence qu'aux utilisateurs en évaluation.

{{% /alert %}} {{% alert color="primary" %}} 

Si vous souhaitez tester **Aspose.Cells** sans limitations de la version d'évaluation, demandez une licence temporaire de 30 jours. Veuillez vous référer à [Comment obtenir une licence temporaire?](https://purchase.aspose.com/temporary-license) pour plus d'informations.

{{% /alert %}}

## **Limitations de la version d'évaluation**

La version d'évaluation du produit **Aspose.Cells** (sans licence spécifiée) offre toutes les fonctionnalités du produit, mais est limitée à l'ouverture de 100 fichiers dans un seul programme et à une feuille de calcul supplémentaire avec un filigrane d'évaluation.

Les limitations sont affichées ci-dessous :

### **1ère limitation : Nombre de fichiers ouverts**

Lors de l'exécution de votre programme, vous ne pouvez ouvrir que 100 fichiers Excel. Si votre application dépasse ce nombre, une exception sera levée.

### **2ème limitation : Feuille de calcul avec filigrane d'évaluation**

![todo:image_alt_text](licensing_1.png)

Cette feuille de calcul apparaîtra toujours comme la feuille de calcul active. Seule dans la version sous licence, vous pouvez définir la feuille de calcul active sur d'autres feuilles de calcul.

## **Définition d'une licence**

La licence est un fichier XML en texte clair qui contient des détails tels que le nom du produit, le nombre de développeurs pour lequel il est autorisé, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, donc ne le modifiez pas; même l'ajout involontaire d'un saut de ligne supplémentaire le rendra invalide.

Vous devez définir une licence avant d'utiliser Aspose.Cells si vous voulez éviter ses limitations d'évaluation. Vous devez définir une licence une seule fois par application ou processus.

La licence peut être chargée à partir d'un fichier dans les emplacements suivants :

1. Chemin explicite.
1. Dossier de travail.

Utilisez la méthode [License.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License) pour accorder la licence au composant. Le moyen le plus simple de définir une licence est souvent de placer le fichier de licence dans le même dossier que Aspose.Cells.jar et de spécifier uniquement le nom du fichier sans chemin, comme le montre l'exemple suivant :

### **Exemple**

Dans cet exemple, **Aspose.Cells** tentera de trouver le fichier de licence dans votre dossier de travail.

{{< highlight python >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
