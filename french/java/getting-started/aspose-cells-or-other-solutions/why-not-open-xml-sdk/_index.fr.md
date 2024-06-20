---
title: Pourquoi ne pas utiliser Open XML SDK
type: docs
weight: 20
url: /fr/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

Nous entendons parfois cette question :

**Pourquoi devrions-nous utiliser les produits Aspose plutôt que le SDK Open XML gratuit ?**

Cette question est facile à répondre : **fonctionnalités et performance**.

{{% /alert %}} 
## **Qu'est-ce que le SDK Open XML ?**
Selon la bibliothèque MSDN, Open XML SDK est défini comme suit : Open XML SDK 2.0 simplifie la tâche de manipulation des packages Open XML et des éléments de schéma Open XML sous-jacents au sein d'un package. Open XML SDK 2.0 encapsule de nombreuses tâches courantes effectuées par les développeurs sur les packages Open XML, de sorte que vous pouvez effectuer des opérations complexes avec seulement quelques lignes de code. Les documents OOXML sont essentiellement des fichiers XML compressés et Open XML SDK est une collection de classes qui vous permet de travailler avec le contenu des documents OOXML de manière fortement typée. Au lieu de décompresser un fichier pour extraire du XML, charger ce XML dans un arbre DOM et travailler directement avec les éléments et les attributs XML, Open XML SDK fournit des classes pour faire cela.
## **Qu'est-ce que Aspose.Cells ?**
Aspose.Cells est une bibliothèque de classes qui permet à votre application d'effectuer les tâches de traitement de feuilles de calcul suivantes : Conversions de haute qualité entre tous les formats Excel populaires, y compris la conversion en PDF, HTML, TIFF et l'impression. Programmation avec un modèle d'objet classeur. Possibilité de construire des documents à partir de fragments, à partir d'un ou de plusieurs documents, tout en fusionnant automatiquement les données par une mise en forme stylistique, des graphiques et des images. Fonctions de haut niveau, telles que l'importation de données à partir de différentes sources de données, y compris Array, ArrayList, DataTable / ResultSet. Moteur de calcul de formules robuste prenant en charge presque toutes les fonctions standard et avancées de Microsoft Excel.

{{% alert color="primary" %}}
## **Comparer Open XML SDK et Aspose.Cells**
Le tableau suivant compare les fonctionnalités de Open XML SDK et Aspose.Cells. {{% /alert %}}

|**Fonction ou catégorie de fonctionnalités**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Formats Excel pris en charge ou autres formats|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, délimité par des tabulations, ODS, texte brut (TXT), PDF, XPS|
|Convertir entre les formats Excel|Non|Oui|
|<p>Programmation de haut niveau avec un modèle d'objet classeur :</p><p>- Trouver et remplacer.</p><p>- Assembler des feuilles de calcul.</p><p>- Copier des fragments et des feuilles de calcul entre des classeurs.|Non|Oui|
|Programmation détaillée avec un modèle d'objet document, accès aux éléments individuels et aux propriétés de mise en forme de tous les éléments de la feuille de calcul.|Oui|Oui|
|Accès direct et complet de bas niveau aux éléments et attributs XML sous-jacents tels que les identifiants de relation, les identifiants de liste d'un document OOXML.|Oui|Non|
|<p>Générer des rapports, peupler des documents avec des données :</p><p>- Importer/Exporter des données à partir d'un *DataTable /* ResultSet.</p><p>- Fonctionnalité de marqueurs intelligents.</p><p>- Insérer/Supprimer des lignes/colonnes/plages.</p><p>- Sources de données personnalisées.</p>|Non|Oui|
|<p>Rendu et impression :* Rendre les pages de la feuille de calcul en images matricielles (TIFF, TIFF multipage, PNG, JPEG, BMP).* Rendre les pages de la feuille de calcul en images vectorielles (EMF).* Convertir les graphiques en images (TIFF, TIFF multipage, PNG, JPEG, BMP, EMF, etc.)</p><p>- Spécifier la résolution, la qualité, la compression et d'autres options des images.</p><p>- Imprimer des feuilles de calcul en utilisant l'infrastructure d'impression .NET. Le composant possède une méthode d'impression intégrée pour imprimer les feuilles de calcul comme dans l'aperçu avant impression d'Excel.</p>|Non|Oui|
|Calculer/Recalculer les formules de manière dynamique|Non|Oui|
|Plateformes prises en charge|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Conclusion**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
