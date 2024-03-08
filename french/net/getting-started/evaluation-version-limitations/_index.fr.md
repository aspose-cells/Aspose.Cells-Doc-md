---
title: Limites de la version d'évaluation
type: docs
weight: 110
url: /fr/net/evaluation-version-limitations/
description: Aspose.Cells for .NET propose différents plans d'achat ou propose un essai gratuit et une licence temporaire de 30 jours pour évaluation à l'aide des politiques de licence et d'abonnement du C#.
keywords: Evaluation Version Limitations, Number of Opened Files in Evaluation Version, Evaluation Watermark using Evaluation Version.
---
##  **Comment obtenir la version d'évaluation de Aspose.Cells**

 Vous pouvez télécharger une version d'évaluation de**Aspose.Cells** pour NET de[sa page de téléchargement](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven dépôts. La version d'évaluation offre absolument les mêmes fonctionnalités que la version sous licence du produit. De plus, la version d'évaluation devient simplement sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour appliquer la licence.

 Une fois que vous êtes satisfait de votre évaluation du *Aspose.Cells**, vous pouvez[acheter une licence](https://purchase.aspose.com) sur le site Aspose. Familiarisez-vous avec les différents types d'abonnements proposés. Si vous avez des questions, n'hésitez pas à contacter l'équipe commerciale du Aspose.

Chaque licence Aspose comporte un abonnement d'un an pour des mises à niveau gratuites vers toute nouvelle version ou correctif publié pendant cette période. Le support technique est gratuit et illimité et fourni aux utilisateurs sous licence et en évaluation.

##  **Comment tester Aspose.Cells sans limitations de la version d'évaluation**

 Si tu veux tester**Aspose.Cells** sans limitations de la version d’évaluation, demandez une licence temporaire de 30 jours. Prière de se référer à[Comment obtenir un permis temporaire ?](https://purchase.aspose.com/temporary-license) pour plus d'informations.


##  **Limites de la version d'évaluation**

 Version d'évaluation de**Aspose.Cells** Le produit (sans licence spécifiée) fournit toutes les fonctionnalités du produit, mais il est limité à l'ouverture de 100 fichiers dans un programme et à une feuille de calcul supplémentaire avec un filigrane d'évaluation.

Les limites sont indiquées ci-dessous :

###  **1ère limitation : nombre de fichiers ouverts**

Lors de l'exécution de votre programme, vous ne pouvez ouvrir que 100 fichiers Excel. Si votre candidature dépasse ce nombre, une exception sera levée.

###  **2e limitation : feuille de travail avec filigrane d'évaluation**
Cette feuille de calcul s'affichera toujours comme feuille de calcul active. Uniquement dans la version sous licence, vous pouvez définir la feuille de calcul active sur d'autres feuilles de calcul.
<br>
<image src="1.png" width="70%" />
<br>

###  **3e limitation : texte brut avec informations d'évaluation**
Dans le fichier de texte brut de sortie par Aspose.Cells, des informations d'évaluation seraient ajoutées à la fin du document.
<br>
<image src="2.png" width="70%" />
<br>

###  **4ème limitation : PDF et image avec filigrane d'évaluation**
Dans le fichier de sortie PDF ou image par Aspose.Cells, un filigrane d'évaluation sera collé en haut du document/image. Vous ne pouvez pas non plus masquer l'avertissement de copyright d'évaluation (la feuille de calcul supplémentaire) dans le contrôle GridWeb, il sera toujours ajouté. (à la fin dans les onglets de la feuille de calcul) dans le champ.
<br>
<image src="3.png" width="70%" />
<br>

###  **5ème limitation : paramètres du fichier de configuration (Aspose.Cells.GridWeb)**
Vous ne pouvez pas re-spécifier le chemin du script en ajoutant les lignes de code suivantes dans la section de configuration (par exemple dans le fichier web.config). Le acw_client est un dossier qui contient des fichiers et Aspose.Cells.GridWeb utilise ce dossier pour gérer sa configuration interne, il contient des fichiers de script, des fichiers image et d'autres fichiers pour spécifier le comportement de GridWeb et définir d'autres opérations. Le fichier de configuration est utilisé pour empêcher le contrôle d'utiliser les ressources client intégrées (images, scripts, etc.), ce qui est utile dans certains cas/scénarios. De plus, ces paramètres de configuration dans le fichier web.config ne prendront effet qu'avec la version LICENSED du contrôle.

**XML**
{{< highlight "csharp" >}}
<appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Ces paramètres peuvent être obligatoires dans certains cas/scénarios si vous utilisez le contrôle Aspose.Cells.GridWeb dans les sites Web du système de fichiers ou les extensions MS Ajax, etc.

{{% /alert %}}