---
title: Pourquoi ne pas utiliser Open XML SDK
type: docs
weight: 90
url: /fr/net/why-not-open-xml-sdk/
---

{{% alert color="primary" %}}

Nous entendons parfois cette question :

**Pourquoi devrions-nous utiliser les produits Aspose plutôt que le SDK Open XML gratuit ?**

Cette question est facile à répondre : fonctionnalités et fonctionnalité.

{{% /alert %}}

## **Qu'est-ce que Open XML SDK ?**

Selon la [bibliothèque MSDN](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN), le SDK Open XML est défini comme suit :

"Le SDK Open XML 2.5 simplifie la tâche de manipulation des packages Open XML et des éléments de schéma Open XML sous-jacents dans un package. Le SDK Open XML 2.5 encapsule de nombreuses tâches courantes effectuées par les développeurs sur les packages Open XML, de sorte que vous pouvez effectuer des opérations complexes avec seulement quelques lignes de code."

Les documents OOXML sont essentiellement des fichiers XML zippés et Open XML SDK est une collection de classes qui vous permet de travailler avec le contenu des documents OOXML de manière typée. Au lieu de décompresser un fichier pour extraire du XML, charger ce XML dans un arbre DOM et travailler avec des éléments et des attributs XML directement, Open XML SDK fournit des classes pour le faire.

## **Qu'est-ce que Aspose.Cells ?**

Aspose.Cells est une bibliothèque de classes qui permet aux applications d'effectuer les tâches de traitement de feuilles de calcul suivantes :

- Conversions de haute qualité entre tous les formats Microsoft Excel populaires, y compris la conversion en PDF, HTML, TIFF et l'impression.
- Programmation avec un modèle d'objet de classeur.
- Capacité à construire des documents à partir de fragments, à partir d'un ou de plusieurs documents, tout en fusionnant automatiquement les données par mise en forme stylistique, graphiques et graphiques.
- Des fonctions de haut niveau, telles que l'importation de données à partir de différentes sources de données, y compris Array, ArrayList, DataTable / ResultSet.
- Moteur de calcul de formules robuste prenant en charge presque toutes les fonctions standard et avancées de Microsoft Excel.

## **Comparer le SDK Open XML et Aspose.Cells**

Le tableau suivant compare les fonctionnalités du SDK Open XML et d'Aspose.Cells.

|**Fonction ou catégorie de fonctionnalités**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Formats Excel pris en charge ou autres formats|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, délimité par des tabulations, ODS, texte brut (TXT), PDF, XPS|
|Convertir entre les formats Excel|Non|Oui|
|<p>Programmation de haut niveau avec un modèle d'objet classeur :</p><p>- Trouver et remplacer.</p><p>- Assembler des feuilles de calcul.</p><p>- Copier des fragments et des feuilles de calcul entre des classeurs.|Non|Oui|
|Programmation détaillée avec un modèle d'objet document, accès aux éléments individuels et aux propriétés de mise en forme de tous les éléments de la feuille de calcul.|Oui|Oui|
|Accès direct et complet de bas niveau aux éléments et attributs XML sous-jacents tels que les identifiants de relation, les identifiants de liste d'un document OOXML.|Oui|Non|
|<p>Générer des rapports, peupler des documents avec des données :</p><p>- Importer/Exporter des données vers/depuis un DataTable / _ResultSet.</p><p>- Fonctionnalité Smart Markers.</p><p>- Insérer/Supprimer des lignes/colonnes/plages.</p><p>- Sources de données personnalisées.</p>|Non|Oui|
|<p>Rendu et impression :* Rendre les pages de feuille de calcul en images raster (TIFF, TIFF multipage, PNG, JPEG, BMP).* Rendre les pages de feuille de calcul en images vectorielles (EMF).</p><p>- Convertir les graphiques en images (TIFF, TIFF multipage, PNG, JPEG, BMP, EMF, etc.)</p><p>- Spécifier la résolution, la qualité, la compression et d'autres options des images.</p><p>- Imprimer les feuilles de calcul en utilisant l'infrastructure d'impression .NET. Le composant a une méthode d'impression intégrée pour imprimer les feuilles de calcul comme indiqué dans l'aperçu avant impression de Microsoft Excel.</p>|Non|Oui|
|Calculer/Recalculer les formules dynamiquement|Non|Oui|
|Plateformes prises en charge|Windows, .NET|Windows, Linux, Java, .NET, Mono|

Vous pouvez comparer OpenXML avec Aspose.Cells Pour ce faire, nous vous suggérons de vous familiariser avec le projet Aspose.Cells for OpenXML - il montre comment différentes tâches peuvent être effectuées en utilisant l'API Aspose.Cells for .NET par rapport à OpenXML. Le projet couvre également des fonctionnalités pour travailler avec des documents texte qui ne sont disponibles que dans Aspose.Cells et non dans OpenXML.

Ce projet est également utile pour les développeurs souhaitant migrer d'OpenXML vers Aspose.Cells.

{{% alert color="primary" %}}

Explorez [le plugin avec des exemples de code source des fonctionnalités Aspose.Cells for .NET en comparaison avec OpenXML](https://github.com/asposemarketplace/Aspose_for_OpenXML).

Ce plugin utilise la version d'évaluation d'Aspose.Cells. Lorsque vous êtes satisfait de votre évaluation, vous pouvez acheter une licence sur le [site Aspose](https://purchase.aspose.com/buy). Pour supprimer le message d'évaluation et les limitations de fonctionnalités, vous devez appliquer une licence de produit. Après l'achat du produit, vous recevrez un fichier de licence. Veuillez suivre les instructions de l'article ["Licences et abonnements"](/cells/fr/net/licensing/) pour le faire.

{{% /alert %}}

**Conclusion** : Le SDK Open XML et Aspose.Cells ne sont pas en concurrence directe car ils répondent à des besoins et à un public assez différents.

## **Pourquoi pas Open XML SDK**
Open XML SDK est une bibliothèque de classes qui fournit un moyen typé fort de travailler avec des documents OOXML. Aspose.Cells est une bibliothèque de traitement de feuilles de calcul très utile qui offre un excellent support pour tous les formats de fichier Microsoft Excel et autres.

Si tout ce que vous avez à faire est une opération de programmation assez basique sur un document XLSX, alors Open XML SDK pourrait être un choix approprié. Avec Open XML SDK, vous serez assez à l'aise pour effectuer des tâches simples comme générer un document XLSX simple ou supprimer des commentaires, des en-têtes/pieds de page, extraire des images ou autres. 
Certaines tâches peuvent être effectuées avec le SDK Open XML, mais ne peuvent pas être effectuées avec Aspose.Cells. Par exemple, si vous avez besoin d'accéder directement aux éléments et attributs XML d'un document OOXML, alors vous devez utiliser le SDK Open XML.

Cependant, si vous devez effectuer des opérations complexes sur des documents, comme certaines des tâches suivantes, alors utiliser Aspose.Cells est votre meilleure option :

- Prise en charge d'autres formats de fichier en plus de XLSX.
- Copier des fragments et des feuilles de calcul entre des classeurs ou fusionner des classeurs de manière à combiner des objets, des styles et d'autres formatages de manière appropriée.
- Remplacer du texte formaté ou non formaté.
- Des fonctions de haut niveau, telles que l'importation de données à partir de différentes sources de données, y compris Array, ArrayList, DataTable / ResultSet.
- Générer un document commercial, tel qu'une commande avec des détails de commande à partir d'une source de données.
- Convertir un document en PDF ou XPS pour qu'il apparaisse exactement comme Microsoft Excel l'aurait converti.
- Développer une application .NET ou Java.

{{< app/cells/assistant language="csharp" >}}
