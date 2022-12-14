---
title: Pourquoi ne pas ouvrir le SDK XML
type: docs
weight: 20
url: /fr/java/why-not-open-xml-sdk/
---
{{% alert color="primary" %}} 

On entend parfois cette question :

**Pourquoi devrions-nous utiliser les produits Aspose plutôt que le SDK Open XML gratuit ?**

 Il est facile de répondre à cette question :**caractéristiques et fonctionnalités**.

{{% /alert %}} 
## ** Qu'est-ce qu'Open XML SDK ?**
Selon la bibliothèque MSDN, le SDK Open XML est défini comme suit : Le SDK Open XML 2.0 simplifie la tâche de manipulation des packages Open XML et des éléments de schéma Open XML sous-jacents dans un package. L'Open XML SDK 2.0 encapsule de nombreuses tâches courantes que les développeurs effectuent sur les packages Open XML, de sorte que vous pouvez effectuer des opérations complexes avec seulement quelques lignes de code. Les documents OOXML sont essentiellement des fichiers XML compressés et Open XML SDK est une collection de classes qui permet vous permet de travailler avec le contenu des documents OOXML de manière fortement typée. C'est-à-dire qu'au lieu de décompresser un fichier pour extraire le XML, de charger ce XML dans une arborescence DOM et de travailler directement avec les éléments et les attributs XML, Open XML SDK fournit des classes pour le faire.
## ** Qu'est-ce que le Aspose.Cells ?**
Aspose.Cells est une bibliothèque de classes qui permet à votre application d'effectuer les tâches de traitement de feuille de calcul suivantes : Conversions de haute qualité entre tous les formats Excel populaires, y compris la conversion en PDF, HTML, TIFF et l'impression. Programmation avec un modèle d'objet de classeur. Capacité à construire des documents à partir de fragments, à partir d'un ou plusieurs documents, tout en fusionnant automatiquement les données par mise en forme stylistique, tableaux et graphiques. Fonctions de haut niveau, telles que l'importation de données à partir de différentes sources de données, notamment Array, ArrayList, DataTable / ResultSet. Moteur de calcul de formule robuste qui prend en charge presque toutes les fonctions Excel Microsoft standard et avancées.

{{% alert color="primary" %}}
## ** Comparez Open XML SDK et Aspose.Cells**
 Le tableau suivant compare les fonctionnalités Open XML SDK et Aspose.Cells.{{% /alert %}}

|**Caractéristique ou catégorie de fonctionnalités**|**Kit de développement XML ouvert**|**Aspose.Cells**|
|:- |:- |:- |
|Formats Excel ou autres pris en charge|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, délimité par des tabulations, ODS, texte brut (TXT), PDF, XPS|
|Convertir entre les formats Excel|Non|Oui|
|<p>Programmation de haut niveau avec un modèle d'objet de classeur :</p><p>- Trouver et remplacer.</p><p>- Assembler des feuilles de calcul.</p><p>- Copiez des fragments et des feuilles de calcul entre des classeurs.</p>|Non|Oui|
|Programmation détaillée avec un modèle d'objet de document, accès aux éléments individuels et propriétés de formatage de tous les éléments de la feuille de calcul.|Oui|Oui|
|Accès direct et complet de bas niveau aux éléments et attributs XML sous-jacents tels que les identifiants de relation, les identifiants de liste d'un document OOXML.|Oui|Non|
|<p>Générez des rapports, remplissez des documents avec des données :</p><p>- Importer/Exporter des données vers/depuis un*Tableau de données /*Jeu de résultats.</p><p>- Fonction marqueurs intelligents.</p><p>- Insérer/Supprimer des lignes/colonnes/plages.</p><p>- Sources de données personnalisées.</p>|Non|Oui|
|<p>Rendu et impression :* Rendu des pages de feuille de calcul en images raster (TIFF, TIFF multipage, PNG, JPEG, BMP).*Convertissez des pages de feuille de calcul en images vectorielles (EMF).* Convertissez des graphiques en images (TIFF, TIFF multipage, PNG, JPEG, BMP, EMF, etc.)</p><p>- Spécifiez la résolution, la qualité, la compression et d'autres options de l'image. </p><p>- Imprimez des feuilles de calcul à l'aide de l'infrastructure d'impression .NET. Le composant a une méthode d'impression intégrée pour imprimer les feuilles de calcul comme indiqué dans l'aperçu avant impression de MS Excel.</p>|Non|Oui|
|Calculer/ Recalculer des formules dynamiquement| Non| Oui|
|Plates-formes prises en charge|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Conclusion**
  {{% alert color="primary" %}}Open XML SDK et Aspose.Cells ne sont pas en concurrence directe car ils répondent à des besoins et à des publics assez différents. Open XML SDK est une bibliothèque de classes permettant de travailler avec des documents OOXML avec un typage fort. Aspose.Cells est une bibliothèque de traitement de feuille de calcul très utile qui offre un excellent support pour tous les Microsoft Excel et d'autres formats de fichiers. Si tout ce que vous avez à faire est une opération de programmation assez basique sur un document XLSX, alors Open XML SDK peut être un choix approprié. Avec Open XML SDK, vous serez assez à l'aise pour effectuer des tâches simples comme générer un simple document XLSX ou supprimer des commentaires, des en-têtes/pieds de page, extraire des images ou autres. Certaines tâches peuvent être réalisées avec Open XML SDK, mais pas avec Aspose.Cells. Par exemple, si vous devez accéder directement aux éléments et attributs XML d'un document OOXML, vous devez utiliser Open XML SDK.Cependant, si vous devez effectuer des opérations complexes sur des documents, telles que certaines des tâches suivantes, alors l'utilisation de Aspose.Cells est votre meilleure option : Prend en charge d'autres formats de fichiers en plus de XLSX. Copiez des fragments et des feuilles de calcul entre des classeurs ou joignez des classeurs de manière à combiner des objets, des styles et d'autres mises en forme de manière appropriée. Remplacer le texte formaté ou non formaté. Fonctions de haut niveau, telles que l'importation de données à partir de différentes sources de données, notamment Array, ArrayList, DataTable / ResultSet. Générez un document commercial, tel qu'une commande avec les détails de la commande à partir d'une source de données. Convertissez un document au format PDF ou XPS afin qu'il apparaisse exactement comme Microsoft Excel l'aurait converti. Développer une application .NET ou Java.{{% /alert %}}
