---
title: Limitations de la version d évaluation
type: docs
weight: 110
url: /fr/net/evaluation-version-limitations/
description: Aspose.Cells for .NET propose différents plans d achat ou offre un essai gratuit et une licence temporaire de 30 jours pour une évaluation en utilisant les politiques de licence et d abonnement en C#.
keywords: Limitations de la version d évaluation, Nombre de fichiers ouverts dans la version d évaluation, Filigrane d évaluation en utilisant la version d évaluation.
---

## **Comment obtenir la version d'évaluation d'Aspose.Cells**

Vous pouvez télécharger une version d'évaluation d'**Aspose.Cells** pour .NET à partir de [sa page de téléchargement](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repos. La version d'évaluation offre exactement les mêmes fonctionnalités que la version sous licence du produit. De plus, la version d'évaluation devient simplement sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour appliquer la licence.

Une fois que vous êtes satisfait de votre évaluation d'**Aspose.Cells**, vous pouvez [acheter une licence](https://purchase.aspose.com) sur le site Web Aspose. Familiarisez-vous avec les différents types d'abonnements proposés. Si vous avez des questions, n'hésitez pas à contacter l'équipe de vente d'Aspose.

Chaque licence Aspose comprend un abonnement d'un an pour les mises à jour gratuites vers toutes les nouvelles versions ou correctifs qui sortent pendant cette période. Le support technique est gratuit et illimité et est fourni aussi bien aux utilisateurs titulaires d'une licence qu'aux utilisateurs en évaluation.

## **Comment tester Aspose.Cells sans limitations de version d'évaluation**

Si vous souhaitez tester **Aspose.Cells** sans limitations de la version d'évaluation, demandez une licence temporaire de 30 jours. Veuillez vous référer à [Comment obtenir une licence temporaire?](https://purchase.aspose.com/temporary-license) pour plus d'informations.


## **Limitations de la version d'évaluation**

La version d'évaluation du produit **Aspose.Cells** (sans licence spécifiée) offre toutes les fonctionnalités du produit, mais est limitée à l'ouverture de 100 fichiers dans un seul programme et à une feuille de calcul supplémentaire avec un filigrane d'évaluation.

Les limitations sont affichées ci-dessous :

### **1ère limitation : Nombre de fichiers ouverts**

Lors de l'exécution de votre programme, vous ne pouvez ouvrir que 100 fichiers Excel. Si votre application dépasse ce nombre, une exception sera levée.

### **2ème limitation : Feuille de calcul avec filigrane d'évaluation**
Cette feuille de calcul apparaîtra toujours comme la feuille de calcul active. Seule dans la version sous licence, vous pouvez définir la feuille de calcul active sur d'autres feuilles de calcul.
<br>
<image src="1.png" width="70%" />
<br>

### **3ème limitation : Texte brut avec information d'évaluation**
Dans le fichier texte brut généré par Aspose.Cells, une information d’évaluation serait ajoutée à la fin du document. Lorsqu’on enregistre un fichier au format texte brut (tel que CSV et TSV), seul le contenu de la première feuille de travail sera exporté.
<br>
<image src="2.png" width="70%" />
<br>

### **4ème limitation : PDF et image avec filigrane d'évaluation**
Dans le fichier PDF ou image de Aspose.Cells, un filigrane d'évaluation sera ajouté en haut du document/image. Vous ne pouvez pas masquer l'avertissement de droits d'auteur en évaluation (la feuille de calcul supplémentaire) dans le contrôle GridWeb, car il sera toujours ajouté (à la fin dans les onglets de la feuille de calcul) dans le contrôle.
<br>
<image src="3.png" width="70%" />
<br>

### **5ème limitation : Paramètres du fichier de configuration (Aspose.Cells.GridWeb)**
Vous ne pouvez pas spécifier à nouveau le chemin du script en ajoutant les lignes de code suivantes dans la section de configuration (par exemple dans le fichier web.config). Le dossier acw_client contient des fichiers et Aspose.Cells.GridWeb utilise ce dossier pour gérer sa configuration interne, il contient des fichiers de script, des fichiers d'image et d'autres fichiers pour spécifier le comportement de GridWeb et définir d'autres opérations. Le fichier de configuration est utilisé pour empêcher le contrôle d'utiliser les ressources client intégrées (images, scripts, etc.), ce qui est utile dans certains cas/scénarios. De plus, ces paramètres de configuration dans le fichier web.config n'auront effet qu'avec la version LICENCIÉE du contrôle.

**XML**
{{< highlight csharp >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Ces paramètres peuvent être obligatoires dans certains cas/scénarios si vous utilisez le contrôle Aspose.Cells.GridWeb dans des sites Web du système de fichiers ou des extensions MS Ajax, etc.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
