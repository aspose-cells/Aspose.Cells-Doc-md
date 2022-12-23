---
title: Pourquoi ne pas ouvrir le SDK XML
type: docs
weight: 90
url: /fr/net/why-not-open-xml-sdk/
---
{{% alert color="primary" %}}

On entend parfois cette question :

**Pourquoi devrions-nous utiliser les produits Aspose plutôt que le SDK Open XML gratuit ?**

Il est facile de répondre à cette question : fonctionnalités et fonctionnalités.

{{% /alert %}}

## **Qu'est-ce qu'Open XML SDK ?**

 Selon le[Bibliothèque MSDN](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN), le SDK Open XML est défini comme suit :

"Le SDK Open XML 2.5 simplifie la tâche de manipulation des packages Open XML et des éléments de schéma Open XML sous-jacents dans un package. Le SDK Open XML 2.5 encapsule de nombreuses tâches courantes que les développeurs effectuent sur les packages Open XML, afin que vous puissiez effectuer des opérations complexes avec quelques lignes de code."

Les documents OOXML sont essentiellement des fichiers XML compressés et Open XML SDK est une collection de classes qui vous permet de travailler avec le contenu des documents OOXML de manière fortement typée. C'est-à-dire qu'au lieu de décompresser un fichier pour extraire le XML, de charger ce XML dans une arborescence DOM et de travailler directement avec les éléments et les attributs XML, Open XML SDK fournit des classes pour le faire.

## **Qu'est-ce que le Aspose.Cells ?**

Aspose.Cells est une bibliothèque de classes qui permet aux applications d'effectuer les tâches de traitement de feuille de calcul suivantes :

- Conversions de haute qualité entre tous les formats Excel Microsoft populaires, y compris la conversion en PDF, HTML, TIFF et l'impression.
- Programmation avec un modèle d'objet de classeur.
- Possibilité de créer des documents à partir de fragments, à partir d'un ou plusieurs documents, tout en fusionnant automatiquement les données par formatage stylistique, tableaux et graphiques.
- Fonctions de haut niveau, telles que l'importation de données à partir de différentes sources de données, notamment Array, ArrayList, DataTable / ResultSet.
- Moteur de calcul de formule robuste qui prend en charge presque toutes les fonctions Excel Microsoft standard et avancées.

## **Comparez Open XML SDK et Aspose.Cells**

Le tableau suivant compare les fonctionnalités Open XML SDK et Aspose.Cells.

|**Caractéristique ou catégorie de fonctionnalités**|**Kit de développement XML ouvert**|**Aspose.Cells**|
|:- |:- |:- |
|Formats Excel ou autres pris en charge|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Délimité par des tabulations, ODS, Texte brut (TXT), PDF, XPS|
|Convertir entre les formats Excel|Non|Oui|
|<p>Programmation de haut niveau avec un modèle d'objet de classeur :</p><p>- Trouver et remplacer.</p><p>- Assembler des feuilles de calcul.</p><p>- Copiez des fragments et des feuilles de calcul entre des classeurs.</p>|Non|Oui|
|Programmation détaillée avec un modèle d'objet de document, accès aux éléments individuels et propriétés de formatage de tous les éléments de la feuille de calcul.|Oui|Oui|
|Accès direct et complet de bas niveau aux éléments et attributs XML sous-jacents tels que les identifiants de relation, les identifiants de liste d'un document OOXML.|Oui|Non|
|<p>Générez des rapports, remplissez des documents avec des données :</p><p>- Importer/Exporter des données vers/depuis un DataTable / _ResultSet.</p><p>- Fonction Smart Markers.</p><p>- Insérer/Supprimer des lignes/colonnes/plages.</p><p>- Sources de données personnalisées.</p>|Non|Oui|
|<p>Rendu et impression :* Rendu des pages de feuille de calcul en images raster (TIFF, multipage TIFF, PNG, JPEG, BMP).* Rendu des pages de feuille de calcul en images vectorielles (EMF).</p><p>- Convertir des graphiques en images (TIFF, multipage TIFF, PNG, JPEG, BMP, EMF, etc.)</p><p>- Spécifiez la résolution, la qualité, la compression et d'autres options de l'image.</p><p>- Imprimer des feuilles de calcul en utilisant l'infrastructure d'impression .NET. Le composant a une méthode d'impression intégrée pour imprimer les feuilles de calcul comme indiqué dans l'aperçu avant impression de Microsoft Excel.</p>|Non|Oui|
|Calculer/ Recalculer des formules dynamiquement|Non|Oui|
|Plates-formes prises en charge|Windows, .NET|Windows, Linux, Java, .NET, Mono|

Vous pouvez comparer OpenXML avec Aspose.Cells Pour ce faire, nous vous suggérons de vous familiariser avec le projet Aspose.Cells pour OpenXML - il montre comment différentes tâches peuvent être effectuées en utilisant le Aspose.Cells for .NET API par rapport à OpenXML. Le projet couvre également les fonctionnalités permettant de travailler avec des documents texte qui ne sont disponibles que dans Aspose.Cells, mais pas dans OpenXML.

Ce projet est également utile pour les développeurs qui souhaitent migrer d'OpenXML vers Aspose.Cells.

{{% alert color="primary" %}}

 Explorer[le plugin avec des exemples de code source des fonctionnalités Aspose.Cells for .NET en comparaison avec OpenXML](https://github.com/asposemarketplace/Aspose_for_OpenXML).

 Ce plugin utilise la version d'évaluation de Aspose.Cells. Lorsque vous êtes satisfait de votre évaluation, vous pouvez acheter une licence auprès du[Aspose site web](https://purchase.aspose.com/buy) . Pour supprimer le message d'évaluation et les limitations des fonctionnalités, vous devez appliquer une licence de produit. Après l'achat du produit, vous recevrez un fichier de licence. Veuillez suivre les instructions du[« Licence et abonnement »](/cells/fr/net/licensing/) article pour ce faire.

{{% /alert %}}

**Conclusion**: Open XML SDK et Aspose.Cells ne sont pas en concurrence directe car ils répondent à des besoins et des publics assez différents.

## **Pourquoi ne pas ouvrir le SDK XML**
Open XML SDK est une bibliothèque de classes permettant de travailler avec des documents OOXML avec un typage fort. Aspose.Cells est une bibliothèque de traitement de feuille de calcul très utile qui offre un excellent support pour tous les Microsoft Excel et autres formats de fichiers.

Si tout ce que vous devez faire est une opération de programmation assez basique sur un document XLSX, alors Open XML SDK peut être un choix approprié. Avec Open XML SDK, vous serez assez à l'aise pour effectuer des tâches simples comme générer un simple document XLSX ou supprimer des commentaires, des en-têtes/pieds de page, extraire des images ou autres.
Certaines tâches peuvent être réalisées avec Open XML SDK, mais ne peuvent pas l'être avec Aspose.Cells. Par exemple, si vous devez accéder directement aux éléments et attributs XML d'un document OOXML, vous devez utiliser Open XML SDK.

Toutefois, si vous devez effectuer des opérations complexes sur des documents, telles que certaines des tâches suivantes, l'utilisation de Aspose.Cells est votre meilleure option :

- Prend en charge d'autres formats de fichiers en plus de XLSX.
- Copiez des fragments et des feuilles de calcul entre des classeurs ou joignez des classeurs de manière à combiner des objets, des styles et d'autres mises en forme de manière appropriée.
- Remplacer le texte formaté ou non formaté.
- Fonctions de haut niveau, telles que l'importation de données à partir de différentes sources de données, notamment Array, ArrayList, DataTable / ResultSet.
- Générez un document commercial, tel qu'une commande avec les détails de la commande à partir d'une source de données.
- Convertissez un document en PDF ou XPS pour qu'il apparaisse exactement comme Microsoft Excel l'aurait converti.
- Développer une application .NET ou Java.

